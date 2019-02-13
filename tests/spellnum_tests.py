"""
Unit tests for spellnum module.
"""

import unittest
import spellnum


class LexiconStructure(unittest.TestCase):
    """
    Verifies that the lexicon tuples were built and aligned properly
    """
    
    def test_1DigitIntegers(self):
        self.assertTupleEqual(spellnum.functions.lexicon._UNIQUE_WORDS[:9],
                              spellnum.functions.lexicon.INTEGERS_LT_1000[:9])
        
    def test_2DigitIntegers(self):
        self.assertTupleEqual(spellnum.functions.lexicon.INTEGERS_LT_1000[10:99],
                              spellnum.functions.lexicon._INTEGERS_LT_100[10:99])
        
    def test_3DigitIntegers(self):
        for index in range(100, 1000):
            self.assertRegex(spellnum.functions.lexicon.INTEGERS_LT_1000[index],
                             f'^[a-z]+ hundred {spellnum.functions.lexicon._INTEGERS_LT_100[index%100]}'.strip())
            
            
class SuffixInputValidity(unittest.TestCase):
    """
    Tests valid and invalid input type and boundary values for get_period_suffix
    """
    
    def test_InputEQMinimum(self):
        expected = ''
        self.assertMultiLineEqual(expected, spellnum.functions.get_period_suffix(-1))
        self.assertMultiLineEqual(expected, spellnum.functions.get_period_suffix('-1'))
        
    def test_InputEQMaximum(self):
        expected = 'novenonagintanongentillion'
        self.assertMultiLineEqual(expected, spellnum.functions.get_period_suffix(999))
        self.assertMultiLineEqual(expected, spellnum.functions.get_period_suffix('999'))
        
    def test_InputLTMinimum(self):
        self.assertRaises(ValueError, spellnum.functions.get_period_suffix, -2)
        self.assertRaises(ValueError, spellnum.functions.get_period_suffix, '-2')
        
    def test_InputGTMaximum(self):
        self.assertRaises(ValueError, spellnum.functions.get_period_suffix, 1000)
        self.assertRaises(ValueError, spellnum.functions.get_period_suffix, '1000')
        
    def test_InputNotInteger(self):
        self.assertRaises(ValueError, spellnum.functions.get_period_suffix, None)
        self.assertRaises(ValueError, spellnum.functions.get_period_suffix, 'abc')
        self.assertRaises(ValueError, spellnum.functions.get_period_suffix, 12.34)
        self.assertRaises(ValueError, spellnum.functions.get_period_suffix, '12.34')
        self.assertRaises(ValueError, spellnum.functions.get_period_suffix, [123, ])
        self.assertRaises(ValueError, spellnum.functions.get_period_suffix, (123, ))
        self.assertRaises(ValueError, spellnum.functions.get_period_suffix, {123, })
        
        
class SuffixControl(unittest.TestCase):
    """
    Tests generic use cases for get_period_suffix
    """
    
    def test_NominalCases(self):
        self.assertMultiLineEqual('unnonagintillion', spellnum.functions.get_period_suffix(91))
        self.assertMultiLineEqual('duononagintillion', spellnum.functions.get_period_suffix(92))
        self.assertMultiLineEqual('trenonagintillion', spellnum.functions.get_period_suffix(93))
        self.assertMultiLineEqual('quattuornonagintillion', spellnum.functions.get_period_suffix(94))
        self.assertMultiLineEqual('quinquanonagintillion', spellnum.functions.get_period_suffix(95))
        self.assertMultiLineEqual('senonagintillion', spellnum.functions.get_period_suffix(96))
        self.assertMultiLineEqual('septenonagintillion', spellnum.functions.get_period_suffix(97))
        self.assertMultiLineEqual('octononagintillion', spellnum.functions.get_period_suffix(98))
        self.assertMultiLineEqual('novenonagintillion', spellnum.functions.get_period_suffix(99))
        self.assertMultiLineEqual('trecentillion', spellnum.functions.get_period_suffix(300))
        
    def test_UniqueSuffixes(self):
        self.assertEqual(1001, len(set(spellnum.get_period_suffix(base_illion) for base_illion in range(-1, 1000))))
        
        
class SuffixExceptions(unittest.TestCase):
    """
    Tests for following lexical exceptions in a period suffix:
        se + x:         86 106 806
        se/tre + s:     23 26 33 36 43 46 53 56 83 103 303 306 403 406 503 506 803
        septe/nove + m: 27 29 87 89 807 809
        septe/nove + n: 17 19 37 39 47 49 57 59 67 69 77 79 107 109 207 209 307 309 407 409 507 509 607 609 707 709
    """
    
    def test_X_Exceptions(self):
        self.assertMultiLineEqual('sexoctogintillion', spellnum.functions.get_period_suffix(86))
        self.assertMultiLineEqual('sexcentillion', spellnum.functions.get_period_suffix(106))
        self.assertMultiLineEqual('sexoctingentillion', spellnum.functions.get_period_suffix(806))
        
    def test_S_Exceptions(self):
        self.assertMultiLineEqual('tresvigintillion', spellnum.functions.get_period_suffix(23))
        self.assertMultiLineEqual('sesvigintillion', spellnum.functions.get_period_suffix(26))
        self.assertMultiLineEqual('trestrigintillion', spellnum.functions.get_period_suffix(33))
        self.assertMultiLineEqual('sestrigintillion', spellnum.functions.get_period_suffix(36))
        self.assertMultiLineEqual('tresquadragintillion', spellnum.functions.get_period_suffix(43))
        self.assertMultiLineEqual('sesquadragintillion', spellnum.functions.get_period_suffix(46))
        self.assertMultiLineEqual('tresquinquagintillion', spellnum.functions.get_period_suffix(53))
        self.assertMultiLineEqual('sesquinquagintillion', spellnum.functions.get_period_suffix(56))
        self.assertMultiLineEqual('tresoctogintillion', spellnum.functions.get_period_suffix(83))
        self.assertMultiLineEqual('trescentillion', spellnum.functions.get_period_suffix(103))
        self.assertMultiLineEqual('trestrecentillion', spellnum.functions.get_period_suffix(303))
        self.assertMultiLineEqual('sestrecentillion', spellnum.functions.get_period_suffix(306))
        self.assertMultiLineEqual('tresquadringentillion', spellnum.functions.get_period_suffix(403))
        self.assertMultiLineEqual('sesquadringentillion', spellnum.functions.get_period_suffix(406))
        self.assertMultiLineEqual('tresquingentillion', spellnum.functions.get_period_suffix(503))
        self.assertMultiLineEqual('sesquingentillion', spellnum.functions.get_period_suffix(506))
        self.assertMultiLineEqual('tresoctingentillion', spellnum.functions.get_period_suffix(803))
        
    def test_M_Exceptions(self):
        self.assertMultiLineEqual('septemvigintillion', spellnum.functions.get_period_suffix(27))
        self.assertMultiLineEqual('novemvigintillion', spellnum.functions.get_period_suffix(29))
        self.assertMultiLineEqual('septemoctogintillion', spellnum.functions.get_period_suffix(87))
        self.assertMultiLineEqual('novemoctogintillion', spellnum.functions.get_period_suffix(89))
        self.assertMultiLineEqual('septemoctingentillion', spellnum.functions.get_period_suffix(807))
        self.assertMultiLineEqual('novemoctingentillion', spellnum.functions.get_period_suffix(809))
        
    def test_N_Exceptions(self):
        self.assertMultiLineEqual('septendecillion', spellnum.functions.get_period_suffix(17))
        self.assertMultiLineEqual('novendecillion', spellnum.functions.get_period_suffix(19))
        self.assertMultiLineEqual('septentrigintillion', spellnum.functions.get_period_suffix(37))
        self.assertMultiLineEqual('noventrigintillion', spellnum.functions.get_period_suffix(39))
        self.assertMultiLineEqual('septenquadragintillion', spellnum.functions.get_period_suffix(47))
        self.assertMultiLineEqual('novenquadragintillion', spellnum.functions.get_period_suffix(49))
        self.assertMultiLineEqual('septenquinquagintillion', spellnum.functions.get_period_suffix(57))
        self.assertMultiLineEqual('novenquinquagintillion', spellnum.functions.get_period_suffix(59))
        self.assertMultiLineEqual('septensexagintillion', spellnum.functions.get_period_suffix(67))
        self.assertMultiLineEqual('novensexagintillion', spellnum.functions.get_period_suffix(69))
        self.assertMultiLineEqual('septenseptuagintillion', spellnum.functions.get_period_suffix(77))
        self.assertMultiLineEqual('novenseptuagintillion', spellnum.functions.get_period_suffix(79))
        self.assertMultiLineEqual('septencentillion', spellnum.functions.get_period_suffix(107))
        self.assertMultiLineEqual('novencentillion', spellnum.functions.get_period_suffix(109))
        self.assertMultiLineEqual('septenducentillion', spellnum.functions.get_period_suffix(207))
        self.assertMultiLineEqual('novenducentillion', spellnum.functions.get_period_suffix(209))
        self.assertMultiLineEqual('septentrecentillion', spellnum.functions.get_period_suffix(307))
        self.assertMultiLineEqual('noventrecentillion', spellnum.functions.get_period_suffix(309))
        self.assertMultiLineEqual('septenquadringentillion', spellnum.functions.get_period_suffix(407))
        self.assertMultiLineEqual('novenquadringentillion', spellnum.functions.get_period_suffix(409))
        self.assertMultiLineEqual('septenquingentillion', spellnum.functions.get_period_suffix(507))
        self.assertMultiLineEqual('novenquingentillion', spellnum.functions.get_period_suffix(509))
        self.assertMultiLineEqual('septensescentillion', spellnum.functions.get_period_suffix(607))
        self.assertMultiLineEqual('novensescentillion', spellnum.functions.get_period_suffix(609))
        self.assertMultiLineEqual('septenseptingentillion', spellnum.functions.get_period_suffix(707))
        self.assertMultiLineEqual('novenseptingentillion', spellnum.functions.get_period_suffix(709))
        
        
class SpellingInputValidity(unittest.TestCase):
    """
    Tests valid and invalid input type and boundary values for spell_number
    """
    
    def test_InputEQMinimum(self):
        # smallest value would actually be -9.99...(repeating forever)...e3002
        expected = 'negative nine hundred ninety-nine novenonagintanongentillion'
        actual = spellnum.functions.spell_number('-9.99e3002')
        self.assertMultiLineEqual(expected, actual)
        
    def test_InputEQMaximum(self):
        # largest value would actually be 9.99...(repeating forever)...e3002
        expected = 'nine hundred ninety-nine novenonagintanongentillion'
        actual = spellnum.functions.spell_number('9.99e3002')
        self.assertMultiLineEqual(expected, actual)
        
    def test_PrecisionEQMaximum(self):
        expected = 'one one hundred novenonagintanongentillionth'
        actual = spellnum.functions.spell_number('1e-3002')
        self.assertMultiLineEqual(expected, actual)
        
    def test_InputLTMinimum(self):
        self.assertRaises(ValueError, spellnum.functions.spell_number, '-1e3003')
        
    def test_InputGTMaximum(self):
        self.assertRaises(ValueError, spellnum.functions.spell_number, '1e3003')
        
    def test_PrecisionGTMaximum(self):
        self.assertRaises(ValueError, spellnum.functions.spell_number, '0.1e-3002')
        
    def test_InputNone(self):
        self.assertRaises(ValueError, spellnum.functions.spell_number, None)
        
    def test_InputSet(self):
        self.assertRaises(ValueError, spellnum.functions.spell_number, {123, })
        
    def test_InputList(self):
        self.assertRaises(ValueError, spellnum.functions.spell_number, [123, ])
        
    def test_InputTuple(self):
        self.assertRaises(ValueError, spellnum.functions.spell_number, (123,))
        
    def test_ValidFormat_dXXX(self):
        expected = 'one hundred twenty-three one thousandths'
        self.assertMultiLineEqual(expected, spellnum.functions.spell_number(.123))
        self.assertMultiLineEqual(expected, spellnum.functions.spell_number('.123'))
        self.assertMultiLineEqual(f'negative {expected}', spellnum.functions.spell_number(-.123))
        self.assertMultiLineEqual(f'negative {expected}', spellnum.functions.spell_number('-.123'))
        
    def test_ValidFormat_dXeX(self):
        expected = 'one hundred million'
        self.assertMultiLineEqual(expected, spellnum.functions.spell_number(.1e9))
        self.assertMultiLineEqual(expected, spellnum.functions.spell_number('.1e9'))
        self.assertMultiLineEqual(f'negative {expected}', spellnum.functions.spell_number(-.1e9))
        self.assertMultiLineEqual(f'negative {expected}', spellnum.functions.spell_number('-.1e9'))
        
    def test_ValidFormat_XdXEX(self):
        expected = 'one billion two hundred million'
        self.assertMultiLineEqual(expected, spellnum.functions.spell_number(1.2E9))
        self.assertMultiLineEqual(expected, spellnum.functions.spell_number('1.2E9'))
        self.assertMultiLineEqual(f'negative {expected}', spellnum.functions.spell_number(-1.2E9))
        self.assertMultiLineEqual(f'negative {expected}', spellnum.functions.spell_number('-1.2E9'))
        
    def test_ValidFormat_XdXeX(self):
        expected = 'one billion two hundred million'
        self.assertMultiLineEqual(expected, spellnum.functions.spell_number(1.2e9))
        self.assertMultiLineEqual(expected, spellnum.functions.spell_number('1.2e9'))
        self.assertMultiLineEqual(f'negative {expected}', spellnum.functions.spell_number(-1.2e9))
        self.assertMultiLineEqual(f'negative {expected}', spellnum.functions.spell_number('-1.2e9'))
        
    def test_ValidFormat_XdXenX(self):
        expected = 'twelve ten billionths'
        self.assertMultiLineEqual(expected, spellnum.functions.spell_number(1.2e-9))
        self.assertMultiLineEqual(expected, spellnum.functions.spell_number('1.2e-9'))
        self.assertMultiLineEqual(f'negative {expected}', spellnum.functions.spell_number(-1.2e-9))
        self.assertMultiLineEqual(f'negative {expected}', spellnum.functions.spell_number('-1.2e-9'))
        
    def test_ValidFormat_0dXeX(self):
        expected = 'one hundred million'
        self.assertMultiLineEqual(expected, spellnum.functions.spell_number(0.1e9))
        self.assertMultiLineEqual(expected, spellnum.functions.spell_number('0.1e9'))
        self.assertMultiLineEqual(f'negative {expected}', spellnum.functions.spell_number(-0.1e9))
        self.assertMultiLineEqual(f'negative {expected}', spellnum.functions.spell_number('-0.1e9'))
        
    def test_ValidFormat_Xd0eX(self):
        expected = 'one billion'
        self.assertMultiLineEqual(expected, spellnum.functions.spell_number(1.0e9))
        self.assertMultiLineEqual(expected, spellnum.functions.spell_number('1.0e9'))
        self.assertMultiLineEqual(f'negative {expected}', spellnum.functions.spell_number(-1.0e9))
        self.assertMultiLineEqual(f'negative {expected}', spellnum.functions.spell_number('-1.0e9'))
        
    def test_ValidFormat_XXXdXXXeXXX(self):
        expected = 'one hundred twenty-three quadragintillion four hundred fifty-six noventrigintillion'
        self.assertMultiLineEqual(expected, spellnum.functions.spell_number(123.456e123))
        self.assertMultiLineEqual(expected, spellnum.functions.spell_number('123.456e123'))
        self.assertMultiLineEqual(f'negative {expected}', spellnum.functions.spell_number(-123.456e123))
        self.assertMultiLineEqual(f'negative {expected}', spellnum.functions.spell_number('-123.456e123'))
        
    def test_ValidFormat_0XXdXX0e0XX(self):
        expected = 'twelve trillion three hundred forty billion'
        self.assertMultiLineEqual(expected, spellnum.functions.spell_number(012.340e012))
        self.assertMultiLineEqual(expected, spellnum.functions.spell_number('012.340e012'))
        self.assertMultiLineEqual(f'negative {expected}', spellnum.functions.spell_number(-012.340e012))
        self.assertMultiLineEqual(f'negative {expected}', spellnum.functions.spell_number('-012.340e012'))
        
    def test_PrecisionRetention(self):
        expected = ('one quadragintillion two hundred thirty-four noventrigintillion five hundred sixty-seven '
                    'octotrigintillion eight hundred ninety-eight septentrigintillion seven hundred sixty-five '
                    'sestrigintillion four hundred thirty-two quinquatrigintillion one hundred quattuortrigintillion')
        self.assertMultiLineEqual(expected, spellnum.functions.spell_number(1.2345678987654321e123))
        self.assertMultiLineEqual(expected, spellnum.functions.spell_number('1.2345678987654321e123'))
        self.assertMultiLineEqual(f'negative {expected}', spellnum.functions.spell_number(-1.2345678987654321e123))
        self.assertMultiLineEqual(f'negative {expected}', spellnum.functions.spell_number('-1.2345678987654321e123'))
        
    def test_InvalidInputs(self):
        self.assertRaises(ValueError, spellnum.functions.spell_number, '')
        self.assertRaises(ValueError, spellnum.functions.spell_number, '.')
        self.assertRaises(ValueError, spellnum.functions.spell_number, 'e')
        self.assertRaises(ValueError, spellnum.functions.spell_number, '-')
        self.assertRaises(ValueError, spellnum.functions.spell_number, '+')
        self.assertRaises(ValueError, spellnum.functions.spell_number, '.e')
        self.assertRaises(ValueError, spellnum.functions.spell_number, '.0e')
        self.assertRaises(ValueError, spellnum.functions.spell_number, '.0e-')
        self.assertRaises(ValueError, spellnum.functions.spell_number, '0.0e')
        self.assertRaises(ValueError, spellnum.functions.spell_number, '0.0e-')
        self.assertRaises(ValueError, spellnum.functions.spell_number, '0.e-0')
        self.assertRaises(ValueError, spellnum.functions.spell_number, '--123')
        self.assertRaises(ValueError, spellnum.functions.spell_number, '++123')
        self.assertRaises(ValueError, spellnum.functions.spell_number, '-+123')
        self.assertRaises(ValueError, spellnum.functions.spell_number, '+-123')
        self.assertRaises(ValueError, spellnum.functions.spell_number, '1.2.3')
        
        
class SpellingControl(unittest.TestCase):
    """
    Tests generic use cases for spell_number
    """
    
    def test_ZeroInputs(self):
        expected = 'zero'
        self.assertMultiLineEqual(expected, spellnum.functions.spell_number(0))
        self.assertMultiLineEqual(expected, spellnum.functions.spell_number(0.0))
        self.assertMultiLineEqual(expected, spellnum.functions.spell_number(0e0))
        self.assertMultiLineEqual(expected, spellnum.functions.spell_number(0.0e0))
        self.assertMultiLineEqual(expected, spellnum.functions.spell_number(-0))
        self.assertMultiLineEqual(expected, spellnum.functions.spell_number(-0.0))
        self.assertMultiLineEqual(expected, spellnum.functions.spell_number(-0e-0))
        self.assertMultiLineEqual(expected, spellnum.functions.spell_number(-0.0e-0))
        self.assertMultiLineEqual(expected, spellnum.functions.spell_number('0'))
        self.assertMultiLineEqual(expected, spellnum.functions.spell_number('0.0'))
        self.assertMultiLineEqual(expected, spellnum.functions.spell_number('0e0'))
        self.assertMultiLineEqual(expected, spellnum.functions.spell_number('0.0e0'))
        self.assertMultiLineEqual(expected, spellnum.functions.spell_number('-0'))
        self.assertMultiLineEqual(expected, spellnum.functions.spell_number('-0.0'))
        self.assertMultiLineEqual(expected, spellnum.functions.spell_number('-0e-0'))
        self.assertMultiLineEqual(expected, spellnum.functions.spell_number('-0.0e-0'))
        
        
class SpellingScientific(unittest.TestCase):
    """
    Tests spelling numbers in scientific notation
    """
    
    def test_Float_XXdXXe3(self):
        expected = spellnum.functions.spell_number(12340)
        actual = spellnum.functions.spell_number(12.34e3)
        self.assertMultiLineEqual(expected, actual)
        
    def test_Float_XXdXXe2(self):
        expected = spellnum.functions.spell_number(1234)
        actual = spellnum.functions.spell_number(12.34e2)
        self.assertMultiLineEqual(expected, actual)
        
    def test_Float_XXdXXe1(self):
        expected = spellnum.functions.spell_number(123.4)
        actual = spellnum.functions.spell_number(12.34e1)
        self.assertMultiLineEqual(expected, actual)
        
    def test_Float_XXdXXe0(self):
        expected = spellnum.functions.spell_number(12.34)
        actual = spellnum.functions.spell_number(12.34e0)
        self.assertMultiLineEqual(expected, actual)
        
    def test_Float_XXdXXen0(self):
        expected = spellnum.functions.spell_number(12.34)
        actual = spellnum.functions.spell_number(12.34e-0)
        self.assertMultiLineEqual(expected, actual)
        
    def test_Float_XXdXXen1(self):
        expected = spellnum.functions.spell_number(1.234)
        actual = spellnum.functions.spell_number(12.34e-1)
        self.assertMultiLineEqual(expected, actual)
        
    def test_Float_XXdXXen2(self):
        expected = spellnum.functions.spell_number(.1234)
        actual = spellnum.functions.spell_number(12.34e-2)
        self.assertMultiLineEqual(expected, actual)
        
    def test_Float_XXdXXen3(self):
        expected = spellnum.functions.spell_number(.01234)
        actual = spellnum.functions.spell_number(12.34e-3)
        self.assertMultiLineEqual(expected, actual)
        
    def test_String_XXdXXe3(self):
        expected = spellnum.functions.spell_number(12340)
        actual = spellnum.functions.spell_number('12.34e3')
        self.assertMultiLineEqual(expected, actual)
        
    def test_String_XXdXXe2(self):
        expected = spellnum.functions.spell_number(1234)
        actual = spellnum.functions.spell_number('12.34e2')
        self.assertMultiLineEqual(expected, actual)
        
    def test_String_XXdXXe1(self):
        expected = spellnum.functions.spell_number(123.4)
        actual = spellnum.functions.spell_number('12.34e1')
        self.assertMultiLineEqual(expected, actual)
        
    def test_String_XXdXXe0(self):
        expected = spellnum.functions.spell_number(12.34)
        actual = spellnum.functions.spell_number('12.34e0')
        self.assertMultiLineEqual(expected, actual)
        
    def test_String_XXdXXen0(self):
        expected = spellnum.functions.spell_number(12.34)
        actual = spellnum.functions.spell_number('12.34e-0')
        self.assertMultiLineEqual(expected, actual)
        
    def test_String_XXdXXen1(self):
        expected = spellnum.functions.spell_number(1.234)
        actual = spellnum.functions.spell_number('12.34e-1')
        self.assertMultiLineEqual(expected, actual)
        
    def test_String_XXdXXen2(self):
        expected = spellnum.functions.spell_number(.1234)
        actual = spellnum.functions.spell_number('12.34e-2')
        self.assertMultiLineEqual(expected, actual)
        
    def test_String_XXdXXen3(self):
        expected = spellnum.functions.spell_number(.01234)
        actual = spellnum.functions.spell_number('12.34e-3')
        self.assertMultiLineEqual(expected, actual)
        
    def test_Float_0d1eXX(self):
        expected = 'one vigintillion'
        actual = spellnum.functions.spell_number(0.1e64)
        self.assertMultiLineEqual(expected, actual)
        
    def test_Float_1d0eXX(self):
        expected = 'one vigintillion'
        actual = spellnum.functions.spell_number(1.0e63)
        self.assertMultiLineEqual(expected, actual)
        
    def test_Float_0d1enXX(self):
        expected = 'one one vigintillionth'
        actual = spellnum.functions.spell_number(0.1e-62)
        self.assertMultiLineEqual(expected, actual)
        
    def test_Float_1d0enXX(self):
        expected = 'one one vigintillionth'
        actual = spellnum.functions.spell_number(1.0e-63)
        self.assertMultiLineEqual(expected, actual)
        
    def test_String_0d1eXX(self):
        expected = 'one vigintillion'
        actual = spellnum.functions.spell_number('0.1e64')
        self.assertMultiLineEqual(expected, actual)
        
    def test_String_1d0eXX(self):
        expected = 'one vigintillion'
        actual = spellnum.functions.spell_number('1.0e63')
        self.assertMultiLineEqual(expected, actual)
        
    def test_String_0d1enXX(self):
        expected = 'one one vigintillionth'
        actual = spellnum.functions.spell_number('0.1e-62')
        self.assertMultiLineEqual(expected, actual)
        
    def test_String_1d0enXX(self):
        expected = 'one one vigintillionth'
        actual = spellnum.functions.spell_number('1.0e-63')
        self.assertMultiLineEqual(expected, actual)
        
        
class SpellingDecimal(unittest.TestCase):
    """
    Tests spelling numbers with fractions in decimal format
    """
    
    def test_Tenths(self):
        expected = 'ten million two and three tenths'
        self.assertMultiLineEqual(expected, spellnum.functions.spell_number(10000002.3))
        self.assertMultiLineEqual(expected, spellnum.functions.spell_number('10000002.3'))
        
    def test_Hundredths(self):
        expected = 'one million two and thirty-four one hundredths'
        self.assertMultiLineEqual(expected, spellnum.functions.spell_number(1000002.34))
        self.assertMultiLineEqual(expected, spellnum.functions.spell_number('1000002.34'))
        
    def test_OneThousandths(self):
        expected = 'one hundred thousand two and three hundred four one thousandths'
        self.assertMultiLineEqual(expected, spellnum.functions.spell_number(100002.304))
        self.assertMultiLineEqual(expected, spellnum.functions.spell_number('100002.304'))
        
    def test_TenThousandths(self):
        expected = 'ten thousand two and three thousand four ten thousandths'
        self.assertMultiLineEqual(expected, spellnum.functions.spell_number(10002.3004))
        self.assertMultiLineEqual(expected, spellnum.functions.spell_number('10002.3004'))
        
    def test_OneHundredThousandths(self):
        expected = 'one thousand two and thirty thousand four one hundred thousandths'
        self.assertMultiLineEqual(expected, spellnum.functions.spell_number(1002.30004))
        self.assertMultiLineEqual(expected, spellnum.functions.spell_number('1002.30004'))
        
    def test_OneMillionths(self):
        expected = 'one hundred two and three hundred thousand four one millionths'
        self.assertMultiLineEqual(expected, spellnum.functions.spell_number(102.300004))
        self.assertMultiLineEqual(expected, spellnum.functions.spell_number('102.300004'))
        
    def test_TenMillionths(self):
        expected = 'twelve and three million four ten millionths'
        self.assertMultiLineEqual(expected, spellnum.functions.spell_number(12.3000004))
        self.assertMultiLineEqual(expected, spellnum.functions.spell_number('12.3000004'))
        
    def test_OneHundredMillionths(self):
        expected = 'two and thirty million four one hundred millionths'
        self.assertMultiLineEqual(expected, spellnum.functions.spell_number(2.30000004))
        self.assertMultiLineEqual(expected, spellnum.functions.spell_number('2.30000004'))
        
    def test_OneBillionths(self):
        expected = 'three hundred million four one billionths'
        self.assertMultiLineEqual(expected, spellnum.functions.spell_number(.300000004))
        self.assertMultiLineEqual(expected, spellnum.functions.spell_number('.300000004'))
        
    def test_SingularFractions(self):
        expected = 'one one thousandth'
        self.assertMultiLineEqual(expected, spellnum.functions.spell_number(0.001))
        self.assertMultiLineEqual(expected, spellnum.functions.spell_number('0.001'))
