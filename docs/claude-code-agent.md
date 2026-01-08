# Building Claude Code Agents

This document outlines the research and approach for implementing Python-based software engineering agents using the Claude Code Agent SDK (Anthropic API & Tools).

## Core Technologies

1.  **Anthropic Python SDK (`anthropic`)**: The official library to interact with Claude models (e.g., Claude 3.5 Sonnet).
2.  **Tool Use (Function Calling)**: Claude's ability to invoke client-side tools is central to creating "agents".
3.  **Model Context Protocol (MCP)**: A standard for connecting AI models to data and tools. This is crucial for standardized integrations with Git, Databases, etc.

## Architecture Patterns

### 1. The Tool-Using Agent Loop
A basic autonomous agent operates in a loop:
1.  **Think**: Analyze the user's task and current context.
2.  **Act**: Decide to call a tool (e.g., `read_file`, `run_git_command`) or provide a final answer.
3.  **Observe**: Execute the tool and feed the output back to Claude.
4.  **Repeat**: Continue until the task is complete.

### 2. Implementation with Python (Async/FastAPI)

The application will be structured to support both CLI workers and a Web API.

#### Dependencies
- `anthropic`: For API interaction.
- `fastapi`: For the web interface.
- `typer` or `click`: For the CLI.
- `asyncio`: For concurrent operations.
- `pydantic`: For data validation and schema definition (essential for Tool definitions).

#### Agent Lifecycle
- **Initialization**: Load context, system prompts, and available tools.
- **Execution**: The `run` loop that handles the conversation history and tool execution.
- **State Management**: Persisting conversation history and state in PostgreSQL.

## Integration Strategies

### Git Integration
- **Local CLI**: The agent uses `subprocess` to run git commands in the local repo.
- **Git Hooks**: The CLI can be invoked by git hooks (e.g., `pre-commit`) to check code or generate commit messages.
- **API**: Using libraries like `GitPython` or direct shell commands to manipulate repositories.

### Autonomous Capabilities
To enable autonomy, the agent needs:
- **Planning**: Ability to break down complex tasks.
- **Memory**: Short-term (context window) and Long-term (vector DB or summary in Postgres).
- **Safety**: Sandboxed execution for file writes and command execution.

## Example: Agent "Step" Logic

```python
async def agent_step(messages, tools):
    response = await client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=1024,
        messages=messages,
        tools=tools
    )
    
    if response.stop_reason == "tool_use":
        # Execute tools and append results to messages
        ...
    else:
        # Return final answer
        ...
```

## References
- [Anthropic Tool Use Documentation](https://docs.anthropic.com/en/docs/build-with-claude/tool-use)
- [Model Context Protocol](https://modelcontextprotocol.io/)
