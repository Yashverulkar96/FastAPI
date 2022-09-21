from sqlalchemy.orm import Session
from models import AddressModel

#create_friend
def create_Address(db:Session, name, lat, lng):
    """
    function to create a friend model object
    """
    # create friend instance 
    new_address = AddressModel(name=name, lat=lat, lng=lng)
    #place object in the database session
    db.add(new_address)
    #commit your instance to the database
    db.commit()
    #refresh the attributes of the given instance
    db.refresh(new_address)
    return new_address
#get_friend
def get_Address(db:Session, id:int):
    """
    get the first record with a given id, if no such record exists, will return null
    """
    data = db.query(AddressModel).filter(AddressModel.id==id).first()
    return data
#ist_friends
def list_Address(db:Session):
    """
    Return a list of all existing Friend records
    """
    all_address = db.query(AddressModel).all()
    return all_address

#update_friend
def update_Address(db:Session, id:int,name: str, lat: float, lng:float):
    """
    Update a Friend object's attributes
    """
    update_data = get_Address(db=db, id=id)
    update_data.name = name
    update_data.lat = lat
    update_data.lng = lng

    db.commit()
    db.refresh(update_data ) #refresh the attribute of the given instance
    return update_data 
#elete_friend
def delete_Address(db:Session, id:int):
    """
    Delete a Friend object
    """
    delete_data  = get_Address(db=db, id=id)
    db.delete(delete_data )
    db.commit() #save changes to db