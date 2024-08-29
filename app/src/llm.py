from requests import request

from app.initilizer import ENV_VARS


class LLM:
    def __init__(self):
        pass

    def health_check(self) -> bool:
        response = request.get(f"{ENV_VARS.LAMMACPP_BASE_URL.value}/health")
        if response.status_code == 200 and response.json()["status"] == "ok":
            return True
        return False

    def predict_completion(self, prompt: str, **kwargs) -> tuple[str, bool]:
        data = {}
        if kwargs:
            data = kwargs
        data["prompt"] = prompt
        response = request.post(
            f"{ENV_VARS.LAMMACPP_BASE_URL.value}/completion",
            headers={"Content-Type": "application/json"},
            json=data,
        )
        if response.status_code == 200:
            return response.json().get("content"), True
        return "Error in completion", False

    def tokenize_input(self, prompt: str, **kwargs) -> str:
        pass

    def detokenize_output(self, output: str, **krwargs) -> str:
        pass

    def embedding(self, text: str, **kwargs) -> str:
        pass

    def infill(self, prefix: str, suffix: str, *kwargs) -> str:
        pass

    def get_server_info(self) -> str:
        pass
