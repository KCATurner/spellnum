"""
Functions of the spellnum module.
"""

import spellnum.lexicon
import spellnum.regexlib
import spellnum.exceptions


def get_period_suffix(base_illion):
    """
    Constructs the period suffix/name from tuples of lexical components
    using each digit in the given base-illion value; currently limited
    to base-illion values less than 1000 (millinillion).
    
    :param base_illion: the base-illion value of the period name
    :return str: the suffix for the period with the given base-illion
    """
    # capture any numerical integer string input
    if spellnum.regexlib.VALID_NUMERIC_FLOAT.match(str(base_illion)):
        base_illion = float(base_illion)
        
    # catch input outside function capabilities
    if base_illion not in range(-1, 1000, 1):
        raise spellnum.exceptions.BaseIllionOutOfBounds(base_illion)
    elif base_illion == -1:
        return ''
    elif base_illion < 10:
        return spellnum.lexicon.UNIQUE_PERIODS[int(base_illion)]
    
    # build suffix from lexical components
    hund, tens, unit = (int(digit) for digit in str(int(base_illion)).zfill(3))
    result = spellnum.lexicon.PERIOD_COMPONENTS_UNIT[unit]\
             + spellnum.lexicon.PERIOD_COMPONENTS_TENS[tens]\
             + spellnum.lexicon.PERIOD_COMPONENTS_HUND[hund] + 'llion'
    
    # catch and correct lexical component combination exceptions
    if spellnum.lexicon.PERIOD_COMPONENTS_UNIT[unit] in ('tre', 'se', 'septe', 'nove'):
        result = spellnum.regexlib.X_LEXICAL_EXCEPTION.sub(repl='x', string=result)
        result = spellnum.regexlib.S_LEXICAL_EXCEPTION.sub(repl='s', string=result)
        result = spellnum.regexlib.M_LEXICAL_EXCEPTION.sub(repl='m', string=result)
        result = spellnum.regexlib.N_LEXICAL_EXCEPTION.sub(repl='n', string=result)
        
    return result.replace('allion', 'illion')


def num2txt(number):
    """
    Constructs the English short-scale spelling of the given number.
    
    :param number: an int float or numeric string to be spelled
    :return str: the spelling of the given number as a string
    """
    # raise exception for invalid numerical input
    match = spellnum.regexlib.VALID_NUMERIC_FLOAT.match(str(number).strip())
    if not match:
        raise spellnum.exceptions.InvalidNumericalFormat(str(number))
    
    # collect number components
    sign, whole, fraction, exponent = match.groups(default='')
    
    # parses input if given in scientific notation
    if int(exponent or 0):
        digits = whole + fraction
        position = len(whole) + int(exponent)
        whole = digits[:max(position, 0):].ljust(max(position, 1), '0')
        fraction = digits[max(position, 0)::].rjust(max(len(digits)-position, 1), '0')
        
    # handle negative numbers recursively
    if sign == '-' and whole + fraction:
        return 'negative ' + num2txt('{}.{}'.format(whole.zfill(1), fraction.zfill(1)))
    
    # spell the whole potion of the number
    periods = '{:,}'.format(int(whole or 0)).split(',') # splits number into list of periods
    whole = ' '.join([spellnum.lexicon.INTEGERS_LT_1000[int(p)] + ' ' + get_period_suffix(b)
                      for b, p in zip(range(len(periods)-2, -2, -1), periods) if int(p) > 0]).strip()
    
    # spell any fractional potion of the number recursively
    fraction = '{} {}th{}'.format(num2txt(fraction),
                                  num2txt(10 ** len(fraction)),
                                  's' if int(fraction) > 1 else '') if int(fraction or 0) else ''
    
    # return resulting spelling or 'zero' if nothing was spelled
    return whole + (' and ' if whole and fraction else '') + fraction or 'zero'


def txt2num(spelling):
    """"""
    # handle negatives recursively
    if spelling.startswith('negative'):
        return '-{}'.format(txt2num(spelling.replace('negative', '', 1)))
    
    whole = spelling.strip()
    match = spellnum.regexlib.FRACTION_SPELLING_FORMAT.match(whole)
    if match: # handle fractions recursively
        whole, numerator, denominator = match.groups(default='')
        numerator, denominator = int(txt2num(numerator)), int(txt2num(denominator))
        return '{}.{}'.format(int(txt2num(whole)) + (numerator // denominator),
                              str(numerator % denominator).zfill(str(denominator).count('0')))
    
    suffixes = spellnum.lexicon.UNIQUE_PERIODS \
               + tuple(get_period_suffix(b) for b in range(21, 1000))
    
    result = 0
    period = list()
    for word in str(spelling).split():
        if word not in ('hundred',) + spellnum.lexicon.INTEGERS_LT_100:
            # TODO: raise more meaningful exception on index failure...
            value = spellnum.lexicon.INTEGERS_LT_1000.index(' '.join(period))
            result += value * (10**((suffixes.index(word) + 1) * 3))
            period = list()
        else:
            period.append(word)
            
    result += spellnum.lexicon.INTEGERS_LT_1000.index(' '.join(period))
    return str(result)
