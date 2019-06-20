"""
Separate home for useful, precompiled regular expressions.
"""

import re as _re


X_LEXICAL_EXCEPTION = _re.compile(r'(?<=^se)(?=[co])')
S_LEXICAL_EXCEPTION = _re.compile(r'(?<=^se)(?=[qtv])|(?<=^tre)(?=[coqtv])')
M_LEXICAL_EXCEPTION = _re.compile(r'(?<=^septe)(?=[ov])|(?<=^nove)(?=[ov])')
N_LEXICAL_EXCEPTION = _re.compile(r'(?<=^septe)(?=[cdqst])|(?<=^nove)(?=[cdqst])')

VALID_NUMERIC_FLOAT = _re.compile((r'^(?P<sign>[-+]?)(?# capture sign if exists)'
                                   r'0*(?# match, but exclude leading zeros from whole)'
                                   r'(?P<whole>\d+)?(?# capture whole number value)'
                                   r'\.?(?# match decimal that may come after whole number)'
                                   r'(?P<fraction>(?<=\.)(?# must follow decimal)\d*[1-9])?'
                                   r'0*(?# match, but exclude trailing zeros from fraction)'
                                   r'(?<!\.)(?# e/E cannot follow decimal without fraction)'
                                   r'[eE]?(?# match, but exclude e/E from exponent)'
                                   r'(?P<exponent>(?<=[eE])(?# must follow e/E)[-+]?\d+)'
                                   r'?(?<=\d)(?# match must end with at least one digit)$'))
