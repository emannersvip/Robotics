#!/usr/bin/python3

import click

@click.command()
@click.argument("name")
def cli(name):
    click.echo()

if __name__ == "__main__":
    cli()