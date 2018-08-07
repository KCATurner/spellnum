from __future__ import absolute_import, division, print_function

import re
from spellnum import lexicon
from spellnum import messages


def _get_period_suffix(base_illion):
    # type: (int) -> str
    """
    Constructs and the period name/suffix from a three dimensional table of prefixes for each digit in the given
    base-illion value; currently limited to base-illions less than 1000 (millinillion)
    
    :param base_illion: the base-illion suffix of the period name
    :return: the name of the period with the given base-illion as a string
    """
    if base_illion not in range(-1, 1000, 1):
        raise ValueError(messages.ERROR_INVALID_BASEILLION)
    elif base_illion == -1:
        return ''
    elif base_illion < 10:
        return lexicon.UNIQUE_PERIODS[base_illion]
    
    result = '{unit}{tens}{hund}llion'.format(
        unit=lexicon.PERIOD_PREFIXES_UNIT[(base_illion % 10) // 1],
        tens=lexicon.PERIOD_PREFIXES_TENS[(base_illion % 100) // 10],
        hund=lexicon.PERIOD_PREFIXES_HUND[(base_illion % 1000) // 100]
    )
    
    result = re.sub('(?<=^se)(?=[co])', repl='x', string=result)
    result = re.sub('(?<=^se)(?=[qtv])|(?<=^tre)(?=[coqtv])', repl='s', string=result)
    result = re.sub('(?<=^septe)(?=[ov])|(?<=^nove)(?=[ov])', repl='m', string=result)
    result = re.sub('(?<=^septe)(?=[cdqst])|(?<=nove)(?=[cdqst])', repl='n', string=result)
    
    return result.replace('allion', 'illion')


def _get_period_spelling(period):
    # type: (int) -> str
    """
    Constructs the English spelling of the given integer
    
    :param period: a positive integer less than 1000
    :return: the spelling of the given integer as a string
    """
    if period not in range(0, 1000, 1):
        raise ValueError(messages.ERROR_INVALID_PERIOD)
    
    unit = period % 10
    tens = period % 100 - unit
    hund = period - tens - unit
    
    prefix = '{0} hundred'.format(lexicon.NUMS_LT_TWENTY[hund//100]) if hund else ''
    suffix = '{0}-{1}'.format(lexicon.TENS_GE_TWENTY[tens//10], lexicon.NUMS_LT_TWENTY[unit]).strip('-')
    
    if tens < 20:
        suffix = lexicon.NUMS_LT_TWENTY[tens + unit]
        
    return '{0} {1}'.format(prefix, suffix).strip()


def spell_integer(number):
    """
    Constructs the English short-scale spelling of the given integer
    
    :param number: a positive integer to be spelt
    :return: the spelling of the given integer as a string
    """
    number = str(number)
    
    if number == '-0':
        return 'zero'
    if number[0] == '-':
        return 'negative {0}'.format(spell_integer(number=number[1:]))
    
    number = '{:,}'.format(int(number))
    periods = number.split(',')
    base_illion = len(periods) - 2
    
    result = str()
    for period in periods:
        if int(period):
            result += ' {spelling} {name}'.format(
                spelling=_get_period_spelling(period=int(period)),
                name=_get_period_suffix(base_illion=base_illion)
            )
        base_illion -= 1
        
    return result.strip() or 'zero'
