from fastapi import FastAPI
from router import auth,services,appointment,providers,contact
from db.database import Base,engine
from modules import appointment_mod, provider_mod



 
app = FastAPI()

Base.metadata.create_all(bind=engine)


app.include_router(auth.router)
app.include_router(services.router)
app.include_router(appointment.router)
app.include_router(providers.router)
app.include_router(contact.router)
