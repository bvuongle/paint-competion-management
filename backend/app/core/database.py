from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from app.core.config import settings

# Main SQLAlchemy engine
engine = create_engine(settings.DATABASE_URL, echo=False)

# DB session for each request
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    """
    Dependency function to get DB session in endpoints
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
