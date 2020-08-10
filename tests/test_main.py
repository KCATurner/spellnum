"""
Unit tests for the conwech.__main__.
"""

import re
import pytest
import pyperclip
import subprocess
import conwech.__main__


class TestRead:

    @pytest.mark.parametrize(
        argnames='numeral',
        argvalues=['negative twelve thousand and three tenths', ])
    def test_copy_flag(self, numeral):
        pyperclip.copy('test')
        output = subprocess.run(
            f'python -m conwech read "{numeral}"',
            capture_output=True, text=True, check=True).stdout
        assert pyperclip.paste() == 'test' # clipboard should be unaffected
        output = subprocess.run(
            f'python -m conwech read --copy "{numeral}"',
            capture_output=True, text=True, check=True).stdout
        for color in conwech.__main__.Colors:
            output = output.replace(color.value, '')
        assert pyperclip.paste() == output.strip() # clipboard should hold output


class TestSpell:

    @pytest.mark.parametrize(
        argnames='number',
        argvalues=['-12000.3'])
    def test_copy_flag(self, number):
        pyperclip.copy('test')
        output = subprocess.run(
            f'python -m conwech spell "{number}"',
            capture_output=True, text=True, check=True).stdout
        assert pyperclip.paste() == 'test' # clipboard should be unaffected
        output = subprocess.run(
            f'python -m conwech spell --copy "{number}"',
            capture_output=True, text=True, check=True).stdout
        for color in conwech.__main__.Colors:
            output = output.replace(color.value, '')
        assert pyperclip.paste() == output.strip() # clipboard should hold output

    def test_recursive_flag(self):
        output = subprocess.run(
            f'python -m conwech spell --recursive "323"',
            capture_output=True, text=True, check=True).stdout
        for color in conwech.__main__.Colors:
            output = output.replace(color.value, '')
        numbers = [int(n) for n in re.findall(r'\b(\d+)\b', output)]
        assert numbers == [23, 11, 6, 3, 5, 4, 4]
