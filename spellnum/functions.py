"""
Functions of the spellnum module.
"""

from re import compile
from spellnum import lexicon


__RE_X_EXCEPTION = compile(r'(?<=^se)(?=[co])')
__RE_S_EXCEPTION = compile(r'(?<=^se)(?=[qtv])|(?<=^tre)(?=[coqtv])')
__RE_M_EXCEPTION = compile(r'(?<=^septe)(?=[ov])|(?<=^nove)(?=[ov])')
__RE_N_EXCEPTION = compile(r'(?<=^septe)(?=[cdqst])|(?<=nove)(?=[cdqst])')

__RE_BASE_ILLION = compile(r'^(?P<sign>[-+]?)0*?(?P<value>\d{1,3})(\.0+)?$')
__RE_VALID_FLOAT = compile((r'^(?P<sign>[-+]?)(?# capture sign if exists)'
                            r'0*(?# match, but exclude leading zeros from whole)'
                            r'(?P<whole>\d+)?(?# capture whole number value)'
                            r'\.?(?# match decimal that may come after whole number)'
                            r'(?P<fraction>(?<=\.)(?# must follow decimal)\d*[1-9])?'
                            r'0*(?# match, but exclude trailing zeros from fraction)'
                            r'(?<!\.)(?# e/E cannot follow decimal without fraction)'
                            r'[eE]?(?# match, but exclude e/E from exponent)'
                            r'(?P<exponent>(?<=[eE])(?# must follow e/E)[-+]?\d+)'
                            r'?(?<=\d)(?# match must end with at least one digit)$'))

__ERROR_INVALID_BASEILLION = 'base-illion must be an integer in the range [-1, 1000)'
__ERROR_INVALID_NUMBER = "we gave it our best, but we don't understand what you meant by "


def get_period_suffix(base_illion):
    """
    Constructs the period suffix/name from tuples of lexical components
    using each digit in the given base-illion value; currently limited
    to base-illion values less than 1000 (millinillion).
    
    :param base_illion: The base-illion value of the period name
    :return str: The suffix for the period with the given base-illion
    """
    # capture any numerical integer string input
    base_illion = int(str(base_illion)) if __RE_BASE_ILLION.match(str(base_illion)) else base_illion
    
    # catch input outside function capabilities
    if base_illion not in range(-1, 1000, 1):
        raise ValueError(__ERROR_INVALID_BASEILLION)
    elif base_illion == -1:
        return ''
    elif base_illion < 10:
        return lexicon.UNIQUE_PERIODS[base_illion]
    
    # build suffix from lexical components
    hund, tens, unit = (int(digit) for digit in str(base_illion).zfill(3))
    result = (f'{lexicon.PERIOD_COMPONENTS_UNIT[unit]}'
              f'{lexicon.PERIOD_COMPONENTS_TENS[tens]}'
              f'{lexicon.PERIOD_COMPONENTS_HUND[hund]}llion')
    
    # catch and correct lexical component combination exceptions
    if lexicon.PERIOD_COMPONENTS_UNIT[unit] in ('tre', 'se', 'septe', 'nove'):
        result = __RE_X_EXCEPTION.sub(repl='x', string=result)
        result = __RE_S_EXCEPTION.sub(repl='s', string=result)
        result = __RE_M_EXCEPTION.sub(repl='m', string=result)
        result = __RE_N_EXCEPTION.sub(repl='n', string=result)
        
    return result.replace('allion', 'illion')


def spell_number(number):
    """
    Constructs the English short-scale spelling of the given number.
    
    :param number: a number to be spelt
    :return str: the spelling of the given number as a string
    """
    # raise exception for invalid numerical input
    match = __RE_VALID_FLOAT.match(str(number).strip())
    if not match:
        raise ValueError(__ERROR_INVALID_NUMBER + str(number))
    
    # collect number components
    sign, whole, fraction, exponent = match.groups(default='')
    
    # parses input if given in scientific notation
    if int(exponent or 0):
        digits = whole + fraction
        position = len(whole) + int(exponent)
        whole, fraction = [digits[:max(position, 0):].ljust(max(position, 1), '0'),
                           digits[max(position, 0)::].rjust(max(len(digits)-position, 1), '0')]
        
    # handle negative numbers recursively
    if sign == '-' and whole + fraction:
        return f'negative {spell_number(f"{whole.zfill(1)}.{fraction.zfill(1)}")}'
    
    # spell the whole potion of the number
    periods = f'{int(whole or 0):,}'.split(',') # splits number into list of periods
    whole = ' '.join([f'{lexicon.INTEGERS_LT_1000[int(p)]} {get_period_suffix(b)}'
                      for b, p in zip(range(len(periods)-2, -2, -1), periods) if int(p) > 0]).strip()
    
    # spell any fractional potion of the number recursively
    fraction = (f"{spell_number(fraction)} {spell_number(10 ** len(fraction))}th"
                f"{'s' if int(fraction) > 1 else ''}") if int(fraction or 0) else ''
    
    return f"{whole}{' and ' if whole and fraction else ''}{fraction}".strip() or 'zero'
