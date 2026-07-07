from pydantic import BaseModel
from typing import Optional
from datetime import date

class PatientCreate(BaseModel):
    name: str
    age: int
    gender: str
    disease: str
    doctor_id: int
    admission_date: date