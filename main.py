from fastapi import FastAPI
import random
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow all origins in this example; you can adjust the allowed origins, methods, headers, etc., as needed.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "ja esta caralho", 'data': 0}

@app.post("/data/")
async def create_data(data: dict):
    # Do something with the received data
    # For example, you can save it to a database or process it in any way you need.
    # In this example, we'll just return the received data as a response.
    print(data)
    return {"message": "Data received successfully!", "data": data}
