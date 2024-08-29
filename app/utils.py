import asyncio
from functools import wraps
from typing import Callable

# Queue to hold incoming requests
request_queue = asyncio.Queue()


def dynamic_batching(batch_size: int = 8, timeout: float = 0.1):
    def decorator(func: Callable):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            # Create a future to hold the response for this request
            response_future = asyncio.get_event_loop().create_future()

            # Put the request data (args, kwargs) and future into the queue
            await request_queue.put((args, kwargs, response_future))

            # Wait for the response (this will be set by the batch processor)
            return await response_future

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

                # Extract arguments and futures from the batch
                args_batch = [item[0] for item in batch]
                kwargs_batch = [item[1] for item in batch]
                futures_batch = [item[2] for item in batch]

                # Call the decorated function with batched inputs
                results = await func(args_batch, kwargs_batch)

                # Handle the responses and set them in their respective futures
                for future, result in zip(futures_batch, results):
                    future.set_result(result)

        # Start the batch processor when the decorator is applied
        asyncio.create_task(batch_processor())

        return wrapper

    return decorator
