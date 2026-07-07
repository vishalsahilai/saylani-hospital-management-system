from sqlalchemy.orm import Session
from app.models.patient import Patient
from app.schemas.patient import PatientCreate, PatientUpdate

def create_patient(db: Session, data: PatientCreate) -> Patient:
    patient = Patient(**data.model_dump())
    db.add(patient)
    db.commit()
    db.refresh(patient)
    return patient

def get_patient(db: Session, patient_id: int) -> Patient | None:
    return db.query(Patient).filter(Patient.id == patient_id).first()

def get_all_patients(db: Session) -> list[Patient]:
    return db.query(Patient).all()

def update_patient(db: Session, patient_id: int, data: PatientUpdate) -> Patient | None:
    patient = get_patient(db, patient_id)
    if not patient:
        return None
    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(patient, key, value)
    db.commit()
    db.refresh(patient)
    return patient

def delete_patient(db: Session, patient_id: int) -> bool:
    patient = get_patient(db, patient_id)
    if not patient:
        return False
    db.delete(patient)
    db.commit()
    return True