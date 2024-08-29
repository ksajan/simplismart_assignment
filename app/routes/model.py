from fastapi import APIRouter

from app.handler.llm import predict_completion
from app.models.llm_models import LlamaCppCompletionOptions

model_router = APIRouter()


@model_router.get("/health")
def health_check():
    return {"status": "ok"}


@model_router.get("/predict")
def predict_completion(request_body: LlamaCppCompletionOptions):
    return predict_completion(request_body)
