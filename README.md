# Overview
spellnum is a Python module for spelling really large numbers in english using a small combination of functions and some cleverly built tuples. For more information on the large number names and period naming conventions used by this module see the wikipedia page [here](https://en.wikipedia.org/wiki/Names_of_large_numbers).

# Component Files
The spellnum module is currently comprised of three different files: `lexicon.py`, `messages.py`, and `functions.py`.

## lexicon.py
`lexicon.py` is home to a set of tuples containing number name and period suffix component strings. They are defined in such a way that indexing them will return the appropriate number name or period spelling for the index given (all lowercase). The main construct here is the `INTEGERS_LT_1000` tuple. Indexing this will return the spelling for any integer less than 1000 as the name suggests.
```
>>> from spellnum import *
>>> INTEGERS_LT_1000[7]
'seven'
>>> INTEGERS_LT_1000[13]
'thirteen'
>>> INTEGERS_LT_1000[999]
'nine hundred ninety-nine'
```
For functional purposes, the first index of lexicon's `INTEGERS_LT_1000` tuple is an empty string as opposed to being the string literal 'zero' ...
```
>>> from spellnum import *
>>> INTEGERS_LT_1000[0:3]
('', 'one', 'two')
```

## messages.py
`messages.py` is just home to a couple error messages used by the modules functions and it is not implicitly imported with the rest of the module.

## functions.py
`functions.py` is home to all of the fun stuff, which currently really only consists of two main functions, `get_period_suffix` and `spell_number`.

### `get_period_suffix(base_illion)`
This function will return the period suffix or full period name for a number with the given base-illion value. `get_period_suffix` raises a ValueError if the **base_illion** argument falls outside the range [-1, 1000). The base-illion property of a number in the short-scale system is equal to one less than the number of periods in the number, where a period is a set of one to three consecutive digits often separated by commas.
#### Examples
```
>>> from spellnum import *
>>> get_period_suffix(base_illion=4)
'quadrillion'
>>> get_period_suffix(base_illion=789)
'novemoctogintaseptingentillion'
```

### `spell_number(number)`
The `spell_number` function is the main focus of the module. It will return the english short-scale spelling for the **number** argument which can be any positive or negative number with an absolute value less than 10<sup>3003</sup> (1 Millinillion). That's a 1 followed by 3003 zeros. To put that into perspective, most of the scientific community seems to agree that there are somewhere between 10<sup>78</sup> and 10<sup>82</sup> atoms in the known universe... If you need a bigger number spelled, you'll just have to look elsewhere. When **number** falls outside the aforementioned range, the subsequent call to `get_period_suffix` will raise a value error as the **base_illion** argument will fall outside the range [-1, 1000). The **number** argument can be a integer, float, or string.

It should be noted that `spell_number` *can* handle values that exceed limitations on numerical types. Pass **number** as a string for values requiring more precision or values greater maximum and minimum int/float values.
#### Examples
```
>>> from spellnum import *
>>> spell_number(-123456)
'negative one hundred twenty-three thousand four hundred fifty-six'
>>> spell_number(4.56e100)
'forty-five duotrigintillion six hundred untrigintillion'
>>> spell_number('7.89e500')
'seven hundred eighty-nine quinquasexagintacentillion'
>>> spell_number('-1.2e-9')
'negative twelve ten billionths'
```
