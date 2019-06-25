"""
Usage: spellnum [OPTIONS] NUMBER

Options:
  --four    Spell recursively to four.
  --help    Show this message and exit.
"""

from __future__ import print_function

import sys
import click
import clipboard
from colorama import init, Fore
from spellnum.functions import spell, unspell


@click.command()
@click.argument('number')
@click.option('--four', is_flag=True, help='Spell recursively to four.')
@click.option('--copy', is_flag=True, help='Copy result to clipboard.')
def cli(number, four=False, copy=False):
    """
    Command line interface for spellnum package.
    """
    
    # deduce whether to spell or unspell
    
    
    
    # because Windows is just the wrong kind of special
    if sys.platform == 'win32':
        init()
        
        
    template = ''
    
    
    result = str()
    spelling = str()
    while spelling != 'four':
        
        try:
            spelling = spell(number)
            
            
            message = 'There are {}{}{} letters in {}{}{}'.format(
                Fore.CYAN, str(number), Fore.RESET,
                Fore.LIGHTBLACK_EX, spelling, Fore.RESET,
            )
            
            result += spelling
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
    if copy:
        clipboard.copy(result)
