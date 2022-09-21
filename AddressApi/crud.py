from sqlalchemy.orm import Session
from models import AddressModel


def create_Address(db:Session, name, lat, lng):
    # create Address instance 
    new_address = AddressModel(name=name, lat=lat, lng=lng)
    #place object in the database session
    db.add(new_address)
    #commit your instance to the database
    db.commit()
    #refresh the attributes of the given instance
    db.refresh(new_address)
    return new_address

def get_Address(db:Session, id:int):
    data = db.query(AddressModel).filter(AddressModel.id==id).first()
    return data

def list_Address(db:Session):
    all_address = db.query(AddressModel).all()
    return all_address


def update_Address(db:Session, id:int,name: str, lat: float, lng:float):
    update_data = get_Address(db=db, id=id)
    update_data.name = name
    update_data.lat = lat
    update_data.lng = lng
    db.commit()
    db.refresh(update_data ) #refresh the attribute of the given instance
    return update_data 

def delete_Address(db:Session, id:int):
    delete_data  = get_Address(db=db, id=id)
    db.delete(delete_data )
    db.commit() #save changes to db