from fastapi import FastAPI
import httpx

app = FastAPI()
@app.get("/get_data")
async def get_data():
    # Define the path to the Unix Domain Socket
    uds_path = "/tmp/service_b.sock"
    # Use a custom transport to make requests via the UDS
    transport = httpx.AsyncHTTPTransport(uds=uds_path)
    # Standard URL format without http+unix://
    url = "http://service_b/get_data"
    async with httpx.AsyncClient(transport=transport) as client:
        response = await client.get(url)
    return response.json()


@app.post("/add_data")
async def add_data():
    # Define the path to the Unix Domain Socket
    uds_path = "/tmp/service_b.sock"
    # Use a custom transport to make requests via the UDS
    transport = httpx.AsyncHTTPTransport(uds=uds_path)
    # Standard URL format without http+unix://
    url = "http://service_b/add_data"
    async with httpx.AsyncClient(transport=transport) as client:
        response = await client.post(url)
    return response.json()

@app.delete("/delete_data")
async def add_data():
    # Define the path to the Unix Domain Socket
    uds_path = "/tmp/service_b.sock"
    # Use a custom transport to make requests via the UDS
    transport = httpx.AsyncHTTPTransport(uds=uds_path)
    # Standard URL format without http+unix://
    url = "http://service_b/delete_data"
    async with httpx.AsyncClient(transport=transport) as client:
        response = await client.delete(url)
    return response.json()