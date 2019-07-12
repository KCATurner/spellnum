"""
Separate home for lexical components used by spellnum functions.

Attributes:
    INTEGERS_LT_100 (tuple): index-aligned 2 digit spellings
    INTEGERS_LT_1000 (tuple): index-aligned 3 digit spellings
    COMPOSITE_PERIOD_PREFIXES (tuple): index-aligned prefixes for any base-illion period value
    
    _UNIQUE_WORDS (tuple): index-aligned unique spellings
    _UNIQUE_PERIOD_NAMES (tuple): index-aligned unique period names (base-illion 0-9)
    _PREFIX_COMPONENTS_UNIT (tuple): index-aligned period prefix components for base-illion units
    _PREFIX_COMPONENTS_TENS (tuple): index-aligned period prefix components for base-illion tens
    _PREFIX_COMPONENTS_HUND (tuple): index-aligned period prefix components for base-illion hundreds
    
"""


import re as __re


_UNIQUE_WORDS = ('', 'one', 'two', 'three', 'four',
                 'five', 'six', 'seven', 'eight', 'nine',
                 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen',
                 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen')\
                 + ('twenty',) + ('',)*9 + ('thirty',) + ('',)*9\
                 + ('forty',) + ('',)*9 + ('fifty',) + ('',)*9\
                 + ('sixty',) + ('',)*9 + ('seventy',) + ('',)*9\
                 + ('eighty',) + ('',)*9 + ('ninety',) + ('',)*9

INTEGERS_LT_100 = _UNIQUE_WORDS[:20]\
                  + tuple('{}-{}'.format(_UNIQUE_WORDS[10*(i//10)],
                                         _UNIQUE_WORDS[i % 10]
                                         ).strip('-') for i in range(20, 100))

INTEGERS_LT_1000 = tuple('{} {}'.format(INTEGERS_LT_100[i//100]
                                        + ' hundred' if i >= 100 else '',
                                        INTEGERS_LT_100[i % 100]
                                        ).strip() for i in range(1000))


_UNIQUE_PERIOD_NAMES = ('nillion', 'million', 'billion', 'trillion',
                        'quadrillion', 'quintillion', 'sextillion',
                        'septillion', 'octillion', 'nonillion')

_PREFIX_COMPONENTS_UNIT = ('', 'un', 'duo', 'tre', 'quattuor',
                           'quinqua', 'se', 'septe', 'octo', 'nove')

_PREFIX_COMPONENTS_TENS = ('', 'deci', 'viginti', 'triginta',
                           'quadraginta', 'quinquaginta', 'sexaginta',
                           'septuaginta', 'octoginta', 'nonaginta')

_PREFIX_COMPONENTS_HUND = ('', 'centi', 'ducenti', 'trecenti',
                           'quadringenti', 'quingenti', 'sescenti',
                           'septingenti', 'octingenti', 'nongenti')


# prefix combination exception patterns
__X_LEXICAL_EXCEPTION = __re.compile(r'(?<=^se)(?=[co])')
__S_LEXICAL_EXCEPTION = __re.compile(r'(?<=^se)(?=[qtv])|(?<=^tre)(?=[coqtv])')
__M_LEXICAL_EXCEPTION = __re.compile(r'(?<=^septe)(?=[ov])|(?<=^nove)(?=[ov])')
__N_LEXICAL_EXCEPTION = __re.compile(r'(?<=^septe)(?=[cdqst])|(?<=^nove)(?=[cdqst])')


def __buildprefix(base_illion):
    """ For internal use only! Inaccurate for base_illion outside [10, 1000) """
    
    # build prefix from lexical components
    base_illion = str(base_illion).zfill(3)
    prefix = str(_PREFIX_COMPONENTS_UNIT[int(base_illion[-1])]
                 + _PREFIX_COMPONENTS_TENS[int(base_illion[-2])]
                 + _PREFIX_COMPONENTS_HUND[int(base_illion[-3])])
    
    # catch and correct exceptions
    if int(base_illion[-1]) in (3, 6, 7, 9):
        prefix = __X_LEXICAL_EXCEPTION.sub(repl='x', string=prefix)
        prefix = __S_LEXICAL_EXCEPTION.sub(repl='s', string=prefix)
        prefix = __M_LEXICAL_EXCEPTION.sub(repl='m', string=prefix)
        prefix = __N_LEXICAL_EXCEPTION.sub(repl='n', string=prefix)
        
    # prefix shouldn't end in "a" or "i"
    return prefix.rstrip('ai')


COMPOSITE_PERIOD_PREFIXES = tuple(__s.replace('illion', '') for __s in _UNIQUE_PERIOD_NAMES) \
                            + tuple(__buildprefix(__i) for __i in range(10, 1000))
