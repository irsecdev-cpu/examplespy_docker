# 1. Base image for a lightweight Python environment
FROM python:3.11-slim

# 2. Install system dependencies and security updates
# Combined commands to reduce layer count and clean cache
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# 3. Create a non-privileged user for security (UID 1000 is standard)
RUN useradd -m -u 1000 appuser

# 4. Set the working directory
WORKDIR /app

# 5. Optimize Pip & Dependencies (CRUCIAL STEP)
# Copy only requirements.txt first to leverage Docker cache
COPY --chown=appuser:appuser requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# 6. Copy the entrypoint script and set execution permissions
COPY --chown=appuser:appuser entrypoint.sh .
RUN chmod +x entrypoint.sh

# 7. Copy the rest of the code (test1.py, test_logic.py, XML data)
# Ensure all files are owned by the non-root user from the start
COPY --chown=appuser:appuser . .

# 8. Switch to the non-privileged user
USER appuser

# 9. Configure the entry point
ENTRYPOINT ["./entrypoint.sh"]

# 10. Default command
CMD ["python", "test1.py"]
