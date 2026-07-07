from pydantic import BaseModel, EmailStr
from typing import Optional

class DoctorCreate(BaseModel):
    name: str
    specialization: str
    email: EmailStr
    phone: Optional[str] = None
    salary: Optional[float] = 0.0