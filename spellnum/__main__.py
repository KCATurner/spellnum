"""
Usage: spellnum [OPTIONS] NUMBER

Options:
  --cosmic  Execute the cosmic algorithm.
  --help    Show this message and exit.
"""

import click
import spellnum.functions


@click.command()
@click.argument('number')
@click.option('--cosmic', is_flag=True, help='Execute the cosmic algorithm.')
def cli(number, cosmic=False):
    """
    Command line interface for spellnum package.
    """
    spelling = str()
    while spelling != 'four':
        try:
            spelling = spellnum.functions.spell_number(number)
            print('\n{}\n{}'.format(number, spelling))
            number = len(spelling.replace('-', '').replace(' ', ''))
        except ValueError as error:
            print(error)
            break
        if not cosmic:
            break
