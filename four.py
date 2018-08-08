"""Prints a path to four using the 'cosmic four' algorithm"""

import spellnum


if __name__ == '__main__':
    number = str()
    print('Welcome!')
    while number != 'exit':
        number = raw_input('\n>>\t')
        if number == 'exit':
            continue
        if not number.isdigit():
            print("Enter a number or type 'exit' to quit")
            continue
        while number != 4:
            spelling = spellnum.spell_number(number)
            print('{0:,}: {1}'.format(int(number), spelling))
            number = len(spelling.translate(None, ' -'))
        print('4: four')
    print('\nGoodbye!')
