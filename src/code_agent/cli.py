
import typer
from rich.console import Console
from rich.panel import Panel

app = typer.Typer(help="Claude Code Agent CLI")
console = Console()

@app.command()
def run(
    task: str = typer.Argument(..., help="The task for the agent to perform"),
    headless: bool = typer.Option(False, "--headless", help="Run without interactive confirmation"),
) -> None:
    """
    Execute a single autonomous task.
    """
    console.print(Panel(f"[bold blue]Starting Task:[/bold blue] {task}"))
    if headless:
         console.print("[yellow]Running in headless mode[/yellow]")
    
    # Placeholder for Agent execution logic
    console.print("[green]Agent initialized (Simulation)[/green]")
    console.print("Thinking...")
    # TODO: Initialize AgentEngine and run loop

@app.command()
def interactive() -> None:
    """
    Start an interactive design or requirement gathering session.
    """
    console.print(Panel("[bold green]Starting Interactive Session[/bold green]"))
    console.print("Hello! I am your Claude Code Agent. What are we building today?")
    # TODO: Start chat loop

@app.command()
def server(
    port: int = typer.Option(8000, help="Port to run the Web API on"),
    host: str = typer.Option("0.0.0.0", help="Host to bind the Web API to")
) -> None:
    """
    Start the Agent Web API server.
    """
    import uvicorn
    console.print(f"[bold green]Starting Web Server on {host}:{port}[/bold green]")
    # We import inside the function to avoid strict dependency on uvicorn if just using CLI
    uvicorn.run("code_agent.server:app", host=host, port=port, reload=True)

@app.callback()
def main(
    verbose: bool = typer.Option(False, "--verbose", "-v", help="Enable verbose output"),
) -> None:
    """
    Code Agent CLI - Your Autonomous Engineering Assistant.
    """
    if verbose:
        console.print("[dim]Verbose mode enabled[/dim]")

if __name__ == "__main__":
    app()
