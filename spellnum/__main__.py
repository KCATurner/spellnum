"""
Usage: spellnum [OPTIONS] NUMBER

Options:
  --four    Spell recursively to four.
  --help    Show this message and exit.
"""

import sys
import click
from colorama import init, Fore
from spellnum.functions import spell, unspell


@click.command()
@click.argument('number')
@click.option('--four', is_flag=True, help='Spell recursively to four.')
def cli(number, four=False):
    """
    Command line interface for spellnum package.
    """
    
    # because Windows is just the wrong kind of special
    if sys.platform == 'win32':
        init()
        
    spelling = str()
    while spelling != 'four':
        try:
            spelling = spell(number)
            if four:
                number = len(spelling.replace('-', '').replace(' ', ''))
                print('There are ', Fore.CYAN, str(number), Fore.RESET,
                      ' letters in ', Fore.LIGHTBLACK_EX, spelling, Fore.RESET, sep='')
            else:
                print(spelling)
                break
        except ValueError as error:
            print(error)
            break
