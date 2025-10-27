# Use an official Python image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the rest of the app code
COPY . .

# Install uvicorn explicitly
RUN pip install uvicorn

# Command to start the FastAPI server
CMD ["python", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
