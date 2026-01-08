.PHONY: install test lint format clean help check

help:
	@echo "Available commands:"
	@echo "  install    - Install dependencies (including dev) and pre-commit hooks"
	@echo "  lint       - Run linters (ruff, mypy) in check mode"
	@echo "  format     - format code (ruff)"
	@echo "  test       - Run tests with pytest"
	@echo "  check      - Run all checks (lint + test)"
	@echo "  clean      - Remove build artifacts"

install:
	pip install -e .[dev]
	pre-commit install

test:
	pytest tests/ --cov=src/code_agent --cov-report=term-missing

lint:
	ruff check .
	ruff format --check .
	mypy src/code_agent

format:
	ruff format .
	ruff check --fix .

check: lint test

clean:
	rm -rf .pytest_cache .coverage .mypy_cache build dist *.egg-info
	find . -name "*.pyc" -delete
	find . -name "__pycache__" -delete
