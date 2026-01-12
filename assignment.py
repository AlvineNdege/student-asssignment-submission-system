from sqlalchemy import Column, Integer, String, Numeric, Text, ForeignKey, DateTime,Boolean 
from datetime import datetime, timezone

from app.db.base import Base

class Assignment(Base):
    __tablename__ = "assignments"

    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey("users.id"))
    subject = Column(String(100))
    title = Column(String(150))
    description = Column(Text)
    file_url = Column(String)
    status = Column(String, default="submitted")
    score = Column(Integer, nullable=True)
    feedback = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), default=datetime.now(timezone.utc))
    updated_at = Column(DateTime(timezone=True), default=datetime.now(timezone.utc))