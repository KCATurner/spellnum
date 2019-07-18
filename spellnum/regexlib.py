"""
Separate home for useful, pre-compiled regular expressions.

TODO: give reasoning for using regular expressions for spellnum...
"""

import re as __re


NUMBER_LIKE_STRING = __re.compile(
    (r'^\s*(?# match, but exclude any leading whitespace)'
     r'(?P<bsign>[-+])?(?# capture base sign if it exists)'
     r'(?!\s*\.\s*(?:[eE]|$))(?# whole or fraction must match)'
     r'0*(?# match, but exclude leading zeros from base whole)'
     r'(?P<bwhole>\d+)?(?# capture base whole number value)'
     r'(?:\.(?# only match base fraction following decimal)'
     r'(?P<bfraction>\d*[1-9])?(?# capture base fraction value)'
     r'0*)?(?# match, but exclude trailing zeros from base fraction)'
     r'(?:(?<=[.\d])(?# exponent flag must follow a digit or decimal)'
     r'[eE](?# only match exponent preceded by an e/E flag)'
     r'(?P<esign>[-+])?(?# capture exponent sign if exists)'
     r'0*(?# match, but exclude leading zeros from exponent value)'
     r'(?P<evalue>\d+)?)?(?# capture exponent value if exists)'
     r'(?<=[.\d])(?# number must end in a decimal or digit to be valid)'
     r'\s*(?# match, but exclude any trailing whitespace)$')
)
"""
Pattern for matching number-like strings.

This compiled regular expression captures the numerical elements of a
number-like string in the following named capture groups:

``bsign`` (optional) - A '+' or '-' the at the beginning of the string
representing the sign of the base.

``bwhole`` (optional) - Digits before the decimal following the
``bsign`` group or the beginning of the string, ignoring any leading
zeros.

``bfraction`` (optional) - Digits following the decimal and preceding
the exponent indicator ('e' or 'E'), ignoring any trailing zeros.

``esign`` (optional) - A '+' or '-' directly following the exponent
indicator ('e' or 'E') representing the sign of the exponent.

``evalue`` (optional) - Digits following the exponent marker and the
optional ``esign`` group, excluding any leading zeros.
"""


NUMBER_TEXT_FORMAT = __re.compile(
    (r'^(?!\s*$)(?# assert string not empty or only whitespace)'
     r'\s*(?# match but do not capture leading whitespace)'
     r'(?P<whole>.+\w)?(?# capture whole number text)'
     r'(?<!th)(?<!ths)(?# whole portion cannot end in th/ths)'
     r'(?(whole)(?# if any whole portion is captured...)'
     r'(?=\s+and\s+(?# ... anticipate " and " separator ...)'
     r'|\s*$)(?# ... or end of string...)|(?# ...otherwise nothing))'
     r'(?:\s+and\s+)?(?# match " and " if possible without capturing)'
     r'(?:(?P<numerator>.+\w)(?# capture fraction numerator text)'
     r'\s+(?# whitespace must separate numerator and denominator)'
     r'(?P<denominator>(?# capture fraction denominator text)'
     r'(?:\bone\s+hundred|\bten|\bone\b)(?# denominator period value)'
     r'\s*\w*)ths?)?(?# to capture fraction, must end in th/ths)'
     r'\s*$(?# match but do not capture trailing whitespace)')
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
will match and the `whole` will consume the entire string. While,
technically, all groups are optional (lazy) the expression is not
allowed to match an empty or whitespace-only string.
"""


PERIOD_TEXT_FORMAT = __re.compile(
    (r'(?:^|\s+)(?# period must follow whitespace or start of string)'
     r'\b(?P<value>.+?)(?# capture period value and leave the name)'
     r'(?:\s+(?# whitespace must separate period value and name)'
     r'(?P<name>\w+illion\b|thousand\b)(?# capture the period name)'
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
