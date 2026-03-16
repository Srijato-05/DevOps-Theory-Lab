import logging
from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from src.db.database import get_db_session
from src.db.models import Record
from src.schemas.record import RecordCreate, RecordResponse

logger = logging.getLogger(__name__)
router = APIRouter()

@router.get("/health", status_code=status.HTTP_200_OK)
async def health_check():
    return {"status": "healthy"}

@router.post("/records", response_model=RecordResponse, status_code=status.HTTP_201_CREATED)
async def create_record(record: RecordCreate, db: AsyncSession = Depends(get_db_session)):
    logger.info(f"Creating record: {record.name}")
    new_record = Record(name=record.name, description=record.description)
    db.add(new_record)
    try:
        await db.commit()
        await db.refresh(new_record)
        return new_record
    except Exception as e:
        await db.rollback()
        logger.error(f"Error creating record: {str(e)}")
        raise HTTPException(status_code=500, detail="Database insertion error")

@router.get("/records", response_model=List[RecordResponse])
async def get_records(db: AsyncSession = Depends(get_db_session)):
    logger.info("Fetching all records")
    try:
        result = await db.execute(select(Record))
        records = result.scalars().all()
        return records
    except Exception as e:
        logger.error(f"Error fetching records: {str(e)}")
        raise HTTPException(status_code=500, detail="Database fetch error")
