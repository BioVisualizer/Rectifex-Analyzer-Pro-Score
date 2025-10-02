# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Install poetry
RUN pip install --no-cache-dir poetry

# Copy only the dependency definition file to leverage Docker layer caching
COPY pyproject.toml ./

# Generate the lock file based on pyproject.toml
# This ensures a reproducible build inside the container
RUN poetry lock

# Install project dependencies using the generated lock file
# Using --no-root to avoid installing the project itself, as we'll copy the source code in the next step
RUN poetry config virtualenvs.create false && poetry install --no-dev --no-interaction --no-ansi

# Copy the rest of the application's code
COPY ./app ./app

# Expose the port the app runs on
EXPOSE 8000