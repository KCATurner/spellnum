"""
Separate home for useful, precompiled regular expressions.
"""

import re as _re


X_LEXICAL_EXCEPTION = _re.compile(r'(?<=^se)(?=[co])')
S_LEXICAL_EXCEPTION = _re.compile(r'(?<=^se)(?=[qtv])|(?<=^tre)(?=[coqtv])')
M_LEXICAL_EXCEPTION = _re.compile(r'(?<=^septe)(?=[ov])|(?<=^nove)(?=[ov])')
N_LEXICAL_EXCEPTION = _re.compile(r'(?<=^septe)(?=[cdqst])|(?<=^nove)(?=[cdqst])')

VALID_NUMERIC_STRING = _re.compile((r'^(?P<sign>[-+])?(?# capture sign if exists)'
                                    r'0*(?# match, but exclude leading zeros from whole)'
                                    r'(?P<whole>\d+)?(?# capture whole number value)'
                                    r'(?:\.(?# only match fraction following decimal)'
                                    r'(?P<fraction>\d*[1-9])?(?# capture fraction value)'
                                    r'0*)?(?# match, but exclude trailing zeros from fraction)'
                                    r'(?:(?<!\.)[eE](?# only match exponent following e/E)'
                                    r'(?P<exponent>[-+]?\d+))?(?# capture exponent value)'
                                    r'(?<=\d)$(?# number must end in a digit to be valid)'))

FRACTION_SPELLING_FORMAT = _re.compile(r'^(?:(?P<whole>.+)\s+and\s+)?(?# " and " separates whole from fraction)'
                                       r'(?P<fnumer>.+\s+)?(?# fraction made of numerator and base-10 denominator)'
                                       r'(?P<fdenom>(?:one hundred|ten|one\s+)(?# denominator period value)'
                                       r'\s*\w*)(?# capture period suffix if exists)'
                                       r'ths?$(?# spelling is only valid if it ends in "th" or "ths")')
