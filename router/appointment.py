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
        phone=app_data.phone,
        date=app_data.date,
        time=app_data.time,
        service=app_data.service,
        user_id=app_data.user_id
    )
    db.add(new_app)
    db.commit()
    db.refresh(new_app)
    return new_app


# GET ALL
@router.get("/", response_model=list[AppointmentResponse])
def get_all_appointments(db: Session = Depends(get_db)):
    return db.query(Appointment).all()


# GET ONE
@router.get("/{appointment_id}", response_model=AppointmentResponse)
def get_one_appointment(appointment_id: int, db: Session = Depends(get_db)):
    appointment = db.query(Appointment).filter(Appointment.id == appointment_id).first()

    if not appointment:
        raise HTTPException(status_code=404, detail="Appointment not found")

    return appointment


# DELETE
@router.delete("/{appointment_id}")
def delete_appointment(appointment_id: int, db: Session = Depends(get_db)):
    appointment = db.query(Appointment).filter(Appointment.id == appointment_id).first()

    if not appointment:
        raise HTTPException(status_code=404, detail="Appointment not found")

    db.delete(appointment)
    db.commit()

    return {"message": "Appointment Deleted Successfully"}


@router.get("/user/{user_id}", response_model=list[AppointmentResponse])
def get_appointments_by_user(user_id: int, db: Session = Depends(get_db)):
    appointments = db.query(Appointment).filter(Appointment.user_id == user_id).all()
    return appointments

# accept
@router.put("/{appointment_id}/accept")
def accept_appointment(appointment_id: int, db: Session = Depends(get_db)):
    appointment = db.query(Appointment).filter(Appointment.id == appointment_id).first()

    if not appointment:
        raise HTTPException(status_code=404, detail="Appointment not found")

    appointment.status = "Accepted"
    db.commit()
    db.refresh(appointment)

    return {"message": "Appointment Accepted", "appointment_id": appointment.id}

#reject
@router.put("/{appointment_id}/reject")
def reject_appointment(appointment_id: int, db: Session = Depends(get_db)):
    appointment = db.query(Appointment).filter(Appointment.id == appointment_id).first()

    if not appointment:
        raise HTTPException(status_code=404, detail="Appointment not found")

    appointment.status = "Rejected"
    db.commit()
    db.refresh(appointment)

    return {"message": "Appointment Rejected", "appointment_id": appointment.id}

