from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from app.database import Base

class Doctor(Base):
    __tablename__ = "doctors"

    id           = Column(Integer, primary_key=True, index=True)
    name         = Column(String(100), nullable=False)
    specialization = Column(String(100), nullable=False)
    email        = Column(String(100), unique=True, nullable=False)
    phone        = Column(String(20))
    salary       = Column(Float, default=0.0)

    patients     = relationship("Patient", back_populates="doctor")