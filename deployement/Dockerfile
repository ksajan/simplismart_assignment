FROM python:3.10-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
  curl \
  git \
  gcc \
  make \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /simplismart

# Copy the server scripts from the deployment directory
COPY deployement/server-llm.sh /simplismart/server-llm.sh
COPY deployement/api-server.sh /simplismart/api-server.sh

# Copy the rest of the application code
COPY . /simplismart
RUN ls
# Install Python dependencies for the API server
RUN pip install --no-cache-dir -r requirements.txt

# Make the server scripts executable
RUN chmod +x server-llm.sh api-server.sh

# Expose relevant ports
EXPOSE 8888 
EXPOSE 8000

# Set a default command to prevent the container from exiting immediately
CMD ["bash"]

