import logging
import json
import os
import redis.asyncio as redis
from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from src.db.database import get_db_session
from src.db.models import Record, User
from src.schemas.record import RecordCreate, RecordResponse
from src.schemas.user import Token, UserCreate, UserResponse
from src.auth import verify_password, get_password_hash, create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES
from datetime import timedelta
from src.deps import get_current_user

logger = logging.getLogger(__name__)
router = APIRouter()

REDIS_HOST = os.getenv("REDIS_HOST", "redis")
cache = redis.Redis(host=REDIS_HOST, port=6379, db=0, decode_responses=True)

@router.get("/health", status_code=status.HTTP_200_OK)
async def health_check():
    return {"status": "healthy"}

@router.post("/register", response_model=UserResponse)
async def register(user: UserCreate, db: AsyncSession = Depends(get_db_session)):
    result = await db.execute(select(User).where(User.email == user.email))
    if result.scalars().first():
        raise HTTPException(status_code=400, detail="Email already registered")
    
    new_user = User(
        email=user.email,
        hashed_password=get_password_hash(user.password)
    )
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return new_user

@router.post("/login", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: AsyncSession = Depends(get_db_session)):
    result = await db.execute(select(User).where(User.email == form_data.username))
    user = result.scalars().first()
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/records", response_model=RecordResponse, status_code=status.HTTP_201_CREATED)
async def create_record(record: RecordCreate, current_user: User = Depends(get_current_user), db: AsyncSession = Depends(get_db_session)):
    logger.info(f"Creating record: {record.name} by {current_user.email}")
    new_record = Record(name=record.name, description=record.description)
    db.add(new_record)
    try:
        await db.commit()
        await db.refresh(new_record)
        # Invalidate cache
        await cache.delete("all_records")
        return new_record
    except Exception as e:
        await db.rollback()
        logger.error(f"Error creating record: {str(e)}")
        raise HTTPException(status_code=500, detail="Database insertion error")

@router.get("/records", response_model=List[RecordResponse])
async def get_records(current_user: User = Depends(get_current_user), db: AsyncSession = Depends(get_db_session)):
    logger.info(f"Fetching records requested by {current_user.email}")
    try:
        cached_records = await cache.get("all_records")
        if cached_records:
            logger.info("Serving records from Redis Cache")
            return json.loads(cached_records)

        result = await db.execute(select(Record))
        records = result.scalars().all()
        records_data = [{"id": r.id, "name": r.name, "description": r.description} for r in records]
        
        # Cache for 60 seconds
        await cache.setex("all_records", 60, json.dumps(records_data))
        logger.info("Serving records from Database")
        return records
    except Exception as e:
        logger.error(f"Error fetching records: {str(e)}")
        raise HTTPException(status_code=500, detail="Database fetch error")
