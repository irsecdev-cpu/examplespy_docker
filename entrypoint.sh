#!/bin/bash
set -e

# --- [STEP 1] Syntax Validation ---
# Automatically check all Python files for syntax errors before starting
echo "--- [GUARD] Validating Python syntax..."
python -m py_compile *.py

if [ $? -eq 0 ]; then
    echo "--- [SUCCESS] Syntax check passed! ---"
else
    echo "--- [ERROR] Syntax check failed! Aborting start. ---"
    exit 1
fi

# --- [STEP 2] Execute Command ---
# Execute the CMD from Dockerfile or docker-compose
echo "--- [START] Running: $@ ---"
exec "$@"

