from fastapi import FastAPI
from router import auth,services,appointment,providers
from db.database import Base,engine

 
app = FastAPI()

Base.metadata.create_all(bind=engine)


app.include_router(auth.router)
app.include_router(services.router)
app.include_router(appointment.router)
app.include_router(providers.router)
