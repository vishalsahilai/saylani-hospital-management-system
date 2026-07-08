from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.doctor import DoctorCreate, DoctorUpdate, DoctorResponse
from app.crud.doctor import create_doctor, get_doctor, get_all_doctors, update_doctor, delete_doctor

router = APIRouter(prefix="/doctor", tags=["Doctor"])


@router.post("/", response_model=DoctorResponse)
def add_doctor(data: DoctorCreate, db: Session = Depends(get_db)):
    return create_doctor(db, data)

@router.get("/", response_model=list[DoctorResponse])
def list_doctors(db: Session = Depends(get_db)):
    return get_all_doctors(db)

@router.get("/{doctor_id}", response_model=DoctorResponse)
def fetch_doctor(doctor_id: int, db: Session = Depends(get_db)):
    doctor = get_doctor(db, doctor_id)
    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")
    return doctor

@router.put("/{doctor_id}", response_model=DoctorResponse)
def edit_doctor(doctor_id: int, data: DoctorUpdate, db: Session = Depends(get_db)):
    doctor = update_doctor(db, doctor_id, data)
    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")
    return doctor