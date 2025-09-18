# 1. Use a more specific base image for reproducible builds
FROM python:3.12-slim-bookworm

# 2. Set the working directory
WORKDIR /app

# 3. Create a non-root user for security
RUN useradd --create-home appuser
USER appuser

# 4. Copy only the requirements file to leverage Docker's layer cache
COPY --chown=appuser:appuser requirements.txt .

# 5. Install Python dependencies, avoiding the cache to keep the image small
RUN pip install --no-cache-dir -r requirements.txt

# 6. Copy the rest of the application code
COPY --chown=appuser:appuser . .

# 7. Define the command to run your application
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app:app"]