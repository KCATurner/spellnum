"""
Unit tests for the conwech._regexlib submodule.
"""

import abc
import pytest
import inspect
import itertools
import conwech._regexlib


class BasePatternTests(abc.ABC):

    pattern = NotImplemented
    groups = NotImplemented

    @classmethod
    def __init_subclass__(cls, **kwargs):
        super(BasePatternTests, cls).__init_subclass__(**kwargs)
        if cls.pattern is NotImplemented and not inspect.isabstract(cls):
            raise NotImplementedError(
                str(cls) + " missing 'pattern' class attribute!")
        if cls.groups is NotImplemented and not inspect.isabstract(cls):
            raise NotImplementedError(
                str(cls) + " missing 'groups' class attribute!")

    def test_group_names(self):
        """
        Test expected capture group names.
        """
        assert self.groups == tuple(self.pattern.groupindex.keys())

    @pytest.mark.parametrize(argnames='string', argvalues=(' ', '\r', '\n', '\t'))
    def test_empty_string(self, string):
        """
        Empty or whitespace-only strings should never match.
        """
        assert self.pattern.match(string) is None


class TestNumericString(BasePatternTests):
    """
    Unit tests for the NUMERIC_STRING regular expresion.
    """

    pattern = conwech._regexlib.NUMERIC_STRING
    groups = ('bsign', 'bwhole', 'bfraction', 'esign', 'evalue')

    @pytest.mark.parametrize(
        argnames='string',
        argvalues=('   0.0e0', '0.0e0   ', '   0.0e0   '))
    def test_whitespace(self, string):
        """
        Strings with leading or trailing whitespace can match, but
        the whitespace should be ignored.
        """
        match = self.pattern.match(string)
        assert match is not None
        expected = dict.fromkeys(self.groups)
        assert expected == match.groupdict()

    @pytest.mark.parametrize(
        argnames=str('string'),
        argvalues=(r''.join(p) for p in itertools.product(
            ('', '-', '+'), ('', '0', '1'), ('', '.'), ('0', '1'),
            ('', 'e', 'E'), ('', '-', '+'), ('', '0', '1'))))
    def test_float_syntax(self, string):
        """
        Strings should mirror built-in float syntax.
        """
        try:
            float(string)
            assert self.pattern.match(string) is not None
        except ValueError:
            assert self.pattern.match(string) is None

    @pytest.mark.parametrize(
        argnames='string',
        argvalues=('{}0{}0'.format(*p) for p in itertools.product(
            ('', '-', '+'), '0123456789')))
    def test_int_format(self, string):
        """
        Strings like integers should match.
        """
        expected = dict.fromkeys(self.groups)
        # pattern should only capture signs explicitly given ('+' / '-')
        expected['bsign'] = string[0] if string.startswith(('+', '-')) else None
        # pattern should capture whole starting at first non-zero digit
        expected['bwhole'] = string.lstrip('-+0') or None
        match = self.pattern.match(string)
        assert match is not None
        assert expected == match.groupdict()

    @pytest.mark.parametrize(
        argnames='string',
        argvalues=('{}0.0{}0'.format(*p) for p in itertools.product(
            ('', '-', '+'), '0123456789')))
    def test_dec_formats(self, string):
        """
        Strings like decimal numbers should match.
        """
        expected = dict.fromkeys(self.groups)
        # pattern should only capture signs explicitly given ('+' / '-')
        expected['bsign'] = string[0] if string.startswith(('+', '-')) else None
        # pattern should capture fraction ending with the last non-zero digit
        expected['bfraction'] = string.split('.')[-1].rstrip('0') or None
        match = self.pattern.match(string)
        assert match is not None
        assert expected == match.groupdict()

    @pytest.mark.parametrize(
        argnames='string',
        argvalues=('0.0{}{}0{}0'.format(*p) for p in itertools.product(
            'eE', ('', '-', '+'), '0123456789')))
    def test_sci_formats(self, string):
        """
        Strings like numbers in scientific notation should match.
        """
        expected = dict.fromkeys(self.groups)
        # pattern should only capture signs explicitly given ('+' / '-')
        expected['esign'] = string[4] if string[4] in ('+', '-') else None
        # pattern should capture exponent starting at first non-zero digit after flag
        expected['evalue'] = string.lstrip('-+0.eE0') or None
        match = self.pattern.match(string)
        assert match is not None
        assert expected == match.groupdict()


class TestNumeralString(BasePatternTests):
    """
    Unit tests for the NUMERAL_STRING regular expresion.
    """

    pattern = conwech._regexlib.NUMERAL_STRING
    groups = ('sign', 'whole', 'numerator', 'denominator')

    @pytest.mark.skip(reason='unfinished test')
    def test_todo(self):
        """
        TODO: finish unit testing...
        """
        pass


class TestPeriodString(BasePatternTests):
    """
    Unit tests for the PERIOD_STRING regular expresion.
    """

    pattern = conwech._regexlib.PERIOD_STRING
    groups = ('value', 'name')

    @pytest.mark.skip(reason='unfinished test')
    def test_todo(self):
        """
        TODO: finish unit testing...
        """
        pass
