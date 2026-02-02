from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from datetime import datetime
from app.infrastructure.database import Base

class ImageModel(Base):
    __tablename__ = "images"

    id = Column(Integer, primary_key=True)
    owner_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    filename = Column(String(255), nullable=False)
    title = Column(String(255))
    created_at = Column(DateTime, default=datetime.utcnow)
