"""
Unit tests for conwech.lexicon.
"""

from unittest import TestCase
from conwech import lexicon


class LexiconStructureTests(TestCase):
    """
    Verify that the lexicon number tuples are built properly.
    """
    
    def test_1_digit_integers(self):
        """
        Check numbers [0, 10)
        """
        for index in range(10):
            with self.subTest(msg='POS', number=index):
                expected = lexicon.NATURAL_NUMBERS_LT_20[index]
                actual = lexicon.NATURAL_NUMBERS_LT_1000[index]
                self.assertMultiLineEqual(expected, actual)
                
    def test_2_digit_integers(self):
        """
        Check numbers [10, 100)
        """
        for index in range(10, 100):
            with self.subTest(msg='POS', number=index):
                self.subTest(msg='POS', index=index)
                expected = lexicon.NATURAL_NUMBERS_LT_100[index]
                actual = lexicon.NATURAL_NUMBERS_LT_1000[index]
                self.assertMultiLineEqual(expected, actual)
                
    def test_3_digit_integers(self):
        """
        Check numbers [100, 1000)
        """
        for index in range(100, 1000):
            with self.subTest(msg='POS', number=index):
                hundred = lexicon.NATURAL_NUMBERS_LT_20[index // 100]
                tens = lexicon.NATURAL_NUMBERS_LT_100[index % 100]
                expected = '{} hundred {}'.format(hundred, tens).strip()
                actual = lexicon.NATURAL_NUMBERS_LT_1000[index]
                self.assertMultiLineEqual(expected, actual)
                
                
class ZillionPrefixTests(TestCase):
    """
    Verify that the lexicon period prefixes were built properly.
    """
    
    def setUp(self):
        self.unit = lexicon._UNIT_PREFIX_COMPONENTS
        self.tens = lexicon._TENS_PREFIX_COMPONENTS
        self.hund = lexicon._HUND_PREFIX_COMPONENTS
        self.prefixes = lexicon.ZILLION_PERIOD_PREFIXES
        
    def test_known_similarities(self):
        """
        Test prefixes known to be extremely similar.
            
             du[o]centillion  !=   du[ ]centillion
            tre[s]centillion  !=  tre[ ]centillion
             se[x]centillion  !=   se[s]centillion
        """
        for pair in (102, 200), (103, 300), (106, 600):
            with self.subTest(msg='NEG', pair=pair):
                self.assertNotEqual(*[self.prefixes[b].rstrip('ia') for b in pair])
                
    def test_prefix_uniqueness(self):
        """
        All prefixes must be unique.
        """
        expected = len(self.prefixes)
        with self.subTest(msg='POS', expected_length=expected):
            actual = len(set(self.prefixes))
            self.assertEqual(expected, actual)
        
    def test_m_exceptions(self):
        """
        Test when 'm' is appended to the 'septe' or 'nove' prefixes.
        
        Billion Exceptions:
            - septe(m):  27,  87, 807
            -  nove(m):  29,  89, 809
        """
        for zillion in (27, 87, 807, 29, 89, 809):
            with self.subTest(msg='POS', zillion=zillion):
                hund, tens, unit = (int(digit) for digit in str(zillion).zfill(3))
                expected = str(self.unit[unit] + 'm' + self.tens[tens] + self.hund[hund]).rstrip('ai')
                self.assertMultiLineEqual(expected, self.prefixes[zillion])
                
    def test_n_exceptions(self):
        """
        Test when 'n' is appended to the 'septe' or 'nove' prefixes.
        
        Billion Exceptions:
            - septe(n):  17,  37,  47,  57,  67,  77, 107, 207, 307, 407, 507, 607, 707
            -  nove(n):  19,  39,  49,  59,  69,  79, 109, 209, 309, 409, 509, 609, 709
        """
        for zillion in (17, 37, 47, 57, 67, 77, 107, 207, 307, 407, 507, 607, 707,
                        19, 39, 49, 59, 69, 79, 109, 209, 309, 409, 509, 609, 709):
            with self.subTest(msg='POS', zillion=zillion):
                hund, tens, unit = (int(digit) for digit in str(zillion).zfill(3))
                expected = str(self.unit[unit] + 'n' + self.tens[tens] + self.hund[hund]).rstrip('ai')
                self.assertMultiLineEqual(expected, self.prefixes[zillion])
                
    def test_s_exceptions(self):
        """
        Test when 's' is appended to the 'tre' or 'se' prefixes.
        
        Billion Exceptions:
            - tre(s):  23,  33,  43,  53,  83, 103, 303, 403, 503, 803
            -  se(s):  26,  36,  46,  56, 306, 406, 506
        """
        for zillion in (23, 33, 43, 53, 83, 103, 303, 403, 503, 803,
                        26, 36, 46, 56, 306, 406, 506):
            with self.subTest(msg='POS', zillion=zillion):
                hund, tens, unit = (int(digit) for digit in str(zillion).zfill(3))
                expected = str(self.unit[unit] + 's' + self.tens[tens] + self.hund[hund]).rstrip('ai')
                self.assertMultiLineEqual(expected, self.prefixes[zillion])
                
    def test_x_exceptions(self):
        """
        Test when 'x' is added to the 'se' prefix.
        
        Billion Exceptions:
            - se(x):  86, 106, 806
        """
        for zillion in (86, 106, 806):
            with self.subTest(msg='POS', zillion=zillion):
                hund, tens, unit = (int(digit) for digit in str(zillion).zfill(3))
                expected = str(self.unit[unit] + 'x' + self.tens[tens] + self.hund[hund]).rstrip('ai')
                self.assertMultiLineEqual(expected, self.prefixes[zillion])
