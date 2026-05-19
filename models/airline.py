from sqlalchemy import Column, Integer, String
from database import Base

class Airline(Base):

    __tablename__ = "airlines"

    id = Column(Integer, primary_key=True)

    name = Column(String, nullable=False)

    code = Column(String, nullable=False)