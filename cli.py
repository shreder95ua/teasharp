import click
from teasharp.interpreter import interpret

@click.command()
@click.argument('path', type = click.Path(exists = True), required = False)
def main(path):
    interpret(path)