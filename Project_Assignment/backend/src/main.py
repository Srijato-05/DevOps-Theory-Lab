import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.api.router import router

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def create_app() -> FastAPI:
    app = FastAPI(
        title="Project Assignment 1 API",
        description="FastAPI Backend for Demo",
        version="1.0.0",
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(router, prefix="/api/v1")

    @app.on_event("startup")
    async def startup_event():
        logger.info("Starting up application...")
    
    @app.on_event("shutdown")
    async def shutdown_event():
        logger.info("Shutting down application...")

    return app

app = create_app()
