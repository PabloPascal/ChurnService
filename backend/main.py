from fastapi import FastAPI
from api.predict import router
from database.db_init import init_db
from contextlib import asynccontextmanager
import uvicorn


@asynccontextmanager
async def lifespan(app : FastAPI):
    await init_db() 
    yield 



app = FastAPI(title="Churn predict service", lifespan=lifespan)
app.include_router(router)


@app.get("/")
async def root():
    return {"api" : "service is running..."}


if __name__ == "__main__":
    uvicorn.run("main:app", port=8080, host = "127.0.0.1")
