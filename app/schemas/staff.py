from pydantic import BaseModel
from typing import Optional

class StaffCreate(BaseModel):
    name: str
    role: str
    shift: str
    salary: Optional[float] = 0.0