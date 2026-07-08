from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.doctor import DoctorCreate, DoctorUpdate, DoctorResponse
from app.crud.doctor import create_doctor, get_doctor, get_all_doctors, update_doctor, delete_doctor

router = APIRouter(prefix="/doctor", tags=["Doctor"])


@router.post("/", response_model=DoctorResponse)
def add_doctor(data: DoctorCreate, db: Session = Depends(get_db)):
    return create_doctor(db, data)