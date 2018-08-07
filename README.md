# Overview
spellnum is a Python module for spelling really large numbers in english using a small combination of functions and some cleverly built tuples. For more information on the large number names and period naming conventions used by this module see the wikipedia page [here](https://en.wikipedia.org/wiki/Names_of_large_numbers).

# Component Files
The spellnum module is currently comprised of three different files: lexicon.py, messages.py, and functions.py.

## lexicon.py
lexicon.py is home to a set of tuples containing number name and period suffix component strings. They are defined in such a way that indexing them will return the appropriate number name or period prefix for the index given (all lowercase). For example, the following code would print the word 'thirteen':
```
>>> from spellnum.lexicon import *
>>> NUMS_LT_TWENTY[13]
'thirteen'
```
For functional purposes, the first index for most of the lexicon's tuples is an empty string as opposed to being the string literal 'zero' ...
```
>>> from spellnum.lexicon import *
>>> NUMS_LT_TWENTY[0:2]
('', 'one')
```
... and in the case of TENS_GE_TWENTY, the second index is also an empty string:
```
>>> from spellnum.lexicon import *
>>> TENS_GE_TWENTY[0:3]
('', '', 'twenty')
```

## messages.py
messages.py is just home to a couple error messages used by the modules functions and it is not implicitly imported with the rest of the module.

## functions.py
functions.py is home to all of the fun stuff, which currently really only consists of one main function and two semi-private functions.

### get_period_suffix(base_illion)
This function will return the period suffix or full period name for a number with the given base-illion value. **get_period_suffix** raises a ValueError if the **base_illion** argument falls outside the range [-1, 1000). The base-illion property of a number in the short-scale system is equal to one less than the number of periods in the number, where a period is a set of one to three consecutive digits often separated by commas.
```
>>> from spellnum import *
>>> get_period_suffix(base_illion=4)
'quadrillion'
>>> get_period_suffix(base_illion=789)
'novemoctogintaseptingentillion'
```

### get_period_spelling(period)
This function constructs the spelling for an individual number period consisting of one to three decimal digits, which is just a fancy way of saying it spells any number from 1-999. **get_period_spelling** will raise a ValueError if the **period** argument is not an int in the range [1, 1000).
#### Example
```
>>> from spellnum import *
>>> get_period_spelling(period=123)
'one hundred twenty-three'
```

### spell_integer(number)
The **spell_integer** function is the main focus of the module. It will return the english short-scale spelling for the **number** argument which can be any positive or negative integer with an absolute value less than 10<sup>3003</sup> (1 Millinillion). That's a 1 followed by 3003 zeros. To put that into perspective, most of the scientific community seems to agree that there are somewhere between 10<sup>78</sup> and 10<sup>82</sup> atoms in the known universe... If you need a bigger number spelled, you'll just have to look elsewhere. When **number** falls outside the aforementioned range, the subsequent call to **get_period_suffix** will raise a value error as the **base_illion** argument will fall outside the range [-1, 1000). The **number** argument can be an integer or a string.
#### Example
```
>>> from spellnum import *
>>> spell_integer(-123456)
'negative one hundred twenty-three thousand four hundred fifty-six'
>>> spell_integer('789000000000000000000000000000000000000000000000000')
'seven hundred eighty-nine quinquadecillion'
```
