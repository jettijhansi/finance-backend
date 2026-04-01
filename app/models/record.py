from sqlalchemy import Column, Integer, String, Float, ForeignKey, Date
from app.database import Base

class Record(Base):
    __tablename__ = "records"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    amount = Column(Float)
    type = Column(String)  # income / expense
    category = Column(String)
    date = Column(Date)
    notes = Column(String)