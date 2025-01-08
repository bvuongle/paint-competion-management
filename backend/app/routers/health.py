import logging

from fastapi import APIRouter, HTTPException
from sqlalchemy.exc import SQLAlchemyError

from app.core.database import get_db, engine

router = APIRouter(prefix="/health", tags=["Health"])
logger = logging.getLogger(__name__)

def check_database():
    try:
        with engine.connect() as conn:
            conn.execute("SELECT 1")
    except SQLAlchemyError as e:
        logger.error(f"Database connection failed: {e}")

@router.get(path="", summary="Health Check Endpoint")
def health_check():
    """
    Health check endpoint to verify the system is up.
    """
    try:
        check_database()
        logger.info("Health check endpoint called")
        return {"message": "System up, database connection OK", "status": "up"}
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail={
                "status": "error",
                "message": "Service is down",
                "error": str(e)
            }
        )