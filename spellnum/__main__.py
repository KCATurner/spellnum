"""
usage: spellnum [-h] [-nl] [-c4] number

positional arguments:
  number      a number to spell

optional arguments:
  -h, --help  show this help message and exit
  -nl         delimit periods with newlines
  -c4         execute cosmic four algorithm
"""

import argparse
import spellnum


def main():
    """
    CLI entry point for spellnum
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('number', type=str, help='a number to spell')
    parser.add_argument('-nl', action='store_true', help='delimit periods with newlines')
    parser.add_argument('-c4', action='store_true', help='execute cosmic four algorithm')
    args = parser.parse_args()
    
    print(f'\n\n{__file__}\n\n')
    
    spelling = str()
    number = args.number
    delimiter = '\n' if args.nl else ' '
    while spelling != 'four':
        
        try:
            spelling = spellnum.functions.spell_number(number)
            spelling = spelling.replace('illion ', f'illion{delimiter}')
            spelling = spelling.replace('thousand ', f'thousand{delimiter}')
            print(f'{number}{delimiter if args.nl else ": "}{spelling}')
            number = len(spelling.replace('-', '').replace(' ', ''))
        
        except ValueError as error:
            print(error)
            break
        
        if not args.c4:
            break


if __name__ == '__main__':
    main()
