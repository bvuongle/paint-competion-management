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

app = FastAPI(title="Competition Management System API", version="0.1.0")

Base.metadata.create_all(bind=engine)


@app.get("/")
def read_root():
    return {"message": "DB models are set up and tables are created."}
