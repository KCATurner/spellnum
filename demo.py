"""

"""

import argparse
import spellnum


HELP_NUMBER = 'a number to spell'
HELP_NEWLINE = 'delimit periods with newlines'
HELP_COSMIC4 = 'execute cosmic four algorithm'


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('number', type=str, help=HELP_NUMBER)
    parser.add_argument('-nl', action='store_true', help=HELP_NEWLINE)
    parser.add_argument('-c4', action='store_true', help=HELP_COSMIC4)
    args = parser.parse_args()
    
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
