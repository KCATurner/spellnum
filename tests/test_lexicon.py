"""
Unit tests for the conwech.lexicon submodule.
"""

import pytest
import conwech.lexicon


class TestNumeralTuples:
    """
    Verify that the lexicon numeral tuples are built properly.
    """

    @pytest.mark.parametrize(argnames='number', argvalues=range(10))
    def test_1_digit_integer(self, number):
        """
        Check numbers [0, 10)
        """
        expected = conwech.lexicon.NATURAL_NUMBERS_LT_20[number]
        actual = conwech.lexicon.NATURAL_NUMBERS_LT_1000[number]
        assert actual == expected

    @pytest.mark.parametrize(argnames='number', argvalues=range(10, 100))
    def test_2_digit_integer(self, number):
        """
        Check numbers [10, 100)
        """
        expected = conwech.lexicon.NATURAL_NUMBERS_LT_100[number]
        actual = conwech.lexicon.NATURAL_NUMBERS_LT_1000[number]
        assert actual == expected

    @pytest.mark.parametrize(argnames='number', argvalues=range(100, 1000))
    def test_3_digit_integer(self, number):
        """
        Check numbers [100, 1000)
        """
        hundred = conwech.lexicon.NATURAL_NUMBERS_LT_20[number // 100]
        tens = conwech.lexicon.NATURAL_NUMBERS_LT_100[number % 100]
        expected = '{h} hundred {t}'.format(h=hundred, t=tens).strip()
        actual = conwech.lexicon.NATURAL_NUMBERS_LT_1000[number]
        assert actual == expected


class TestZillionPrefixes:
    """
    Verify that the lexicon period prefixes were built properly.
    """

    @pytest.mark.parametrize(
        argnames=('index', 'prefix'),
        argvalues=zip(range(len(conwech.lexicon.ZILLION_PERIOD_PREFIXES)),
                      conwech.lexicon.ZILLION_PERIOD_PREFIXES))
    def test_prefix_novelty(self, index, prefix):
        """
        All prefixes must be unique.
        """
        prefixes = conwech.lexicon.ZILLION_PERIOD_PREFIXES[:index]
        if prefix in prefixes:
            pytest.fail(msg="{d}:{p} duplicates {i}:{p}!".format(
                d=index, i=prefixes.index(prefix), p=prefix))

    @pytest.mark.parametrize(
        argnames=('zillion1', 'zillion2'),
        argvalues=((102, 200), (103, 300), (106, 600)))
    def test_known_similarity(self, zillion1, zillion2):
        """
        Test prefixes known to be extremely similar.
             du[o]centillion  !=   du[ ]centillion
            tre[s]centillion  !=  tre[ ]centillion
             se[x]centillion  !=   se[s]centillion
        """
        prefix1 = conwech.lexicon.ZILLION_PERIOD_PREFIXES[zillion1]
        prefix2 = conwech.lexicon.ZILLION_PERIOD_PREFIXES[zillion2]
        assert prefix1 != prefix2

    @pytest.mark.parametrize(
        argnames='zillion',
        argvalues=(27, 87, 807, 29, 89, 809))
    def test_m_exception(self, zillion):
        """
        Test when 'm' is appended to the 'septe' or 'nove' prefixes.

        Billion Exceptions:
            - septe(m):  27,  87, 807
            -  nove(m):  29,  89, 809
        """
        expected = '{u}m{t}{h}'.format(
            u=conwech.lexicon._UNIT_PREFIX_COMPONENTS[zillion % 10],
            t=conwech.lexicon._TENS_PREFIX_COMPONENTS[zillion % 100 // 10],
            h=conwech.lexicon._HUND_PREFIX_COMPONENTS[zillion // 100]).rstrip('ai')
        assert conwech.lexicon.ZILLION_PERIOD_PREFIXES[zillion] == expected

    @pytest.mark.parametrize(
        argnames='zillion',
        argvalues=(17, 37, 47, 57, 67, 77, 107, 207, 307, 407, 507, 607, 707,
                   19, 39, 49, 59, 69, 79, 109, 209, 309, 409, 509, 609, 709))
    def test_n_exception(self, zillion):
        """
        Test when 'n' is appended to the 'septe' or 'nove' prefixes.

        Billion Exceptions:
            - septe(n):  17,  37,  47,  57,  67,  77, 107, 207, 307, 407, 507, 607, 707
            -  nove(n):  19,  39,  49,  59,  69,  79, 109, 209, 309, 409, 509, 609, 709
        """
        expected = '{u}n{t}{h}'.format(
            u=conwech.lexicon._UNIT_PREFIX_COMPONENTS[zillion % 10],
            t=conwech.lexicon._TENS_PREFIX_COMPONENTS[zillion % 100 // 10],
            h=conwech.lexicon._HUND_PREFIX_COMPONENTS[zillion // 100]).rstrip('ai')
        assert conwech.lexicon.ZILLION_PERIOD_PREFIXES[zillion] == expected

    @pytest.mark.parametrize(
        argnames='zillion',
        argvalues=(23, 33, 43, 53, 83, 103, 303, 403, 503, 803,
                   26, 36, 46, 56, 306, 406, 506))
    def test_s_exception(self, zillion):
        """
        Test when 's' is appended to the 'tre' or 'se' prefixes.

        Billion Exceptions:
            - tre(s):  23,  33,  43,  53,  83, 103, 303, 403, 503, 803
            -  se(s):  26,  36,  46,  56,           306, 406, 506
        """
        expected = '{u}s{t}{h}'.format(
            u=conwech.lexicon._UNIT_PREFIX_COMPONENTS[zillion % 10],
            t=conwech.lexicon._TENS_PREFIX_COMPONENTS[zillion % 100 // 10],
            h=conwech.lexicon._HUND_PREFIX_COMPONENTS[zillion // 100]).rstrip('ai')
        assert conwech.lexicon.ZILLION_PERIOD_PREFIXES[zillion] == expected

    @pytest.mark.parametrize(
        argnames='zillion',
        argvalues=(86, 106, 806))
    def test_x_exception(self, zillion):
        """
        Test when 'x' is added to the 'se' prefix.

        Billion Exceptions:
            - se(x):  86, 106, 806
        """
        expected = '{u}x{t}{h}'.format(
            u=conwech.lexicon._UNIT_PREFIX_COMPONENTS[zillion % 10],
            t=conwech.lexicon._TENS_PREFIX_COMPONENTS[zillion % 100 // 10],
            h=conwech.lexicon._HUND_PREFIX_COMPONENTS[zillion // 100]).rstrip('ai')
        assert conwech.lexicon.ZILLION_PERIOD_PREFIXES[zillion] == expected
