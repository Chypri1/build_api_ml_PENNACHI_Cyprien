from fastapi import FastAPI
from pymongo import MongoClient
from pydantic import BaseModel
from typing import List

# Initialisation de l'application
app = FastAPI()

# Connexion à la base de données MongoDB
client = MongoClient("mongodb://root:example@mongo:27017/")
db = client["local"]
collection = db["startup_log"]

# Modèle Pydantic pour l'insertion
class Document(BaseModel):
    name: str
    value: int

# Route pour récupérer toutes les données
@app.get("/get_data")
async def get_data():
    cursor = collection.find({})
    response = [doc for doc in cursor]
    print("format response : " + str(response))
    return response

# Route pour ajouter des documents
@app.post("/add_data")
async def add_data(documents_to_insert: List[Document]):
    docs = [doc.dict() for doc in documents_to_insert]
    result = collection.insert_many(docs)
    response = {"inserted_ids": str(result.inserted_ids)}
    print("format response : " + str(response))
    return response

# Route pour mettre à jour des documents
@app.post("/update_data")
async def update_data(id: str, new_values: Document):
    result = collection.update_one({"_id": id}, {"$set": new_values.dict()})
    response = {"matched_count": result.matched_count, "modified_count": result.modified_count}
    print("format response : " + str(response))
    return response

# Route pour supprimer un document
@app.post("/delete_data")
async def delete_data(id: str):
    result = collection.delete_one({"_id": id})
    response = {"deleted_count": result.deleted_count}
    print("format response : " + str(response))
    return response
