from fastapi import FastAPI,Depends
import models
import crud
from crud import Session
from db import engine, SessionLocal

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

#define endpoint
# @app.get("/")
# def getallAddress():
#     return {"Ahoy": "Captain"}

#get all Addresses
@app.get("/")
def list_Address(db:Session = Depends(get_db)):
    Address_list = crud.list_Address(db=db)
    return Address_list

#get by id
@app.get("/{id}") #id is a path parameter
def get_Address(id:int, db:Session = Depends(get_db)):
    data = crud.get_Address(db=db, id=id)
    return data

#create new address
@app.post("/")
def create_Address(name:str, lat:float, lng:float, db:Session = Depends(get_db)):
    data = crud.create_Address(db=db, name=name, lat=lat, lng=lng)
##return object created
    return {"Address": data}

#Update Address
@app.put("/{id}") #id is a path parameter
def update_friend(id:int, name:str, lat:float, lng:float, db:Session=Depends(get_db)):
    #get friend object from database
    old_data = crud.get_Address(db=db, id=id)
    #check if friend object exists
    if old_data:
        updated_data = crud.update_Address(db=db, id=id, name=name, lat=lat, lng=lng)
        return updated_data
    else:
        return {"error": "Address with id {id} does not exist"}

@app.delete("/{id}") #id is a path parameter
def delete_Address(id:int, db:Session=Depends(get_db)):
    #get friend object from database
    data = crud.get_Address(db=db, id=id)
    #check if friend object exists
    if data:
        return crud.delete_Address(db=db, id=id)
    else:
        return {"error": "Address with id {id} does not exist"}

