from fastapi import FastAPI,Depends
import models
import crud
from crud import Session
from db import engine, SessionLocal
from math import radians, cos, sin, asin, sqrt

#create the database tables on app startup or reload
models.Base.metadata.create_all(bind=engine)

#initailize FastApi instance
app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#get all Addresses
# @app.get("/")
# def list_Address(db:Session = Depends(get_db)):
#     Address_list = crud.list_Address(db=db)
#     return Address_list

#get by id
@app.get("/{id}") #id is a path parameter
def get_Address(id:int, db:Session = Depends(get_db)):
    data = crud.get_Address(db=db, id=id)
    return data

@app.get("/")
def get_custom_address(distance:int,lat:float, lng:float, db:Session = Depends(get_db)):
    lat = radians(lat)
    lng = radians(lng)
    #load all addresses
    data=crud.list_Address(db=db)
    result={}
        #logic for getting custom data
    for d in data:
            lat2 = radians(d.lat)
            lng2 = radians(d.lng)
            # Haversine formula
            dlng = lng2 - lng
            dlat = lat2 - lat
            a = sin(dlat / 2)**2 + cos(lat) * cos(lat2) * sin(dlng / 2)**2
            c = 2 * asin(sqrt(a))
            # Radius of earth in kilometers. Use 3956 for miles
            r = 6371
            # calculate the result
            dist =c * r
            if distance>=dist:
            # return d
                result[d.id]=(d.name,d.lat,d.lng)
    if result:
        return result
    else:
        return {"error": "Address does not exist"}

#create new address
@app.post("/")
def create_Address(name:str, lat:float, lng:float, db:Session = Depends(get_db)):
    data = crud.create_Address(db=db, name=name, lat=lat, lng=lng)
##return object created
    return {"Address": data}

#Update Address
@app.put("/{id}") #id is a path parameter
def update_Address(id:int, name:str, lat:float, lng:float, db:Session=Depends(get_db)):
    #get object from database
    old_data = crud.get_Address(db=db, id=id)
    #check if  object exists
    if old_data:
        updated_data = crud.update_Address(db=db, id=id, name=name, lat=lat, lng=lng)
        return updated_data
    else:
        return {"error": "Address with id {id} does not exist"}

@app.delete("/{id}") #id is a path parameter
def delete_Address(id:int, db:Session=Depends(get_db)):
    #get  object from database
    data = crud.get_Address(db=db, id=id)
    #check if object exists
    if data:
        return crud.delete_Address(db=db, id=id)
    else:
        return {"error": "Address with id {id} does not exist"}

