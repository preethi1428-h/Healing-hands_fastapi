from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db.database import Base

class Appointment(Base):
    __tablename__ = "appointments"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    date = Column(String, nullable=False)
    time = Column(String, nullable=False)
    service = Column(String, nullable=False)
    status = Column(String, default="Pending") 

    user_id = Column(Integer, ForeignKey("users.id"))  

    user = relationship("User", back_populates="appointment")  
