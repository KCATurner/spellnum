"""
Unit tests for spellnum module.
"""

import unittest
import spellnum


class LexiconStructure(unittest.TestCase):
    """
    Verifies that the lexicon tuples were built and aligned properly.
    """
    
    def test_1_digit_integers(self):
        expected = spellnum.lexicon._UNIQUE_WORDS[:9]
        actual = spellnum.lexicon.INTEGERS_LT_1000[:9]
        self.assertTupleEqual(expected, actual)
        
    def test_2_digit_integers(self):
        expected = spellnum.lexicon.INTEGERS_LT_100[10:99]
        actual = spellnum.lexicon.INTEGERS_LT_1000[10:99]
        self.assertTupleEqual(expected, actual)
        
    def test_3_digit_integers(self):
        for index in range(100, 1000):
            hundred = spellnum.lexicon._UNIQUE_WORDS[index // 100]
            tens = spellnum.lexicon.INTEGERS_LT_100[index % 100]
            expected = '{} hundred {}'.format(hundred, tens).strip()
            actual = spellnum.lexicon.INTEGERS_LT_1000[index]
            self.assertMultiLineEqual(expected, actual)
            
            
class SuffixInputValidity(unittest.TestCase):
    """
    Tests valid and invalid input type and boundary values for get_period_suffix.
    """
    
    def test_input_EQ_minimum(self):
        expected = ''
        self.assertMultiLineEqual(expected, spellnum.functions.get_period_suffix(-1))
        self.assertMultiLineEqual(expected, spellnum.functions.get_period_suffix('-1'))
        
    def test_input_EQ_maximum(self):
        expected = 'novenonagintanongentillion'
        self.assertMultiLineEqual(expected, spellnum.functions.get_period_suffix(999))
        self.assertMultiLineEqual(expected, spellnum.functions.get_period_suffix('999'))
        
    def test_input_LT_minimum(self):
        self.assertRaises(ValueError, spellnum.functions.get_period_suffix, -2)
        self.assertRaises(ValueError, spellnum.functions.get_period_suffix, '-2')
        
    def test_input_GT_maximum(self):
        self.assertRaises(ValueError, spellnum.functions.get_period_suffix, 1000)
        self.assertRaises(ValueError, spellnum.functions.get_period_suffix, '1000')
        
    def test_input_none(self):
        self.assertRaises(ValueError, spellnum.functions.get_period_suffix, None)
        
    def test_input_float(self):
        self.assertRaises(ValueError, spellnum.functions.get_period_suffix, 12.34)
        
    def test_input_string(self):
        self.assertRaises(ValueError, spellnum.functions.get_period_suffix, '12.34')
        
    def test_input_set(self):
        self.assertRaises(ValueError, spellnum.functions.get_period_suffix, set())
        
    def test_input_list(self):
        self.assertRaises(ValueError, spellnum.functions.get_period_suffix, list())
        
    def test_input_tuple(self):
        self.assertRaises(ValueError, spellnum.functions.get_period_suffix, tuple())
        
        
class SuffixNominalCases(unittest.TestCase):
    """
    Tests generic use cases for get_period_suffix.
    The nonaginatillions have no lexical exceptions making them a good spot-check for nominal testing.
    """
    
    def test_suffix_uniqueness(self):
        expected = 1001  # expected number of unique suffixes
        unique_suffix_count = len(set(spellnum.functions.get_period_suffix(bi) for bi in range(-1, 1000)))
        self.assertEqual(expected, unique_suffix_count)
        
    def test_90(self):
        expected = 'nonagintillion'
        actual = spellnum.functions.get_period_suffix(90)
        self.assertMultiLineEqual(expected, actual)
        
    def test_91(self):
        expected = 'unnonagintillion'
        actual = spellnum.functions.get_period_suffix(91)
        self.assertMultiLineEqual(expected, actual)
        
    def test_92(self):
        expected = 'duononagintillion'
        actual = spellnum.functions.get_period_suffix(92)
        self.assertMultiLineEqual(expected, actual)
        
    def test_93(self):
        expected = 'trenonagintillion'
        actual = spellnum.functions.get_period_suffix(93)
        self.assertMultiLineEqual(expected, actual)
        
    def test_94(self):
        expected = 'quattuornonagintillion'
        actual = spellnum.functions.get_period_suffix(94)
        self.assertMultiLineEqual(expected, actual)
        
    def test_95(self):
        expected = 'quinquanonagintillion'
        actual = spellnum.functions.get_period_suffix(95)
        self.assertMultiLineEqual(expected, actual)
        
    def test_96(self):
        expected = 'senonagintillion'
        actual = spellnum.functions.get_period_suffix(96)
        self.assertMultiLineEqual(expected, actual)
        
    def test_97(self):
        expected = 'septenonagintillion'
        actual = spellnum.functions.get_period_suffix(97)
        self.assertMultiLineEqual(expected, actual)
        
    def test_98(self):
        expected = 'octononagintillion'
        actual = spellnum.functions.get_period_suffix(98)
        self.assertMultiLineEqual(expected, actual)
        
    def test_99(self):
        expected = 'novenonagintillion'
        actual = spellnum.functions.get_period_suffix(99)
        self.assertMultiLineEqual(expected, actual)
        
        
class SuffixExceptions(unittest.TestCase):
    """
    Tests for following lexical exceptions in a period suffix:
        tre + s:    23 33 43 53 83 103 303 403 503 803
        se + s:     26 36 46 56 306 406 506
        se + x:     86 106 806
        septe + m:  27 87 807
        septe + n:  17 37 47 57 67 77 107 207 307 407 507 607 707
        nove + m:   29 89 809
        nove + n:   19 39 49 59 69 79 109 209 309 409 509 609 709
    """
    
    def test_se_s_exception_26(self):
        expected = 'sesvigintillion'
        actual = spellnum.functions.get_period_suffix(26)
        self.assertMultiLineEqual(expected, actual)
        
    def test_se_s_exception_36(self):
        expected = 'sestrigintillion'
        actual = spellnum.functions.get_period_suffix(36)
        self.assertMultiLineEqual(expected, actual)
        
    def test_se_s_exception_46(self):
        expected = 'sesquadragintillion'
        actual = spellnum.functions.get_period_suffix(46)
        self.assertMultiLineEqual(expected, actual)
        
    def test_se_s_exception_56(self):
        expected = 'sesquinquagintillion'
        actual = spellnum.functions.get_period_suffix(56)
        self.assertMultiLineEqual(expected, actual)
        
    def test_se_s_exception_306(self):
        expected = 'sestrecentillion'
        actual = spellnum.functions.get_period_suffix(306)
        self.assertMultiLineEqual(expected, actual)
        
    def test_se_s_exception_406(self):
        expected = 'sesquadringentillion'
        actual = spellnum.functions.get_period_suffix(406)
        self.assertMultiLineEqual(expected, actual)
        
    def test_se_s_exception_506(self):
        expected = 'sesquingentillion'
        actual = spellnum.functions.get_period_suffix(506)
        self.assertMultiLineEqual(expected, actual)
        
    def test_tre_s_exception_23(self):
        expected = 'tresvigintillion'
        actual = spellnum.functions.get_period_suffix(23)
        self.assertMultiLineEqual(expected, actual)
        
    def test_tre_s_exception_33(self):
        expected = 'trestrigintillion'
        actual = spellnum.functions.get_period_suffix(33)
        self.assertMultiLineEqual(expected, actual)
        
    def test_tre_s_exception_43(self):
        expected = 'tresquadragintillion'
        actual = spellnum.functions.get_period_suffix(43)
        self.assertMultiLineEqual(expected, actual)
        
    def test_tre_s_exception_53(self):
        expected = 'tresquinquagintillion'
        actual = spellnum.functions.get_period_suffix(53)
        self.assertMultiLineEqual(expected, actual)
        
    def test_tre_s_exception_83(self):
        expected = 'tresoctogintillion'
        actual = spellnum.functions.get_period_suffix(83)
        self.assertMultiLineEqual(expected, actual)
        
    def test_tre_s_exception_103(self):
        expected = 'trescentillion'
        actual = spellnum.functions.get_period_suffix(103)
        self.assertMultiLineEqual(expected, actual)
        
    def test_tre_s_exception_303(self):
        expected = 'trestrecentillion'
        actual = spellnum.functions.get_period_suffix(303)
        self.assertMultiLineEqual(expected, actual)
        
    def test_tre_s_exception_403(self):
        expected = 'tresquadringentillion'
        actual = spellnum.functions.get_period_suffix(403)
        self.assertMultiLineEqual(expected, actual)
        
    def test_tre_s_exception_503(self):
        expected = 'tresquingentillion'
        actual = spellnum.functions.get_period_suffix(503)
        self.assertMultiLineEqual(expected, actual)
        
    def test_tre_s_exception_803(self):
        expected = 'tresoctingentillion'
        actual = spellnum.functions.get_period_suffix(803)
        self.assertMultiLineEqual(expected, actual)
        
    def test_se_x_exception_86(self):
        expected = 'sexoctogintillion'
        actual = spellnum.functions.get_period_suffix(86)
        self.assertMultiLineEqual(expected, actual)
        
    def test_se_x_exception_106(self):
        expected = 'sexcentillion'
        actual = spellnum.functions.get_period_suffix(106)
        self.assertMultiLineEqual(expected, actual)
        
    def test_se_x_exception_806(self):
        expected = 'sexoctingentillion'
        actual = spellnum.functions.get_period_suffix(806)
        self.assertMultiLineEqual(expected, actual)
        
    def test_septe_m_exception_27(self):
        expected = 'septemvigintillion'
        actual = spellnum.functions.get_period_suffix(27)
        self.assertMultiLineEqual(expected, actual)
        
    def test_septe_m_exception_87(self):
        expected = 'septemoctogintillion'
        actual = spellnum.functions.get_period_suffix(87)
        self.assertMultiLineEqual(expected, actual)
        
    def test_septe_m_exception_807(self):
        expected = 'septemoctingentillion'
        actual = spellnum.functions.get_period_suffix(807)
        self.assertMultiLineEqual(expected, actual)
        
    def test_septe_n_exception_17(self):
        expected = 'septendecillion'
        actual = spellnum.functions.get_period_suffix(17)
        self.assertMultiLineEqual(expected, actual)
        
    def test_septe_n_exception_37(self):
        expected = 'septentrigintillion'
        actual = spellnum.functions.get_period_suffix(37)
        self.assertMultiLineEqual(expected, actual)
        
    def test_septe_n_exception_47(self):
        expected = 'septenquadragintillion'
        actual = spellnum.functions.get_period_suffix(47)
        self.assertMultiLineEqual(expected, actual)
        
    def test_septe_n_exception_57(self):
        expected = 'septenquinquagintillion'
        actual = spellnum.functions.get_period_suffix(57)
        self.assertMultiLineEqual(expected, actual)
        
    def test_septe_n_exception_67(self):
        expected = 'septensexagintillion'
        actual = spellnum.functions.get_period_suffix(67)
        self.assertMultiLineEqual(expected, actual)
        
    def test_septe_n_exception_77(self):
        expected = 'septenseptuagintillion'
        actual = spellnum.functions.get_period_suffix(77)
        self.assertMultiLineEqual(expected, actual)
        
    def test_septe_n_exception_107(self):
        expected = 'septencentillion'
        actual = spellnum.functions.get_period_suffix(107)
        self.assertMultiLineEqual(expected, actual)
        
    def test_septe_n_exception_207(self):
        expected = 'septenducentillion'
        actual = spellnum.functions.get_period_suffix(207)
        self.assertMultiLineEqual(expected, actual)
        
    def test_septe_n_exception_307(self):
        expected = 'septentrecentillion'
        actual = spellnum.functions.get_period_suffix(307)
        self.assertMultiLineEqual(expected, actual)
        
    def test_septe_n_exception_407(self):
        expected = 'septenquadringentillion'
        actual = spellnum.functions.get_period_suffix(407)
        self.assertMultiLineEqual(expected, actual)
        
    def test_septe_n_exception_507(self):
        expected = 'septenquingentillion'
        actual = spellnum.functions.get_period_suffix(507)
        self.assertMultiLineEqual(expected, actual)
        
    def test_septe_n_exception_607(self):
        expected = 'septensescentillion'
        actual = spellnum.functions.get_period_suffix(607)
        self.assertMultiLineEqual(expected, actual)
        
    def test_septe_n_exception_707(self):
        expected = 'septenseptingentillion'
        actual = spellnum.functions.get_period_suffix(707)
        self.assertMultiLineEqual(expected, actual)
        
    def test_nove_m_exception_29(self):
        expected = 'novemvigintillion'
        actual = spellnum.functions.get_period_suffix(29)
        self.assertMultiLineEqual(expected, actual)
        
    def test_nove_m_exception_89(self):
        expected = 'novemoctogintillion'
        actual = spellnum.functions.get_period_suffix(89)
        self.assertMultiLineEqual(expected, actual)
        
    def test_nove_m_exception_809(self):
        expected = 'novemoctingentillion'
        actual = spellnum.functions.get_period_suffix(809)
        self.assertMultiLineEqual(expected, actual)
        
    def test_nove_n_exception_19(self):
        expected = 'novendecillion'
        actual = spellnum.functions.get_period_suffix(19)
        self.assertMultiLineEqual(expected, actual)
        
    def test_nove_n_exception_39(self):
        expected = 'noventrigintillion'
        actual = spellnum.functions.get_period_suffix(39)
        self.assertMultiLineEqual(expected, actual)
        
    def test_nove_n_exception_49(self):
        expected = 'novenquadragintillion'
        actual = spellnum.functions.get_period_suffix(49)
        self.assertMultiLineEqual(expected, actual)
        
    def test_nove_n_exception_59(self):
        expected = 'novenquinquagintillion'
        actual = spellnum.functions.get_period_suffix(59)
        self.assertMultiLineEqual(expected, actual)
        
    def test_nove_n_exception_69(self):
        expected = 'novensexagintillion'
        actual = spellnum.functions.get_period_suffix(69)
        self.assertMultiLineEqual(expected, actual)
        
    def test_nove_n_exception_79(self):
        expected = 'novenseptuagintillion'
        actual = spellnum.functions.get_period_suffix(79)
        self.assertMultiLineEqual(expected, actual)
        
    def test_nove_n_exception_109(self):
        expected = 'novencentillion'
        actual = spellnum.functions.get_period_suffix(109)
        self.assertMultiLineEqual(expected, actual)
        
    def test_nove_n_exception_209(self):
        expected = 'novenducentillion'
        actual = spellnum.functions.get_period_suffix(209)
        self.assertMultiLineEqual(expected, actual)
        
    def test_nove_n_exception_309(self):
        expected = 'noventrecentillion'
        actual = spellnum.functions.get_period_suffix(309)
        self.assertMultiLineEqual(expected, actual)
        
    def test_nove_n_exception_409(self):
        expected = 'novenquadringentillion'
        actual = spellnum.functions.get_period_suffix(409)
        self.assertMultiLineEqual(expected, actual)
        
    def test_nove_n_exception_509(self):
        expected = 'novenquingentillion'
        actual = spellnum.functions.get_period_suffix(509)
        self.assertMultiLineEqual(expected, actual)
        
    def test_nove_n_exception_609(self):
        expected = 'novensescentillion'
        actual = spellnum.functions.get_period_suffix(609)
        self.assertMultiLineEqual(expected, actual)
        
    def test_nove_n_exception_709(self):
        expected = 'novenseptingentillion'
        actual = spellnum.functions.get_period_suffix(709)
        self.assertMultiLineEqual(expected, actual)
        
    def test_103_vs_300(self):
        """
        This is a known 'close' case. It is the reason for conditional
        in get_period_suffix where lexical component combination
        exceptions are caught and corrected with regular expressions.
        A base-illion of 103 should return 'trescentillion' since it IS an exception.
        A base-illion of 300 should return 'trecentillion' since it IS NOT an exception.
        """
        trescentillion = spellnum.functions.get_period_suffix(103)
        trecentillion = spellnum.functions.get_period_suffix(300)
        self.assertNotEqual(trescentillion, trecentillion)
        
        
class SpellingInputValidity(unittest.TestCase):
    """
    Tests valid and invalid input type and boundary values for spell.
    """
    
    def test_input_EQ_minimum(self):
        # smallest value would actually be -9.99...(repeating forever)...e3002
        expected = 'negative nine hundred ninety-nine novenonagintanongentillion'
        actual = spellnum.functions.spell('-9.99e3002')
        self.assertMultiLineEqual(expected, actual)
        
    def test_input_EQ_maximum(self):
        # largest value would actually be 9.99...(repeating forever)...e3002
        expected = 'nine hundred ninety-nine novenonagintanongentillion'
        actual = spellnum.functions.spell('9.99e3002')
        self.assertMultiLineEqual(expected, actual)
        
    def test_precision_EQ_maximum(self):
        expected = 'one one hundred novenonagintanongentillionth'
        actual = spellnum.functions.spell('1e-3002')
        self.assertMultiLineEqual(expected, actual)
        
    def test_input_LT_minimum(self):
        self.assertRaises(ValueError, spellnum.functions.spell, '-1e3003')
        
    def test_input_GT_Maximum(self):
        self.assertRaises(ValueError, spellnum.functions.spell, '1e3003')
        
    def test_precision_GT_maximum(self):
        self.assertRaises(ValueError, spellnum.functions.spell, '0.1e-3002')
        
    def test_input_none(self):
        self.assertRaises(ValueError, spellnum.functions.spell, None)
        
    def test_input_set(self):
        self.assertRaises(ValueError, spellnum.functions.spell, {123, })
        
    def test_input_list(self):
        self.assertRaises(ValueError, spellnum.functions.spell, [123, ])
        
    def test_input_tuple(self):
        self.assertRaises(ValueError, spellnum.functions.spell, (123,))
        
    def test_string_dXXX(self):
        expected = 'one hundred twenty-three one thousandths'
        self.assertMultiLineEqual(expected, spellnum.functions.spell('.123'))
        self.assertMultiLineEqual('negative ' + expected, spellnum.functions.spell('-.123'))
        
    def test_string_ndXXX(self):
        expected = 'one hundred twenty-three one thousandths'
        self.assertMultiLineEqual(expected, spellnum.functions.spell('.123'))
        self.assertMultiLineEqual('negative ' + expected, spellnum.functions.spell('-.123'))
        
    def test_ValidFormat_dXeX(self):
        expected = 'one hundred million'
        self.assertMultiLineEqual(expected, spellnum.functions.spell(.1e9))
        self.assertMultiLineEqual(expected, spellnum.functions.spell('.1e9'))
        self.assertMultiLineEqual('negative ' + expected, spellnum.functions.spell(-.1e9))
        self.assertMultiLineEqual('negative ' + expected, spellnum.functions.spell('-.1e9'))
        
    def test_ValidFormat_XdXEX(self):
        expected = 'one billion two hundred million'
        self.assertMultiLineEqual(expected, spellnum.functions.spell(1.2E9))
        self.assertMultiLineEqual(expected, spellnum.functions.spell('1.2E9'))
        self.assertMultiLineEqual('negative ' + expected, spellnum.functions.spell(-1.2E9))
        self.assertMultiLineEqual('negative ' + expected, spellnum.functions.spell('-1.2E9'))
        
    def test_ValidFormat_XdXeX(self):
        expected = 'one billion two hundred million'
        self.assertMultiLineEqual(expected, spellnum.functions.spell(1.2e9))
        self.assertMultiLineEqual(expected, spellnum.functions.spell('1.2e9'))
        self.assertMultiLineEqual('negative ' + expected, spellnum.functions.spell(-1.2e9))
        self.assertMultiLineEqual('negative ' + expected, spellnum.functions.spell('-1.2e9'))
        
    def test_ValidFormat_XdXenX(self):
        expected = 'twelve ten billionths'
        self.assertMultiLineEqual(expected, spellnum.functions.spell(1.2e-9))
        self.assertMultiLineEqual(expected, spellnum.functions.spell('1.2e-9'))
        self.assertMultiLineEqual('negative ' + expected, spellnum.functions.spell(-1.2e-9))
        self.assertMultiLineEqual('negative ' + expected, spellnum.functions.spell('-1.2e-9'))
        
    def test_ValidFormat_0dXeX(self):
        expected = 'one hundred million'
        self.assertMultiLineEqual(expected, spellnum.functions.spell(0.1e9))
        self.assertMultiLineEqual(expected, spellnum.functions.spell('0.1e9'))
        self.assertMultiLineEqual('negative ' + expected, spellnum.functions.spell(-0.1e9))
        self.assertMultiLineEqual('negative ' + expected, spellnum.functions.spell('-0.1e9'))
        
    def test_ValidFormat_Xd0eX(self):
        expected = 'one billion'
        self.assertMultiLineEqual(expected, spellnum.functions.spell(1.0e9))
        self.assertMultiLineEqual(expected, spellnum.functions.spell('1.0e9'))
        self.assertMultiLineEqual('negative ' + expected, spellnum.functions.spell(-1.0e9))
        self.assertMultiLineEqual('negative ' + expected, spellnum.functions.spell('-1.0e9'))
        
    def test_ValidFormat_XXXdXXXeXXX(self):
        expected = 'one hundred twenty-three quadragintillion four hundred fifty-six noventrigintillion'
        self.assertMultiLineEqual(expected, spellnum.functions.spell(123.456e123))
        self.assertMultiLineEqual(expected, spellnum.functions.spell('123.456e123'))
        self.assertMultiLineEqual('negative ' + expected, spellnum.functions.spell(-123.456e123))
        self.assertMultiLineEqual('negative ' + expected, spellnum.functions.spell('-123.456e123'))
        
    def test_ValidFormat_0XXdXX0e0XX(self):
        expected = 'twelve trillion three hundred forty billion'
        self.assertMultiLineEqual(expected, spellnum.functions.spell(012.340e012))
        self.assertMultiLineEqual(expected, spellnum.functions.spell('012.340e012'))
        self.assertMultiLineEqual('negative ' + expected, spellnum.functions.spell(-012.340e012))
        self.assertMultiLineEqual('negative ' + expected, spellnum.functions.spell('-012.340e012'))
        
    def test_PrecisionRetention(self):
        expected = ('one quadragintillion two hundred thirty-four noventrigintillion five hundred sixty-seven '
                    'octotrigintillion eight hundred ninety-eight septentrigintillion seven hundred sixty-five '
                    'sestrigintillion four hundred thirty-two quinquatrigintillion one hundred quattuortrigintillion')
        self.assertMultiLineEqual(expected, spellnum.functions.spell('1.2345678987654321e123'))
        self.assertMultiLineEqual('negative ' + expected, spellnum.functions.spell('-1.2345678987654321e123'))
        
    def test_InvalidInputs(self):
        self.assertRaises(ValueError, spellnum.functions.spell, '')
        self.assertRaises(ValueError, spellnum.functions.spell, '.')
        self.assertRaises(ValueError, spellnum.functions.spell, 'e')
        self.assertRaises(ValueError, spellnum.functions.spell, '-')
        self.assertRaises(ValueError, spellnum.functions.spell, '+')
        self.assertRaises(ValueError, spellnum.functions.spell, '.e')
        self.assertRaises(ValueError, spellnum.functions.spell, '.0e')
        self.assertRaises(ValueError, spellnum.functions.spell, '.0e-')
        self.assertRaises(ValueError, spellnum.functions.spell, '0.0e')
        self.assertRaises(ValueError, spellnum.functions.spell, '0.0e-')
        self.assertRaises(ValueError, spellnum.functions.spell, '0.e-0')
        self.assertRaises(ValueError, spellnum.functions.spell, '--123')
        self.assertRaises(ValueError, spellnum.functions.spell, '++123')
        self.assertRaises(ValueError, spellnum.functions.spell, '-+123')
        self.assertRaises(ValueError, spellnum.functions.spell, '+-123')
        self.assertRaises(ValueError, spellnum.functions.spell, '1.2.3')
        
        
class SpellingExceptions(unittest.TestCase):
    """
    Tests 'zero' spelling use cases for spell.
    NOTE: Due to the number of valid input formats, these tests are not exhaustive.
    """
    
    def test_singular_fraction(self):
        expected = 'one tenth'
        actual = spellnum.functions.spell(0.1)
        self.assertMultiLineEqual(expected, actual)
        
    def test_float_0(self):
        expected = 'zero'
        actual = spellnum.functions.spell(0)
        self.assertMultiLineEqual(expected, actual)
        
    def test_float_0d0(self):
        expected = 'zero'
        actual = spellnum.functions.spell(0.0)
        self.assertMultiLineEqual(expected, actual)
        
    def test_float_0e0(self):
        expected = 'zero'
        actual = spellnum.functions.spell(0e0)
        self.assertMultiLineEqual(expected, actual)
        
    def test_float_d0e0(self):
        expected = 'zero'
        actual = spellnum.functions.spell(.0e0)
        self.assertMultiLineEqual(expected, actual)
        
    def test_float_0d0e0(self):
        expected = 'zero'
        actual = spellnum.functions.spell(0.0e0)
        self.assertMultiLineEqual(expected, actual)
        
    def test_float_n0(self):
        expected = 'zero'
        actual = spellnum.functions.spell(-0)
        self.assertMultiLineEqual(expected, actual)
        
    def test_float_n0d0(self):
        expected = 'zero'
        actual = spellnum.functions.spell(-0.0)
        self.assertMultiLineEqual(expected, actual)
        
    def test_float_n0en0(self):
        expected = 'zero'
        actual = spellnum.functions.spell(-0e-0)
        self.assertMultiLineEqual(expected, actual)
        
    def test_float_n0d0en0(self):
        expected = 'zero'
        actual = spellnum.functions.spell(-0.0e-0)
        self.assertMultiLineEqual(expected, actual)
        
    def test_string_0(self):
        expected = 'zero'
        actual = spellnum.functions.spell('0')
        self.assertMultiLineEqual(expected, actual)
        
    def test_string_0d0(self):
        expected = 'zero'
        actual = spellnum.functions.spell('0.0')
        self.assertMultiLineEqual(expected, actual)
        
    def test_string_d0e0(self):
        expected = 'zero'
        actual = spellnum.functions.spell('.0e0')
        self.assertMultiLineEqual(expected, actual)
        
    def test_string_0e0(self):
        expected = 'zero'
        actual = spellnum.functions.spell('0e0')
        self.assertMultiLineEqual(expected, actual)
        
    def test_string_0d0e0(self):
        expected = 'zero'
        actual = spellnum.functions.spell('0.0e0')
        self.assertMultiLineEqual(expected, actual)
        
    def test_string_n0(self):
        expected = 'zero'
        actual = spellnum.functions.spell('-0')
        self.assertMultiLineEqual(expected, actual)
        
    def test_string_n0d0(self):
        expected = 'zero'
        actual = spellnum.functions.spell('-0.0')
        self.assertMultiLineEqual(expected, actual)
        
    def test_string_n0en0(self):
        expected = 'zero'
        actual = spellnum.functions.spell('-0e-0')
        self.assertMultiLineEqual(expected, actual)
        
    def test_string_n0d0en0(self):
        expected = 'zero'
        actual = spellnum.functions.spell('-0.0e-0')
        self.assertMultiLineEqual(expected, actual)
        
        
class SpellingScientific(unittest.TestCase):
    """
    Tests spelling numbers in scientific notation.
    """
    
    def test_float_XXdXXe3(self):
        expected = spellnum.functions.spell(12340)
        actual = spellnum.functions.spell(12.34e3)
        self.assertMultiLineEqual(expected, actual)
        
    def test_float_XXdXXe2(self):
        expected = spellnum.functions.spell(1234)
        actual = spellnum.functions.spell(12.34e2)
        self.assertMultiLineEqual(expected, actual)
        
    def test_float_XXdXXe1(self):
        expected = spellnum.functions.spell(123.4)
        actual = spellnum.functions.spell(12.34e1)
        self.assertMultiLineEqual(expected, actual)
        
    def test_float_XXdXXe0(self):
        expected = spellnum.functions.spell(12.34)
        actual = spellnum.functions.spell(12.34e0)
        self.assertMultiLineEqual(expected, actual)
        
    def test_float_XXdXXen0(self):
        expected = spellnum.functions.spell(12.34)
        actual = spellnum.functions.spell(12.34e-0)
        self.assertMultiLineEqual(expected, actual)
        
    def test_float_XXdXXen1(self):
        expected = spellnum.functions.spell(1.234)
        actual = spellnum.functions.spell(12.34e-1)
        self.assertMultiLineEqual(expected, actual)
        
    def test_float_XXdXXen2(self):
        expected = spellnum.functions.spell(.1234)
        actual = spellnum.functions.spell(12.34e-2)
        self.assertMultiLineEqual(expected, actual)
        
    def test_float_XXdXXen3(self):
        expected = spellnum.functions.spell(.01234)
        actual = spellnum.functions.spell(12.34e-3)
        self.assertMultiLineEqual(expected, actual)
        
    def test_string_XXdXXe3(self):
        expected = spellnum.functions.spell(12340)
        actual = spellnum.functions.spell('12.34e3')
        self.assertMultiLineEqual(expected, actual)
        
    def test_string_XXdXXe2(self):
        expected = spellnum.functions.spell(1234)
        actual = spellnum.functions.spell('12.34e2')
        self.assertMultiLineEqual(expected, actual)
        
    def test_string_XXdXXe1(self):
        expected = spellnum.functions.spell(123.4)
        actual = spellnum.functions.spell('12.34e1')
        self.assertMultiLineEqual(expected, actual)
        
    def test_string_XXdXXe0(self):
        expected = spellnum.functions.spell(12.34)
        actual = spellnum.functions.spell('12.34e0')
        self.assertMultiLineEqual(expected, actual)
        
    def test_string_XXdXXen0(self):
        expected = spellnum.functions.spell(12.34)
        actual = spellnum.functions.spell('12.34e-0')
        self.assertMultiLineEqual(expected, actual)
        
    def test_string_XXdXXen1(self):
        expected = spellnum.functions.spell(1.234)
        actual = spellnum.functions.spell('12.34e-1')
        self.assertMultiLineEqual(expected, actual)
        
    def test_string_XXdXXen2(self):
        expected = spellnum.functions.spell(.1234)
        actual = spellnum.functions.spell('12.34e-2')
        self.assertMultiLineEqual(expected, actual)
        
    def test_string_XXdXXen3(self):
        expected = spellnum.functions.spell(.01234)
        actual = spellnum.functions.spell('12.34e-3')
        self.assertMultiLineEqual(expected, actual)
        
    def test_float_0d1eXX(self):
        expected = 'one vigintillion'
        actual = spellnum.functions.spell(0.1e64)
        self.assertMultiLineEqual(expected, actual)
        
    def test_float_1d0eXX(self):
        expected = 'one vigintillion'
        actual = spellnum.functions.spell(1.0e63)
        self.assertMultiLineEqual(expected, actual)
        
    def test_float_0d1enXX(self):
        expected = 'one one vigintillionth'
        actual = spellnum.functions.spell(0.1e-62)
        self.assertMultiLineEqual(expected, actual)
        
    def test_float_1d0enXX(self):
        expected = 'one one vigintillionth'
        actual = spellnum.functions.spell(1.0e-63)
        self.assertMultiLineEqual(expected, actual)
        
    def test_string_0d1eXX(self):
        expected = 'one vigintillion'
        actual = spellnum.functions.spell('0.1e64')
        self.assertMultiLineEqual(expected, actual)
        
    def test_string_1d0eXX(self):
        expected = 'one vigintillion'
        actual = spellnum.functions.spell('1.0e63')
        self.assertMultiLineEqual(expected, actual)
        
    def test_string_0d1enXX(self):
        expected = 'one one vigintillionth'
        actual = spellnum.functions.spell('0.1e-62')
        self.assertMultiLineEqual(expected, actual)
        
    def test_string_1d0enXX(self):
        expected = 'one one vigintillionth'
        actual = spellnum.functions.spell('1.0e-63')
        self.assertMultiLineEqual(expected, actual)
        
        
class SpellingDecimal(unittest.TestCase):
    """
    Tests spelling numbers with fractions in decimal format.
    """
    
    def test_float_X00XdX(self):
        expected = 'one thousand two and three tenths'
        actual = spellnum.functions.spell(1002.3)
        self.assertMultiLineEqual(expected, actual)
        
    def test_float_X0XdXX(self):
        expected = 'one hundred two and thirty-four one hundredths'
        actual = spellnum.functions.spell(102.34)
        self.assertMultiLineEqual(expected, actual)
        
    def test_float_XXdX0X(self):
        expected = 'twelve and three hundred four one thousandths'
        actual = spellnum.functions.spell(12.304)
        self.assertMultiLineEqual(expected, actual)
        
    def test_float_XdX00X(self):
        expected = 'two and three thousand four ten thousandths'
        actual = spellnum.functions.spell(2.3004)
        self.assertMultiLineEqual(expected, actual)
        
    def test_float_dX000X(self):
        expected = 'thirty thousand four one hundred thousandths'
        actual = spellnum.functions.spell(.30004)
        self.assertMultiLineEqual(expected, actual)
        
    def test_string_X00XdX(self):
        expected = 'one thousand two and three tenths'
        actual = spellnum.functions.spell('1002.3')
        self.assertMultiLineEqual(expected, actual)
        
    def test_string_X0XdXX(self):
        expected = 'one hundred two and thirty-four one hundredths'
        actual = spellnum.functions.spell('102.34')
        self.assertMultiLineEqual(expected, actual)
        
    def test_string_XXdX0X(self):
        expected = 'twelve and three hundred four one thousandths'
        actual = spellnum.functions.spell('12.304')
        self.assertMultiLineEqual(expected, actual)
        
    def test_string_XdX00X(self):
        expected = 'two and three thousand four ten thousandths'
        actual = spellnum.functions.spell('2.3004')
        self.assertMultiLineEqual(expected, actual)
        
    def test_string_dX000X(self):
        expected = 'thirty thousand four one hundred thousandths'
        actual = spellnum.functions.spell('.30004')
        self.assertMultiLineEqual(expected, actual)
