import click

from teasharp.interpreter import interpret
from teasharp.utils.help import hlp

@click.command()
@click.argument('path', type = click.Path(exists = True), metavar = '<PATH_TO_TEASHARP_SCRIPT>', required = False)
@click.option('--docs', '-d', help = 'Show the Teasharp language docs.', is_flag = True, required = False)
def main(path: str, docs: bool) -> None:

    '''
        Call the Teasharp interpreter.

        If there's no file path specified, it will call the interpreter in REPL mode.
        
        If there's a file path, it will interpret that file.
    '''

    if docs:
        hlp()
        return

    interpret(path)