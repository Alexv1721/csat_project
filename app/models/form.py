from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.sql import func
from app.database import Base

class Form(Base):
    __tablename__ = "forms"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200))
    description = Column(Text)
    slug = Column(String(100), unique=True) 
    questions = Column(Text)   # JSON STRING
    admin_id = Column(Integer, ForeignKey("admins.id"))
    created_at = Column(DateTime(timezone=True), server_default=func.now())

