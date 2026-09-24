from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from pymongo import MongoClient
app=FastAPI()
mongo_url="mongodb://localhost:27017"
client=MongoClient(mongo_url)
db=client["hospital"]
student_collection=db["technician"]
@app.get("/students")
def all_students():
    student=list(student_collection.find({},{"_id":0}))
    return student
#to search student by rollno
@app.get("/student/{student_id}")
def technician_get(name,password):
    student=list(student_collection.find({"name":name,"password":password},{"_id":0}))
    return student
#to post new records
class studentadd(BaseModel):
    name:str
    roll:int
@app.post("/studentadd")
def add(student):
    student_collection.insert_one(student)
    return "record added succesfully"
#for updating a record
@app.put("/student/{student_id}")
def update(student_id:int,student:studentadd):
    res=student_collection.update_one({"roll":student_id},{"$set":student.model_dump()})
    if res is None:
        raise HTTPException(status_code=404,detail="invalid id")
    return "record updated successfully!"
#deleting a rceord
@app.delete("/student/{student_id}")
def delete(student_id:int):
    res=student_collection.delete_one({"roll":student_id})
    if res is None:
        raise HTTPException(status_code=404,detail="id not found")
    return "deleted succesfully"
