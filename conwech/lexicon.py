"""
Separate home for lexical components used by conwech functions.
"""

import conwech.regexlib


NATURAL_NUMBERS_LT_20 = ('', 'one', 'two', 'three', 'four',
                         'five', 'six', 'seven', 'eight', 'nine',
                         'ten', 'eleven', 'twelve', 'thirteen', 'fourteen',
                         'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen')
"""
Tuple of 20 strings where each member is the english word for its index
with the exception of an empty string for 0.
"""

NATURAL_DECADES_LT_100 = ('', 'ten', 'twenty', 'thirty', 'forty',
                          'fifty', 'sixty', 'seventy', 'eighty', 'ninety')
"""
Tuple of 10 strings where each member is the english word for 10 times
its index with the exception of an empty string for 0.
"""


NATURAL_NUMBERS_LT_100 = NATURAL_NUMBERS_LT_20 \
                         + tuple('-'.join((NATURAL_DECADES_LT_100[__ // 10],
                                           NATURAL_NUMBERS_LT_20[__ % 10])
                                          ).strip('-') for __ in range(20, 100))
"""
Tuple of 100 strings where each member is the english word for its
index with the exception of an empty string for 0.
"""


NATURAL_NUMBERS_LT_1000 = NATURAL_NUMBERS_LT_100 \
                          + tuple(' hundred '.join((NATURAL_NUMBERS_LT_100[__ // 100],
                                                    NATURAL_NUMBERS_LT_100[__ % 100])
                                                   ).strip() for __ in range(100, 1000))
"""
Tuple of 1000 strings where each member is the english word for its
index with the exception of an empty string for 0.
"""


_UNIQUE_PERIOD_PREFIXES = ('n', 'm', 'b', 'tr', 'quadr', 'quint',
                           'sext', 'sept', 'oct', 'non')
"""
Unique period prefixes for single digit base-illion values.
"""


_UNIT_PREFIX_COMPONENTS = ('', 'un', 'duo', 'tre', 'quattuor',
                           'quinqua', 'se', 'septe', 'octo', 'nove')
"""
Prefix components for the units digit of a base-illion period.
"""


_TENS_PREFIX_COMPONENTS = ('', 'deci', 'viginti', 'triginta',
                           'quadraginta', 'quinquaginta', 'sexaginta',
                           'septuaginta', 'octoginta', 'nonaginta')
"""
Prefix components for the tens digit of a base-illion period.
"""


_HUND_PREFIX_COMPONENTS = ('', 'centi', 'ducenti', 'trecenti',
                           'quadringenti', 'quingenti', 'sescenti',
                           'septingenti', 'octingenti', 'nongenti')
"""
Prefix components for the hundreds digit of a base-illion period.
"""


def __build_base_illion_prefixes():
    """
    Constructs prefixes for all base-illion periods from subcomponents.
    """
    result = list(_UNIQUE_PERIOD_PREFIXES)
    
    for period in range(10, 1000):
        # build prefix from lexical components
        base_illion = str(period).zfill(3)
        prefix = str(_UNIT_PREFIX_COMPONENTS[int(base_illion[-1])]
                     + _TENS_PREFIX_COMPONENTS[int(base_illion[-2])]
                     + _HUND_PREFIX_COMPONENTS[int(base_illion[-3])])
        
        # catch and correct exceptions
        if int(base_illion[-1]) in (3, 6, 7, 9):
            prefix = conwech.regexlib.PREFIX_COMBINATION_EXCEPTION_X.sub('x', prefix)
            prefix = conwech.regexlib.PREFIX_COMBINATION_EXCEPTION_S.sub('s', prefix)
            prefix = conwech.regexlib.PREFIX_COMBINATION_EXCEPTION_M.sub('m', prefix)
            prefix = conwech.regexlib.PREFIX_COMBINATION_EXCEPTION_N.sub('n', prefix)
            
        # prefix shouldn't end in "a" or "i"
        result.append(prefix.rstrip('ai'))
        
    return tuple(result)


PERIOD_PREFIXES_LT_1000 = __build_base_illion_prefixes()
"""
Prefixes for all base-illion period values.
"""
