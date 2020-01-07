"""
Unit tests for conwech.regexlib module.
"""

from unittest import TestCase
from conwech import regexlib


class NumericStringTests(TestCase):
    """
    Unit tests for the NUMERIC_STRING regular expresion.
    """
    
    def setUp(self):
        self.valid_flags = 'e', 'E'
        self.valid_signs = '', '-', '+'
        self.valid_digits = '0123456789'
        self.pattern = regexlib.NUMERIC_STRING
        self.expected = dict.fromkeys(self.pattern.groupindex.keys())
        # assert names of capture groups because most tests will likely rely on them
        self.assertTupleEqual(('bsign', 'bwhole', 'bfraction', 'esign', 'evalue'),
                              tuple(self.pattern.groupindex.keys()))
        
    def test_null_strings(self):
        """
        Empty or whitespace-only strings should never match.
        """
        test_strings = '', ' ', '\r', '\n', '\t',
        for test_string in test_strings:
            with self.subTest(msg='NEG', test_string=test_string):
                self.assertNotRegex(test_string, self.pattern)
                
    def test_whitespace(self):
        """
        Strings with leading or trailing whitespace can match, but
        the whitespace should be ignored.
        """
        test_strings = '   0.0e0', '0.0e0   ', '   0.0e0   '
        for test_string in test_strings:
            with self.subTest(msg='POS', test_string=test_string):
                self.assertRegex(test_string, self.pattern)
                actual = self.pattern.match(test_string).groupdict()
                self.assertDictEqual(self.expected, actual)
                
    def test_float_syntax(self):
        """
        Strings should mirror built-in float syntax.
        """
        for bs in self.valid_signs:
            for bw in '', '0', '1':
                for dec in '', '.':
                    for bf in '', '0', '1':
                        for flag in '', 'e', 'E':
                            for es in self.valid_signs:
                                for ev in '', '0', '1':
                                    test_string = (bs + bw + dec + bf + flag + es + ev)
                                    try: # pattern should match if float cast doesn't fail
                                        float(test_string)
                                        with self.subTest(msg='POS', test_string=test_string):
                                            self.assertRegex(test_string, self.pattern)
                                    except ValueError:
                                        with self.subTest(msg='NEG', test_string=test_string):
                                            self.assertNotRegex(test_string, self.pattern)
                                            
    def test_int_format(self):
        """
        Strings like integers should match.
        """
        for sign in self.valid_signs:
            # pattern should only capture signs explicitly given ('+' / '-')
            self.expected['bsign'] = sign or None
            for digit in self.valid_digits:
                test_string = sign + '0' + digit + '0'
                # pattern should capture whole starting at first non-zero digit
                self.expected['bwhole'] = test_string.lstrip('-+0') or None
                with self.subTest(msg='POS', test_string=test_string):
                    self.assertRegex(test_string, self.pattern)
                    actual = self.pattern.match(test_string).groupdict()
                    self.assertDictEqual(self.expected, actual)
                    
    def test_dec_formats(self):
        """
        Strings like decimal numbers should match.
        """
        for sign in self.valid_signs:
            # pattern should only capture signs explicitly given ('+' / '-')
            self.expected['bsign'] = sign or None
            for digit in self.valid_digits:
                test_string = sign + '0.0' + digit + '0'
                # pattern should capture fraction ending with the last non-zero digit
                self.expected['bfraction'] = test_string.split('.')[-1].rstrip('0') or None
                with self.subTest(msg='POS', test_string=test_string):
                    self.assertRegex(test_string, self.pattern)
                    actual = self.pattern.match(test_string).groupdict()
                    self.assertDictEqual(self.expected, actual)
                    
    def test_sci_formats(self):
        """
        Strings like numbers in scientific notation should match.
        """
        for flag in self.valid_flags:
            for sign in self.valid_signs:
                # pattern should only capture signs explicitly given ('+' / '-')
                self.expected['esign'] = sign or None
                for digit in self.valid_digits:
                    test_string = '0.0' + flag + sign + '0' + digit + '0'
                    # pattern should capture exponent starting at first non-zero digit after flag
                    self.expected['evalue'] = test_string.lstrip('-+0.eE0') or None
                    with self.subTest(msg='POS', test_string=test_string):
                        self.assertRegex(test_string, self.pattern)
                        actual = self.pattern.match(test_string).groupdict()
                        self.assertDictEqual(self.expected, actual)
                        
                        
class NumberTextTests(TestCase):
    """
    Unit tests for the NUMBER_TEXT regular expresion.
    """
    
    def setUp(self):
        self.pattern = regexlib.NUMBER_TEXT
        self.expected = dict.fromkeys(self.pattern.groupindex.keys())
        # assert names of capture groups because most tests will likely rely on them
        self.assertTupleEqual(('whole', 'numerator', 'denominator'),
                              tuple(self.pattern.groupindex.keys()))
        
    def test_null_strings(self):
        """
        Empty or whitespace-only strings should never match.
        """
        test_strings = '', ' ', '\r', '\n', '\t',
        for test_string in test_strings:
            with self.subTest(msg='NEG', test_string=test_string):
                self.assertNotRegex(test_string, self.pattern)
                
    def test_(self):
        """
        TODO: finish unit testing...
        """
        pass
    
    
class PeriodTextTests(TestCase):
    """
    Unit tests for the PERIOD_TEXT regular expresion.
    """
    
    def setUp(self):
        self.pattern = regexlib.PERIOD_TEXT
        self.expected = dict.fromkeys(self.pattern.groupindex.keys())
        # assert names of capture groups because most tests will likely rely on them
        self.assertTupleEqual(('value', 'name'), tuple(self.pattern.groupindex.keys()))
        
    def test_null_strings(self):
        """
        Empty or whitespace-only strings should never match.
        """
        test_strings = '', ' ', '\r', '\n', '\t',
        for test_string in test_strings:
            with self.subTest(msg='NEG', test_string=test_string):
                self.assertNotRegex(test_string, self.pattern)
                
    def test_(self):
        """
        TODO: finish unit testing...
        """
        pass
