from __future__ import absolute_import, division, print_function
from re import sub

__NUMB_LT_TWENTY = ('', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine',
                    'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen')
__TENS_GE_TWENTY = ('', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety')
__UNIQUE_PERIODS = ('thousand', 'million', 'billion', 'trillion', 'quadrillion', 'quintillion', 'sextillion', 'septillion', 'octillion', 'nonillion')
__PERIOD_PREFIXES_UNIT = ('', 'un', 'duo', 'tre', 'quattuor', 'quinqua', 'se', 'septe', 'octo', 'nove')
__PERIOD_PREFIXES_TENS = ('', 'deci', 'viginti', 'triginta', 'quadraginta', 'quinquaginta', 'sexaginta', 'septuaginta', 'octoginta', 'nonaginta')
__PERIOD_PREFIXES_HUND = ('', 'centi', 'ducenti', 'trecenti', 'quadringenti', 'quingenti', 'sescenti', 'septingenti', 'octingenti', 'nongenti')

__ERROR_INVALID_PERIOD = 'period must be an integer in the range [0, 1000)'
__ERROR_INVALID_BASEILLION = 'baseillion must be an integer in the range [-1, 1000)'


def _get_period_suffix(baseillion):
    # type: (int) -> str
    """
    Constructs and the period name/suffix from a three dimensional table of prefixes for each digit in the given
    base-illion value; currently limited to base-illions less than 1000 (millinillion)
    
    :param baseillion: the base-illion suffix of the period name
    :return: the name of the period with the given base-illion as a string
    """
    if baseillion not in range(-1, 1000, 1):
        raise ValueError(__ERROR_INVALID_BASEILLION)
    elif baseillion == -1:
        return ''
    elif baseillion < 10:
        return __UNIQUE_PERIODS[baseillion]
    
    result = '{unit}{tens}{hund}llion'.format(
        unit=__PERIOD_PREFIXES_UNIT[(baseillion % 10) // 1],
        tens=__PERIOD_PREFIXES_TENS[(baseillion % 100) // 10],
        hund=__PERIOD_PREFIXES_HUND[(baseillion % 1000) // 100]
    )
    
    result = sub('(?<=^se)(?=[co])', repl='x', string=result)
    result = sub('(?<=^se)(?=[qtv])|(?<=^tre)(?=[coqtv])', repl='s', string=result)
    result = sub('(?<=^septe)(?=[ov])|(?<=^nove)(?=[ov])', repl='m', string=result)
    result = sub('(?<=^septe)(?=[cdqst])|(?<=nove)(?=[cdqst])', repl='n', string=result)
    
    return result.replace('allion', 'illion')


def _spell_period(period):
    # type: (int) -> str
    """
    Constructs the English spelling of the given integer
    
    :param period: a positive integer less than 1000
    :return: the spelling of the given integer as a string
    """
    if period not in range(0, 1000, 1):
        raise ValueError(__ERROR_INVALID_PERIOD)
    
    unit = period % 10
    tens = period % 100 - unit
    hund = period - tens - unit
    
    prefix = '{0} hundred'.format(__NUMB_LT_TWENTY[hund//100]) if hund else ''
    suffix = '{0}-{1}'.format(__TENS_GE_TWENTY[tens//10], __NUMB_LT_TWENTY[unit]).strip('-')
    
    if tens < 20:
        suffix = __NUMB_LT_TWENTY[tens + unit]
        
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
    baseillion = len(periods) - 2
    
    result = str()
    for period in periods:
        if int(period):
            result += ' {spelling} {name}'.format(
                spelling=_spell_period(period=int(period)),
                name=_get_period_suffix(baseillion=baseillion)
            )
        baseillion -= 1
        
    return result.strip() or 'zero'
