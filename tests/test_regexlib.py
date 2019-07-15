"""
Unit tests for spellnum.regexlib module.
"""

from unittest import TestCase
from spellnum import regexlib


class NumberLikeString(TestCase):
    """"""
    
    def test_empty_string(self):
        match = regexlib.NUMBER_LIKE_STRING.match('')
        self.assertIsNone(match)
        
        
class NumberTextFormat(TestCase):
    """"""
    
    def test_empty_string(self):
        match = regexlib.NUMBER_TEXT_FORMAT.match('')
        self.assertIsNotNone(match)
        
        
class PeriodTextFormat(TestCase):
    """"""
    
    def test_empty_string(self):
        match = regexlib.PERIOD_TEXT_FORMAT.match('')
        self.assertIsNone(match)
