"""
Unit tests for spellnum module.
"""

from unittest import TestCase
from spellnum import nameperiod, readperiod


# TODO: refactor, reevaluate, and expand on test cases where necessary


class NamePeriodTests(TestCase):
    """
    Tests nameperiod functions.
    """
    
    def test_invalid_input_types(self):
        for invalid_type in (None, 1.23, '1.23', set(), list(), tuple()):
            with self.subTest(invalid_type=invalid_type):
                self.assertRaises(TypeError, nameperiod, invalid_type)
                
                
class ReadPeriodTests(TestCase):
    """
    Tests readperiod functions.
    """
    
    def test_invalid_input_name(self):
        for invalid_name in ():
            with self.subTest(invalid_name=invalid_name):
                self.assertRaises(TypeError, nameperiod, invalid_name)
    
    
class SuffixNominalCases(TestCase):
    """
    Tests generic use cases for nameperiod.
    
    The nonaginatillions have no lexical exceptions making them a good
    spot-check for nominal testing.
    """
    
    def test_suffix_uniqueness(self):
        expected = 1001  # expected number of unique suffixes
        unique_suffix_count = len(set(nameperiod(bi) for bi in range(-1, 1000)))
        self.assertEqual(expected, unique_suffix_count)
        
    def test_90(self):
        expected = 'nonagintillion'
        actual = nameperiod(90)
        self.assertMultiLineEqual(expected, actual)
        
    def test_91(self):
        expected = 'unnonagintillion'
        actual = nameperiod(91)
        self.assertMultiLineEqual(expected, actual)
        
    def test_92(self):
        expected = 'duononagintillion'
        actual = nameperiod(92)
        self.assertMultiLineEqual(expected, actual)
        
    def test_93(self):
        expected = 'trenonagintillion'
        actual = nameperiod(93)
        self.assertMultiLineEqual(expected, actual)
        
    def test_94(self):
        expected = 'quattuornonagintillion'
        actual = nameperiod(94)
        self.assertMultiLineEqual(expected, actual)
        
    def test_95(self):
        expected = 'quinquanonagintillion'
        actual = nameperiod(95)
        self.assertMultiLineEqual(expected, actual)
        
    def test_96(self):
        expected = 'senonagintillion'
        actual = nameperiod(96)
        self.assertMultiLineEqual(expected, actual)
        
    def test_97(self):
        expected = 'septenonagintillion'
        actual = nameperiod(97)
        self.assertMultiLineEqual(expected, actual)
        
    def test_98(self):
        expected = 'octononagintillion'
        actual = nameperiod(98)
        self.assertMultiLineEqual(expected, actual)
        
    def test_99(self):
        expected = 'novenonagintillion'
        actual = nameperiod(99)
        self.assertMultiLineEqual(expected, actual)
        
        
class SuffixExceptions(TestCase):
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
        actual = nameperiod(26)
        self.assertMultiLineEqual(expected, actual)
        
    def test_se_s_exception_36(self):
        expected = 'sestrigintillion'
        actual = nameperiod(36)
        self.assertMultiLineEqual(expected, actual)
        
    def test_se_s_exception_46(self):
        expected = 'sesquadragintillion'
        actual = nameperiod(46)
        self.assertMultiLineEqual(expected, actual)
        
    def test_se_s_exception_56(self):
        expected = 'sesquinquagintillion'
        actual = nameperiod(56)
        self.assertMultiLineEqual(expected, actual)
        
    def test_se_s_exception_306(self):
        expected = 'sestrecentillion'
        actual = nameperiod(306)
        self.assertMultiLineEqual(expected, actual)
        
    def test_se_s_exception_406(self):
        expected = 'sesquadringentillion'
        actual = nameperiod(406)
        self.assertMultiLineEqual(expected, actual)
        
    def test_se_s_exception_506(self):
        expected = 'sesquingentillion'
        actual = nameperiod(506)
        self.assertMultiLineEqual(expected, actual)
        
    def test_tre_s_exception_23(self):
        expected = 'tresvigintillion'
        actual = nameperiod(23)
        self.assertMultiLineEqual(expected, actual)
        
    def test_tre_s_exception_33(self):
        expected = 'trestrigintillion'
        actual = nameperiod(33)
        self.assertMultiLineEqual(expected, actual)
        
    def test_tre_s_exception_43(self):
        expected = 'tresquadragintillion'
        actual = nameperiod(43)
        self.assertMultiLineEqual(expected, actual)
        
    def test_tre_s_exception_53(self):
        expected = 'tresquinquagintillion'
        actual = nameperiod(53)
        self.assertMultiLineEqual(expected, actual)
        
    def test_tre_s_exception_83(self):
        expected = 'tresoctogintillion'
        actual = nameperiod(83)
        self.assertMultiLineEqual(expected, actual)
        
    def test_tre_s_exception_103(self):
        expected = 'trescentillion'
        actual = nameperiod(103)
        self.assertMultiLineEqual(expected, actual)
        
    def test_tre_s_exception_303(self):
        expected = 'trestrecentillion'
        actual = nameperiod(303)
        self.assertMultiLineEqual(expected, actual)
        
    def test_tre_s_exception_403(self):
        expected = 'tresquadringentillion'
        actual = nameperiod(403)
        self.assertMultiLineEqual(expected, actual)
        
    def test_tre_s_exception_503(self):
        expected = 'tresquingentillion'
        actual = nameperiod(503)
        self.assertMultiLineEqual(expected, actual)
        
    def test_tre_s_exception_803(self):
        expected = 'tresoctingentillion'
        actual = nameperiod(803)
        self.assertMultiLineEqual(expected, actual)
        
    def test_se_x_exception_86(self):
        expected = 'sexoctogintillion'
        actual = nameperiod(86)
        self.assertMultiLineEqual(expected, actual)
        
    def test_se_x_exception_106(self):
        expected = 'sexcentillion'
        actual = nameperiod(106)
        self.assertMultiLineEqual(expected, actual)
        
    def test_se_x_exception_806(self):
        expected = 'sexoctingentillion'
        actual = nameperiod(806)
        self.assertMultiLineEqual(expected, actual)
        
    def test_septe_m_exception_27(self):
        expected = 'septemvigintillion'
        actual = nameperiod(27)
        self.assertMultiLineEqual(expected, actual)
        
    def test_septe_m_exception_87(self):
        expected = 'septemoctogintillion'
        actual = nameperiod(87)
        self.assertMultiLineEqual(expected, actual)
        
    def test_septe_m_exception_807(self):
        expected = 'septemoctingentillion'
        actual = nameperiod(807)
        self.assertMultiLineEqual(expected, actual)
        
    def test_septe_n_exception_17(self):
        expected = 'septendecillion'
        actual = nameperiod(17)
        self.assertMultiLineEqual(expected, actual)
        
    def test_septe_n_exception_37(self):
        expected = 'septentrigintillion'
        actual = nameperiod(37)
        self.assertMultiLineEqual(expected, actual)
        
    def test_septe_n_exception_47(self):
        expected = 'septenquadragintillion'
        actual = nameperiod(47)
        self.assertMultiLineEqual(expected, actual)
        
    def test_septe_n_exception_57(self):
        expected = 'septenquinquagintillion'
        actual = nameperiod(57)
        self.assertMultiLineEqual(expected, actual)
        
    def test_septe_n_exception_67(self):
        expected = 'septensexagintillion'
        actual = nameperiod(67)
        self.assertMultiLineEqual(expected, actual)
        
    def test_septe_n_exception_77(self):
        expected = 'septenseptuagintillion'
        actual = nameperiod(77)
        self.assertMultiLineEqual(expected, actual)
        
    def test_septe_n_exception_107(self):
        expected = 'septencentillion'
        actual = nameperiod(107)
        self.assertMultiLineEqual(expected, actual)
        
    def test_septe_n_exception_207(self):
        expected = 'septenducentillion'
        actual = nameperiod(207)
        self.assertMultiLineEqual(expected, actual)
        
    def test_septe_n_exception_307(self):
        expected = 'septentrecentillion'
        actual = nameperiod(307)
        self.assertMultiLineEqual(expected, actual)
        
    def test_septe_n_exception_407(self):
        expected = 'septenquadringentillion'
        actual = nameperiod(407)
        self.assertMultiLineEqual(expected, actual)
        
    def test_septe_n_exception_507(self):
        expected = 'septenquingentillion'
        actual = nameperiod(507)
        self.assertMultiLineEqual(expected, actual)
        
    def test_septe_n_exception_607(self):
        expected = 'septensescentillion'
        actual = nameperiod(607)
        self.assertMultiLineEqual(expected, actual)
        
    def test_septe_n_exception_707(self):
        expected = 'septenseptingentillion'
        actual = nameperiod(707)
        self.assertMultiLineEqual(expected, actual)
        
    def test_nove_m_exception_29(self):
        expected = 'novemvigintillion'
        actual = nameperiod(29)
        self.assertMultiLineEqual(expected, actual)
        
    def test_nove_m_exception_89(self):
        expected = 'novemoctogintillion'
        actual = nameperiod(89)
        self.assertMultiLineEqual(expected, actual)
        
    def test_nove_m_exception_809(self):
        expected = 'novemoctingentillion'
        actual = nameperiod(809)
        self.assertMultiLineEqual(expected, actual)
        
    def test_nove_n_exception_19(self):
        expected = 'novendecillion'
        actual = nameperiod(19)
        self.assertMultiLineEqual(expected, actual)
        
    def test_nove_n_exception_39(self):
        expected = 'noventrigintillion'
        actual = nameperiod(39)
        self.assertMultiLineEqual(expected, actual)
        
    def test_nove_n_exception_49(self):
        expected = 'novenquadragintillion'
        actual = nameperiod(49)
        self.assertMultiLineEqual(expected, actual)
        
    def test_nove_n_exception_59(self):
        expected = 'novenquinquagintillion'
        actual = nameperiod(59)
        self.assertMultiLineEqual(expected, actual)
        
    def test_nove_n_exception_69(self):
        expected = 'novensexagintillion'
        actual = nameperiod(69)
        self.assertMultiLineEqual(expected, actual)
        
    def test_nove_n_exception_79(self):
        expected = 'novenseptuagintillion'
        actual = nameperiod(79)
        self.assertMultiLineEqual(expected, actual)
        
    def test_nove_n_exception_109(self):
        expected = 'novencentillion'
        actual = nameperiod(109)
        self.assertMultiLineEqual(expected, actual)
        
    def test_nove_n_exception_209(self):
        expected = 'novenducentillion'
        actual = nameperiod(209)
        self.assertMultiLineEqual(expected, actual)
        
    def test_nove_n_exception_309(self):
        expected = 'noventrecentillion'
        actual = nameperiod(309)
        self.assertMultiLineEqual(expected, actual)
        
    def test_nove_n_exception_409(self):
        expected = 'novenquadringentillion'
        actual = nameperiod(409)
        self.assertMultiLineEqual(expected, actual)
        
    def test_nove_n_exception_509(self):
        expected = 'novenquingentillion'
        actual = nameperiod(509)
        self.assertMultiLineEqual(expected, actual)
        
    def test_nove_n_exception_609(self):
        expected = 'novensescentillion'
        actual = nameperiod(609)
        self.assertMultiLineEqual(expected, actual)
        
    def test_nove_n_exception_709(self):
        expected = 'novenseptingentillion'
        actual = nameperiod(709)
        self.assertMultiLineEqual(expected, actual)
        
    def test_103_vs_300(self):
        """
        This is a known 'close' case. It is the reason for conditional
        in nameperiod where lexical component combination
        exceptions are caught and corrected with regular expressions.
        A base-illion of 103 should return 'trescentillion' since it IS an exception.
        A base-illion of 300 should return 'trecentillion' since it IS NOT an exception.
        """
        trescentillion = nameperiod(103)
        trecentillion = nameperiod(300)
        self.assertNotEqual(trescentillion, trecentillion)
