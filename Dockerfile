# Use official Python image
FROM python:3.12-slim

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    default-libmysqlclient-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy poetry files
COPY pyproject.toml poetry.lock* /app/

# Install poetry
RUN pip install --no-cache-dir "poetry>=2.0"

# Install dependencies via poetry
RUN poetry config virtualenvs.create false \
    && poetry install --no-root --no-dev

# Copy project
COPY . /app

# Expose port
EXPOSE 8000

# Run FastAPI
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
