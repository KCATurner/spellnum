"""
Functions of the spellnum module.
"""

import spellnum.lexicon
import spellnum.regexlib
import spellnum.exceptions


def nameperiod(base_illion):
    """
    Names the period for the given base-illion value.
    
    Constructs a period name from lexical prefix components using each
    period in the given base-illion value. A base-illion value (b)
    represents a period's exponent (x) where b = (x - 3) / 3.
    
    Args:
        base_illion (int): The base-illion value of the period name.
        
    Returns:
        The name for the period with the given base-illion value.
        
    """
    # a base-illion must be an integer (see docstring)
    if not isinstance(base_illion, int):
        raise TypeError('base_illion argument must be an integer!')
    
    # special cases
    if base_illion <= 0:
        return '' if base_illion else 'thousand'
    
    # generates prefix for each period of the base-illion value
    prefixes = (spellnum.lexicon.PERIOD_PREFIXES_LT_1000[int(p)]
                for p in '{:,}'.format(base_illion).split(','))
    
    # combine prefixes and end with "illion"
    return 'illi'.join(prefixes) + 'illion'


def readperiod(period_name):
    """
    Parses the given period name by indexing a tuple of valid period
    prefix components with the given period name.
    
    Args:
        period_name (str): The period name of any number period.
        
    Returns:
        The base-illion value for the period with the given name.
        
    """
    # handle special cases
    if period_name in ['', 'thousand']:
        return -1 if not period_name else 0
    
    # the name will be easier to parse in its composite parts
    period_prefixes = str(period_name).replace('illion', '').split('illi')
    
    base_illion = ''
    for prefix in period_prefixes:
        # iteration > list comprehension here (for more helpful exceptions)
        if prefix not in spellnum.lexicon.PERIOD_PREFIXES_LT_1000:
            raise spellnum.exceptions.InvalidTextForPeriodName(str(period_name), prefix)
        base_illion += str(spellnum.lexicon.PERIOD_PREFIXES_LT_1000.index(prefix)).zfill(3)
        
    # always return base_illion as int
    return int(base_illion)


def number2text(number):
    """
    Constructs the English short-scale spelling of the given number.
    
    Args:
        number (int, float, str): The number to spell.
        
    Returns:
        The spelling of the given number.
        
    """
    # check for valid input format
    match = spellnum.regexlib.NUMBER_LIKE_STRING.match(str(number))
    if not match:
        raise spellnum.exceptions.InvalidNumberLikeString(number)
    
    # capture and "normalize" components of input number
    bsign, bwhole, bfraction, esign, evalue = match.groups(default='')
    exponent = int(esign + (evalue or '0')) - len(bfraction)
    digits = bwhole + bfraction
    position = len(digits) + exponent
    whole = digits[:max(position, 0)]
    numerator = digits[max(position, 0):]
    
    # handle negative numbers recursively
    if bsign == '-' and digits: # checking digits prevents "negative zero"
        return 'negative ' + number2text(str(number).lstrip('-'))
    
    # pad whole to align periods
    whole = '0'*(3 - (max(position, 0) % 3 or 3)) + whole
    whole += '0'*(3 - (len(whole) % 3 or 3))
    
    periods = list()
    base_illion = max(position - 1, 0) // 3 - 1
    # spell each period value and name individually
    for period in (int(whole[i:i+3]) for i in range(0, len(whole), 3)):
        if period > 0:
            periods.append(' '.join([spellnum.lexicon.NATURAL_NUMBERS_LT_1000[period],
                                     nameperiod(base_illion)]))
        base_illion -= 1
        
    # add whole spelling to output list
    text = [' '.join(periods).strip(), ]
    if numerator: # handle fractions recursively
        denominator = number2text('1e' + str(abs(exponent))) + 'th'
        text.append(' '.join([number2text(numerator), denominator])
                    + ('s' if int(numerator) > 1 else '')) # plurality
        
    # return "<whole> and <fraction>" or "zero" if nothing was spelled
    return ' and '.join(t for t in text if t) or 'zero'


def text2number(text):
    """
    Parses the given English short-scale spelling and returns the
    appropriate numerical value as a string.
    
    Args:
        text (str): The spelling of a number as a string.
        
    Returns:
        A numeric string representing the given spelling.
        
    """
    # handle special case(s)
    if text == 'zero':
        return '0'
    # handle negative numbers recursively
    elif text.lstrip().startswith('negative'):
        return '-' + text2number(text.replace('negative', '', 1))
    
    # check for valid input format
    match = spellnum.regexlib.NUMBER_TEXT_FORMAT.match(str(text))
    if not match:
        raise spellnum.exceptions.UnexpectedNumberTextFormat(text)
    
    # reused iterative functionality
    def iterperiods(number_text):
        for period_value, period_name in spellnum.regexlib.PERIOD_TEXT_FORMAT.findall(number_text):
            
            # raise exception for invalid period values
            if period_value not in spellnum.lexicon.NATURAL_NUMBERS_LT_1000:
                raise spellnum.exceptions.UnrecognizedTextForPeriodValue(period_value, period_name)
            
            # yields pairs of (value, base-illion)
            yield (spellnum.lexicon.NATURAL_NUMBERS_LT_1000.index(period_value),
                   3 * readperiod(period_name) + 3)
            
    # get period information for each portion of input text
    whole, numerator, denominator = [list(iterperiods(t)) for t in match.groups(default='')]
    # correct numerator exponents (this line assumes denominator is a multiple of ten)
    fraction = [(v, e - (denominator[0][1] + str(denominator[0][0]).count('0')))
                for v, e in numerator]
    
    periods = dict()
    # combine whole and fraction for all unique parts
    for value, exponent in (whole + fraction)[::-1]:
        periods[exponent + 3], periods[exponent] = divmod(periods.get(exponent, 0) + value, 1000)
        
    periods = ((str(v), e) for e, v in sorted(periods.items(), reverse=True) if v)
    numbers = [next(periods, ('', 0)), ]
    for value, exponent in periods:
        digits, previous = numbers[-1]
        difference = previous - exponent
        if difference > 10000:
            numbers.append((value, exponent))
        else:
            numbers[-1] = digits + value.zfill(difference), exponent
            
    # return string representing the sum of numbers in normalized scientific notation
    return ' + '.join(v[:1] + ('.' + v[1:]).rstrip('.0') + ('e' + str(e + len(v[1:]))).rstrip('e')
                      for v, e in numbers)
