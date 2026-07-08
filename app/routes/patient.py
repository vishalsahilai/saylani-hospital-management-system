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