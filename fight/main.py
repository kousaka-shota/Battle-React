from fastapi import FastAPI
from routers import equipment
import models
import database

app  = FastAPI()
app.include_router(equipment.router)

models.Base.metadata.create_all(bind=database.engine)


@app.get("/")
async def get_index():
    return {"message":"いけたね！"}