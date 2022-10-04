"""Define the command-line interface for the datasummarizer program."""

from pathlib import Path

import typer

from rich.console import Console

cli = typer.Typer()

console = Console()

@cli.command()

def main(
	param: str = "",
    data_file: Path = typer.Option(...),
):
	"""Determine parameters"""
	console.print("Welcome to GeneticMusic :sparkles:")
	console.print(f"   myParameter = {param}")
	console.print(f"   data_file = {data_file}")

	# --> the file was not specified so we cannot continue using program
	if data_file is None:
		console.print("No data file specified!")
		raise typer.Abort()
	# --> the file was specified and it is valid so we should read and check it

	if data_file.is_file():
		console.print("\t [:microscope:] File appears to exist.")
	elif not data_file.exists():
		console.print("The data file does not exist!")

	console.print(":brick:" * 20)

# end of main()
