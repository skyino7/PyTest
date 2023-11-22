import typer
from rich.console import Console
from rich.table import Table

console = Console()

app = typer.Typer()


@app.command(short_help='adds an item')
def add(task: str, category: str):
    typer.echo(f"adding {task}, {category}")
    show()


@app.command(short_help='deletes an item')
def delete(position: int):
    typer.echo(f"deleting {position}")
    show()


@app.command(short_help='updates an item')
def update(postion: int, task: str = None,  category: str = None):
    typer.echo(f"updating {postion}")
    show()


@app.command()
def complete(position: int):
    typer.echo(f"complete {position}")
    show()


@app.command()
def show():
    tasks = [("Task1", "Study"), ("Task2", "Read")]
    console.print("[bold magenta]Todos[/bold magenta]")

    table = Table(show_header=True, header_style="bold blue")
    table.add_column("#", style="dim", width=6)
    table.add_column("Todo", min_width=20)
    table.add_column("Category", min_width=20, justify="right")
    table.add_column("Done", min_width=12, justify="right")

    def get_category_color(category):
        COLORS = {'Learn': 'cyan', 'YouTube': 'red',
                  'Read': 'blue', 'Study': 'green'}
        if category in COLORS:
            return COLORS[category]
        return 'white'

    for idx, task in enumerate(tasks, start=1):
        c = get_category_color(task[1])
        is_done_str = 'Done' if True == 2 else 'On it'
        table.add_row(str(idx), task[0], f'[{c}]{task[1]}[/{c}]', is_done_str)
    console.print(table)


if __name__ == "__main__":
    app()
