# **Machine Learning Engineer Assignment**

## **Overview**

This project implements a FastAPI service that serves a Language Model (LLM) with a [medusa](https://github.com/FasterDecoding/Medusa) head, using the `lmsys/vicuna-7b` model. The focus was on optimizing inference speed using the `llama.cpp` library for model quantization and serving. Additionally, dynamic batching was implemented to handle multiple concurrent requests efficiently.

## **Architecture**

The project is structured into two layers:

1. **API Layer**: A FastAPI-based service that handles routing and calls the model server. This layer is designed for optimization, infrastructure distribution, and ease of scalability.
2. **Model Server Layer**: A server built using `llama.cpp` for quantizing and serving the `vicuna-7b` model with 8-bit quantization.

### **Key Technologies Used**

- **FastAPI**: For building the API layer.
- **llama.cpp**: For model quantization and serving.
- **Dynamic Batching**: Implemented in the API layer with a configuration of a batch size of 4 and a 100ms timeout.
- **Docker & Docker Compose**: For containerizing the application and managing dependencies.

## **Challenges and Limitations**

- **Medusa Head Implementation**: While the project successfully integrated an already trained Medusa head model, the training process could not be replicated due to compute limitations.
- **Library Incompatibilities**: Issues with Axolotl and legacy TGI integration hindered progress on training Medusa. These issues have been reported, but solutions were not feasible within the time constraints.
- **Compute Resource Limitations**: The lack of sufficient GPU resources limited the ability to explore alternative approaches like `vLLM` or `TGI`.

## **Instructions**

### **Running Locally**

1. **Environment Setup**:

   - Create and activate a Python 3.10 environment using Conda:
     ```bash
     conda create -n ml-engineer-assignment python=3.10
     conda activate ml-engineer-assignment
     ```

2. **Start the Model Server**:

   - Navigate to the `deployment` directory.
   - Make the server scripts executable:
     ```bash
     chmod +x server-llm.sh api-server.sh
     ```
   - Run the model server:
     ```bash
     bash server-llm.sh
     ```
   - After the model server is up and running, start the API server:
     ```bash
     bash api-server.sh
     ```

3. **Access the API**:
   - Open your browser and go to `http://localhost:8000/docs` to access the API documentation and interact with the completion API.
   - **Note**: Stream responses are not supported due to time constraints.

### **Running with Docker**

1. **Build and Run the Docker Containers**:

   - Use Docker Compose to set up the environment:
     ```bash
     docker-compose -f deployment/docker-compose.yml up
     ```

2. **Access the API**:
   - Once the containers are up, access the API at `http://localhost:8000/docs`.

## **Testing**

- Basic test cases have been added under the `test` folder. These can be run to validate the functionality of the API and ensure everything is working as expected.

To ensure your API works as expected, we've included test cases using `pytest`. You can run these tests easily using the provided shell script.

### Steps to Run the Tests

1. **Make the script executable** (this step is only needed once):

   ```sh
   chmod +x test.sh
   ```

2. **Run the script**

   ```
   ./test.sh
   ```

## **Benchmarking**

The following table summarizes the performance benchmarks achieved under different configurations:

| **Configuration**                   | **Tokens per Second** |
| ----------------------------------- | --------------------- |
| CPU Only (No Optimization)          | 3.9 TPS               |
| CPU with Quantization               | 10.6 TPS              |
| CPU with Medusa Head                | 5.1 TPS               |
| CPU with Quantization + Medusa Head | 13.3 TPS              |

### **Interpretation**

- **Quantization** significantly improved the inference speed from 3.9 TPS to 10.6 TPS.
- The **Medusa Head** alone provided a modest improvement, increasing the speed to 5.1 TPS.
- Combining **Quantization and the Medusa Head** yielded the best performance, achieving 13.3 TPS.
  > 🚨 **Note:** This was performed locally on CPU

## **Achievements**

- Successfully implemented the API layer with FastAPI, integrated `llama.cpp` for model quantization and serving, and implemented dynamic batching for efficient request handling.
- Integrated an existing Medusa head model but could not replicate training due to resource limitations.
- Used the llamma_cpp hosted server on hugging face [gguf_my_repo](https://huggingface.co/spaces/ggml-org/gguf-my-repo) for easier conversion. 

## **Future Work**

- **Medusa Head**: Further work is needed to successfully train the Medusa head model, which was not feasible within the current constraints.
- **Library Exploration**: Given more time and resources, exploring `vLLM` or `TGI` as alternatives to `llama.cpp` for potentially better performance would be a priority.

## **Why `llama.cpp`?**

`llama.cpp` was chosen for this project because it could be successfully built and tested both locally and on Google Colab. Despite some personal challenges during testing, it is a highly rated library known for its stability. However, if more time and GPU resources were available, `vLLM` or `TGI` (which internally uses `vLLM`) would be strong candidates due to their potential performance gains and recent developments in optimizing and serving models.
