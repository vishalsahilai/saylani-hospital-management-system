from pydantic import BaseModel
from typing import Optional

class StaffCreate(BaseModel):
    name: str
    role: str
    shift: str
    salary: Optional[float] = 0.0

class StaffUpdate(BaseModel):
    name: Optional[str] = None
    role: Optional[str] = None
    shift: Optional[str] = None
    salary: Optional[float] = None

class StaffResponse(BaseModel):
    id: int
    name: str
    role: str
    shift: str
    salary: float