from sqlalchemy import Column, Integer, Text, ForeignKey, DateTime,String,ForeignKey
from sqlalchemy.sql import func
from app.database import Base

class Submission(Base):
    __tablename__ = "submissions"

    id = Column(Integer, primary_key=True, index=True)
    form_id = Column(Integer, ForeignKey("forms.id"))
    user_name = Column(String(100))
    rating = Column(Integer)
    answers = Column(Text)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class FormResponse(Base):
    __tablename__ = "form_responses"

    id = Column(Integer, primary_key=True)
    form_id = Column(Integer, ForeignKey("forms.id"))
    answers = Column(Text)
    created_at = Column(DateTime, server_default=func.now())