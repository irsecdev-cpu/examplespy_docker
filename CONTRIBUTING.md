# Contributing to ExamplesPy Docker Project 🤝

Thank you for your interest in contributing! To maintain a high-quality codebase, please follow these guidelines.

## 🛠 Development Environment
This project uses **Docker Compose Watch** to simplify development.
1. Build the environment: `docker compose build`
2. Start development mode: `docker compose watch`

## 🧪 Testing Requirements
Before submitting a Pull Request, ensure that:
- You have added unit tests in `test_logic.py` for any new logic.
- All tests pass: `docker compose run --rm test-auto pytest`
- The `app` container status is **healthy**: `docker compose ps`

## 📝 Commit Message Guidelines
We follow simple, clear commit messages:
- `feat:` for new features.
- `fix:` for bug fixes.
- `docs:` for documentation changes.
- `refactor:` for code changes that neither fix a bug nor add a feature.

## 🚀 Pull Request Process
1. Fork the repository and create your branch from `main`.
2. Ensure your code follows PEP 8 standards.
3. Update `README.md` if you introduced new environment variables or features.
4. Submit the PR with a brief description of the changes.

## 🧹 Housekeeping
- Do **not** commit `output.png`, `report.html`, or `__pycache__` folders. 
- Ensure your `.gitignore` is up to date.

Thank you for helping us improve!
