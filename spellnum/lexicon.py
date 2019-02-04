"""
Separate home for lexical components used by spellnum functions.
"""

# index-aligned unique spellings
UNIQUE_WORDS = tuple(['', 'one', 'two', 'three', 'four',
                      'five', 'six', 'seven', 'eight', 'nine',
                      'ten', 'eleven', 'twelve', 'thirteen', 'fourteen',
                      'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen',
                      'twenty', *['']*9, 'thirty', *['']*9, 'forty', *['']*9, 'fifty', *['']*9,
                      'sixty', *['']*9, 'seventy', *['']*9, 'eighty', *['']*9, 'ninety', *['']*9])

# index-aligned 2 digit spellings
INTEGERS_LT_100 = tuple([*UNIQUE_WORDS[:20], *((f'{UNIQUE_WORDS[10*(i//10)]}-'
                                                f'{UNIQUE_WORDS[i%10]}').strip('-') for i in range(20, 100))])

# index-aligned 3 digit spellings
INTEGERS_LT_1000 = tuple([*((f"{INTEGERS_LT_100[i//100] + ' hundred' if i >= 100 else ''} "
                             f"{INTEGERS_LT_100[i%100]}").strip() for i in range(1000))])

UNIQUE_PERIODS = ('thousand', 'million', 'billion', 'trillion', 'quadrillion',
                  'quintillion', 'sextillion', 'septillion', 'octillion', 'nonillion')

PERIOD_COMPONENTS_UNIT = ('', 'un', 'duo', 'tre', 'quattuor',
                          'quinqua', 'se', 'septe', 'octo', 'nove')

PERIOD_COMPONENTS_TENS = ('', 'deci', 'viginti', 'triginta', 'quadraginta',
                          'quinquaginta', 'sexaginta', 'septuaginta', 'octoginta', 'nonaginta')

PERIOD_COMPONENTS_HUND = ('', 'centi', 'ducenti', 'trecenti', 'quadringenti',
                          'quingenti', 'sescenti', 'septingenti', 'octingenti', 'nongenti')
