"""
Functions of the spellnum module.
"""

from __future__ import absolute_import, division, print_function

import re
from spellnum import lexicon
from spellnum import messages


__RE_X_EXCEPTION = re.compile(r'(?<=^se)(?=[co])')
__RE_S_EXCEPTION = re.compile(r'(?<=^se)(?=[qtv])|(?<=^tre)(?=[coqtv])')
__RE_M_EXCEPTION = re.compile(r'(?<=^septe)(?=[ov])|(?<=^nove)(?=[ov])')
__RE_N_EXCEPTION = re.compile(r'(?<=^septe)(?=[cdqst])|(?<=nove)(?=[cdqst])')
__RE_BASE_ILLION = re.compile(r'^(?P<sign>[-+]?)0*?(?P<value>\d{1,3})$')
__RE_FLOAT_DEC = re.compile(r'^(?P<sign>[-+]?)(?P<whole>\d*)\.?(?P<frac>\d*[1-9]+)?0*$')
__RE_FLOAT_SCI = re.compile(r'^(?P<sign>[-+]?)(?P<base>(?P<whole>\d*)\.?(?P<frac>\d*))[eE](?P<exp>[-+]?\d+)$')


def get_period_suffix(base_illion):
    """
    Constructs the period suffix/name from tuples of lexical components
    using each digit in the given base-illion value; currently limited
    to base-illion values less than 1000 (millinillion).
    
    :param base_illion: The base-illion value of the period name
    :return str: The suffix for the period with the given base-illion
    """
    # capture any numerical integer string input
    base_illion = int(str(base_illion)) if re.match(__RE_BASE_ILLION, str(base_illion)) else base_illion
    
    # catch input outside function capabilities
    if base_illion not in range(-1, 1000, 1):
        raise ValueError(messages.ERROR_INVALID_BASEILLION)
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
        result = re.sub(__RE_X_EXCEPTION, repl='x', string=result)
        result = re.sub(__RE_S_EXCEPTION, repl='s', string=result)
        result = re.sub(__RE_M_EXCEPTION, repl='m', string=result)
        result = re.sub(__RE_N_EXCEPTION, repl='n', string=result)
        
    return result.replace('allion', 'illion')


def spell_number(number):
    """
    Constructs the English short-scale spelling of the given number.
    
    :param any number: a number to be spelt
    :return str: the spelling of the given number as a string
    """
    # sterilize input as string and pad if necessary
    number = '0' + str(number) if str(number).startswith('.') else str(number)
    
    # parses input if given in scientific notation
    sci_match = re.match(__RE_FLOAT_SCI, number)
    if sci_match:
        digits = sci_match.group('base').replace('.', '')
        # shift decimal and pad with zeros where necessary
        shift = int(sci_match.group('exp'))
        position = sci_match.start('frac') + shift
        number = (f'{sci_match.group("sign")}'
                  f'{digits[:position]}{"".zfill(abs(max(shift - len(sci_match.group("frac")), 1)))}.'
                  f'{"".zfill(abs(min(len(sci_match.group("whole")) + shift, 0)))}{digits[position:]}')
        
    # catch invalid decimal strings
    dec_match = re.match(__RE_FLOAT_DEC, number)
    if not dec_match:
        raise ValueError(messages.ERROR_INVALID_NUMBER + number)
    
    # catch negative numbers
    if dec_match.group('sign') == '-':
        return f'negative {spell_number(number[1:])}'
    
    result = str()
    # split number into list of periods
    periods = f'{int(dec_match.group("whole") or 0):,}'.split(',')
    # calculate base-illion value
    base_illion = len(periods) - 2
    # construct spelling for the whole number component
    for period in (int(period) for period in periods):
        result += f' {lexicon.INTEGERS_LT_1000[period]} {get_period_suffix(base_illion)}'.rstrip() if period > 0 else ''
        base_illion -= 1
        
    # append spelling for any fraction component
    fraction = dec_match.group('frac')
    result += (f"{' and ' if result else ''}{spell_number(fraction)} "
               f"{spell_number(f'1{str().zfill(len(fraction))}')}th"
               f"{'s' if spell_number(fraction) != 'one' else ''}") if fraction else ''
    
    return result.strip() or 'zero'
