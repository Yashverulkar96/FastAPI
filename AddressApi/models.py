from sqlalchemy import Column, Integer, String,Float
from db import Base


# model/table
class  AddressModel(Base):
    __tablename__ = "address"

    # fields 
    id = Column(Integer,primary_key=True, index=True)
    name = Column(String(20))
    lat = Column(Float)
    lng = Column(Float)
