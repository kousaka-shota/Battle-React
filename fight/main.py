from fastapi import FastAPI,Depends
from routers import equipment,sensor
import models
import database

app  = FastAPI()
app.include_router(equipment.router)
app.include_router(sensor.router)

models.Base.metadata.create_all(bind=database.engine)

@app.get("/")
async def get_index():
    return {"message":"はいれたねぇ"}