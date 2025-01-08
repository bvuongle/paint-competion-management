from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, func
from backend.app.core.database import Base


class Jury(Base):
    __tablename__ = "jury"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    region = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
