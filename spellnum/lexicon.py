"""
Separate home for lexical components used by spellnum functions.
"""

import re as __re


_UNIQUE_NUMERIC_WORDS = ('', 'one', 'two', 'three', 'four',
                         'five', 'six', 'seven', 'eight', 'nine',
                         'ten', 'eleven', 'twelve', 'thirteen', 'fourteen',
                         'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen') \
                         + ('twenty',) + ('',)*9 + ('thirty',) + ('',)*9 \
                         + ('forty',) + ('',)*9 + ('fifty',) + ('',)*9 \
                         + ('sixty',) + ('',)*9 + ('seventy',) + ('',)*9 \
                         + ('eighty',) + ('',)*9 + ('ninety',) + ('',)*9
"""
Unique words for english numeric text.
"""


INTEGERS_LT_100 = _UNIQUE_NUMERIC_WORDS[:20] \
                  + tuple('-'.join((_UNIQUE_NUMERIC_WORDS[10 * (__i // 10)],
                                    _UNIQUE_NUMERIC_WORDS[__i % 10])
                                   ).strip('-') for __i in range(20, 100))
"""
All 2 digit numeric text combinations.
"""


INTEGERS_LT_1000 = INTEGERS_LT_100 \
                   + tuple(' hundred '.join((INTEGERS_LT_100[__i // 100],
                                             INTEGERS_LT_100[__i % 100])
                                            ).strip() for __i in range(100, 1000))
"""
All 3 digit numeric text combinations.
"""


_UNIQUE_PERIOD_NAMES = ('nillion', 'million', 'billion', 'trillion',
                        'quadrillion', 'quintillion', 'sextillion',
                        'septillion', 'octillion', 'nonillion')
"""
Unique period names (base-illion 0-9).
"""


_PREFIX_COMPONENTS_UNIT = ('', 'un', 'duo', 'tre', 'quattuor',
                           'quinqua', 'se', 'septe', 'octo', 'nove')
"""
Period prefix components for base-illion units.
"""


_PREFIX_COMPONENTS_TENS = ('', 'deci', 'viginti', 'triginta',
                           'quadraginta', 'quinquaginta', 'sexaginta',
                           'septuaginta', 'octoginta', 'nonaginta')
"""
Period prefix components for base-illion tens.
"""


_PREFIX_COMPONENTS_HUND = ('', 'centi', 'ducenti', 'trecenti',
                           'quadringenti', 'quingenti', 'sescenti',
                           'septingenti', 'octingenti', 'nongenti')
"""
Period prefix components for base-illion hundreds.
"""


# prefix combination exception patterns
__X_LEXICAL_EXCEPTION = __re.compile(r'(?<=^se)(?=[co])')
__S_LEXICAL_EXCEPTION = __re.compile(r'(?<=^se)(?=[qtv])|(?<=^tre)(?=[coqtv])')
__M_LEXICAL_EXCEPTION = __re.compile(r'(?<=^septe)(?=[ov])|(?<=^nove)(?=[ov])')
__N_LEXICAL_EXCEPTION = __re.compile(r'(?<=^septe)(?=[cdqst])|(?<=^nove)(?=[cdqst])')


def __buildprefix(base_illion):
    """
    For internal use only! Inaccurate for base-illion outside [10, 1000).
    """
    
    # build prefix from lexical components
    base_illion = str(base_illion).zfill(3)
    prefix = str(_PREFIX_COMPONENTS_UNIT[int(base_illion[-1])]
                 + _PREFIX_COMPONENTS_TENS[int(base_illion[-2])]
                 + _PREFIX_COMPONENTS_HUND[int(base_illion[-3])])
    
    # catch and correct exceptions
    if int(base_illion[-1]) in (3, 6, 7, 9):
        prefix = __X_LEXICAL_EXCEPTION.sub('x', prefix)
        prefix = __S_LEXICAL_EXCEPTION.sub('s', prefix)
        prefix = __M_LEXICAL_EXCEPTION.sub('m', prefix)
        prefix = __N_LEXICAL_EXCEPTION.sub('n', prefix)
        
    # prefix shouldn't end in "a" or "i"
    return prefix.rstrip('ai')


BASE_ILLION_PERIOD_PREFIXES = tuple(__n.replace('illion', '') for __n in _UNIQUE_PERIOD_NAMES) \
                              + tuple(__buildprefix(__i) for __i in range(10, 1000))
"""
Prefixes for all base-illion `period` values.
"""
