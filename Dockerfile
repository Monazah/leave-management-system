# Base image 
FROM python:3.12-slim

# Setting Working Directory permanently 
WORKDIR /app

# Copying python packages to working Dir inside the container
COPY requirements.txt .

# Installs Dependencies and --no-cache-dir stop pip to keep downloading packages
RUN pip install --no-cache-dir -r requirements.txt

# Copying the project directory to working directory
COPY . .

# Exposing application Port
EXPOSE 8000

# Command to run/Execute Application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]




