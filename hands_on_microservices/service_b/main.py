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

