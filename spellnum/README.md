# Package Organization
The spellnum package is comprised of two primary submodules: `lexicon`, and `functions`. All of the functions are imported into the top level of the package for ease of access. Two additional submodules `exceptions` and `regexlib` are essentially repositories for... well, exactly what it sounds like...

## spellnum.lexicon
[lexicon.py](lexicon.py) is home to a set of tuples containing number name and period suffix component strings. They are defined in such a way that indexing them will return the appropriate number name or period spelling for the index given (all lowercase). The main constructs here are the `INTEGERS_LT_100`, `INTEGERS_LT_1000`, and `BASE_ILLION_PERIOD_PREFIXES` tuples.

### spellnum.lexicon.INTEGERS_LT_1000
Indexing this will return the spelling for any integer less than 1000 as the name suggests.
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
[functions.py](functions.py) is home to all of the fun stuff, which really only consists of two pairs main pairs of functions, `nameperiod`/`readperiod` and `number2text`/`text2number`. As their names might suggest, for both pairs, each function is designed to be the other's inverse (to the extent possible). The intended promise is that calling one with the output of the other will return the input of the other, or at least something equivalent which could be used the same way in the other direction.

### `nameperiod(base_illion)`
This function will return the Conway-Wechsler name for a number with the given base-illion value. The base-illion property of a number in the short-scale system is equal to one less than the number of periods in the number, where a period is a set of one to three consecutive digits often separated by commas.
#### Examples
```
>>> from spellnum.functions import nameperiod
>>> nameperiod(4)
'quadrillion'
>>> nameperiod(789)
'novemoctogintaseptingentillion'
>>> nameperiod(123456789)
'tresviginticentillisesquinquagintaquadringentillinovemoctogintaseptingentillion'
```

### `readperiod(period_name)`
This function will return the base-illion value for a number with the given Conway-Wechsler name. It is the inverse of `nameperiod`.

#### Examples
```
>>> from spellnum.functions import readperiod
>>> readperiod('quadrillion')
4
>>> readperiod('novemoctogintaseptingentillion')
789
>>> readperiod('tresviginticentillisesquinquagintaquadringentillinovemoctogintaseptingentillion')
123456789
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

## spellnum.exceptions
Since the great un-bounding of `nameperiod` and subsequently `number2text`, [exceptions.py](exceptions.py) is home to only one custom exception, `InvalidNumericalFormat`, which extends the built-in `ValueError` purely for the sake of verbosity.
