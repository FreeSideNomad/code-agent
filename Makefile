.PHONY: install test lint format clean help check

help:
	@echo "Available commands:"
	@echo "  install    - Sync dependencies with uv"
	@echo "  lint       - Run linters (ruff, mypy)"
	@echo "  format     - Format code (ruff)"
	@echo "  test       - Run tests (pytest)"
	@echo "  check      - Run all checks"
	@echo "  clean      - Cleanup artifacts"

install:
	uv sync --all-extras --dev
	uv run pre-commit install

test:
	uv run pytest tests/ --cov=src/code_agent --cov-report=term-missing

lint:
	uv run ruff check .
	uv run ruff format --check .
	uv run mypy src/code_agent

format:
	uv run ruff format .
	uv run ruff check --fix .

check: lint test

clean:
	rm -rf .pytest_cache .coverage .mypy_cache build dist *.egg-info .venv
	find . -name "*.pyc" -delete
	find . -name "__pycache__" -delete