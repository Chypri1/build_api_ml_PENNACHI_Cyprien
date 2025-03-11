from fastapi import FastAPI
from pymongo import MongoClient


app = FastAPI()
@app.get("/data")
async def get_data():
    
    client = MongoClient("mongodb://root:example@mongo:27017/")
    db = client["local"]
    collection = db["startup_log"]
    cursor = collection.find({})
    response = list(cursor)
    print("format response :  " +str(response))
    return response

@app.post("/add_data")
async def add_data(documents_to_insert):
    
    client = MongoClient("mongodb://root:example@mongo:27017/")
    db = client["local"]
    collection = db["startup_log"]
    result = collection.insert_many(documents_to_insert)
    response = list(result)
    print("format response :  " +str(response))
    return response


@app.post("/add_data")
async def delete_data(id:str):
    
    client = MongoClient("mongodb://root:example@mongo:27017/")
    db = client["local"]
    collection = db["startup_log"]
    result = collection.pop({id:id})
    response = list(result)
    print("format response :  " +str(response))
    return response