from __future__ import absolute_import, division, print_function


NUMB_LT_TWENTY = ('', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine',
                  "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen")
TENS_GE_TWENTY = ("", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety")
UNIQUE_PERIODS = ("thousand", "million", "billion", "trillion", "quadrillion", "quintillion", "sextillion", "septillion", "octillion", "nonillion")
PERIOD_PREFIXES_UNIT = ("", "un", "duo", "tre", "quattuor", "quinqua", "se", "septe", "octo", "nove")
PERIOD_PREFIXES_TENS = ("", "deci", "viginti", "triginta", "quadraginta", "quinquaginta", "sexaginta", "septuaginta", "octoginta", "nonaginta")
PERIOD_PREFIXES_HUND = ("", "centi", "ducenti", "trecenti", "quadringenti", "quingenti", "sescenti", "septingenti", "octingenti", "nongenti")

ERROR_INVALID_PERIOD = 'period must be an integer in the range [0, 1000)'
ERROR_INVALID_BASEILLION = 'baseillion must be an integer in the range [-1, 1000)'


def get_period_suffix(baseillion):
    """
    Constructs and the period name/suffix from a three dimensional table of prefixes for each digit in the given base-illion
    value; currently limited to base-illions less than 1000 (millinillion)
    
    :param baseillion: the base-illion value of the period
    :return: the name of the period with the given base-illion as a string
    """
    if not baseillion in range(-1, 1000, 1):
        raise ValueError(ERROR_INVALID_BASEILLION)
    if baseillion < 0:
        return ''
    if baseillion < 10:
        return UNIQUE_PERIODS[baseillion]

    unit_prefix = PERIOD_PREFIXES_UNIT[(baseillion % 10) // 1]
    tens_prefix = PERIOD_PREFIXES_TENS[(baseillion % 100) // 10]
    hund_prefix = PERIOD_PREFIXES_HUND[(baseillion % 1000) // 100]
    result = "{0}{1}{2}llion".format(unit_prefix, tens_prefix, hund_prefix)

    if not str(unit_prefix).endswith('e'):
        return result.replace("allion", "illion")
    if 'sec' in result or 'seo' in result:
        unit_prefix += 'x'
    if 'seq' in result or 'set' in result or 'sev' in result:
        unit_prefix += 's'
    if 'trec' in result or 'treo' in result or 'treq' in result or 'tret' in result or 'trev' in result:
        unit_prefix += 's'
    if 'septeo' in result or 'septev' in result:
        unit_prefix += 'm'
    if 'septec' in result or 'septed' in result or 'septeq' in result or 'septes' in result or 'septet' in result:
        unit_prefix += 'n'
    if 'noveo' in result or 'novev' in result:
        unit_prefix += 'm'
    if 'novec' in result or 'noved' in result or 'noveq' in result or 'noves' in result or 'novet' in result:
        unit_prefix += 'n'

    return "{0}{1}{2}llion".format(unit_prefix, tens_prefix, hund_prefix).replace("allion", "illion")


def _spell_period(period):
    """
    Constructs the English spelling of the given integer
    
    :param period: a positive integer less than 1000
    :return: the spelling of the given integer as a string
    """
    if period not in range(0, 1000, 1):
        raise ValueError(ERROR_INVALID_PERIOD)

    unit = period % 10
    tens = period % 100 - unit
    hund = period - tens - unit

    prefix = '{0} hundred'.format(NUMB_LT_TWENTY[hund//100]) if hund else ''
    suffix = '{0}-{1}'.format(TENS_GE_TWENTY[tens//10], NUMB_LT_TWENTY[unit]).strip('-')

    if tens < 20:
        suffix = NUMB_LT_TWENTY[tens + unit]

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

    result = str()
    number = '{:,}'.format(int(number))
    periods = number.split(',')
    baseillion = len(periods) - 2

    for period in periods:
        name = get_period_suffix(baseillion=baseillion)
        spelling = _spell_period(period=int(period))

        if int(period): # if the period is not '000'
            result += ' {0} {1}'.format(spelling, name)

        baseillion -= 1

    return result.strip() or 'zero'
