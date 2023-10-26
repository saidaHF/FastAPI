# Use the official Python 3.10 image
FROM python:3.10

# Set the working directory to /app
WORKDIR /app

# Copy the requirements files to the container
COPY requirements.txt .

# Install project dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the API source code into the container
COPY src/ .

# Expose the port on which the API will run
EXPOSE 8080

# Define the command to run the API
CMD ["uvicorn", "__init__:app", "--host", "0.0.0.0", "--port", "8080"]

# RUN for depurated
RUN cat requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt