from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.patient import PatientCreate, PatientUpdate, PatientResponse
from app.crud.patient import create_patient, get_patient, get_all_patients, update_patient, delete_patient

router = APIRouter(prefix="/patient", tags=["Patient"])


@router.post("/", response_model=PatientResponse)
def add_patient(data: PatientCreate, db: Session = Depends(get_db)):
    return create_patient(db, data)

@router.get("/", response_model=list[PatientResponse])
def list_patients(db: Session = Depends(get_db)):
    return get_all_patients(db)

@router.get("/{patient_id}", response_model=PatientResponse)
def fetch_patient(patient_id: int, db: Session = Depends(get_db)):
    patient = get_patient(db, patient_id)
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    return patient

@router.put("/{patient_id}", response_model=PatientResponse)
def edit_patient(patient_id: int, data: PatientUpdate, db: Session = Depends(get_db)):
    patient = update_patient(db, patient_id, data)
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    return patient

@router.delete("/{patient_id}")
def remove_patient(patient_id: int, db: Session = Depends(get_db)):
    success = delete_patient(db, patient_id)
    if not success:
        raise HTTPException(status_code=404, detail="Patient not found")
    return {"message": "Patient deleted successfully"}