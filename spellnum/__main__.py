"""
usage: spellnum [-h] {read,spell,four} ...

positional arguments:
  {read,spell,four}
    read             convert text to number
    spell            convert number to text
    four             spell recursively to four

optional arguments:
  -h, --help         show this help message and exit
"""

from __future__ import print_function

import sys
import pyperclip
from colorama import init, Fore
from argparse import ArgumentParser
from spellnum.lexicon import NATURAL_NUMBERS_LT_100
from spellnum.functions import number2text, text2number


def __read(number, copy=False):
    """ For internal use only! """
    result = text2number(text=number)
    
    if copy:
        pyperclip.copy(result)
    
    print(result)


def __spell(number, copy=False):
    """ For internal use only! """
    result = number2text(number=number)
    
    if copy:
        pyperclip.copy(result)
    
    message = list()
    for word in result.split(sep=' '):
        if word in ('hundred',) + NATURAL_NUMBERS_LT_100:
            message.append(Fore.LIGHTBLACK_EX + word)
        elif word in ('negative', 'and'):
            message.append(Fore.YELLOW + word)
        else: # (period names)
            message.append(Fore.RESET + word)
            
    message = ' '.join(message)
    print(message)


def __four(number, copy=False):
    """ For internal use only! """
    result = spelling = str()
    while spelling != 'four':
        try:
            spelling = number2text(number)
            number = len(spelling.replace('-', '').replace(' ', ''))
            print('There are ', Fore.CYAN, str(number), Fore.RESET,
                  ' letters in ', Fore.LIGHTBLACK_EX, spelling, Fore.RESET, sep='')
        except ValueError as error:
            print(error)
            break
            
    if copy:
        pyperclip.copy(result)
        
        
def cli():
    """
    Command line interface for spellnum package.
    """
    
    # because Windows is just the wrong kind of special
    if sys.platform == 'win32':
        init()
        
    arguments = ArgumentParser(add_help=False)
    arguments.add_argument('number', type=str, help='number or text to convert')
    arguments.add_argument('-c', '--copy', action='store_true', help='copy result to clipboard')
    
    parser = ArgumentParser()
    command = parser.add_subparsers()
    
    read = command.add_parser('read', parents=[arguments], help='convert text to number')
    read.set_defaults(func=__read)
    
    spell = command.add_parser('spell', parents=[arguments], help='convert number to text')
    spell.set_defaults(func=__spell)
    
    four = command.add_parser('four', parents=[arguments], help='spell recursively to four')
    four.set_defaults(func=__four)
    
    inputs = vars(parser.parse_args())
    func = inputs.pop('func')
    func(**inputs)


if __name__ == '__main__':
    cli()
