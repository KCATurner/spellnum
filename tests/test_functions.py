"""
Unit tests for spellnum module.
"""

import sys
import random
from unittest import TestCase

from spellnum.functions import *
from spellnum.exceptions import *
from spellnum.lexicon import PERIOD_PREFIXES_LT_1000


class NamePeriodTests(TestCase):
    """
    Unit tests for ``nameperiod`` function.
    """
    
    def test_invalid_input(self):
        """
        Function should raise ``TypeError`` when input is not an int.
        """
        for invalid_type in (None, 1.23, '1.23', set(), list(), tuple()):
            with self.subTest(msg='NEG', invalid_type=invalid_type):
                self.assertRaises(TypeError, nameperiod, invalid_type)
                
    def test_special_cases(self):
        """
        0 should return 'thousand' and -1 should return an empty string.
        """
        special_cases = (-1, ''), (0, 'thousand')
        for base_illion, period_name in special_cases:
            with self.subTest(msg='NEG', base_illion=base_illion):
                self.assertEqual(period_name, nameperiod(base_illion))
                
    def test_good_monkey(self):
        """
        Function should (theoretically) handle any whole number >= -1.
        """
        samples = random.sample(range(1, sys.maxsize), 100)
        for base_illion in (s ** random.randrange(1, 100) for s in samples):
            prefixes = (PERIOD_PREFIXES_LT_1000[int(p)] for p in '{:,}'.format(base_illion).split(','))
            period_name = 'illi'.join(prefixes) + 'illion'
            with self.subTest(msg='POS', base_illion=base_illion, period_name=period_name):
                self.assertEqual(period_name, nameperiod(base_illion))
                
    def test_performance(self):
        """
        TODO: Write a reasonable performance test.
        """
        pass
    
    
class ReadPeriodTests(TestCase):
    """
    Unit tests for ``readperiod`` function.
    """
    
    def test_invalid_input(self):
        """
        Function should raise ``ValueError`` when input is unrecognized.
        """
        for invalid_name in (' ', 'not-a-illion'):
            with self.subTest(msg='NEG', invalid_name=invalid_name):
                self.assertRaises(InvalidTextForPeriodName, readperiod, invalid_name)
                
    def test_special_cases(self):
        """
        Empty strings should return -1 and 'thousand' should return 0.
        """
        special_cases = (-1, ''), (0, 'thousand')
        for base_illion, period_name in special_cases:
            with self.subTest(msg='NEG', period_name=period_name):
                self.assertEqual(base_illion, readperiod(period_name))
                
    def test_good_monkey(self):
        """
        
        """
        samples = random.sample(range(1, sys.maxsize), 100)
        for base_illion in (s ** random.randrange(1, 100) for s in samples):
            prefixes = (PERIOD_PREFIXES_LT_1000[int(p)] for p in '{:,}'.format(base_illion).split(','))
            period_name = 'illi'.join(prefixes) + 'illion'
            with self.subTest(msg='POS', base_illion=base_illion, period_name=period_name):
                self.assertEqual(base_illion, readperiod(period_name))
                
    def test_performance(self):
        """
        TODO: Write a reasonable performance test.
        """
        pass
    
    
class Number2TextTests(TestCase):
    """
    Unit Tests for ``number2text`` function.
    
    TODO: refactor existing unit tests...
    """
    
    def test_invalid_input_type(self):
        """
        TODO: finish docstring...
        """
        for invalid_type in (None, {123, }, [123, ], (123,)):
            with self.subTest(invalid_type=invalid_type):
                self.assertRaises(InvalidNumberLikeString, number2text, invalid_type)
                
    def test_zero_input(self):
        """
        TODO: finish docstring...
        """
        for number in 0, 0.0, 0e0, '0', '-0':
            with self.subTest(msg='POS', number=number):
                self.assertMultiLineEqual('zero', number2text(number))
                
    def test_units_period(self):
        """
        TODO: finish docstring...
        """
        for number in range(1, 1000):
            with self.subTest(msg='POS', number=number):
                expected = spellnum.lexicon.NATURAL_NUMBERS_LT_1000[number]
                self.assertMultiLineEqual(expected, number2text(number))
                
    def test_string_dXXX(self):
        expected = 'one hundred twenty-three one thousandths'
        self.assertMultiLineEqual(expected, number2text('.123'))
        self.assertMultiLineEqual('negative ' + expected, number2text('-.123'))

    def test_string_ndXXX(self):
        expected = 'one hundred twenty-three one thousandths'
        self.assertMultiLineEqual(expected, number2text('.123'))
        self.assertMultiLineEqual('negative ' + expected, number2text('-.123'))

    def test_ValidFormat_dXeX(self):
        expected = 'one hundred million'
        self.assertMultiLineEqual(expected, number2text(.1e9))
        self.assertMultiLineEqual(expected, number2text('.1e9'))
        self.assertMultiLineEqual('negative ' + expected, number2text(-.1e9))
        self.assertMultiLineEqual('negative ' + expected, number2text('-.1e9'))

    def test_ValidFormat_XdXEX(self):
        expected = 'one billion two hundred million'
        self.assertMultiLineEqual(expected, number2text(1.2E9))
        self.assertMultiLineEqual(expected, number2text('1.2E9'))
        self.assertMultiLineEqual('negative ' + expected, number2text(-1.2E9))
        self.assertMultiLineEqual('negative ' + expected, number2text('-1.2E9'))

    def test_ValidFormat_XdXeX(self):
        expected = 'one billion two hundred million'
        self.assertMultiLineEqual(expected, number2text(1.2e9))
        self.assertMultiLineEqual(expected, number2text('1.2e9'))
        self.assertMultiLineEqual('negative ' + expected, number2text(-1.2e9))
        self.assertMultiLineEqual('negative ' + expected, number2text('-1.2e9'))

    def test_ValidFormat_XdXenX(self):
        expected = 'twelve ten billionths'
        self.assertMultiLineEqual(expected, number2text(1.2e-9))
        self.assertMultiLineEqual(expected, number2text('1.2e-9'))
        self.assertMultiLineEqual('negative ' + expected, number2text(-1.2e-9))
        self.assertMultiLineEqual('negative ' + expected, number2text('-1.2e-9'))

    def test_ValidFormat_0dXeX(self):
        expected = 'one hundred million'
        self.assertMultiLineEqual(expected, number2text(0.1e9))
        self.assertMultiLineEqual(expected, number2text('0.1e9'))
        self.assertMultiLineEqual('negative ' + expected, number2text(-0.1e9))
        self.assertMultiLineEqual('negative ' + expected, number2text('-0.1e9'))

    def test_ValidFormat_Xd0eX(self):
        expected = 'one billion'
        self.assertMultiLineEqual(expected, number2text(1.0e9))
        self.assertMultiLineEqual(expected, number2text('1.0e9'))
        self.assertMultiLineEqual('negative ' + expected, number2text(-1.0e9))
        self.assertMultiLineEqual('negative ' + expected, number2text('-1.0e9'))

    def test_ValidFormat_XXXdXXXeXXX(self):
        expected = 'one hundred twenty-three quadragintillion four hundred fifty-six noventrigintillion'
        self.assertMultiLineEqual(expected, number2text(123.456e123))
        self.assertMultiLineEqual(expected, number2text('123.456e123'))
        self.assertMultiLineEqual('negative ' + expected, number2text(-123.456e123))
        self.assertMultiLineEqual('negative ' + expected, number2text('-123.456e123'))

    def test_ValidFormat_0XXdXX0e0XX(self):
        expected = 'twelve trillion three hundred forty billion'
        self.assertMultiLineEqual(expected, number2text(012.340e012))
        self.assertMultiLineEqual(expected, number2text('012.340e012'))
        self.assertMultiLineEqual('negative ' + expected, number2text(-012.340e012))
        self.assertMultiLineEqual('negative ' + expected, number2text('-012.340e012'))

    def test_PrecisionRetention(self):
        expected = ('one quadragintillion two hundred thirty-four noventrigintillion five hundred sixty-seven '
                    'octotrigintillion eight hundred ninety-eight septentrigintillion seven hundred sixty-five '
                    'sestrigintillion four hundred thirty-two quinquatrigintillion one hundred quattuortrigintillion')
        self.assertMultiLineEqual(expected, number2text('1.2345678987654321e123'))
        self.assertMultiLineEqual('negative ' + expected, number2text('-1.2345678987654321e123'))

    def test_float_XXdXXe3(self):
        expected = number2text(12340)
        actual = number2text(12.34e3)
        self.assertMultiLineEqual(expected, actual)

    def test_float_XXdXXe2(self):
        expected = number2text(1234)
        actual = number2text(12.34e2)
        self.assertMultiLineEqual(expected, actual)

    def test_float_XXdXXe1(self):
        expected = number2text(123.4)
        actual = number2text(12.34e1)
        self.assertMultiLineEqual(expected, actual)

    def test_float_XXdXXe0(self):
        expected = number2text(12.34)
        actual = number2text(12.34e0)
        self.assertMultiLineEqual(expected, actual)

    def test_float_XXdXXen0(self):
        expected = number2text(12.34)
        actual = number2text(12.34e-0)
        self.assertMultiLineEqual(expected, actual)

    def test_float_XXdXXen1(self):
        expected = number2text(1.234)
        actual = number2text(12.34e-1)
        self.assertMultiLineEqual(expected, actual)

    def test_float_XXdXXen2(self):
        expected = number2text(.1234)
        actual = number2text(12.34e-2)
        self.assertMultiLineEqual(expected, actual)

    def test_float_XXdXXen3(self):
        expected = number2text(.01234)
        actual = number2text(12.34e-3)
        self.assertMultiLineEqual(expected, actual)

    def test_string_XXdXXe3(self):
        expected = number2text(12340)
        actual = number2text('12.34e3')
        self.assertMultiLineEqual(expected, actual)

    def test_string_XXdXXe2(self):
        expected = number2text(1234)
        actual = number2text('12.34e2')
        self.assertMultiLineEqual(expected, actual)

    def test_string_XXdXXe1(self):
        expected = number2text(123.4)
        actual = number2text('12.34e1')
        self.assertMultiLineEqual(expected, actual)

    def test_string_XXdXXe0(self):
        expected = number2text(12.34)
        actual = number2text('12.34e0')
        self.assertMultiLineEqual(expected, actual)

    def test_string_XXdXXen0(self):
        expected = number2text(12.34)
        actual = number2text('12.34e-0')
        self.assertMultiLineEqual(expected, actual)

    def test_string_XXdXXen1(self):
        expected = number2text(1.234)
        actual = number2text('12.34e-1')
        self.assertMultiLineEqual(expected, actual)

    def test_string_XXdXXen2(self):
        expected = number2text(.1234)
        actual = number2text('12.34e-2')
        self.assertMultiLineEqual(expected, actual)

    def test_string_XXdXXen3(self):
        expected = number2text(.01234)
        actual = number2text('12.34e-3')
        self.assertMultiLineEqual(expected, actual)

    def test_float_0d1eXX(self):
        expected = 'one vigintillion'
        actual = number2text(0.1e64)
        self.assertMultiLineEqual(expected, actual)

    def test_float_1d0eXX(self):
        expected = 'one vigintillion'
        actual = number2text(1.0e63)
        self.assertMultiLineEqual(expected, actual)

    def test_float_0d1enXX(self):
        expected = 'one one vigintillionth'
        actual = number2text(0.1e-62)
        self.assertMultiLineEqual(expected, actual)

    def test_float_1d0enXX(self):
        expected = 'one one vigintillionth'
        actual = number2text(1.0e-63)
        self.assertMultiLineEqual(expected, actual)

    def test_string_0d1eXX(self):
        expected = 'one vigintillion'
        actual = number2text('0.1e64')
        self.assertMultiLineEqual(expected, actual)

    def test_string_1d0eXX(self):
        expected = 'one vigintillion'
        actual = number2text('1.0e63')
        self.assertMultiLineEqual(expected, actual)

    def test_string_0d1enXX(self):
        expected = 'one one vigintillionth'
        actual = number2text('0.1e-62')
        self.assertMultiLineEqual(expected, actual)

    def test_string_1d0enXX(self):
        expected = 'one one vigintillionth'
        actual = number2text('1.0e-63')
        self.assertMultiLineEqual(expected, actual)

    def test_float_X00XdX(self):
        expected = 'one thousand two and three tenths'
        actual = number2text(1002.3)
        self.assertMultiLineEqual(expected, actual)

    def test_float_X0XdXX(self):
        expected = 'one hundred two and thirty-four one hundredths'
        actual = number2text(102.34)
        self.assertMultiLineEqual(expected, actual)

    def test_float_XXdX0X(self):
        expected = 'twelve and three hundred four one thousandths'
        actual = number2text(12.304)
        self.assertMultiLineEqual(expected, actual)

    def test_float_XdX00X(self):
        expected = 'two and three thousand four ten thousandths'
        actual = number2text(2.3004)
        self.assertMultiLineEqual(expected, actual)

    def test_float_dX000X(self):
        expected = 'thirty thousand four one hundred thousandths'
        actual = number2text(.30004)
        self.assertMultiLineEqual(expected, actual)

    def test_string_X00XdX(self):
        expected = 'one thousand two and three tenths'
        actual = number2text('1002.3')
        self.assertMultiLineEqual(expected, actual)

    def test_string_X0XdXX(self):
        expected = 'one hundred two and thirty-four one hundredths'
        actual = number2text('102.34')
        self.assertMultiLineEqual(expected, actual)

    def test_string_XXdX0X(self):
        expected = 'twelve and three hundred four one thousandths'
        actual = number2text('12.304')
        self.assertMultiLineEqual(expected, actual)

    def test_string_XdX00X(self):
        expected = 'two and three thousand four ten thousandths'
        actual = number2text('2.3004')
        self.assertMultiLineEqual(expected, actual)

    def test_string_dX000X(self):
        expected = 'thirty thousand four one hundred thousandths'
        actual = number2text('.30004')
        self.assertMultiLineEqual(expected, actual)
    
    def test_good_monkey(self):
        """
        TODO: write monkey tests.
        """
        pass
    
    def test_performance(self):
        """
        TODO: Write a reasonable performance test.
        """
        pass
    
    
class Text2NumberTests(TestCase):
    """
    Unit Tests for ``text2number`` function.
    
    TODO: finish unit testing...
    """
    
    def test_special_cases(self):
        """
        TODO: write test for special cases.
        """
        pass
    
    def test_good_monkey(self):
        """
        TODO: write monkey tests.
        """
        pass
    
    def test_performance(self):
        """
        TODO: Write a reasonable performance test.
        """
        pass
    
    
class InverseFunctions(TestCase):
    """
    Verify that function pairs behave as inverses.
    """
    
    def setUp(self):
        self.maxDiff = None
        
    def test_read_named_periods(self):
        """
        ``nameperiod`` and ``readperiod`` should be inverses.
        """
        samples = random.sample(range(1, sys.maxsize), 100)
        for base_illion in (s**random.randrange(1, 100) for s in samples):
            with self.subTest(msg='POS', base_illion=base_illion):
                self.assertEqual(base_illion, readperiod(nameperiod(base_illion)))
                
    def test_read_spelled_numbers(self):
        """
        ``number2text`` and ``test2number`` should be inverses.
        """
        samples = random.sample(range(1, sys.maxsize), 100)
        for number in (str(s**random.randrange(1, 100)) for s in samples):
            number = number[:1] + '.' + number[1:].rstrip('0') + 'e' + str(len(number[1:]))
            with self.subTest(msg='POS', number=number):
                self.assertEqual(number, text2number(number2text(number)))
