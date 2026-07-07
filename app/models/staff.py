from sqlalchemy import Column, Integer, String, Float
from app.database import Base

class Staff(Base):
    __tablename__ = "staff"

    id     = Column(Integer, primary_key=True, index=True)
    name   = Column(String(100), nullable=False)
    role   = Column(String(100), nullable=False)
    shift  = Column(String(50), nullable=False)
    salary = Column(Float, default=0.0)