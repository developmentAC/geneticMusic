#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from rich.console import Console
import typer

# create a Typer object to support the command-line interface
cli = typer.Typer()


@cli.command()
def main(myParameter: str = "", myFile: str = ""):
    """determine parameter"""
    console = Console()
    console.print("Welcome to GeneticMusic {:music:}")
    console.print(f"   myParameter = {myParameter}")


# end of main()
