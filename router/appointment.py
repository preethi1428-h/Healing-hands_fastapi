from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.database import get_db
from modules.appointment_mod import Appointment
from schemas.appointment import AppointmentCreate, AppointmentResponse



router = APIRouter(prefix="/appointments", tags=["Appointments"])

# CREATE APPOINTMENT
@router.post("/", response_model=AppointmentResponse)
def create_appointment(app_data: AppointmentCreate, db: Session = Depends(get_db)):
    new_app = Appointment(
        name=app_data.name,
        email=app_data.email,
        counselor_name=app_data.counselor_name,
        phone=app_data.phone,
        date=app_data.date,
        time=app_data.time,
        service=app_data.service,
        additional=app_data.additional,
        user_id=app_data.user_id
    )
    db.add(new_app)
    db.commit()
    db.refresh(new_app)
    return new_app

@router.get("/provider/{provider_id}", response_model=list[AppointmentResponse])
def get_appointments_for_provider(provider_id: int, db: Session = Depends(get_db)):
    return db.query(Appointment).filter(Appointment.provider_id == provider_id).all()


@router.get("/", response_model=list[AppointmentResponse])
def get_all_appointments(db: Session = Depends(get_db)):
    return db.query(Appointment).all()



@router.get("/{appointment_id}", response_model=AppointmentResponse)
def get_one_appointment(appointment_id: int, db: Session = Depends(get_db)):
    appointment = db.query(Appointment).filter(Appointment.id == appointment_id).first()

    if not appointment:
        raise HTTPException(status_code=404, detail="Appointment not found")

    return appointment

@router.get("/user/{user_id}", response_model=list[AppointmentResponse])
def get_appointments_by_user(user_id: int, db: Session = Depends(get_db)):
    appointments = db.query(Appointment).filter(Appointment.user_id == user_id).all()

    for app in appointments:
        if app.email is None:
            app.email = "unknown@healinghands.com"
        if app.additional is None:
            app.additional = ""

    return appointments



@router.delete("/{appointment_id}")
def delete_appointment(appointment_id: int, db: Session = Depends(get_db)):
    appointment = db.query(Appointment).filter(Appointment.id == appointment_id).first()

    if not appointment:
        raise HTTPException(status_code=404, detail="Appointment not found")

    db.delete(appointment)
    db.commit()

    return {"message": "Appointment Deleted Successfully"}



@router.put("/{appointment_id}/provider/accept")
def provider_accept(appointment_id: int, db: Session = Depends(get_db)):
    appointment = db.query(Appointment).filter(Appointment.id == appointment_id).first()

    if not appointment:
        raise HTTPException(status_code=404, detail="Appointment not found")

    appointment.status = "Accepted"
    db.commit()
    return {"message": "Appointment Accepted"}



@router.put("/{appointment_id}/provider/reject")
def provider_reject(appointment_id: int, db: Session = Depends(get_db)):
    appointment = db.query(Appointment).filter(Appointment.id == appointment_id).first()

    if not appointment:
        raise HTTPException(status_code=404, detail="Appointment not found")

    appointment.status = "Rejected"
    db.commit()
    return {"message": "Appointment Rejected"}


