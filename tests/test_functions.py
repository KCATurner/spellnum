"""
Unit tests for the conwech.functions.
"""

import sys
import pytest
import random
import conwech.lexicon
import conwech.functions
import conwech._exceptions


class TestNamePeriod:
    """
    Unit tests for `nameperiod` function.
    """

    @pytest.mark.parametrize(
        argnames='invalid',
        argvalues=(None, 1.23, '1.23', {123, }, [123, ], (123, )))
    def test_invalid_input_type(self, invalid):
        """
        Function should raise `TypeError` when input is not an int.
        """
        with pytest.raises(TypeError):
            conwech.functions.nameperiod(invalid)

    @pytest.mark.parametrize(
        argnames=('zillion', 'name'),
        argvalues=((-1, ''), (0, 'thousand')))
    def test_special_cases(self, zillion, name):
        """
        0 should return 'thousand' and -1 should return an empty string.
        """
        assert conwech.functions.nameperiod(zillion) == name

    @pytest.mark.monkey
    @pytest.mark.parametrize(
        argnames='zillion',
        argvalues=(s**random.randrange(1, 100)
                   for s in random.sample(range(1, sys.maxsize), 100)))
    def test_good_monkey(self, zillion):
        """
        Function should (theoretically) handle any whole number >= -1.
        """
        prefixes = (conwech.lexicon.ZILLION_PERIOD_PREFIXES[int(p)]
                    for p in '{:,}'.format(zillion).split(','))
        assert conwech.functions.nameperiod(zillion) == 'illi'.join(prefixes) + 'illion'


class TestReadPeriod:
    """
    Unit tests for conwech's `readperiod` function.
    """

    @pytest.mark.parametrize(
        argnames='invalid',
        argvalues=(None, 123, 1.23, {123, }, [123, ], (123,)))
    def test_invalid_input_type(self, invalid):
        """
        Function should raise `TypeError` when input is not a str.
        """
        with pytest.raises(TypeError):
            conwech.functions.readperiod(invalid)

    @pytest.mark.parametrize(argnames='invalid', argvalues=(' ', 'not-a-illion'))
    def test_invalid_input_format(self, invalid):
        """
        `readperiod` should raise `InvalidPeriodNameText` when passed a
        name with any sub-component (prefix) not found in
        :data:`.ZILLION_PERIOD_PREFIXES`.
        """
        with pytest.raises(conwech._exceptions.InvalidPeriodNameText):
            conwech.functions.readperiod(invalid)

    @pytest.mark.parametrize(
        argnames=('zillion', 'name'),
        argvalues=((-1, ''), (0, 'thousand')))
    def test_special_cases(self, zillion, name):
        """
        The `readperiod` function should return -1 when `name` is an
        empty string and 0 when `name` is 'thousand'.
        """
        assert conwech.functions.readperiod(name) == zillion

    @pytest.mark.monkey
    @pytest.mark.parametrize(
        argnames='zillion',
        argvalues=(s**random.randrange(1, 100)
                   for s in random.sample(range(1, sys.maxsize), 100)))
    def test_good_monkey(self, zillion):
        """
        Function should handle any period with a whole number zillion.
        """
        prefixes = (conwech.lexicon.ZILLION_PERIOD_PREFIXES[int(p)]
                    for p in '{:,}'.format(zillion).split(','))
        assert conwech.functions.readperiod('illi'.join(prefixes) + 'illion') == zillion


class TestNumber2Text:
    """
    Unit Tests for `number2text` function.

    TODO: refactor old unit tests...
    """

    @pytest.mark.parametrize(
        argnames='invalid',
        argvalues=(None, {123, }, [123, ], (123,)))
    def test_invalid_input_type(self, invalid):
        """
        Test correct exception is raised when given invalid input.
        """
        with pytest.raises(TypeError):
            conwech.functions.number2text(invalid)

    @pytest.mark.parametrize(
        argnames='invalid',
        argvalues=('', ))
    def test_invalid_input_format(self, invalid):
        """
        `number2text` should raise `InvalidNumericString` when passed a
        string that doesn't match Python's float format (see
        :data:`.NUMERIC_STRING`).
        """
        with pytest.raises(conwech._exceptions.InvalidNumericString):
            conwech.functions.number2text(invalid)

    @pytest.mark.parametrize(
        argnames='number',
        argvalues=(0, 0.0, 0e-0, 0.0e0, '0', '0.0', '0e-0', '0.0e0'))
    def test_zero_input(self, number):
        """
        Test some valid forms of zero input.
        """
        assert conwech.functions.number2text(number) == 'zero'

    @pytest.mark.parametrize(argnames='number', argvalues=range(1, 1000))
    def test_units_period(self, number):
        """
        Test first 999 natural numbers (numbers without a period name).
        """
        expected = conwech.lexicon.NATURAL_NUMBERS_LT_1000[number]
        assert conwech.functions.number2text(number) == expected

    @pytest.mark.legacy
    def test_string_dxxx(self):
        expected = 'one hundred twenty-three thousandths'
        assert conwech.functions.number2text('.123') == expected
        assert conwech.functions.number2text('-.123') == 'negative ' + expected

    @pytest.mark.legacy
    def test_string_ndxxx(self):
        expected = 'one hundred twenty-three thousandths'
        assert conwech.functions.number2text('.123') == expected
        assert conwech.functions.number2text('-.123') == 'negative ' + expected

    @pytest.mark.legacy
    def test_valid_format_dxex(self):
        expected = 'one hundred million'
        assert conwech.functions.number2text(.1e9) == expected
        assert conwech.functions.number2text('.1e9') == expected
        assert conwech.functions.number2text(-.1e9) == 'negative ' + expected
        assert conwech.functions.number2text('-.1e9') == 'negative ' + expected

    @pytest.mark.legacy
    def test_valid_format_xdxEx(self):
        expected = 'one billion two hundred million'
        assert conwech.functions.number2text(1.2E9) == expected
        assert conwech.functions.number2text('1.2E9') == expected
        assert conwech.functions.number2text(-1.2E9) == 'negative ' + expected
        assert conwech.functions.number2text('-1.2E9') == 'negative ' + expected

    @pytest.mark.legacy
    def test_valid_format_xdxex(self):
        expected = 'one billion two hundred million'
        assert conwech.functions.number2text(1.2e9) == expected
        assert conwech.functions.number2text('1.2e9') == expected
        assert conwech.functions.number2text(-1.2e9) == 'negative ' + expected
        assert conwech.functions.number2text('-1.2e9') == 'negative ' + expected

    @pytest.mark.legacy
    def test_valid_format_xdxenx(self):
        expected = 'twelve ten-billionths'
        assert conwech.functions.number2text(1.2e-9) == expected
        assert conwech.functions.number2text('1.2e-9') == expected
        assert conwech.functions.number2text(-1.2e-9) == 'negative ' + expected
        assert conwech.functions.number2text('-1.2e-9') == 'negative ' + expected

    @pytest.mark.legacy
    def test_valid_format_0dxex(self):
        expected = 'one hundred million'
        assert conwech.functions.number2text(0.1e9) == expected
        assert conwech.functions.number2text('0.1e9') == expected
        assert conwech.functions.number2text(-0.1e9) == 'negative ' + expected
        assert conwech.functions.number2text('-0.1e9') == 'negative ' + expected

    @pytest.mark.legacy
    def test_valid_format_xd0ex(self):
        expected = 'one billion'
        assert conwech.functions.number2text(1.0e9) == expected
        assert conwech.functions.number2text('1.0e9') == expected
        assert conwech.functions.number2text(-1.0e9) == 'negative ' + expected
        assert conwech.functions.number2text('-1.0e9') == 'negative ' + expected

    @pytest.mark.legacy
    def test_valid_format_xxxdxxxexxx(self):
        expected = ('one hundred twenty-three quadragintillion'
                    ' four hundred fifty-six noventrigintillion')
        assert conwech.functions.number2text(123.456e123) == expected
        assert conwech.functions.number2text('123.456e123') == expected
        assert conwech.functions.number2text(-123.456e123) == 'negative ' + expected
        assert conwech.functions.number2text('-123.456e123') == 'negative ' + expected

    @pytest.mark.legacy
    def test_valid_format_0xxdxx0e0xx(self):
        expected = 'twelve trillion three hundred forty billion'
        assert conwech.functions.number2text(012.340e012) == expected
        assert conwech.functions.number2text('012.340e012') == expected
        assert conwech.functions.number2text(-012.340e012) == 'negative ' + expected
        assert conwech.functions.number2text('-012.340e012') == 'negative ' + expected

    @pytest.mark.legacy
    def test_precision_retention(self):
        expected = ('one quadragintillion'
                    ' two hundred thirty-four noventrigintillion'
                    ' five hundred sixty-seven octotrigintillion'
                    ' eight hundred ninety-eight septentrigintillion'
                    ' seven hundred sixty-five sestrigintillion'
                    ' four hundred thirty-two quinquatrigintillion'
                    ' one hundred quattuortrigintillion')
        assert conwech.functions.number2text('1.2345678987654321e123') == expected
        assert conwech.functions.number2text('-1.2345678987654321e123') == 'negative ' + expected

    @pytest.mark.legacy
    def test_float_xxdxxe3(self):
        assert conwech.functions.number2text(12.34e3) == conwech.functions.number2text(12340)

    @pytest.mark.legacy
    def test_float_xxdxxe2(self):
        assert conwech.functions.number2text(12.34e2) == conwech.functions.number2text(1234)

    @pytest.mark.legacy
    def test_float_xxdxxe1(self):
        assert conwech.functions.number2text(12.34e1) == conwech.functions.number2text(123.4)

    @pytest.mark.legacy
    def test_float_xxdxxe0(self):
        assert conwech.functions.number2text(12.34e0) == conwech.functions.number2text(12.34)

    @pytest.mark.legacy
    def test_float_xxdxxen0(self):
        assert conwech.functions.number2text(12.34e-0) == conwech.functions.number2text(12.34)

    @pytest.mark.legacy
    def test_float_xxdxxen1(self):
        assert conwech.functions.number2text(12.34e-1) == conwech.functions.number2text(1.234)

    @pytest.mark.legacy
    def test_float_xxdxxen2(self):
        assert conwech.functions.number2text(12.34e-2) == conwech.functions.number2text(.1234)

    @pytest.mark.legacy
    def test_float_xxdxxen3(self):
        assert conwech.functions.number2text(12.34e-3) == conwech.functions.number2text(.01234)

    @pytest.mark.legacy
    def test_string_xxdxxe3(self):
        assert conwech.functions.number2text('12.34e3') == conwech.functions.number2text(12340)

    @pytest.mark.legacy
    def test_string_xxdxxe2(self):
        assert conwech.functions.number2text('12.34e2') == conwech.functions.number2text(1234)

    @pytest.mark.legacy
    def test_string_xxdxxe1(self):
        assert conwech.functions.number2text('12.34e1') == conwech.functions.number2text(123.4)

    @pytest.mark.legacy
    def test_string_xxdxxe0(self):
        assert conwech.functions.number2text('12.34e0') == conwech.functions.number2text(12.34)

    @pytest.mark.legacy
    def test_string_xxdxxen0(self):
        assert conwech.functions.number2text('12.34e-0') == conwech.functions.number2text(12.34)

    @pytest.mark.legacy
    def test_string_xxdxxen1(self):
        assert conwech.functions.number2text('12.34e-1') == conwech.functions.number2text(1.234)

    @pytest.mark.legacy
    def test_string_xxdxxen2(self):
        assert conwech.functions.number2text('12.34e-2') == conwech.functions.number2text(.1234)

    @pytest.mark.legacy
    def test_string_xxdxxen3(self):
        assert conwech.functions.number2text('12.34e-3') == conwech.functions.number2text(.01234)

    @pytest.mark.legacy
    def test_float_0d1exx(self):
        assert conwech.functions.number2text(0.1e64) == 'one vigintillion'

    @pytest.mark.legacy
    def test_float_1d0exx(self):
        assert conwech.functions.number2text(1.0e63) == 'one vigintillion'

    @pytest.mark.legacy
    def test_float_0d1enxx(self):
        assert conwech.functions.number2text(0.1e-62) == 'one vigintillionth'

    @pytest.mark.legacy
    def test_float_1d0enxx(self):
        assert conwech.functions.number2text(1.0e-63) == 'one vigintillionth'

    @pytest.mark.legacy
    def test_string_0d1exx(self):
        assert conwech.functions.number2text('0.1e64') == 'one vigintillion'

    @pytest.mark.legacy
    def test_string_1d0exx(self):
        assert conwech.functions.number2text('1.0e63') == 'one vigintillion'

    @pytest.mark.legacy
    def test_string_0d1enxx(self):
        assert conwech.functions.number2text('0.1e-62') == 'one vigintillionth'

    @pytest.mark.legacy
    def test_string_1d0enxx(self):
        assert conwech.functions.number2text('1.0e-63') == 'one vigintillionth'

    @pytest.mark.legacy
    def test_float_x00xdx(self):
        expected = 'one thousand two and three tenths'
        assert conwech.functions.number2text(1002.3) == expected

    @pytest.mark.legacy
    def test_float_x0xdxx(self):
        expected = 'one hundred two and thirty-four hundredths'
        assert conwech.functions.number2text(102.34) == expected

    @pytest.mark.legacy
    def test_float_xxdx0x(self):
        expected = 'twelve and three hundred four thousandths'
        assert conwech.functions.number2text(12.304) == expected

    @pytest.mark.legacy
    def test_float_xdx00x(self):
        expected = 'two and three thousand four ten-thousandths'
        assert conwech.functions.number2text(2.3004) == expected

    @pytest.mark.legacy
    def test_float_dx000x(self):
        expected = 'thirty thousand four hundred-thousandths'
        assert conwech.functions.number2text(.30004) == expected

    @pytest.mark.legacy
    def test_string_x00xdx(self):
        expected = 'one thousand two and three tenths'
        assert conwech.functions.number2text('1002.3') == expected

    @pytest.mark.legacy
    def test_string_x0xdxx(self):
        expected = 'one hundred two and thirty-four hundredths'
        assert conwech.functions.number2text('102.34') == expected

    @pytest.mark.legacy
    def test_string_xxdx0x(self):
        expected = 'twelve and three hundred four thousandths'
        assert conwech.functions.number2text('12.304') == expected

    @pytest.mark.legacy
    def test_string_xdx00x(self):
        expected = 'two and three thousand four ten-thousandths'
        assert conwech.functions.number2text('2.3004') == expected

    @pytest.mark.legacy
    def test_string_dx000x(self):
        expected = 'thirty thousand four hundred-thousandths'
        assert conwech.functions.number2text('.30004') == expected


class TestText2Number:
    """
    Unit Tests for `text2number` function.
    """

    @pytest.mark.parametrize(
        argnames='invalid',
        argvalues=(None, {123, }, [123, ], (123,)))
    def test_invalid_input_type(self, invalid):
        """
        Test correct exception is raised when given invalid input.
        """
        with pytest.raises(TypeError):
            conwech.functions.text2number(invalid)

    @pytest.mark.parametrize(
        argnames='invalid',
        argvalues=('onebilliontwomillionthreethousandandfourtenths', ))
    def test_invalid_input_format(self, invalid):
        """
        `text2number` should raise InvalidNumeralString when passed a
        string of text that doesn't match the required format (see
        :data:`.NUMERAL_STRING`).
        """
        with pytest.raises(conwech._exceptions.InvalidNumeralString):
            conwech.functions.text2number(invalid)

    @pytest.mark.parametrize(
        argnames='invalid',
        argvalues=('one billion invalid million thre thousand', ))
    def test_invalid_period_value(self, invalid):
        """
        `text2number` should raise `InvalidPeriodValueText` upon
        encountering a period value numeral sub-string not found in
        :data:`.NATURAL_NUMBERS_LT_1000` contained in a string of text
        meeting the required numeral string format.

        The the message from the raised exception should identify the
        first offending period value.
        """
        with pytest.raises(conwech._exceptions.InvalidPeriodValueText):
            conwech.functions.text2number(invalid)

    @pytest.mark.parametrize(
        argnames='invalid',
        argvalues=('one billion two invalidillion thre thousand', ))
    def test_invalid_period_name(self, invalid):
        """
        `text2number` should raise `InvalidPeriodNameText` upon
        encountering a period name with any prefix not found in
        :data:`.ZILLION_PERIOD_PREFIXES` contained in a string of text
        meeting the required numeral string format.

        The the message from the raised exception should identify the
        first offending period name.
        """
        with pytest.raises(conwech._exceptions.InvalidPeriodNameText):
            conwech.functions.text2number(invalid)

    @pytest.mark.parametrize(
        argnames='numeral',
        argvalues=('zero', 'negative zero', 'zero and zero tenths'))
    def test_zero_input(self, numeral):
        """
        Test some valid forms of zero input.
        """
        assert int(float(conwech.functions.text2number(numeral))) == 0

    @pytest.mark.parametrize(
        argnames='numeral',
        argvalues=conwech.lexicon.NATURAL_NUMBERS_LT_1000[1:])
    def test_units_period(self, numeral):
        """
        Test first 999 natural numbers (numbers without a period name).
        """
        expected = conwech.lexicon.NATURAL_NUMBERS_LT_1000.index(numeral)
        assert int(float(conwech.functions.text2number(numeral))) == expected


class TestSymmetry:

    @pytest.mark.monkey
    @pytest.mark.symmetry
    @pytest.mark.parametrize(
        argnames='zillion',
        argvalues=(s ** random.randrange(1, 100)
                   for s in random.sample(range(1, sys.maxsize), 100)))
    def test_zillion_cycle(self, zillion):
        """
        `readperiod` should invert `nameperiod`.
        """
        assert conwech.functions.readperiod(conwech.functions.nameperiod(zillion)) == zillion

    @pytest.mark.monkey
    @pytest.mark.symmetry
    @pytest.mark.parametrize(
        argnames='numeric',
        argvalues=(str(s ** random.randrange(1, 100))
                   for s in random.sample(range(1, sys.maxsize), 100)))
    def test_numeric_cycle(self, numeric):
        """
        `text2number` should invert `number2text`.
        """
        numeric = numeric[:1] + '.' + numeric[1:].rstrip('0') + 'e' + str(len(numeric[1:]))
        assert conwech.functions.text2number(conwech.functions.number2text(numeric)) == numeric
