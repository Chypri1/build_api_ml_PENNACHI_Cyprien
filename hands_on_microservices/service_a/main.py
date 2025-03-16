from fastapi import FastAPI, HTTPException, Depends, Request
import httpx
import datetime

app = FastAPI()

# Chemin vers le socket Unix
UDS_PATH = "/tmp/service_b.sock"

# Liste des utilisateurs et super-utilisateurs acceptés
LIST_SUPERUSER = ["SuperUser1", "SuperUser2"]
LIST_USER = ["User1", "User2"]

list_token_superuser = []
list_token_user = []

# Création d'un token qui dure une heure
def creating_token(username: str, role: str):
    token = {
        "username": username,
        "role": role,
        "datetime": datetime.datetime.now() + datetime.timedelta(hours=1)
    }
    return token

# Fonction pour vérifier l'authentification
def authenticate(request: Request):
    username = request.query_params.get("username")
    if not username:
        raise HTTPException(status_code=401, detail="Nom d'utilisateur manquant")
    
    # Vérification des superusers
    if username in LIST_SUPERUSER:
        for token_superuser in list_token_superuser:
            if token_superuser["username"] == username:
                if token_superuser["datetime"] < datetime.datetime.now():
                    list_token_superuser.remove(token_superuser)
                    list_token_superuser.append(creating_token(username, "ADMIN"))
                return token_superuser
        # Si aucun token valide n'existe, en créer un
        new_token = creating_token(username, "ADMIN")
        list_token_superuser.append(new_token)
        return new_token
    
    # Vérification des utilisateurs classiques
    elif username in LIST_USER:
        for token_user in list_token_user:
            if token_user["username"] == username:
                if token_user["datetime"] < datetime.datetime.now():
                    list_token_user.remove(token_user)
                    list_token_user.append(creating_token(username, "USER"))
                return token_user
        # Si aucun token valide n'existe, en créer un
        new_token = creating_token(username, "USER")
        list_token_user.append(new_token)
        return new_token

    raise HTTPException(status_code=401, detail="Authentification échouée")

# Vérifie si l'utilisateur est superuser
def require_superuser(token: dict):
    if token.get("role") != "ADMIN":
        raise HTTPException(status_code=403, detail="Accès réservé aux superutilisateurs")

# Fonction utilitaire pour effectuer les requêtes via UDS
async def request_via_uds(method: str, url: str, json_data=None):
    transport = httpx.AsyncHTTPTransport(uds=UDS_PATH)
    async with httpx.AsyncClient(transport=transport) as client:
        try:
            response = await client.request(method, url, json=json_data)
            response.raise_for_status()
            return response.json()
        except httpx.RequestError as e:
            raise HTTPException(status_code=500, detail=f"Erreur de requête: {str(e)}")
        except httpx.HTTPStatusError as e:
            raise HTTPException(status_code=response.status_code, detail=f"Erreur HTTP: {response.text}")

# Route pour récupérer les données (superuser uniquement)
@app.get("/get_data")
async def get_data(token: dict = Depends(authenticate)):
    require_superuser(token)  # Vérifie que l'utilisateur est un superuser
    url = "http://service_b/get_data"
    return await request_via_uds("GET", url)

# Route pour ajouter des données (utilisateurs classiques et superusers)
@app.post("/add_data")
async def add_data(data: dict, token: dict = Depends(authenticate)):
    url = "http://service_b/add_data"
    return await request_via_uds("POST", url, json_data=data)

# Route pour mettre à jour des données (superuser uniquement)
@app.post("/update_data")
async def update_data(data: dict, token: dict = Depends(authenticate)):
    require_superuser(token)  # Vérifie que l'utilisateur est un superuser
    url = "http://service_b/update_data"
    return await request_via_uds("POST", url, json_data=data)

# Route pour supprimer des données (utilisateurs classiques et superusers)
@app.delete("/delete_data")
async def delete_data(data: dict, token: dict = Depends(authenticate)):
    url = "http://service_b/delete_data"
    return await request_via_uds("DELETE", url, json_data=data)
