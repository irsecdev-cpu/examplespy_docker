# ExamplesPy Docker Project v1.0.0 🚀

A security-hardened, containerized Python system for XML data processing and visualization, optimized for high-performance development.

## 🛡️ Security Features (v1.0.0)
- **Non-Root Execution**: Runs as `appuser` (UID 1000) to prevent container escape.
- **Privilege Hardening**: Configured with `no-new-privileges` to block escalation.
- **Resource Constraints**: Capped at 0.5 CPU and 512MB RAM to prevent DoS.
- **Layer Optimization**: Minimal image size using `.dockerignore` and `python:3.11-slim`.

## 🛠️ Core Features
- **Health Monitoring**: Self-healing checks verifying `output.png` generation.
- **Dev Mode**: Native `docker compose watch` for sub-second code sync.
- **Automated Testing**: Real-time validation via `pytest-watch` (ptw).
- **Entrypoint Guard**: Pre-execution Python syntax validation.

## 📂 Project Structure
- `test1.py`: Plotting & Data Visualization.
- `xml_to_xls.py`: XML to Excel conversion engine.
- `test_logic.py`: Unit tests for business logic.
- `entrypoint.sh`: Lifecycle manager & syntax validator.
- `docker-compose.yml`: Hardened service orchestration.

## 🚀 Getting Started

### 1. Build & Secure
```bash
docker compose build --no-cache

2. Launch Live Development
This mode syncs your local changes into the container instantly:
bash

docker compose watch

Folosește codul cu precauție.
3. Run Automated Tests
bash

docker compose run --rm test-auto

4. XML Conversion Utility
bash

docker compose run --rm converter

🧪 Verification Commands

    Check User: docker compose run --rm app whoami (Should return appuser).
    Check Health: docker ps (Wait 10s for the (healthy) status).
    Check Resources: docker stats (To see memory/CPU limits in action).

🤝 Contribution Guidelines

    Ensure your code passes the Entrypoint Guard (syntax check).
    All new logic must include tests in test_logic.py.
    Verify that the .dockerignore excludes your temporary artifacts before PR.

License: MIT

