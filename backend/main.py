from fastapi import FastAPI
from api.predict import router
import uvicorn



app = FastAPI(title="Churn predict service")
app.include_router(router)


@app.get("/")
async def root():
    return {"api" : "service is running..."}


if __name__ == "__main__":
    uvicorn.run("main:app", port=8080, host = "127.0.0.1")
