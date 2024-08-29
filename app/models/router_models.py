from pydantic import BaseModel


class InputData(BaseModel):
    input_data: int


class OutputData(BaseModel):
    request_id: str
    output_data: str
