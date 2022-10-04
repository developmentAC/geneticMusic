from rich.console import Console
import typer

# create a Typer object to support the command-line interface
cli = typer.Typer()


@cli.command()
def main(param: str = "", myFile: str = ""):
    """determine parameter"""
    console = Console()
    console.print("Welcome to GeneticMusic :sparkles:")
    console.print(f"   myParameter = {param}")
    console.print(":brick:" * 20)

# end of main()
