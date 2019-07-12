"""
Separate home for useful, precompiled regular expressions.

Attributes:
    NUMERIC_STRING_PATTERN (Pattern): Pre-compiled regular expression
        for capturing numerical elements of a number-like string.
        
    FRACTION_TEXT_PATTERN (Pattern): Pre-compiled regular expression
        for capturing specific segments of number text.
        
    PERIOD_TEXT_PATTERN (Pattern): Pre-compiled regular expression
        for capturing the value and name of each period in each segment
        of numeric text.
        
"""

import re as __re


NUMERIC_STRING_PATTERN = __re.compile((r'^(?P<sign>[-+])?(?# capture sign if exists)'
                                       r'0*(?# match, but exclude leading zeros from whole)'
                                       r'(?P<whole>\d+)?(?# capture whole number value)'
                                       r'(?:\.(?# only match fraction following decimal)'
                                       r'(?P<fraction>\d*[1-9])?(?# capture fraction value)'
                                       r'0*)?(?# match, but exclude trailing zeros from fraction)'
                                       r'(?:(?<!\.)[eE](?# only match exponent following e/E)'
                                       r'(?P<exponent>[-+]?\d+))?(?# capture exponent value)'
                                       r'(?<=\d)$(?# number must end in a digit to be valid)'))

FRACTION_TEXT_PATTERN = __re.compile((r'^(?P<whole>.+\w)?(?# capture whole number text)'
                                      r'(?<!th)(?<!ths)(?# whole portion cannot end in th/ths)'
                                      r'(?(whole)(?# if any whole portion is captured...)'
                                      r'(?=\s+and\s+(?# ... anticipate " and " separator ...)'
                                      r'|$)(?# ... or end of string...)|(?# ...otherwise nothing))'
                                      r'(?:\s+and\s+)?(?# match " and " if possible without capturing)'
                                      r'(?:(?P<numerator>.+\w)(?# capture fraction numerator text)'
                                      r'\s+(?# whitespace must separate numerator and denominator)'
                                      r'(?P<denominator>(?# capture fraction denominator text)'
                                      r'(?:\bone\s+hundred|\bten|\bone\b)(?# denominator period value)'
                                      r'\s*\w*)ths?(?# to capture fraction, must end in th/ths)'
                                      r')?$(?# string must end after whole or fraction)'))

# TODO: comment this expression
PERIOD_TEXT_PATTERN = __re.compile((r'(?:^|\s+)(?# )'
                                    r'\b(?P<value>.+?)(?# )'
                                    r'(?:\s+(?# )'
                                    r'(?P<period>\w+illion\b|thousand\b)(?# )'
                                    r'|\s*$)(?# )'))
