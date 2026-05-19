from sqlalchemy import Column, Integer, String
from database import Base

class Airport(Base):

    __tablename__ = "airports"

    id = Column(Integer, primary_key=True)

    code = Column(String, nullable=False)

    city = Column(String)

    country = Column(String)