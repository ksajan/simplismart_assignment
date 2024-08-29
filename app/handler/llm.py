from fastapi.exceptions import HTTPException

from app.models.llm_models import LlamaCppCompletionOptions
from app.src.llm import LLM
from app.utils import dynamic_batching

GENERIC_MODEL_CLASS = LLM()


@dynamic_batching(batch_size=4, timeout=0.1)
def predict_completion(options: LlamaCppCompletionOptions):
    prompt = options.prompt
    output, status = GENERIC_MODEL_CLASS.predict_completion(
        prompt,
        **options.model_dump(
            exclude={"prompt"}, exclude_unset=True, exclude_defaults=True
        )
    )
    if status:
        return {"prediction": output, "status": "success"}
    return HTTPException(status_code=500, detail="Error in completion")
