import typer
from rich.console import Console
from rich.table import Table

console = Console()

app = typer.Typer()


@app.command(short_help='adds an item')
def add(task: str, category: str):
    typer.echo(f"adding {task}, {category}")


@app.command()
def delete(position: int):
    typer.echo(f"deleting {position}")


@app.command()
def update(postion: int, task: str = None,  category: str = None):
    typer.echo(f"updating {postion}")


if __name__ == "__main__":
    app()
