from fastapi import FastAPI
from routers import equipment

app  = FastAPI()
app.include_router(equipment.router)


@app.get("/")
async def get_index():
    return {"message":"いけたね！"}