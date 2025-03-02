import asyncio

from fastapi import FastAPI

app = FastAPI()

app.include_router(login.router)

@app.get("/")
async def root():
    await asyncio.sleep(0.2)
    return {"Hello": "World"}