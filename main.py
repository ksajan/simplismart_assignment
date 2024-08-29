from fastapi import FastAPI
from uvicorn import run

from app.routes.model import model_router

app = FastAPI()

app.include_router(model_router)

if __name__ == "__main__":
    run(app, host="0.0.0.0", port=8000)
