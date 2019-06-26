"""
Unit tests for spellnum.functions.num2txt function.
"""

import unittest
import spellnum


class InputValidity(unittest.TestCase):
    """
    Tests valid and invalid input type and boundary values for spell.
    """
    
    def test_input_EQ_minimum(self):
        # smallest value would actually be -9.99...(repeating forever)...e3002
        expected = 'negative nine hundred ninety-nine novenonagintanongentillion'
        actual = spellnum.__functions.num2txt('-9.99e3002')
        self.assertMultiLineEqual(expected, actual)
    
    def test_input_EQ_maximum(self):
        # largest value would actually be 9.99...(repeating forever)...e3002
        expected = 'nine hundred ninety-nine novenonagintanongentillion'
        actual = spellnum.__functions.num2txt('9.99e3002')
        self.assertMultiLineEqual(expected, actual)
    
    def test_precision_EQ_maximum(self):
        expected = 'one one hundred novenonagintanongentillionth'
        actual = spellnum.__functions.num2txt('1e-3002')
        self.assertMultiLineEqual(expected, actual)
    
    def test_input_LT_minimum(self):
        self.assertRaises(ValueError, spellnum.__functions.num2txt, '-1e3003')
    
    def test_input_GT_Maximum(self):
        self.assertRaises(ValueError, spellnum.__functions.num2txt, '1e3003')
    
    def test_precision_GT_maximum(self):
        self.assertRaises(ValueError, spellnum.__functions.num2txt, '0.1e-3002')
    
    def test_input_none(self):
        self.assertRaises(ValueError, spellnum.__functions.num2txt, None)
    
    def test_input_set(self):
        self.assertRaises(ValueError, spellnum.__functions.num2txt, {123, })
    
    def test_input_list(self):
        self.assertRaises(ValueError, spellnum.__functions.num2txt, [123, ])
    
    def test_input_tuple(self):
        self.assertRaises(ValueError, spellnum.__functions.num2txt, (123,))
    
    def test_string_dXXX(self):
        expected = 'one hundred twenty-three one thousandths'
        self.assertMultiLineEqual(expected, spellnum.__functions.num2txt('.123'))
        self.assertMultiLineEqual('negative ' + expected, spellnum.__functions.num2txt('-.123'))
    
    def test_string_ndXXX(self):
        expected = 'one hundred twenty-three one thousandths'
        self.assertMultiLineEqual(expected, spellnum.__functions.num2txt('.123'))
        self.assertMultiLineEqual('negative ' + expected, spellnum.__functions.num2txt('-.123'))
    
    def test_ValidFormat_dXeX(self):
        expected = 'one hundred million'
        self.assertMultiLineEqual(expected, spellnum.__functions.num2txt(.1e9))
        self.assertMultiLineEqual(expected, spellnum.__functions.num2txt('.1e9'))
        self.assertMultiLineEqual('negative ' + expected, spellnum.__functions.num2txt(-.1e9))
        self.assertMultiLineEqual('negative ' + expected, spellnum.__functions.num2txt('-.1e9'))
    
    def test_ValidFormat_XdXEX(self):
        expected = 'one billion two hundred million'
        self.assertMultiLineEqual(expected, spellnum.__functions.num2txt(1.2E9))
        self.assertMultiLineEqual(expected, spellnum.__functions.num2txt('1.2E9'))
        self.assertMultiLineEqual('negative ' + expected, spellnum.__functions.num2txt(-1.2E9))
        self.assertMultiLineEqual('negative ' + expected, spellnum.__functions.num2txt('-1.2E9'))
    
    def test_ValidFormat_XdXeX(self):
        expected = 'one billion two hundred million'
        self.assertMultiLineEqual(expected, spellnum.__functions.num2txt(1.2e9))
        self.assertMultiLineEqual(expected, spellnum.__functions.num2txt('1.2e9'))
        self.assertMultiLineEqual('negative ' + expected, spellnum.__functions.num2txt(-1.2e9))
        self.assertMultiLineEqual('negative ' + expected, spellnum.__functions.num2txt('-1.2e9'))
    
    def test_ValidFormat_XdXenX(self):
        expected = 'twelve ten billionths'
        self.assertMultiLineEqual(expected, spellnum.__functions.num2txt(1.2e-9))
        self.assertMultiLineEqual(expected, spellnum.__functions.num2txt('1.2e-9'))
        self.assertMultiLineEqual('negative ' + expected, spellnum.__functions.num2txt(-1.2e-9))
        self.assertMultiLineEqual('negative ' + expected, spellnum.__functions.num2txt('-1.2e-9'))
    
    def test_ValidFormat_0dXeX(self):
        expected = 'one hundred million'
        self.assertMultiLineEqual(expected, spellnum.__functions.num2txt(0.1e9))
        self.assertMultiLineEqual(expected, spellnum.__functions.num2txt('0.1e9'))
        self.assertMultiLineEqual('negative ' + expected, spellnum.__functions.num2txt(-0.1e9))
        self.assertMultiLineEqual('negative ' + expected, spellnum.__functions.num2txt('-0.1e9'))
    
    def test_ValidFormat_Xd0eX(self):
        expected = 'one billion'
        self.assertMultiLineEqual(expected, spellnum.__functions.num2txt(1.0e9))
        self.assertMultiLineEqual(expected, spellnum.__functions.num2txt('1.0e9'))
        self.assertMultiLineEqual('negative ' + expected, spellnum.__functions.num2txt(-1.0e9))
        self.assertMultiLineEqual('negative ' + expected, spellnum.__functions.num2txt('-1.0e9'))
    
    def test_ValidFormat_XXXdXXXeXXX(self):
        expected = 'one hundred twenty-three quadragintillion four hundred fifty-six noventrigintillion'
        self.assertMultiLineEqual(expected, spellnum.__functions.num2txt(123.456e123))
        self.assertMultiLineEqual(expected, spellnum.__functions.num2txt('123.456e123'))
        self.assertMultiLineEqual('negative ' + expected, spellnum.__functions.num2txt(-123.456e123))
        self.assertMultiLineEqual('negative ' + expected, spellnum.__functions.num2txt('-123.456e123'))
    
    def test_ValidFormat_0XXdXX0e0XX(self):
        expected = 'twelve trillion three hundred forty billion'
        self.assertMultiLineEqual(expected, spellnum.__functions.num2txt(012.340e012))
        self.assertMultiLineEqual(expected, spellnum.__functions.num2txt('012.340e012'))
        self.assertMultiLineEqual('negative ' + expected, spellnum.__functions.num2txt(-012.340e012))
        self.assertMultiLineEqual('negative ' + expected, spellnum.__functions.num2txt('-012.340e012'))
    
    def test_PrecisionRetention(self):
        expected = ('one quadragintillion two hundred thirty-four noventrigintillion five hundred sixty-seven '
                    'octotrigintillion eight hundred ninety-eight septentrigintillion seven hundred sixty-five '
                    'sestrigintillion four hundred thirty-two quinquatrigintillion one hundred quattuortrigintillion')
        self.assertMultiLineEqual(expected, spellnum.__functions.num2txt('1.2345678987654321e123'))
        self.assertMultiLineEqual('negative ' + expected, spellnum.__functions.num2txt('-1.2345678987654321e123'))
    
    def test_InvalidInputs(self):
        self.assertRaises(ValueError, spellnum.__functions.num2txt, '')
        self.assertRaises(ValueError, spellnum.__functions.num2txt, '.')
        self.assertRaises(ValueError, spellnum.__functions.num2txt, 'e')
        self.assertRaises(ValueError, spellnum.__functions.num2txt, '-')
        self.assertRaises(ValueError, spellnum.__functions.num2txt, '+')
        self.assertRaises(ValueError, spellnum.__functions.num2txt, '.e')
        self.assertRaises(ValueError, spellnum.__functions.num2txt, '.0e')
        self.assertRaises(ValueError, spellnum.__functions.num2txt, '.0e-')
        self.assertRaises(ValueError, spellnum.__functions.num2txt, '0.0e')
        self.assertRaises(ValueError, spellnum.__functions.num2txt, '0.0e-')
        self.assertRaises(ValueError, spellnum.__functions.num2txt, '0.e-0')
        self.assertRaises(ValueError, spellnum.__functions.num2txt, '--123')
        self.assertRaises(ValueError, spellnum.__functions.num2txt, '++123')
        self.assertRaises(ValueError, spellnum.__functions.num2txt, '-+123')
        self.assertRaises(ValueError, spellnum.__functions.num2txt, '+-123')
        self.assertRaises(ValueError, spellnum.__functions.num2txt, '1.2.3')


class SpellingExceptions(unittest.TestCase):
    """
    Tests 'zero' spelling use cases for spell.
    NOTE: Due to the number of valid input formats, these tests are not exhaustive.
    """
    
    def test_singular_fraction(self):
        expected = 'one tenth'
        actual = spellnum.__functions.num2txt(0.1)
        self.assertMultiLineEqual(expected, actual)
    
    def test_float_0(self):
        expected = 'zero'
        actual = spellnum.__functions.num2txt(0)
        self.assertMultiLineEqual(expected, actual)
    
    def test_float_0d0(self):
        expected = 'zero'
        actual = spellnum.__functions.num2txt(0.0)
        self.assertMultiLineEqual(expected, actual)
    
    def test_float_0e0(self):
        expected = 'zero'
        actual = spellnum.__functions.num2txt(0e0)
        self.assertMultiLineEqual(expected, actual)
    
    def test_float_d0e0(self):
        expected = 'zero'
        actual = spellnum.__functions.num2txt(.0e0)
        self.assertMultiLineEqual(expected, actual)
    
    def test_float_0d0e0(self):
        expected = 'zero'
        actual = spellnum.__functions.num2txt(0.0e0)
        self.assertMultiLineEqual(expected, actual)
    
    def test_float_n0(self):
        expected = 'zero'
        actual = spellnum.__functions.num2txt(-0)
        self.assertMultiLineEqual(expected, actual)
    
    def test_float_n0d0(self):
        expected = 'zero'
        actual = spellnum.__functions.num2txt(-0.0)
        self.assertMultiLineEqual(expected, actual)
    
    def test_float_n0en0(self):
        expected = 'zero'
        actual = spellnum.__functions.num2txt(-0e-0)
        self.assertMultiLineEqual(expected, actual)
    
    def test_float_n0d0en0(self):
        expected = 'zero'
        actual = spellnum.__functions.num2txt(-0.0e-0)
        self.assertMultiLineEqual(expected, actual)
    
    def test_string_0(self):
        expected = 'zero'
        actual = spellnum.__functions.num2txt('0')
        self.assertMultiLineEqual(expected, actual)
    
    def test_string_0d0(self):
        expected = 'zero'
        actual = spellnum.__functions.num2txt('0.0')
        self.assertMultiLineEqual(expected, actual)
    
    def test_string_d0e0(self):
        expected = 'zero'
        actual = spellnum.__functions.num2txt('.0e0')
        self.assertMultiLineEqual(expected, actual)
    
    def test_string_0e0(self):
        expected = 'zero'
        actual = spellnum.__functions.num2txt('0e0')
        self.assertMultiLineEqual(expected, actual)
    
    def test_string_0d0e0(self):
        expected = 'zero'
        actual = spellnum.__functions.num2txt('0.0e0')
        self.assertMultiLineEqual(expected, actual)
    
    def test_string_n0(self):
        expected = 'zero'
        actual = spellnum.__functions.num2txt('-0')
        self.assertMultiLineEqual(expected, actual)
    
    def test_string_n0d0(self):
        expected = 'zero'
        actual = spellnum.__functions.num2txt('-0.0')
        self.assertMultiLineEqual(expected, actual)
    
    def test_string_n0en0(self):
        expected = 'zero'
        actual = spellnum.__functions.num2txt('-0e-0')
        self.assertMultiLineEqual(expected, actual)
    
    def test_string_n0d0en0(self):
        expected = 'zero'
        actual = spellnum.__functions.num2txt('-0.0e-0')
        self.assertMultiLineEqual(expected, actual)


class SpellingScientific(unittest.TestCase):
    """
    Tests spelling numbers in scientific notation.
    """
    
    def test_float_XXdXXe3(self):
        expected = spellnum.__functions.num2txt(12340)
        actual = spellnum.__functions.num2txt(12.34e3)
        self.assertMultiLineEqual(expected, actual)
    
    def test_float_XXdXXe2(self):
        expected = spellnum.__functions.num2txt(1234)
        actual = spellnum.__functions.num2txt(12.34e2)
        self.assertMultiLineEqual(expected, actual)
    
    def test_float_XXdXXe1(self):
        expected = spellnum.__functions.num2txt(123.4)
        actual = spellnum.__functions.num2txt(12.34e1)
        self.assertMultiLineEqual(expected, actual)
    
    def test_float_XXdXXe0(self):
        expected = spellnum.__functions.num2txt(12.34)
        actual = spellnum.__functions.num2txt(12.34e0)
        self.assertMultiLineEqual(expected, actual)
    
    def test_float_XXdXXen0(self):
        expected = spellnum.__functions.num2txt(12.34)
        actual = spellnum.__functions.num2txt(12.34e-0)
        self.assertMultiLineEqual(expected, actual)
    
    def test_float_XXdXXen1(self):
        expected = spellnum.__functions.num2txt(1.234)
        actual = spellnum.__functions.num2txt(12.34e-1)
        self.assertMultiLineEqual(expected, actual)
    
    def test_float_XXdXXen2(self):
        expected = spellnum.__functions.num2txt(.1234)
        actual = spellnum.__functions.num2txt(12.34e-2)
        self.assertMultiLineEqual(expected, actual)
    
    def test_float_XXdXXen3(self):
        expected = spellnum.__functions.num2txt(.01234)
        actual = spellnum.__functions.num2txt(12.34e-3)
        self.assertMultiLineEqual(expected, actual)
    
    def test_string_XXdXXe3(self):
        expected = spellnum.__functions.num2txt(12340)
        actual = spellnum.__functions.num2txt('12.34e3')
        self.assertMultiLineEqual(expected, actual)
    
    def test_string_XXdXXe2(self):
        expected = spellnum.__functions.num2txt(1234)
        actual = spellnum.__functions.num2txt('12.34e2')
        self.assertMultiLineEqual(expected, actual)
    
    def test_string_XXdXXe1(self):
        expected = spellnum.__functions.num2txt(123.4)
        actual = spellnum.__functions.num2txt('12.34e1')
        self.assertMultiLineEqual(expected, actual)
    
    def test_string_XXdXXe0(self):
        expected = spellnum.__functions.num2txt(12.34)
        actual = spellnum.__functions.num2txt('12.34e0')
        self.assertMultiLineEqual(expected, actual)
    
    def test_string_XXdXXen0(self):
        expected = spellnum.__functions.num2txt(12.34)
        actual = spellnum.__functions.num2txt('12.34e-0')
        self.assertMultiLineEqual(expected, actual)
    
    def test_string_XXdXXen1(self):
        expected = spellnum.__functions.num2txt(1.234)
        actual = spellnum.__functions.num2txt('12.34e-1')
        self.assertMultiLineEqual(expected, actual)
    
    def test_string_XXdXXen2(self):
        expected = spellnum.__functions.num2txt(.1234)
        actual = spellnum.__functions.num2txt('12.34e-2')
        self.assertMultiLineEqual(expected, actual)
    
    def test_string_XXdXXen3(self):
        expected = spellnum.__functions.num2txt(.01234)
        actual = spellnum.__functions.num2txt('12.34e-3')
        self.assertMultiLineEqual(expected, actual)
    
    def test_float_0d1eXX(self):
        expected = 'one vigintillion'
        actual = spellnum.__functions.num2txt(0.1e64)
        self.assertMultiLineEqual(expected, actual)
    
    def test_float_1d0eXX(self):
        expected = 'one vigintillion'
        actual = spellnum.__functions.num2txt(1.0e63)
        self.assertMultiLineEqual(expected, actual)
    
    def test_float_0d1enXX(self):
        expected = 'one one vigintillionth'
        actual = spellnum.__functions.num2txt(0.1e-62)
        self.assertMultiLineEqual(expected, actual)
    
    def test_float_1d0enXX(self):
        expected = 'one one vigintillionth'
        actual = spellnum.__functions.num2txt(1.0e-63)
        self.assertMultiLineEqual(expected, actual)
    
    def test_string_0d1eXX(self):
        expected = 'one vigintillion'
        actual = spellnum.__functions.num2txt('0.1e64')
        self.assertMultiLineEqual(expected, actual)
    
    def test_string_1d0eXX(self):
        expected = 'one vigintillion'
        actual = spellnum.__functions.num2txt('1.0e63')
        self.assertMultiLineEqual(expected, actual)
    
    def test_string_0d1enXX(self):
        expected = 'one one vigintillionth'
        actual = spellnum.__functions.num2txt('0.1e-62')
        self.assertMultiLineEqual(expected, actual)
    
    def test_string_1d0enXX(self):
        expected = 'one one vigintillionth'
        actual = spellnum.__functions.num2txt('1.0e-63')
        self.assertMultiLineEqual(expected, actual)


class SpellingDecimal(unittest.TestCase):
    """
    Tests spelling numbers with fractions in decimal format.
    """
    
    def test_float_X00XdX(self):
        expected = 'one thousand two and three tenths'
        actual = spellnum.__functions.num2txt(1002.3)
        self.assertMultiLineEqual(expected, actual)
    
    def test_float_X0XdXX(self):
        expected = 'one hundred two and thirty-four one hundredths'
        actual = spellnum.__functions.num2txt(102.34)
        self.assertMultiLineEqual(expected, actual)
    
    def test_float_XXdX0X(self):
        expected = 'twelve and three hundred four one thousandths'
        actual = spellnum.__functions.num2txt(12.304)
        self.assertMultiLineEqual(expected, actual)
    
    def test_float_XdX00X(self):
        expected = 'two and three thousand four ten thousandths'
        actual = spellnum.__functions.num2txt(2.3004)
        self.assertMultiLineEqual(expected, actual)
    
    def test_float_dX000X(self):
        expected = 'thirty thousand four one hundred thousandths'
        actual = spellnum.__functions.num2txt(.30004)
        self.assertMultiLineEqual(expected, actual)
    
    def test_string_X00XdX(self):
        expected = 'one thousand two and three tenths'
        actual = spellnum.__functions.num2txt('1002.3')
        self.assertMultiLineEqual(expected, actual)
    
    def test_string_X0XdXX(self):
        expected = 'one hundred two and thirty-four one hundredths'
        actual = spellnum.__functions.num2txt('102.34')
        self.assertMultiLineEqual(expected, actual)
    
    def test_string_XXdX0X(self):
        expected = 'twelve and three hundred four one thousandths'
        actual = spellnum.__functions.num2txt('12.304')
        self.assertMultiLineEqual(expected, actual)
    
    def test_string_XdX00X(self):
        expected = 'two and three thousand four ten thousandths'
        actual = spellnum.__functions.num2txt('2.3004')
        self.assertMultiLineEqual(expected, actual)
    
    def test_string_dX000X(self):
        expected = 'thirty thousand four one hundred thousandths'
        actual = spellnum.__functions.num2txt('.30004')
        self.assertMultiLineEqual(expected, actual)
