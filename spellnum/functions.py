from __future__ import absolute_import, division, print_function

import re
from spellnum import lexicon
from spellnum import messages


def get_period_suffix(base_illion):
    """
    Constructs the period name/suffix from tuples of lexical components using each digit in the given base-illion
    value; currently limited to base-illion values less than 1000 (millinillion)
    
    :param int base_illion: The base-illion value of the period name
    :return str: The suffix for the period with the given base-illion
    """
    # catches input outside function capabilities
    if base_illion not in range(-1, 1000, 1):
        raise ValueError(messages.ERROR_INVALID_BASEILLION)
    elif base_illion == -1:
        return ''
    elif base_illion < 10:
        return lexicon.UNIQUE_PERIODS[base_illion]
    
    # builds suffix from lexical components
    result = '{unit}{tens}{hund}llion'.format(
        unit=lexicon.PERIOD_COMPONENTS_UNIT[(base_illion % 10) // 1],
        tens=lexicon.PERIOD_COMPONENTS_TENS[(base_illion % 100) // 10],
        hund=lexicon.PERIOD_COMPONENTS_HUND[(base_illion % 1000) // 100]
    )
    
    # catches and corrects lexical component combination exceptions
    if lexicon.PERIOD_COMPONENTS_UNIT[(base_illion % 10) // 1] in ('tre', 'se', 'septe', 'nove'):
        result = re.sub('(?<=^se)(?=[co])', repl='x', string=result)
        result = re.sub('(?<=^se)(?=[qtv])|(?<=^tre)(?=[coqtv])', repl='s', string=result)
        result = re.sub('(?<=^septe)(?=[ov])|(?<=^nove)(?=[ov])', repl='m', string=result)
        result = re.sub('(?<=^septe)(?=[cdqst])|(?<=nove)(?=[cdqst])', repl='n', string=result)
    
    return result.replace('allion', 'illion')


def get_period_spelling(period):
    """
    Constructs the English spelling of the given integer
    
    :param int period: a positive integer less than 1000
    :return str: the spelling of the given integer as a string
    """
    # catches invalid input
    if period not in range(0, 1000, 1):
        raise ValueError(messages.ERROR_INVALID_PERIOD)
    
    # splits period into components
    unit = period % 10
    tens = period % 100 - unit
    hund = period - tens - unit
    
    # composes prefix and suffix
    prefix = '{h} hundred'.format(h=lexicon.NUMS_LT_TWENTY[hund//100]) if hund else ''
    suffix = '{t}-{u}'.format(t=lexicon.TENS_GE_TWENTY[tens//10], u=lexicon.NUMS_LT_TWENTY[unit]).strip('-')
    
    # overwrites suffix for special cases
    if tens < 20:
        suffix = lexicon.NUMS_LT_TWENTY[tens + unit]
        
    return '{0} {1}'.format(prefix, suffix).strip()


def spell_number(num):
    """
    Constructs the English short-scale spelling of the given number
    
    :param any num: a number to be spelt
    :return str: the spelling of the given number as a string
    """
    # parses input if given in scientific notation (preserves precession for string inputs)
    sci = re.match('^(?P<base>(?P<whole>\d+)\.?\d*)e\+?(?P<exp>-?\d+)$', string=str(num), flags=re.IGNORECASE)
    if sci:
        pos = sci.end('whole') + int(sci.group('exp'))
        num = sci.group('base').replace('.', '')
        if pos >= len(sci.group('base')):
            num = '{num}{zeros}'.format(num=num, zeros=''.zfill(pos-len(num)))
        elif pos <= 0:
            num = '0.{zeros}{num}'.format(zeros=''.zfill(abs(pos)), num=num)
        else:
            num = num[:pos] + '.' + num[pos:]
            
    # catch invalid num input
    match = re.match('^(-?)0*(\d+)\.?(\d*[1-9]+)?0*$', string=str(num))
    if not match:
        raise ValueError(messages.ERROR_INVALID_NUMBER.format(num=num))
    
    # split number into key components
    sign, whole, fraction = match.group(1, 2, 3)
    
    # catches negative numbers
    if sign == '-' and (int(whole) or int(fraction)):
        return 'negative {spelling}'.format(spelling=spell_number(num=str(num)[1:]))
    
    # splits number into list of periods
    periods = '{w:,}'.format(w=int(whole)).split(',')
    # calculates base-illion value
    base_illion = len(periods) - 2
    
    # constructs spelling for the whole number component
    result = str()
    for period in periods:
        if int(period):
            result += ' {sp} {suf}'.format(
                sp=get_period_spelling(period=int(period)),
                suf=get_period_suffix(base_illion=base_illion)
            ).rstrip()
        base_illion -= 1
        
    # appends spelling for any fraction component
    if fraction is not None:
        numerator = spell_number(fraction)
        denominator = spell_number('{one}{zeros}'.format(one=1, zeros=''.zfill(len(fraction))))
        result += '{a}{num} {den}ths'.format(a=' and ' if result else '', num=numerator, den=denominator)
        
    return result.strip() or 'zero'
