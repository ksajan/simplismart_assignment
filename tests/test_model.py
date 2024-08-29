from fastapi import HTTPException
from fastapi.testclient import TestClient
from your_module_name import (  # Replace with your actual module name
    LlamaCppCompletionOptions,
    app,
)

client = TestClient(app)


def test_completion_capital_of_india():
    # Create the request payload with the prompt "Name the capital of India in one word"
    request_payload = {
        "prompt": "Name the capital of India in one word"
        # Add other necessary fields from LlamaCppCompletionOptions if needed
    }

    # Make a POST request to the /predict endpoint
    response = client.post("/predict", json=request_payload)

    # Check if the request was successful
    assert response.status_code == 200

    # Parse the response JSON
    response_data = response.json()

    # Ensure the response includes the correct structure
    assert "prediction" in response_data
    assert response_data["status"] == "success"
    # Optionally, check the content of the prediction
    # assert response_data["prediction"] == "Delhi"  # Assuming the model returns "Delhi"


def test_completion_hello_world():
    # Create the request payload with the prompt "Hello, world!"
    request_payload = {
        "prompt": "Hello, world!"
        # Add other necessary fields from LlamaCppCompletionOptions if needed
    }

    # Make a POST request to the /predict endpoint
    response = client.post("/predict", json=request_payload)

    # Check if the request was successful
    assert response.status_code == 200

    # Parse the response JSON
    response_data = response.json()

    # Ensure the response includes the correct structure
    assert "prediction" in response_data
    assert response_data["status"] == "success"
    # Optionally, check the content of the prediction
    # assert response_data["prediction"] == "Expected completion here"
