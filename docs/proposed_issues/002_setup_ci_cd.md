# Issue Proposal: Setup CI/CD Infrastructure

**Title:** [Chore]: Setup CI/CD, Makefile, and Pre-commit Hooks
**Labels:** chore
**Assignee:** (Current Agent)

## Description
To ensure code quality and consistent development environments, we need to establish a robust CI/CD pipeline, a local task runner (`Makefile`), and git hooks (`pre-commit`). This aligns with best practices for modern Python development.

## Tasks
- [ ] Create `Makefile` for common commands (`install`, `lint`, `test`, `run`).
- [ ] Configure `.pre-commit-config.yaml` with `ruff` (lint/format) and `mypy` (types).
- [ ] Create GitHub Action `.github/workflows/test.yml` to run checks on PRs and push to main.
- [ ] Update `pyproject.toml` with `ruff` and `pytest` configurations.
- [ ] Fix any immediate linting/typing errors revealed by the new tooling.

## Definition of Done
- `make lint` runs without error locally.
- `make test` runs tests locally.
- A new PR passes the GitHub Actions checks.
- Pre-commit hooks run automatically on `git commit`.

---

## Technical Details

### 1. Makefile
```makefile
.PHONY: install test lint clean help

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

clean:
	rm -rf .pytest_cache .coverage .mypy_cache build dist *.egg-info
	find . -name "*.pyc" -delete
```

### 2. .pre-commit-config.yaml
```yaml
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.5.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
      - id: check-added-large-files

  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.1.14
    hooks:
      - id: ruff
        args: [ --fix ]
      - id: ruff-format

  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.8.0
    hooks:
      - id: mypy
        additional_dependencies: [types-all]
```

### 3. GitHub Action (.github/workflows/test.yml)
```yaml
name: CI

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: ["3.10", "3.11", "3.12"]

    steps:
    - uses: actions/checkout@v4
    
    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v5
      with:
        python-version: ${{ matrix.python-version }}
        cache: 'pip'
    
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -e .[dev]
        pip install ruff mypy pytest pytest-cov
        
    - name: Lint with Ruff
      run: |
        ruff check .
        ruff format --check .
        
    - name: Type check with Mypy
      run: mypy src/code_agent
      
    - name: Test with Pytest
      run: pytest tests/ --cov=src/code_agent --cov-report=xml
```
