"""
Unit tests for spellnum.lexicon.
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
