# Use a lightweight Python image
FROM python:3.11-slim

# Install FastAPI, Uvicorn, and httpx
RUN pip install fastapi uvicorn httpx
# Copy the application code
COPY main.py /app/main.py
# Set the working directory to /app
WORKDIR /app
# Expose UDS path as a volume
VOLUME ["/tmp"]
# Run Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8020"]

LABEL org.opencontainers.image.source=https://github.com/${GITHUB_REPOSITORY}
LABEL org.opencontainers.image.title="My App"
LABEL org.opencontainers.image.description="Image générée automatiquement"
LABEL org.opencontainers.image.licenses=MIT
