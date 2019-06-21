"""
Usage: spellnum [OPTIONS] NUMBER

Options:
  --cosmic  Execute the cosmic algorithm.
  --help    Show this message and exit.
"""

import sys
import click
from colorama import init, Fore
from spellnum.functions import spell_number


@click.command()
@click.argument('number')
@click.option('--cosmic', is_flag=True, help='Execute the cosmic algorithm.')
def cli(number, cosmic=False):
    """
    Command line interface for spellnum package.
    """
    
    # because Windows is just the wrong kind of special
    if sys.platform == 'win32':
        init()
        
    spelling = str()
    while spelling != 'four':
        try:
            spelling = spell_number(number)
            if cosmic:
                number = len(spelling.replace('-', '').replace(' ', ''))
                print('There are ', Fore.CYAN, str(number), Fore.RESET,
                      ' letters in ', Fore.LIGHTBLACK_EX, spelling, Fore.RESET, sep='')
            else:
                print(spelling)
                break
        except ValueError as error:
            print(error)
            break
