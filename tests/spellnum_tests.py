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
        self.assertTupleEqual(spellnum.lexicon.__UNIQUE_WORDS[:9],
                              spellnum.lexicon.INTEGERS_LT_1000[:9])
        
    def test_2DigitIntegers(self):
        self.assertTupleEqual(spellnum.lexicon.INTEGERS_LT_1000[10:99],
                              spellnum.lexicon.__INTEGERS_LT_100[10:99])
            
    def test_3DigitIntegers(self):
        for index in range(100, 1000):
            self.assertRegex(spellnum.lexicon.INTEGERS_LT_1000[index],
                             f'^[a-z]+ hundred {spellnum.lexicon.__INTEGERS_LT_100[index%100]}'.strip())
            
            
class LexicalExceptions(unittest.TestCase):
    """
    Tests for following lexical exceptions in a period suffix:
        se + x:         86 106 806
        se/tre + s:     23 26 33 36 43 46 53 56 83 103 303 306 403 406 503 506 803
        septe/nove + m: 27 29 87 89 807 809
        septe/nove + n: 17 19 37 39 47 49 57 59 67 69 77 79 107 109 207 209 307 309 407 409 507 509 607 609 707 709
    """
    def test_NominalCases(self):
        self.assertMultiLineEqual('unnonagintillion', spellnum.get_period_suffix(91))
        self.assertMultiLineEqual('duononagintillion', spellnum.get_period_suffix(92))
        self.assertMultiLineEqual('trenonagintillion', spellnum.get_period_suffix(93))
        self.assertMultiLineEqual('quattuornonagintillion', spellnum.get_period_suffix(94))
        self.assertMultiLineEqual('quinquanonagintillion', spellnum.get_period_suffix(95))
        self.assertMultiLineEqual('senonagintillion', spellnum.get_period_suffix(96))
        self.assertMultiLineEqual('septenonagintillion', spellnum.get_period_suffix(97))
        self.assertMultiLineEqual('octononagintillion', spellnum.get_period_suffix(98))
        self.assertMultiLineEqual('novenonagintillion', spellnum.get_period_suffix(99))
        self.assertMultiLineEqual('trecentillion', spellnum.get_period_suffix(300))
        
    def test_X_Exceptions(self):
        self.assertMultiLineEqual('sexoctogintillion', spellnum.get_period_suffix(86))
        self.assertMultiLineEqual('sexcentillion', spellnum.get_period_suffix(106))
        self.assertMultiLineEqual('sexoctingentillion', spellnum.get_period_suffix(806))
        
    def test_S_Exceptions(self):
        self.assertMultiLineEqual('tresvigintillion', spellnum.get_period_suffix(23))
        self.assertMultiLineEqual('sesvigintillion', spellnum.get_period_suffix(26))
        self.assertMultiLineEqual('trestrigintillion', spellnum.get_period_suffix(33))
        self.assertMultiLineEqual('sestrigintillion', spellnum.get_period_suffix(36))
        self.assertMultiLineEqual('tresquadragintillion', spellnum.get_period_suffix(43))
        self.assertMultiLineEqual('sesquadragintillion', spellnum.get_period_suffix(46))
        self.assertMultiLineEqual('tresquinquagintillion', spellnum.get_period_suffix(53))
        self.assertMultiLineEqual('sesquinquagintillion', spellnum.get_period_suffix(56))
        self.assertMultiLineEqual('tresoctogintillion', spellnum.get_period_suffix(83))
        self.assertMultiLineEqual('trescentillion', spellnum.get_period_suffix(103))
        self.assertMultiLineEqual('trestrecentillion', spellnum.get_period_suffix(303))
        self.assertMultiLineEqual('sestrecentillion', spellnum.get_period_suffix(306))
        self.assertMultiLineEqual('tresquadringentillion', spellnum.get_period_suffix(403))
        self.assertMultiLineEqual('sesquadringentillion', spellnum.get_period_suffix(406))
        self.assertMultiLineEqual('tresquingentillion', spellnum.get_period_suffix(503))
        self.assertMultiLineEqual('sesquingentillion', spellnum.get_period_suffix(506))
        self.assertMultiLineEqual('tresoctingentillion', spellnum.get_period_suffix(803))
        
    def test_M_Exceptions(self):
        self.assertMultiLineEqual('septemvigintillion', spellnum.get_period_suffix(27))
        self.assertMultiLineEqual('novemvigintillion', spellnum.get_period_suffix(29))
        self.assertMultiLineEqual('septemoctogintillion', spellnum.get_period_suffix(87))
        self.assertMultiLineEqual('novemoctogintillion', spellnum.get_period_suffix(89))
        self.assertMultiLineEqual('septemoctingentillion', spellnum.get_period_suffix(807))
        self.assertMultiLineEqual('novemoctingentillion', spellnum.get_period_suffix(809))
        
    def test_N_Exceptions(self):
        self.assertMultiLineEqual('septendecillion', spellnum.get_period_suffix(17))
        self.assertMultiLineEqual('novendecillion', spellnum.get_period_suffix(19))
        self.assertMultiLineEqual('septentrigintillion', spellnum.get_period_suffix(37))
        self.assertMultiLineEqual('noventrigintillion', spellnum.get_period_suffix(39))
        self.assertMultiLineEqual('septenquadragintillion', spellnum.get_period_suffix(47))
        self.assertMultiLineEqual('novenquadragintillion', spellnum.get_period_suffix(49))
        self.assertMultiLineEqual('septenquinquagintillion', spellnum.get_period_suffix(57))
        self.assertMultiLineEqual('novenquinquagintillion', spellnum.get_period_suffix(59))
        self.assertMultiLineEqual('septensexagintillion', spellnum.get_period_suffix(67))
        self.assertMultiLineEqual('novensexagintillion', spellnum.get_period_suffix(69))
        self.assertMultiLineEqual('septenseptuagintillion', spellnum.get_period_suffix(77))
        self.assertMultiLineEqual('novenseptuagintillion', spellnum.get_period_suffix(79))
        self.assertMultiLineEqual('septencentillion', spellnum.get_period_suffix(107))
        self.assertMultiLineEqual('novencentillion', spellnum.get_period_suffix(109))
        self.assertMultiLineEqual('septenducentillion', spellnum.get_period_suffix(207))
        self.assertMultiLineEqual('novenducentillion', spellnum.get_period_suffix(209))
        self.assertMultiLineEqual('septentrecentillion', spellnum.get_period_suffix(307))
        self.assertMultiLineEqual('noventrecentillion', spellnum.get_period_suffix(309))
        self.assertMultiLineEqual('septenquadringentillion', spellnum.get_period_suffix(407))
        self.assertMultiLineEqual('novenquadringentillion', spellnum.get_period_suffix(409))
        self.assertMultiLineEqual('septenquingentillion', spellnum.get_period_suffix(507))
        self.assertMultiLineEqual('novenquingentillion', spellnum.get_period_suffix(509))
        self.assertMultiLineEqual('septensescentillion', spellnum.get_period_suffix(607))
        self.assertMultiLineEqual('novensescentillion', spellnum.get_period_suffix(609))
        self.assertMultiLineEqual('septenseptingentillion', spellnum.get_period_suffix(707))
        self.assertMultiLineEqual('novenseptingentillion', spellnum.get_period_suffix(709))
        
        
class GetPeriodSuffixInputValidity(unittest.TestCase):
    """
    Tests valid and invalid input type and boundary values for get_period_suffix
    """
    
    def test_InputEQMinimum(self):
        expected = ''
        self.assertMultiLineEqual(expected, spellnum.get_period_suffix(-1))
        self.assertMultiLineEqual(expected, spellnum.get_period_suffix('-1'))
        
    def test_InputEQMaximum(self):
        expected = 'novenonagintanongentillion'
        self.assertMultiLineEqual(expected, spellnum.get_period_suffix(999))
        self.assertMultiLineEqual(expected, spellnum.get_period_suffix('999'))
        
    def test_InputLTMinimum(self):
        self.assertRaises(ValueError, spellnum.get_period_suffix, -2)
        self.assertRaises(ValueError, spellnum.get_period_suffix, '-2')
        
    def test_InputGTMaximum(self):
        self.assertRaises(ValueError, spellnum.get_period_suffix, 1000)
        self.assertRaises(ValueError, spellnum.get_period_suffix, '1000')
        
    def test_InputNotIntType(self):
        self.assertRaises(ValueError, spellnum.get_period_suffix, 12.34)
        self.assertRaises(ValueError, spellnum.get_period_suffix, '12.34')
        
        
class SpellNumberInputValidity(unittest.TestCase):
    """
    Tests valid and invalid input type and boundary values for spell_number
    """
    
    def test_ValidFormat_dXXX(self):
        expected = 'one hundred twenty-three one thousandths'
        self.assertMultiLineEqual(expected, spellnum.spell_number(.123))
        self.assertMultiLineEqual(expected, spellnum.spell_number('.123'))
        self.assertMultiLineEqual(f'negative {expected}', spellnum.spell_number(-.123))
        self.assertMultiLineEqual(f'negative {expected}', spellnum.spell_number('-.123'))
        
    def test_ValidFormat_dXeX(self):
        expected = 'one hundred million'
        self.assertMultiLineEqual(expected, spellnum.spell_number(.1e9))
        self.assertMultiLineEqual(expected, spellnum.spell_number('.1e9'))
        self.assertMultiLineEqual(f'negative {expected}', spellnum.spell_number(-.1e9))
        self.assertMultiLineEqual(f'negative {expected}', spellnum.spell_number('-.1e9'))
        
    def test_ValidFormat_XdXEX(self):
        expected = 'one billion two hundred million'
        self.assertMultiLineEqual(expected, spellnum.spell_number(1.2E9))
        self.assertMultiLineEqual(expected, spellnum.spell_number('1.2E9'))
        self.assertMultiLineEqual(f'negative {expected}', spellnum.spell_number(-1.2E9))
        self.assertMultiLineEqual(f'negative {expected}', spellnum.spell_number('-1.2E9'))
        
    def test_ValidFormat_XdXeX(self):
        expected = 'one billion two hundred million'
        self.assertMultiLineEqual(expected, spellnum.spell_number(1.2e9))
        self.assertMultiLineEqual(expected, spellnum.spell_number('1.2e9'))
        self.assertMultiLineEqual(f'negative {expected}', spellnum.spell_number(-1.2e9))
        self.assertMultiLineEqual(f'negative {expected}', spellnum.spell_number('-1.2e9'))
        
    def test_ValidFormat_XdXenX(self):
        expected = 'twelve ten billionths'
        self.assertMultiLineEqual(expected, spellnum.spell_number(1.2e-9))
        self.assertMultiLineEqual(expected, spellnum.spell_number('1.2e-9'))
        self.assertMultiLineEqual(f'negative {expected}', spellnum.spell_number(-1.2e-9))
        self.assertMultiLineEqual(f'negative {expected}', spellnum.spell_number('-1.2e-9'))
        
    def test_ValidFormat_0dXeX(self):
        expected = 'one hundred million'
        self.assertMultiLineEqual(expected, spellnum.spell_number(0.1e9))
        self.assertMultiLineEqual(expected, spellnum.spell_number('0.1e9'))
        self.assertMultiLineEqual(f'negative {expected}', spellnum.spell_number(-0.1e9))
        self.assertMultiLineEqual(f'negative {expected}', spellnum.spell_number('-0.1e9'))
        
    def test_ValidFormat_Xd0eX(self):
        expected = 'one billion'
        self.assertMultiLineEqual(expected, spellnum.spell_number(1.0e9))
        self.assertMultiLineEqual(expected, spellnum.spell_number('1.0e9'))
        self.assertMultiLineEqual(f'negative {expected}', spellnum.spell_number(-1.0e9))
        self.assertMultiLineEqual(f'negative {expected}', spellnum.spell_number('-1.0e9'))
        
    def test_ValidFormat_XXXdXXXeXXX(self):
        expected = 'one hundred twenty-three quadragintillion four hundred fifty-six noventrigintillion'
        self.assertMultiLineEqual(expected, spellnum.spell_number(123.456e123))
        self.assertMultiLineEqual(expected, spellnum.spell_number('123.456e123'))
        self.assertMultiLineEqual(f'negative {expected}', spellnum.spell_number(-123.456e123))
        self.assertMultiLineEqual(f'negative {expected}', spellnum.spell_number('-123.456e123'))
        
    def test_ValidFormat_0XXdXX0e0XX(self):
        expected = 'twelve trillion three hundred forty billion'
        self.assertMultiLineEqual(expected, spellnum.spell_number(012.340e012))
        self.assertMultiLineEqual(expected, spellnum.spell_number('012.340e012'))
        self.assertMultiLineEqual(f'negative {expected}', spellnum.spell_number(-012.340e012))
        self.assertMultiLineEqual(f'negative {expected}', spellnum.spell_number('-012.340e012'))
        
    def test_PrecisionRetention(self):
        expected = ('one quadragintillion two hundred thirty-four noventrigintillion five hundred sixty-seven '
                    'octotrigintillion eight hundred ninety-eight septentrigintillion seven hundred sixty-five '
                    'sestrigintillion four hundred thirty-two quinquatrigintillion one hundred quattuortrigintillion')
        self.assertMultiLineEqual(expected, spellnum.spell_number(1.2345678987654321e123))
        self.assertMultiLineEqual(expected, spellnum.spell_number('1.2345678987654321e123'))
        self.assertMultiLineEqual(f'negative {expected}', spellnum.spell_number(-1.2345678987654321e123))
        self.assertMultiLineEqual(f'negative {expected}', spellnum.spell_number('-1.2345678987654321e123'))
        
    def test_InvalidInputs(self):
        self.assertRaises(ValueError, spellnum.spell_number, '--123')
        self.assertRaises(ValueError, spellnum.spell_number, '++123')
        self.assertRaises(ValueError, spellnum.spell_number, '-+123')
        self.assertRaises(ValueError, spellnum.spell_number, '+-123')
        self.assertRaises(ValueError, spellnum.spell_number, '1.2.3')
        
        
class SpellNumberControl(unittest.TestCase):
    """
    Tests generic use cases for spell_number
    """
    
    def test_000000(self):
        expected = 'zero'
        self.assertMultiLineEqual(expected, spellnum.spell_number(0))
        self.assertMultiLineEqual(expected, spellnum.spell_number('0'))
        
    def test_001000(self):
        expected = 'one thousand'
        self.assertMultiLineEqual(expected, spellnum.spell_number(1000))
        self.assertMultiLineEqual(expected, spellnum.spell_number('1000'))
        
    def test_001111(self):
        expected = 'one thousand one hundred eleven'
        self.assertMultiLineEqual(expected, spellnum.spell_number(1111))
        self.assertMultiLineEqual(expected, spellnum.spell_number('1111'))
        
    def test_001Million(self):
        expected = 'one million'
        self.assertMultiLineEqual(expected, spellnum.spell_number(1000000))
        self.assertMultiLineEqual(expected, spellnum.spell_number('1000000'))
        
    def test_010Million(self):
        expected = 'ten million'
        self.assertMultiLineEqual(expected, spellnum.spell_number(10000000))
        self.assertMultiLineEqual(expected, spellnum.spell_number('10000000'))
        
    def test_100Million(self):
        expected = 'one hundred million'
        self.assertMultiLineEqual(expected, spellnum.spell_number(100000000))
        self.assertMultiLineEqual(expected, spellnum.spell_number('100000000'))
        
        
class SpellNumberFractions(unittest.TestCase):
    """
    Tests spelling numbers with fractions
    """
    
    def test_Tenths(self):
        expected = 'ten million and two tenths'
        self.assertMultiLineEqual(expected, spellnum.spell_number(10000000.2))
        self.assertMultiLineEqual(expected, spellnum.spell_number('10000000.2'))
        
    def test_Hundredths(self):
        expected = 'one million and twenty-three one hundredths'
        self.assertMultiLineEqual(expected, spellnum.spell_number(1000000.23))
        self.assertMultiLineEqual(expected, spellnum.spell_number('1000000.23'))
        
    def test_OneThousandths(self):
        expected = 'one hundred thousand and two hundred three one thousandths'
        self.assertMultiLineEqual(expected, spellnum.spell_number(100000.203))
        self.assertMultiLineEqual(expected, spellnum.spell_number('100000.203'))
        
    def test_TenThousandths(self):
        expected = 'ten thousand and two thousand three ten thousandths'
        self.assertMultiLineEqual(expected, spellnum.spell_number(10000.2003))
        self.assertMultiLineEqual(expected, spellnum.spell_number('10000.2003'))
        
    def test_OneHundredThousandths(self):
        expected = 'one thousand and twenty thousand three one hundred thousandths'
        self.assertMultiLineEqual(expected, spellnum.spell_number(1000.20003))
        self.assertMultiLineEqual(expected, spellnum.spell_number('1000.20003'))
        
    def test_OneMillionths(self):
        expected = 'one hundred and two hundred thousand three one millionths'
        self.assertMultiLineEqual(expected, spellnum.spell_number(100.200003))
        self.assertMultiLineEqual(expected, spellnum.spell_number('100.200003'))
        
    def test_TenMillionths(self):
        expected = 'ten and two million three ten millionths'
        self.assertMultiLineEqual(expected, spellnum.spell_number(10.2000003))
        self.assertMultiLineEqual(expected, spellnum.spell_number('10.2000003'))
        
    def test_OneHundredMillionths(self):
        expected = 'one and twenty million three one hundred millionths'
        self.assertMultiLineEqual(expected, spellnum.spell_number(1.20000003))
        self.assertMultiLineEqual(expected, spellnum.spell_number('1.20000003'))
        
    def test_OneBillionths(self):
        expected = 'two hundred million three one billionths'
        self.assertMultiLineEqual(expected, spellnum.spell_number(.200000003))
        self.assertMultiLineEqual(expected, spellnum.spell_number('.200000003'))
