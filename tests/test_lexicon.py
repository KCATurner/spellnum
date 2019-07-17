"""
Unit tests for spellnum.lexicon.
"""

from unittest import TestCase
from spellnum import lexicon


class LexiconStructure(TestCase):
    """
    Verifies that the lexicon tuples were built and aligned properly.
    """
    
    def test_1_digit_integers(self):
        expected = lexicon._UNIQUE_NUMERIC_WORDS[:9]
        actual = lexicon.NATURAL_NUMBERS_LT_1000[:9]
        self.assertTupleEqual(expected, actual)
        
    def test_2_digit_integers(self):
        expected = lexicon.NATURAL_NUMBERS_LT_100[10:99]
        actual = lexicon.NATURAL_NUMBERS_LT_1000[10:99]
        self.assertTupleEqual(expected, actual)
        
    def test_3_digit_integers(self):
        for index in range(100, 1000):
            hundred = lexicon._UNIQUE_NUMERIC_WORDS[index // 100]
            tens = lexicon.NATURAL_NUMBERS_LT_100[index % 100]
            expected = '{} hundred {}'.format(hundred, tens).strip()
            actual = lexicon.NATURAL_NUMBERS_LT_1000[index]
            self.assertMultiLineEqual(expected, actual)
