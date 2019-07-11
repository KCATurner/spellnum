# Package Organization
The spellnum package is comprised of two primary submodules: `lexicon`, and `functions`. Two additional submodules `exceptions` and `regexlib` are essentially repositories for... well, exactly what it sounds like...

## spellnum.lexicon
[lexicon.py](lexicon.py) is home to a set of tuples containing number name and period suffix component strings. They are defined in such a way that indexing them will return the appropriate number name or period spelling for the index given (all lowercase). The main construct here is the `INTEGERS_LT_1000` tuple. Indexing this will return the spelling for any integer less than 1000 as the name suggests.
```
>>> from spellnum.lexicon import INTEGERS_LT_1000
>>> INTEGERS_LT_1000[7]
'seven'
>>> INTEGERS_LT_1000[13]
'thirteen'
>>> INTEGERS_LT_1000[999]
'nine hundred ninety-nine'
```
For functional purposes, the first index of lexicon's `INTEGERS_LT_1000` tuple is an empty string as opposed to being the string literal 'zero' ...
```
>>> from spellnum.lexicon import INTEGERS_LT_1000
>>> INTEGERS_LT_1000[0:3]
('', 'one', 'two')
```

## spellnum.functions
[functions.py](functions.py) is home to all of the fun stuff, which really only consists of three main functions, `number2text`, `text2number`, and `get_period_name`.

### `get_period_name(base_illion)`
This function will return the Conway-Wechsler name for a number with the given base-illion value. The base-illion property of a number in the short-scale system is equal to one less than the number of periods in the number, where a period is a set of one to three consecutive digits often separated by commas.
#### Examples
```
>>> from spellnum.functions import get_period_name
>>> get_period_name(base_illion=4)
'quadrillion'
>>> get_period_name(base_illion=789)
'novemoctogintaseptingentillion'
```

### `number2text(number)`
The `number2text` function will return the english short-scale spelling for the **number** argument which can be any positive or negative number passed as an integer, float, or string. `number2text` *can* handle values that exceed limitations on numerical types. Pass **number** as a string for values requiring more precision or values greater maximum and minimum int/float values.
#### Examples
```
>>> from spellnum.functions import number2text
>>> number2text(-123456)
'negative one hundred twenty-three thousand four hundred fifty-six'
>>> number2text(4.56e100)
'forty-five duotrigintillion six hundred untrigintillion'
>>> number2text('7.89e500')
'seven hundred eighty-nine quinquasexagintacentillion'
>>> number2text('-1.2e-9')
'negative twelve ten billionths'
```

### `text2number(text)`
This is a work in progress. What I had been working towards would have been fine if `number2text` had remained bounded at millinillion, but my ambition got the better of me and we can now spell whatever the h3ll we want... Stay posted, I guess.

#### Examples
```
>>> from spellnum.functions import text2number
text2number('one hundred twenty-three thousand four hundred fifty-six and seven hundred eighty-nine one thousandths')
'123456.789'
```

## spellnum.regexlib
Pre-compiled regular expression patterns for use with and throughout the package.

- **X_LEXICAL_EXCEPTION** - TODO: document...
- **S_LEXICAL_EXCEPTION** - TODO: document...
- **M_LEXICAL_EXCEPTION** - TODO: document...
- **N_LEXICAL_EXCEPTION** - TODO: document...
- **VALID_INPUT_NUMBER** - TODO: document...
- **VALID_INPUT_TEXT** - TODO: document...

## spellnum.exceptions
Since the great un-bounding of `get_period_name` and subsequently `number2text`, [exceptions.py](exceptions.py) is home to only one custom exception, `InvalidNumericalFormat`, which extends the built-in `ValueError` purely for the sake of verbosity.
