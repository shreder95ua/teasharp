import click
from teasharp.interpreter import interpret

@click.command()
@click.argument('path', type = click.Path(exists = True), metavar = '<PATH_TO_TEASHARP_SCRIPT>', required = False)
def main(path: str):

    '''
        Call the Teasharp interpreter.

        If there's no file path specified, it will call the interpreter in REPL mode.
        
        If there's a file path, it will interpret that file.
    '''

    interpret(path)