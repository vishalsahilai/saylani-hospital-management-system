from sqlalchemy.orm import Session
from app.models.patient import Patient
from app.schemas.patient import PatientCreate, PatientUpdate

def create_patient(db: Session, data: PatientCreate) -> Patient:
    patient = Patient(**data.model_dump())
    db.add(patient)
    db.commit()
    db.refresh(patient)
    return patient
