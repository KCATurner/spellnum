# Package Organization
The conwech package is comprised of two primary submodules: `lexicon`, and `functions`. All of the functions are imported into the top level of the package for ease of access. Two additional submodules `exceptions` and `regexlib` are essentially repositories for... well, exactly what it sounds like. If you really need more information on those, just read the docstrings. That's probably where most of this stuff should be anyway, not in readme...  

## conwech.lexicon
[lexicon.py](lexicon.py) is home to a set of tuples containing number name and period suffix component strings. They are defined in such a way that indexing them will return the appropriate text (all lowercase) for the index given. There are some others, but the main constructs here are the `WHOLE_NUMBERS_LT_100`, `WHOLE_NUMBERS_LT_1000`, and `BASE_ILLION_PERIOD_PREFIXES` tuples.  

### WHOLE_NUMBERS_LT_1000
Indexing this tuple will return the spelling for any integer less than 1000 as the name suggests.  
```
>>> from conwech.lexicon import WHOLE_NUMBERS_LT_1000
>>> WHOLE_NUMBERS_LT_1000[7]
'seven'
>>> WHOLE_NUMBERS_LT_1000[13]
'thirteen'
>>> WHOLE_NUMBERS_LT_1000[999]
'nine hundred ninety-nine'
```
For functional purposes, the first index of lexicon's `INTEGERS_LT_1000` tuple is an empty string as opposed to being the string literal 'zero' ...  
```
>>> from conwech.lexicon import INTEGERS_LT_1000
>>> INTEGERS_LT_1000[0:3]
('', 'one', 'two')
```

### WHOLE_NUMBERS_LT_100
Indexing this tuple will return the spelling for any whole number less than 100 as the name suggests.  
```
>>> from conwech.lexicon import WHOLE_NUMBERS_LT_100
>>> WHOLE_NUMBERS_LT_100[7]
'seven'
>>> WHOLE_NUMBERS_LT_100[13]
'thirteen'
>>> WHOLE_NUMBERS_LT_100[99]
'ninety-nine'
```
For functional purposes, the first index of lexicon's `INTEGERS_LT_100` tuple is an empty string as opposed to being the string literal 'zero' ...  
```
>>> from conwech.lexicon import INTEGERS_LT_1000
>>> INTEGERS_LT_100[0:3]
('', 'one', 'two')
```
It probably goes without saying, but the only real reason to use `WHOLE_NUMBERS_LT_100` instead of `WHOLE_NUMBERS_LT_1000` is for matters where efficiency is a heavy concern.  

### BASE_ILLION_PERIOD_PREFIXES
Indexing this tuple with a base-illion period value will return the appropriate Conway-Wechsler prefix (everything before the "illi"/"illion").  
```
>>> from conwech.lexicon import BASE_ILLION_PERIOD_PREFIXES
>>> BASE_ILLION_PERIOD_PREFIXES[0]
'n'
>>> BASE_ILLION_PERIOD_PREFIXES[12]
'duodec'
>>> BASE_ILLION_PERIOD_PREFIXES[345]
'quinquaquadragintatrecent'
>>> 'illi'.join(BASE_ILLION_PERIOD_PREFIXES[int(p)] for p in '12,000,345'.split(','))) + 'illion'
'duodecillinilliquinquaquadragintatrecentillion'
...
```
All prefixes are constructed using the appropriate sub-prefix combinations and exception rules defined by the Conway-Wechsler naming system.  
```
...
>>> BASE_ILLION_PERIOD_PREFIXES[106]
'sexcent'
>>> BASE_ILLION_PERIOD_PREFIXES[600]
'sescent'
...
```

The first prefix is 'n' (for building 'nilli' components) and the next nine prefixes are based on the standard number names adopted before the inception of the Conway-Wechsler system.  
```
...
>>> BASE_ILLION_PERIOD_PREFIXES[:10]
('n', 'm', 'b', 'tr', 'quadr', 'quint', 'sext', 'sept', 'oct', 'non')
>>> tuple(p + 'illon' for p in BASE_ILLION_PERIOD_PREFIXES[1:10])
('million', 'billion', 'trillion', 'quadrillion', 'quintillion', 'sextillion', 'septillion', 'octillion', 'nonillion')
```

## conwech.functions
[functions.py](functions.py) is home to all of the fun stuff, which really only consists of two pairs main pairs of functions, `nameperiod`/`readperiod` and `number2text`/`text2number`. As their names kind of suggest, for both pairs, each function is designed to be the other's inverse (to the extent possible). The intended promise is that calling one with the output of the other will return the input of the other, or at least something equivalent, which could be used the same way in the other direction.  

### nameperiod(base_illion)
This function will return the Conway-Wechsler name for a number with the given base-illion value. The base-illion property of a number in the short-scale system is equal to one less than the number of periods in the number, where a period is a set of one to three consecutive digits often separated by commas.  
```
>>> from conwech.functions import nameperiod
>>> nameperiod(4)
'quadrillion'
>>> nameperiod(789)
'novemoctogintaseptingentillion'
>>> nameperiod(123456789)
'tresviginticentillisesquinquagintaquadringentillinovemoctogintaseptingentillion'
```

### readperiod(period_name)
This function will return the base-illion value for a number with the given Conway-Wechsler name. It is the inverse of `nameperiod`.  
```
>>> from conwech.functions import readperiod
>>> readperiod('quadrillion')
4
>>> readperiod('novemoctogintaseptingentillion')
789
>>> readperiod('tresviginticentillisesquinquagintaquadringentillinovemoctogintaseptingentillion')
123456789
```

### number2text(number)
The `number2text` function will return the english short-scale spelling for the **number** argument which can be any positive or negative number passed as an integer, float, or string (as long as that string fits a valid numeric pattern). `number2text` *can* handle values that exceed limitations on numerical types. Pass **number** as a string for values requiring more precision or values greater maximum and minimum int/float values.  
```
>>> from conwech.functions import number2text
>>> number2text(-123456)
'negative one hundred twenty-three thousand four hundred fifty-six'
>>> number2text(4.56e100)
'forty-five duotrigintillion six hundred untrigintillion'
>>> number2text('7.89e500')
'seven hundred eighty-nine quinquasexagintacentillion'
>>> number2text('-1.2e-9')
'negative twelve ten billionths'
...
```
__COMING SOON...__  
`number2text` will also be able to interpret any pseudo-sum-like string in the format sometimes returned by the `text2number` function. Currently, this functionality is not yet in place, but should be pushed soon...ish... Bite me.
```
...
>>> number2text('1e3000003 + 2e-3000003')
'one millinillinillion and two one millinillinillionths'
```

### text2number(text)
The `text2number` takes a string and attempts to parse it and return a string containing the number (or in some cases sum of numbers) representing the value of the text. The number(s) in the string will almost always be in scientific notation.  
```
>>> from conwech.functions import text2number
text2number('negative one hundred twenty-three thousand four hundred fifty-six and seven hundred eighty-nine one thousandths')
'-1.23456789e5'
...
```
 The function will return a pseudo-sum-like representation if any of the periods in the given text would result in adding an unreasonable amount of padding zeros.  
```
...
>>> text2number('one millinillinillion and two one millinillinillionths')
'1e3000003 + 2e-3000003'
```
