from rich import print
from rich.console import Console
console = Console()
def lesson011():
    name = console.input("[green]What is your name? ")
    name_length = len(name)
    print(f"Hello, [blue]{name}![/] Your name has [red]{name_length} characters.")
