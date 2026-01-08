# Code Agent Design Document

## Overview
`code-agent` is a flexible platform for autonomous software engineering agents. It can run as a standalone CLI tool for local development tasks or as a centralized Web service (FastAPI) managing multiple agent sessions.

## Goals
- **Autonomy**: Agents can plan and execute multi-step engineering tasks.
- **Integration**: Deep integration with Git (CLI and Hooks) and PostgreSQL.
- **Interactivity**: Support for interactive requirements gathering and design sessions.
- **Extensibility**: Configurable agent personas and toolsets.

## System Architecture

### 1. Core Components
- **Agent Engine**: The brain of the system, wrapping the Claude API. It manages the conversation loop, tool execution, and context.
- **Tool Registry**: A modular system to register tools (File I/O, Git, Shell, Search).
- **Memory Module**: Interfaces with PostgreSQL to store session history, user preferences, and project context.

### 2. Interfaces
- **CLI (`cli.py`)**:
  - `agent run <task>`: Executes a one-off task.
  - `agent interactive`: Starts a chat session for requirements/design.
  - `agent hook <hook-type>`: Invoked by git hooks.
- **Web API (`server.py`)**:
  - `POST /agents/tasks`: Submit a background task.
  - `WS /agents/chat`: Real-time websocket for interactive sessions.

### 3. Data Model (PostgreSQL)
- **Sessions**: Stores conversation history.
- **Tasks**: Tracks autonomous background jobs.
- **Artifacts**: Stores generated designs, requirements, or code snippets.

### 4. Technology Stack
- **Language**: Python 3.12+
- **Web Framework**: FastAPI
- **Database**: PostgreSQL (Async via `asyncpg`/`SQLAlchemy`)
- **AI SDK**: Anthropic Python SDK
- **CLI**: Typer
- **Async**: `asyncio` for non-blocking I/O.

## workflows

### CLI Worker (Autonomous)
1. User runs `code-agent run "Refactor the login module"`
2. CLI initializes `AgentEngine` with local file system tools.
3. Agent analyzes the codebase, plans the refactor, and executes changes.
4. Agent runs tests (if instructed) and commits changes.

### Interactive Design Session
1. User runs `code-agent interactive` or connects via Web UI.
2. User: "I need a design for a new inventory system."
3. Agent asks clarifying questions (guided by a "Requirements Analyst" system prompt).
4. Agent generates `docs/inventory-system-design.md` and commits it.

### Git Hook Integration
1. Developer commits code.
2. `pre-commit` hook triggers `code-agent hook review`.
3. Agent analyzes the staged changes.
4. If issues are found, the commit is blocked with feedback.

## Security
- **Sandboxing**: When running in Web mode, file system access must be restricted to specific workspace directories.
- **Confirmation**: High-impact actions (deleting files, force pushing) require explicit user confirmation (CLI) or policy configuration.

## Roadmap
1. **Prototype**: Basic CLI with File/Shell tools and Claude integration.
2. **Persistence**: Add PostgreSQL storage.
3. **Web API**: Expose agent via FastAPI.
4. **Git Deep Dive**: Advanced git integration (PR reviews, branch management).
