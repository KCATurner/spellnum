"""
Unit tests for spellnum module.
"""

import unittest
import spellnum


# TODO: refactor, reevaluate, and expand on test cases where necessary


class SuffixInputValidity(unittest.TestCase):
    """
    Tests valid and invalid input type and boundary values for nameperiod.
    """
    
    def test_input_EQ_minimum(self):
        expected = ''
        self.assertMultiLineEqual(expected, spellnum.functions.nameperiod(-1))
        
    def test_input_EQ_maximum(self):
        expected = 'novenonagintanongentillion'
        self.assertMultiLineEqual(expected, spellnum.functions.nameperiod(999))
        
    def test_input_none(self):
        self.assertRaises(TypeError, spellnum.functions.nameperiod, None)
        
    def test_input_float(self):
        self.assertRaises(TypeError, spellnum.functions.nameperiod, 12.34)
        
    def test_input_string(self):
        self.assertRaises(TypeError, spellnum.functions.nameperiod, '12.34')
        
    def test_input_set(self):
        self.assertRaises(TypeError, spellnum.functions.nameperiod, set())
        
    def test_input_list(self):
        self.assertRaises(TypeError, spellnum.functions.nameperiod, list())
        
    def test_input_tuple(self):
        self.assertRaises(TypeError, spellnum.functions.nameperiod, tuple())
        
        
class SuffixNominalCases(unittest.TestCase):
    """
    Tests generic use cases for nameperiod.
    The nonaginatillions have no lexical exceptions making them a good spot-check for nominal testing.
    """
    
    def test_suffix_uniqueness(self):
        expected = 1001  # expected number of unique suffixes
        unique_suffix_count = len(set(spellnum.functions.nameperiod(bi) for bi in range(-1, 1000)))
        self.assertEqual(expected, unique_suffix_count)
        
    def test_90(self):
        expected = 'nonagintillion'
        actual = spellnum.functions.nameperiod(90)
        self.assertMultiLineEqual(expected, actual)
        
    def test_91(self):
        expected = 'unnonagintillion'
        actual = spellnum.functions.nameperiod(91)
        self.assertMultiLineEqual(expected, actual)
        
    def test_92(self):
        expected = 'duononagintillion'
        actual = spellnum.functions.nameperiod(92)
        self.assertMultiLineEqual(expected, actual)
        
    def test_93(self):
        expected = 'trenonagintillion'
        actual = spellnum.functions.nameperiod(93)
        self.assertMultiLineEqual(expected, actual)
        
    def test_94(self):
        expected = 'quattuornonagintillion'
        actual = spellnum.functions.nameperiod(94)
        self.assertMultiLineEqual(expected, actual)
        
    def test_95(self):
        expected = 'quinquanonagintillion'
        actual = spellnum.functions.nameperiod(95)
        self.assertMultiLineEqual(expected, actual)
        
    def test_96(self):
        expected = 'senonagintillion'
        actual = spellnum.functions.nameperiod(96)
        self.assertMultiLineEqual(expected, actual)
        
    def test_97(self):
        expected = 'septenonagintillion'
        actual = spellnum.functions.nameperiod(97)
        self.assertMultiLineEqual(expected, actual)
        
    def test_98(self):
        expected = 'octononagintillion'
        actual = spellnum.functions.nameperiod(98)
        self.assertMultiLineEqual(expected, actual)
        
    def test_99(self):
        expected = 'novenonagintillion'
        actual = spellnum.functions.nameperiod(99)
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
        actual = spellnum.functions.nameperiod(26)
        self.assertMultiLineEqual(expected, actual)
        
    def test_se_s_exception_36(self):
        expected = 'sestrigintillion'
        actual = spellnum.functions.nameperiod(36)
        self.assertMultiLineEqual(expected, actual)
        
    def test_se_s_exception_46(self):
        expected = 'sesquadragintillion'
        actual = spellnum.functions.nameperiod(46)
        self.assertMultiLineEqual(expected, actual)
        
    def test_se_s_exception_56(self):
        expected = 'sesquinquagintillion'
        actual = spellnum.functions.nameperiod(56)
        self.assertMultiLineEqual(expected, actual)
        
    def test_se_s_exception_306(self):
        expected = 'sestrecentillion'
        actual = spellnum.functions.nameperiod(306)
        self.assertMultiLineEqual(expected, actual)
        
    def test_se_s_exception_406(self):
        expected = 'sesquadringentillion'
        actual = spellnum.functions.nameperiod(406)
        self.assertMultiLineEqual(expected, actual)
        
    def test_se_s_exception_506(self):
        expected = 'sesquingentillion'
        actual = spellnum.functions.nameperiod(506)
        self.assertMultiLineEqual(expected, actual)
        
    def test_tre_s_exception_23(self):
        expected = 'tresvigintillion'
        actual = spellnum.functions.nameperiod(23)
        self.assertMultiLineEqual(expected, actual)
        
    def test_tre_s_exception_33(self):
        expected = 'trestrigintillion'
        actual = spellnum.functions.nameperiod(33)
        self.assertMultiLineEqual(expected, actual)
        
    def test_tre_s_exception_43(self):
        expected = 'tresquadragintillion'
        actual = spellnum.functions.nameperiod(43)
        self.assertMultiLineEqual(expected, actual)
        
    def test_tre_s_exception_53(self):
        expected = 'tresquinquagintillion'
        actual = spellnum.functions.nameperiod(53)
        self.assertMultiLineEqual(expected, actual)
        
    def test_tre_s_exception_83(self):
        expected = 'tresoctogintillion'
        actual = spellnum.functions.nameperiod(83)
        self.assertMultiLineEqual(expected, actual)
        
    def test_tre_s_exception_103(self):
        expected = 'trescentillion'
        actual = spellnum.functions.nameperiod(103)
        self.assertMultiLineEqual(expected, actual)
        
    def test_tre_s_exception_303(self):
        expected = 'trestrecentillion'
        actual = spellnum.functions.nameperiod(303)
        self.assertMultiLineEqual(expected, actual)
        
    def test_tre_s_exception_403(self):
        expected = 'tresquadringentillion'
        actual = spellnum.functions.nameperiod(403)
        self.assertMultiLineEqual(expected, actual)
        
    def test_tre_s_exception_503(self):
        expected = 'tresquingentillion'
        actual = spellnum.functions.nameperiod(503)
        self.assertMultiLineEqual(expected, actual)
        
    def test_tre_s_exception_803(self):
        expected = 'tresoctingentillion'
        actual = spellnum.functions.nameperiod(803)
        self.assertMultiLineEqual(expected, actual)
        
    def test_se_x_exception_86(self):
        expected = 'sexoctogintillion'
        actual = spellnum.functions.nameperiod(86)
        self.assertMultiLineEqual(expected, actual)
        
    def test_se_x_exception_106(self):
        expected = 'sexcentillion'
        actual = spellnum.functions.nameperiod(106)
        self.assertMultiLineEqual(expected, actual)
        
    def test_se_x_exception_806(self):
        expected = 'sexoctingentillion'
        actual = spellnum.functions.nameperiod(806)
        self.assertMultiLineEqual(expected, actual)
        
    def test_septe_m_exception_27(self):
        expected = 'septemvigintillion'
        actual = spellnum.functions.nameperiod(27)
        self.assertMultiLineEqual(expected, actual)
        
    def test_septe_m_exception_87(self):
        expected = 'septemoctogintillion'
        actual = spellnum.functions.nameperiod(87)
        self.assertMultiLineEqual(expected, actual)
        
    def test_septe_m_exception_807(self):
        expected = 'septemoctingentillion'
        actual = spellnum.functions.nameperiod(807)
        self.assertMultiLineEqual(expected, actual)
        
    def test_septe_n_exception_17(self):
        expected = 'septendecillion'
        actual = spellnum.functions.nameperiod(17)
        self.assertMultiLineEqual(expected, actual)
        
    def test_septe_n_exception_37(self):
        expected = 'septentrigintillion'
        actual = spellnum.functions.nameperiod(37)
        self.assertMultiLineEqual(expected, actual)
        
    def test_septe_n_exception_47(self):
        expected = 'septenquadragintillion'
        actual = spellnum.functions.nameperiod(47)
        self.assertMultiLineEqual(expected, actual)
        
    def test_septe_n_exception_57(self):
        expected = 'septenquinquagintillion'
        actual = spellnum.functions.nameperiod(57)
        self.assertMultiLineEqual(expected, actual)
        
    def test_septe_n_exception_67(self):
        expected = 'septensexagintillion'
        actual = spellnum.functions.nameperiod(67)
        self.assertMultiLineEqual(expected, actual)
        
    def test_septe_n_exception_77(self):
        expected = 'septenseptuagintillion'
        actual = spellnum.functions.nameperiod(77)
        self.assertMultiLineEqual(expected, actual)
        
    def test_septe_n_exception_107(self):
        expected = 'septencentillion'
        actual = spellnum.functions.nameperiod(107)
        self.assertMultiLineEqual(expected, actual)
        
    def test_septe_n_exception_207(self):
        expected = 'septenducentillion'
        actual = spellnum.functions.nameperiod(207)
        self.assertMultiLineEqual(expected, actual)
        
    def test_septe_n_exception_307(self):
        expected = 'septentrecentillion'
        actual = spellnum.functions.nameperiod(307)
        self.assertMultiLineEqual(expected, actual)
        
    def test_septe_n_exception_407(self):
        expected = 'septenquadringentillion'
        actual = spellnum.functions.nameperiod(407)
        self.assertMultiLineEqual(expected, actual)
        
    def test_septe_n_exception_507(self):
        expected = 'septenquingentillion'
        actual = spellnum.functions.nameperiod(507)
        self.assertMultiLineEqual(expected, actual)
        
    def test_septe_n_exception_607(self):
        expected = 'septensescentillion'
        actual = spellnum.functions.nameperiod(607)
        self.assertMultiLineEqual(expected, actual)
        
    def test_septe_n_exception_707(self):
        expected = 'septenseptingentillion'
        actual = spellnum.functions.nameperiod(707)
        self.assertMultiLineEqual(expected, actual)
        
    def test_nove_m_exception_29(self):
        expected = 'novemvigintillion'
        actual = spellnum.functions.nameperiod(29)
        self.assertMultiLineEqual(expected, actual)
        
    def test_nove_m_exception_89(self):
        expected = 'novemoctogintillion'
        actual = spellnum.functions.nameperiod(89)
        self.assertMultiLineEqual(expected, actual)
        
    def test_nove_m_exception_809(self):
        expected = 'novemoctingentillion'
        actual = spellnum.functions.nameperiod(809)
        self.assertMultiLineEqual(expected, actual)
        
    def test_nove_n_exception_19(self):
        expected = 'novendecillion'
        actual = spellnum.functions.nameperiod(19)
        self.assertMultiLineEqual(expected, actual)
        
    def test_nove_n_exception_39(self):
        expected = 'noventrigintillion'
        actual = spellnum.functions.nameperiod(39)
        self.assertMultiLineEqual(expected, actual)
        
    def test_nove_n_exception_49(self):
        expected = 'novenquadragintillion'
        actual = spellnum.functions.nameperiod(49)
        self.assertMultiLineEqual(expected, actual)
        
    def test_nove_n_exception_59(self):
        expected = 'novenquinquagintillion'
        actual = spellnum.functions.nameperiod(59)
        self.assertMultiLineEqual(expected, actual)
        
    def test_nove_n_exception_69(self):
        expected = 'novensexagintillion'
        actual = spellnum.functions.nameperiod(69)
        self.assertMultiLineEqual(expected, actual)
        
    def test_nove_n_exception_79(self):
        expected = 'novenseptuagintillion'
        actual = spellnum.functions.nameperiod(79)
        self.assertMultiLineEqual(expected, actual)
        
    def test_nove_n_exception_109(self):
        expected = 'novencentillion'
        actual = spellnum.functions.nameperiod(109)
        self.assertMultiLineEqual(expected, actual)
        
    def test_nove_n_exception_209(self):
        expected = 'novenducentillion'
        actual = spellnum.functions.nameperiod(209)
        self.assertMultiLineEqual(expected, actual)
        
    def test_nove_n_exception_309(self):
        expected = 'noventrecentillion'
        actual = spellnum.functions.nameperiod(309)
        self.assertMultiLineEqual(expected, actual)
        
    def test_nove_n_exception_409(self):
        expected = 'novenquadringentillion'
        actual = spellnum.functions.nameperiod(409)
        self.assertMultiLineEqual(expected, actual)
        
    def test_nove_n_exception_509(self):
        expected = 'novenquingentillion'
        actual = spellnum.functions.nameperiod(509)
        self.assertMultiLineEqual(expected, actual)
        
    def test_nove_n_exception_609(self):
        expected = 'novensescentillion'
        actual = spellnum.functions.nameperiod(609)
        self.assertMultiLineEqual(expected, actual)
        
    def test_nove_n_exception_709(self):
        expected = 'novenseptingentillion'
        actual = spellnum.functions.nameperiod(709)
        self.assertMultiLineEqual(expected, actual)
        
    def test_103_vs_300(self):
        """
        This is a known 'close' case. It is the reason for conditional
        in nameperiod where lexical component combination
        exceptions are caught and corrected with regular expressions.
        A base-illion of 103 should return 'trescentillion' since it IS an exception.
        A base-illion of 300 should return 'trecentillion' since it IS NOT an exception.
        """
        trescentillion = spellnum.functions.nameperiod(103)
        trecentillion = spellnum.functions.nameperiod(300)
        self.assertNotEqual(trescentillion, trecentillion)
