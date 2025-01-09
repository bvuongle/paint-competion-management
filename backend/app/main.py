import logging

from fastapi import FastAPI
from app.core.database import Base, engine

from app.models import (
    schools,
    users,
    participants,
    jury,
    stage,
    scores,
    thresholds,
    appeals,
)  # noqa: F401
from app.routers import health, auth, users

# ---------
# Logging
# ---------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)
logger = logging.getLogger(__name__)

app = FastAPI(title="Competition Management System API", version="0.1.0")

Base.metadata.create_all(bind=engine)

app.include_router(health.router)
app.include_router(auth.router)
app.include_router(users.router)


@app.get("/", summary="Root Endpoint", tags=["Root"])
def root():
    """
    Root endpoint to verify the system is up.
    """
    logger.info("ROOT ENDPOINT")
    return {"message": "Competition Management System API"}