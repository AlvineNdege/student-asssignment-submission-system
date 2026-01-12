from sqlalchemy import Column, Integer, Text, ForeignKey, DateTime
from datetime import datetime, timezone

from app.db.base import Base

class AssignmentComment(Base):
    __tablename__ = "assignment_comments"

    id = Column(Integer, primary_key=True)
    assignment_id = Column(Integer, ForeignKey("assignments.id"))
    teacher_id = Column(Integer, ForeignKey("users.id"))
    comment = Column(Text)
    created_at = Column(DateTime(timezone=True), default=datetime.now(timezone.utc))
