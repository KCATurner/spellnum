"""
Separate home for useful, pre-compiled regular expressions.

TODO: give reasoning for using regular expressions for spellnum...
"""

import re as __re


NUMBER_LIKE_STRING = __re.compile(
    (r'^(?P<sign>[-+])?(?# capture sign if exists)'
     r'0*(?# match, but exclude leading zeros from whole)'
     r'(?P<whole>\d+)?(?# capture whole number value)'
     r'(?:\.(?# only match fraction following decimal)'
     r'(?P<fraction>\d*[1-9])?(?# capture fraction value)'
     r'0*)?(?# match, but exclude trailing zeros from fraction)'
     r'(?:(?<!\.)[eE](?# only match exponent following e/E)'
     r'(?P<exponent>[-+]?\d+))?(?# capture exponent value)'
     r'(?<=\d)$(?# number must end in a digit to be valid)')
)
"""
Pattern for matching number-like strings.

This compiled regular expression captures the numerical elements of a
number-like string in the following named capture groups:

``sign`` (optional) - A '-' or '+' at the beginning of the string.

``whole`` - Digits before the decimal following the `sign` or the
beginning of the string, ignoring leading zeros.

``fraction`` (optional) - Digits following the decimal and
preceding the exponent indicator, ignoring trailing zeros.

``exponent`` (optional) - Digits following the exponent marker.
"""


NUMBER_TEXT_FORMAT = __re.compile(
    (r'^(?P<whole>.+\w)?(?# capture whole number text)'
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
     r')?$(?# string must end after whole or fraction)')
)
"""
Pattern for matching strings of number text.

This compiled regular expression captures the lexical elements
corresponding to the components of the number that the text represents
according to an expected format in the following named capture groups:

``whole`` (optional) - All text following the start of the string and
preceding the end of the string or the 'and' that separates the whole
from the numerator. The whole cannot match the end of the string if it
would match a literal 'th' or 'ths' which indicates there must be a
numerator and denominator in the string.

``numerator`` (co-optional) - All text following either the word 'and'
or the start of the string (in the absence of a matched ``whole``) and
preceding the ``denominator`` match, separated by whitespace.

``denominator`` (co-optional) - The text that starts with one of
'one hundred' / 'ten' / 'one' following the ``numerator`` match and
necessarily ending in 'th' or 'ths' and the end of the string.

The ``numerator`` & ``denominator`` must both match as part of a
non-capturing group representing all of the fraction text or neither
will match and the ``whole`` will consume the entire string. However,
Since the ``whole`` capture group must also be also optional, the
expression `can` match an empty string.
"""


PERIOD_TEXT_FORMAT = __re.compile(
    (r'(?:^|\s+)(?# period must follow whitespace or start of string)'
     r'\b(?P<value>.+?)(?# capture period value and leave the name)'
     r'(?:\s+(?# whitespace must separate period value and name)'
     r'(?P<period>\w+illion\b|thousand\b)(?# capture the period name)'
     r'|\s*$)(?# second option allows period value to end a match)')
)
"""
Pattern for matching individual period substrings in number text.

This compiled regular expression captures the lexical elements
corresponding to the components of a period in a string of number text
in the following named capture groups:

``value`` - All characters following either the start of the string or
a previously matched period name and preceding either the end of the
string or another period name.

``name`` (optional) - A single word following a period value that is
exactly 'thousand' or ends with the 'illion' suffix.
"""
