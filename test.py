# from llama_cpp import Llama

# llm = Llama.from_pretrained(
#     repo_id="ksajan/vicuna-7b-v1.3-Q8_0-GGUF", filename="*q8_0.gguf", verbose=False
# )

# output = llm(
#     "Q: Name the planets in the solar system? A: ",  # Prompt
#     max_tokens=32,  # Generate up to 32 tokens, set to None to generate up to the end of the context window
#     stop=[
#         "Q:",
#         "\n",
#     ],  # Stop generating just before the model would generate a new question
#     echo=True,  # Echo the prompt back in the output
# )  # Generate a completion, can also call create_completion
# print(output)

import asyncio
from functools import wraps
from typing import Callable, List

from fastapi import FastAPI, Request
from pydantic import BaseModel

app = FastAPI()

# Queue to hold incoming requests for each endpoint
request_queue = asyncio.Queue()


# Define the model for incoming requests
class InputData(BaseModel):
    input_value: int


# Define the model for the response
class OutputData(BaseModel):
    request_id: int
    output_value: int


# Decorator for dynamic batching
def dynamic_batching(batch_size: int = 5, timeout: float = 10):
    def decorator(func: Callable):
        @wraps(func)
        async def wrapper(input_data: InputData):
            response_future = asyncio.get_event_loop().create_future()
            await request_queue.put((input_data, response_future))
            response = await response_future
            return response

        # Background batch processor
        async def batch_processor():
            while True:
                batch = []
                while len(batch) < batch_size:
                    try:
                        request_data = await asyncio.wait_for(
                            request_queue.get(), timeout=timeout
                        )
                        batch.append(request_data)
                    except asyncio.TimeoutError:
                        break

                if not batch:
                    continue

                inputs = [item[0].input_value for item in batch]
                outputs = await func(inputs)

                for item, output_value in zip(batch, outputs):
                    _, response_future = item
                    response = OutputData(
                        request_id=id(item), output_value=output_value
                    )
                    response_future.set_result(response)

        # Start the batch processor
        @app.on_event("startup")
        async def startup_event():
            asyncio.create_task(batch_processor())

        return wrapper

    return decorator


# Example function to process the batch (replace with actual logic)
@dynamic_batching(batch_size=5, timeout=10)
async def process_batch(inputs: List[int]) -> List[int]:
    # Example processing: doubling each input
    return [input_value * 2 for input_value in inputs]


# Apply dynamic batching to an endpoint
@app.post("/process/")
async def process_request(input_data: InputData):
    return await process_batch(input_data)
