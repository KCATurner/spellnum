from unittest import TestCase
from spellnum import functions


class GetPeriodSpellingInputValidityTests(TestCase):
    """
    Tests valid and invalid input type and boundary values for get_period_spelling
    """
    
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    def test_InputLTMinimum(self):
        self.assertRaises(ValueError, functions.get_period_spelling, period=-1)
        
    def test_InputEQMinimum(self):
        expected = ''
        actual = functions.get_period_spelling(period=0)
        self.assertMultiLineEqual(expected, actual)
        
    def test_InputGTMaximum(self):
        self.assertRaises(ValueError, functions.get_period_spelling, period=1000)
        
    def test_InputEQMaximum(self):
        expected = 'nine hundred ninety-nine'
        actual = functions.get_period_spelling(period=999)
        self.assertMultiLineEqual(expected, actual)
        
    def test_TypeStringInput(self):
        self.assertRaises(ValueError, functions.get_period_spelling, period='500')
        
    def test_TypeFloatInput(self):
        self.assertRaises(ValueError, functions.get_period_spelling, period=12.34)
        
        
class GetPeriodSpellingGenericTests(TestCase):
    """
    Tests generic use cases for get_period_spelling
    """
    
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    def test_001(self):
        expected = 'one'
        actual = functions.get_period_spelling(period=1)
        self.assertMultiLineEqual(expected, actual)
        
    def test_002(self):
        expected = 'two'
        actual = functions.get_period_spelling(period=2)
        self.assertMultiLineEqual(expected, actual)
        
    def test_003(self):
        expected = 'three'
        actual = functions.get_period_spelling(period=3)
        self.assertMultiLineEqual(expected, actual)
        
    def test_004(self):
        expected = 'four'
        actual = functions.get_period_spelling(period=4)
        self.assertMultiLineEqual(expected, actual)
        
    def test_005(self):
        expected = 'five'
        actual = functions.get_period_spelling(period=5)
        self.assertMultiLineEqual(expected, actual)

    def test_006(self):
        expected = 'six'
        actual = functions.get_period_spelling(period=6)
        self.assertMultiLineEqual(expected, actual)

    def test_007(self):
        expected = 'seven'
        actual = functions.get_period_spelling(period=7)
        self.assertMultiLineEqual(expected, actual)
        
    def test_008(self):
        expected = 'eight'
        actual = functions.get_period_spelling(period=8)
        self.assertMultiLineEqual(expected, actual)
        
    def test_009(self):
        expected = 'nine'
        actual = functions.get_period_spelling(period=9)
        self.assertMultiLineEqual(expected, actual)
        
    def test_010(self):
        expected = 'ten'
        actual = functions.get_period_spelling(period=10)
        self.assertMultiLineEqual(expected, actual)
        
    def test_011(self):
        expected = 'eleven'
        actual = functions.get_period_spelling(period=11)
        self.assertMultiLineEqual(expected, actual)
        
    def test_012(self):
        expected = 'twelve'
        actual = functions.get_period_spelling(period=12)
        self.assertMultiLineEqual(expected, actual)
        
    def test_013(self):
        expected = 'thirteen'
        actual = functions.get_period_spelling(period=13)
        self.assertMultiLineEqual(expected, actual)
        
    def test_014(self):
        expected = 'fourteen'
        actual = functions.get_period_spelling(period=14)
        self.assertMultiLineEqual(expected, actual)
        
    def test_015(self):
        expected = 'fifteen'
        actual = functions.get_period_spelling(period=15)
        self.assertMultiLineEqual(expected, actual)
        
    def test_016(self):
        expected = 'sixteen'
        actual = functions.get_period_spelling(period=16)
        self.assertMultiLineEqual(expected, actual)
        
    def test_017(self):
        expected = 'seventeen'
        actual = functions.get_period_spelling(period=17)
        self.assertMultiLineEqual(expected, actual)
        
    def test_018(self):
        expected = 'eighteen'
        actual = functions.get_period_spelling(period=18)
        self.assertMultiLineEqual(expected, actual)
        
    def test_019(self):
        expected = 'nineteen'
        actual = functions.get_period_spelling(period=19)
        self.assertMultiLineEqual(expected, actual)
        
    def test_100(self):
        expected = 'one hundred'
        actual = functions.get_period_spelling(period=100)
        self.assertMultiLineEqual(expected, actual)
        
    def test_200(self):
        expected = 'two hundred'
        actual = functions.get_period_spelling(period=200)
        self.assertMultiLineEqual(expected, actual)
        
    def test_300(self):
        expected = 'three hundred'
        actual = functions.get_period_spelling(period=300)
        self.assertMultiLineEqual(expected, actual)
        
    def test_400(self):
        expected = 'four hundred'
        actual = functions.get_period_spelling(period=400)
        self.assertMultiLineEqual(expected, actual)
        
    def test_500(self):
        expected = 'five hundred'
        actual = functions.get_period_spelling(period=500)
        self.assertMultiLineEqual(expected, actual)
        
    def test_600(self):
        expected = 'six hundred'
        actual = functions.get_period_spelling(period=600)
        self.assertMultiLineEqual(expected, actual)
        
    def test_700(self):
        expected = 'seven hundred'
        actual = functions.get_period_spelling(period=700)
        self.assertMultiLineEqual(expected, actual)
        
    def test_800(self):
        expected = 'eight hundred'
        actual = functions.get_period_spelling(period=800)
        self.assertMultiLineEqual(expected, actual)
        
    def test_900(self):
        expected = 'nine hundred'
        actual = functions.get_period_spelling(period=900)
        self.assertMultiLineEqual(expected, actual)
        
        
class GetPeriodSuffixInputValidityTests(TestCase):
    """
    Tests valid and invalid input type and boundary values for get_period_suffix
    """
    
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    def test_InputLTMinimum(self):
        self.assertRaises(ValueError, functions.get_period_suffix, base_illion=-2)
        
    def test_InputEQMinimum(self):
        expected = ''
        actual = functions.get_period_suffix(base_illion=-1)
        self.assertMultiLineEqual(expected, actual)
        
    def test_InputGTMaximum(self):
        self.assertRaises(ValueError, functions.get_period_suffix, base_illion=1000)
        
    def test_InputEQMaximum(self):
        expected = 'novenonagintanongentillion'
        actual = functions.get_period_suffix(base_illion=999)
        self.assertMultiLineEqual(expected, actual)
        
    def test_InputIsStringType(self):
        self.assertRaises(ValueError, functions.get_period_suffix, base_illion='500')
        
    def test_InputIsFloatType(self):
        self.assertRaises(ValueError, functions.get_period_suffix, base_illion=12.34)
        
        
class GetPeriodSuffixLexicalControlTests(TestCase):
    """
    Tests generic use cases for get_period_suffix
    """
    
    def setUp(self):
        pass
    
    def tearDown(self):
        pass

    def test_091(self):
        expected = 'unnonagintillion'
        actual = functions.get_period_suffix(base_illion=91)
        self.assertMultiLineEqual(expected, actual)
        
    def test_092(self):
        expected = 'duononagintillion'
        actual = functions.get_period_suffix(base_illion=92)
        self.assertMultiLineEqual(expected, actual)
        
    def test_093(self):
        expected = 'trenonagintillion'
        actual = functions.get_period_suffix(base_illion=93)
        self.assertMultiLineEqual(expected, actual)
        
    def test_094(self):
        expected = 'quattuornonagintillion'
        actual = functions.get_period_suffix(base_illion=94)
        self.assertMultiLineEqual(expected, actual)
        
    def test_095(self):
        expected = 'quinquanonagintillion'
        actual = functions.get_period_suffix(base_illion=95)
        self.assertMultiLineEqual(expected, actual)
        
    def test_096(self):
        expected = 'senonagintillion'
        actual = functions.get_period_suffix(base_illion=96)
        self.assertMultiLineEqual(expected, actual)
        
    def test_097(self):
        expected = 'septenonagintillion'
        actual = functions.get_period_suffix(base_illion=97)
        self.assertMultiLineEqual(expected, actual)
        
    def test_098(self):
        expected = 'octononagintillion'
        actual = functions.get_period_suffix(base_illion=98)
        self.assertMultiLineEqual(expected, actual)
        
    def test_099(self):
        expected = 'novenonagintillion'
        actual = functions.get_period_suffix(base_illion=99)
        self.assertMultiLineEqual(expected, actual)
        
        
class GetPeriodSuffixLexicalExceptionTests(TestCase):
    """
    Tests for following lexical exceptions in a period suffix:
        se + x:         86 106 806
        se/tre + s:     23 26 33 36 43 46 53 56 83 103 303 306 403 406 503 506 803
        septe/nove + m: 27 29 87 89 807 809
        septe/nove + n: 17 19 37 39 47 49 57 59 67 69 77 79 107 109 207 209 307 309 407 409 507 509 607 609 707 709
    """
    
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    def test_017(self):
        expected = 'septendecillion'
        actual = functions.get_period_suffix(base_illion=17)
        self.assertMultiLineEqual(expected, actual)
        
    def test_019(self):
        expected = 'novendecillion'
        actual = functions.get_period_suffix(base_illion=19)
        self.assertMultiLineEqual(expected, actual)
        
    def test_023(self):
        expected = 'tresvigintillion'
        actual = functions.get_period_suffix(base_illion=23)
        self.assertMultiLineEqual(expected, actual)
        
    def test_026(self):
        expected = 'sesvigintillion'
        actual = functions.get_period_suffix(base_illion=26)
        self.assertMultiLineEqual(expected, actual)
        
    def test_027(self):
        expected = 'septemvigintillion'
        actual = functions.get_period_suffix(base_illion=27)
        self.assertMultiLineEqual(expected, actual)
        
    def test_029(self):
        expected = 'novemvigintillion'
        actual = functions.get_period_suffix(base_illion=29)
        self.assertMultiLineEqual(expected, actual)
        
    def test_033(self):
        expected = 'trestrigintillion'
        actual = functions.get_period_suffix(base_illion=33)
        self.assertMultiLineEqual(expected, actual)
        
    def test_036(self):
        expected = 'sestrigintillion'
        actual = functions.get_period_suffix(base_illion=36)
        self.assertMultiLineEqual(expected, actual)
        
    def test_037(self):
        expected = 'septentrigintillion'
        actual = functions.get_period_suffix(base_illion=37)
        self.assertMultiLineEqual(expected, actual)
        
    def test_039(self):
        expected = 'noventrigintillion'
        actual = functions.get_period_suffix(base_illion=39)
        self.assertMultiLineEqual(expected, actual)
        
    def test_043(self):
        expected = 'tresquadragintillion'
        actual = functions.get_period_suffix(base_illion=43)
        self.assertMultiLineEqual(expected, actual)
        
    def test_046(self):
        expected = 'sesquadragintillion'
        actual = functions.get_period_suffix(base_illion=46)
        self.assertMultiLineEqual(expected, actual)
        
    def test_047(self):
        expected = 'septenquadragintillion'
        actual = functions.get_period_suffix(base_illion=47)
        self.assertMultiLineEqual(expected, actual)
        
    def test_049(self):
        expected = 'novenquadragintillion'
        actual = functions.get_period_suffix(base_illion=49)
        self.assertMultiLineEqual(expected, actual)
        
    def test_053(self):
        expected = 'tresquinquagintillion'
        actual = functions.get_period_suffix(base_illion=53)
        self.assertMultiLineEqual(expected, actual)
        
    def test_056(self):
        expected = 'sesquinquagintillion'
        actual = functions.get_period_suffix(base_illion=56)
        self.assertMultiLineEqual(expected, actual)
        
    def test_057(self):
        expected = 'septenquinquagintillion'
        actual = functions.get_period_suffix(base_illion=57)
        self.assertMultiLineEqual(expected, actual)
        
    def test_059(self):
        expected = 'novenquinquagintillion'
        actual = functions.get_period_suffix(base_illion=59)
        self.assertMultiLineEqual(expected, actual)
        
    def test_067(self):
        expected = 'septensexagintillion'
        actual = functions.get_period_suffix(base_illion=67)
        self.assertMultiLineEqual(expected, actual)
        
    def test_069(self):
        expected = 'novensexagintillion'
        actual = functions.get_period_suffix(base_illion=69)
        self.assertMultiLineEqual(expected, actual)
        
    def test_077(self):
        expected = 'septenseptuagintillion'
        actual = functions.get_period_suffix(base_illion=77)
        self.assertMultiLineEqual(expected, actual)
        
    def test_079(self):
        expected = 'novenseptuagintillion'
        actual = functions.get_period_suffix(base_illion=79)
        self.assertMultiLineEqual(expected, actual)
        
    def test_083(self):
        expected = 'tresoctogintillion'
        actual = functions.get_period_suffix(base_illion=83)
        self.assertMultiLineEqual(expected, actual)
        
    def test_086(self):
        expected = 'sexoctogintillion'
        actual = functions.get_period_suffix(base_illion=86)
        self.assertMultiLineEqual(expected, actual)
        
    def test_087(self):
        expected = 'septemoctogintillion'
        actual = functions.get_period_suffix(base_illion=87)
        self.assertMultiLineEqual(expected, actual)
        
    def test_089(self):
        expected = 'novemoctogintillion'
        actual = functions.get_period_suffix(base_illion=89)
        self.assertMultiLineEqual(expected, actual)
        
    def test_103(self):
        expected = 'trescentillion'
        actual = functions.get_period_suffix(base_illion=103)
        self.assertMultiLineEqual(expected, actual)
        
    def test_106(self):
        expected = 'sexcentillion'
        actual = functions.get_period_suffix(base_illion=106)
        self.assertMultiLineEqual(expected, actual)
        
    def test_107(self):
        expected = 'septencentillion'
        actual = functions.get_period_suffix(base_illion=107)
        self.assertMultiLineEqual(expected, actual)
        
    def test_109(self):
        expected = 'novencentillion'
        actual = functions.get_period_suffix(base_illion=109)
        self.assertMultiLineEqual(expected, actual)
        
    def test_207(self):
        expected = 'septenducentillion'
        actual = functions.get_period_suffix(base_illion=207)
        self.assertMultiLineEqual(expected, actual)
        
    def test_209(self):
        expected = 'novenducentillion'
        actual = functions.get_period_suffix(base_illion=209)
        self.assertMultiLineEqual(expected, actual)
        
    def test_303(self):
        expected = 'trestrecentillion'
        actual = functions.get_period_suffix(base_illion=303)
        self.assertMultiLineEqual(expected, actual)
        
    def test_306(self):
        expected = 'sestrecentillion'
        actual = functions.get_period_suffix(base_illion=306)
        self.assertMultiLineEqual(expected, actual)
        
    def test_307(self):
        expected = 'septentrecentillion'
        actual = functions.get_period_suffix(base_illion=307)
        self.assertMultiLineEqual(expected, actual)
        
    def test_309(self):
        expected = 'noventrecentillion'
        actual = functions.get_period_suffix(base_illion=309)
        self.assertMultiLineEqual(expected, actual)
        
    def test_403(self):
        expected = 'tresquadringentillion'
        actual = functions.get_period_suffix(base_illion=403)
        self.assertMultiLineEqual(expected, actual)
        
    def test_406(self):
        expected = 'sesquadringentillion'
        actual = functions.get_period_suffix(base_illion=406)
        self.assertMultiLineEqual(expected, actual)
        
    def test_407(self):
        expected = 'septenquadringentillion'
        actual = functions.get_period_suffix(base_illion=407)
        self.assertMultiLineEqual(expected, actual)
        
    def test_409(self):
        expected = 'novenquadringentillion'
        actual = functions.get_period_suffix(base_illion=409)
        self.assertMultiLineEqual(expected, actual)
        
    def test_503(self):
        expected = 'tresquingentillion'
        actual = functions.get_period_suffix(base_illion=503)
        self.assertMultiLineEqual(expected, actual)
        
    def test_506(self):
        expected = 'sesquingentillion'
        actual = functions.get_period_suffix(base_illion=506)
        self.assertMultiLineEqual(expected, actual)
        
    def test_507(self):
        expected = 'septenquingentillion'
        actual = functions.get_period_suffix(base_illion=507)
        self.assertMultiLineEqual(expected, actual)
        
    def test_509(self):
        expected = 'novenquingentillion'
        actual = functions.get_period_suffix(base_illion=509)
        self.assertMultiLineEqual(expected, actual)
        
    def test_607(self):
        expected = 'septensescentillion'
        actual = functions.get_period_suffix(base_illion=607)
        self.assertMultiLineEqual(expected, actual)
        
    def test_609(self):
        expected = 'novensescentillion'
        actual = functions.get_period_suffix(base_illion=609)
        self.assertMultiLineEqual(expected, actual)
        
    def test_707(self):
        expected = 'septenseptingentillion'
        actual = functions.get_period_suffix(base_illion=707)
        self.assertMultiLineEqual(expected, actual)
        
    def test_709(self):
        expected = 'novenseptingentillion'
        actual = functions.get_period_suffix(base_illion=709)
        self.assertMultiLineEqual(expected, actual)
        
    def test_803(self):
        expected = 'tresoctingentillion'
        actual = functions.get_period_suffix(base_illion=803)
        self.assertMultiLineEqual(expected, actual)
        
    def test_806(self):
        expected = 'sexoctingentillion'
        actual = functions.get_period_suffix(base_illion=806)
        self.assertMultiLineEqual(expected, actual)
        
    def test_807(self):
        expected = 'septemoctingentillion'
        actual = functions.get_period_suffix(base_illion=807)
        self.assertMultiLineEqual(expected, actual)
        
    def test_809(self):
        expected = 'novemoctingentillion'
        actual = functions.get_period_suffix(base_illion=809)
        self.assertMultiLineEqual(expected, actual)
        
        
class SpellNumberInputValidityTests(TestCase):
    """
    Tests valid and invalid input type and boundary values for spell_number
    """
    
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    def test_InputFloatFormat_XdXeX(self):
        expected = 'one billion two hundred million'
        actual = functions.spell_number(num=1.2e9)
        self.assertMultiLineEqual(expected, actual)
        
    def test_InputFloatFormat_XdXenX(self):
        expected = 'twelve ten billionths'
        actual = functions.spell_number(num=1.2e-9)
        self.assertMultiLineEqual(expected, actual)
        
    def test_InputFloatFormat_0dXeX(self):
        expected = 'one hundred million'
        actual = functions.spell_number(num=0.1e9)
        self.assertMultiLineEqual(expected, actual)
        
    def test_InputFloatFormat_Xd0eX(self):
        expected = 'one billion'
        actual = functions.spell_number(num=1.0e9)
        self.assertMultiLineEqual(expected, actual)
        
    def test_InputFloatFormat_XXXdXXXeXXX(self):
        expected = 'one hundred twenty-three quadragintillion four hundred fifty-six noventrigintillion'
        actual = functions.spell_number(num=123.456e123)
        self.assertMultiLineEqual(expected, actual)
        
    def test_InputFloatFormat_0XXdXX0e0XX(self):
        expected = 'twelve trillion three hundred forty billion'
        actual = functions.spell_number(num=012.340e012)
        self.assertMultiLineEqual(expected, actual)
        
    def test_InputFloatPrecisionLost(self):
        expected = ('one quadragintillion two hundred thirty-four noventrigintillion five hundred sixty-seven '
                    'octotrigintillion eight hundred ninety-eight septentrigintillion seven hundred seventy '
                    'sestrigintillion')
        actual = functions.spell_number(num=1.2345678987654321e123)
        self.assertMultiLineEqual(expected, actual)
        
    def test_InputStringPrecisionRetained(self):
        expected = ('one quadragintillion two hundred thirty-four noventrigintillion five hundred sixty-seven '
                    'octotrigintillion eight hundred ninety-eight septentrigintillion seven hundred sixty-five '
                    'sestrigintillion four hundred thirty-two quinquatrigintillion one hundred quattuortrigintillion')
        actual = functions.spell_number(num='1.2345678987654321e123')
        self.assertMultiLineEqual(expected, actual)
        
    def test_InputStringFormat_XdXeX(self):
        expected = 'one billion two hundred million'
        actual = functions.spell_number(num='1.2e9')
        self.assertMultiLineEqual(expected, actual)
        
    def test_InputStringFormat_XdXEX(self):
        expected = 'one billion two hundred million'
        actual = functions.spell_number(num='1.2E9')
        self.assertMultiLineEqual(expected, actual)
        
    def test_InputStringFormat_XdXenX(self):
        expected = 'twelve ten billionths'
        actual = functions.spell_number(num='1.2e-9')
        self.assertMultiLineEqual(expected, actual)
        
    def test_InputStringFormat_0dXeX(self):
        expected = 'one hundred million'
        actual = functions.spell_number(num='0.1e9')
        self.assertMultiLineEqual(expected, actual)
        
    def test_InputStringFormat_Xd0eX(self):
        expected = 'one billion'
        actual = functions.spell_number(num='1.0e9')
        self.assertMultiLineEqual(expected, actual)
        
    def test_InputStringFormat_XXXdXXXeXXX(self):
        expected = 'one hundred twenty-three quadragintillion four hundred fifty-six noventrigintillion'
        actual = functions.spell_number(num='123.456e123')
        self.assertMultiLineEqual(expected, actual)
        
    def test_InputStringFormat_0XXdXX0e0XX(self):
        expected = 'twelve trillion three hundred forty billion'
        actual = functions.spell_number(num='012.340e012')
        self.assertMultiLineEqual(expected, actual)
        
        
class SpellNumberGenericTests(TestCase):
    """
    Tests generic use cases for spell_number
    """
    
    def test_000000(self):
        expected = 'zero'
        actual = functions.spell_number(num=0)
        self.assertMultiLineEqual(expected, actual)
        
    def test_001000(self):
        expected = 'one thousand'
        actual = functions.spell_number(num=1000)
        self.assertMultiLineEqual(expected, actual)
        
    def test_001111(self):
        expected = 'one thousand one hundred eleven'
        actual = functions.spell_number(num=1111)
        self.assertMultiLineEqual(expected, actual)
        
    def test_001Million(self):
        expected = 'one million'
        actual = functions.spell_number(num=1000000)
        self.assertMultiLineEqual(expected, actual)
        
    def test_010Million(self):
        expected = 'ten million'
        actual = functions.spell_number(num=10000000)
        self.assertMultiLineEqual(expected, actual)
        
    def test_100Million(self):
        expected = 'one hundred million'
        actual = functions.spell_number(num=100000000)
        self.assertMultiLineEqual(expected, actual)
        
        
class SpellNumberWithFractionTests(TestCase):
    """
    Tests spelling numbers with fractions
    """
    
    def test_Tenths(self):
        expected = 'ten million and two tenths'
        actual = functions.spell_number(num=10000000.2)
        self.assertMultiLineEqual(expected, actual)
        
    def test_Hundredths(self):
        expected = 'one million and twenty-three one hundredths'
        actual = functions.spell_number(num=1000000.23)
        self.assertMultiLineEqual(expected, actual)
        
    def test_OneThousandths(self):
        expected = 'one hundred thousand and two hundred three one thousandths'
        actual = functions.spell_number(num=100000.203)
        self.assertMultiLineEqual(expected, actual)
        
    def test_TenThousandths(self):
        expected = 'ten thousand and two thousand three ten thousandths'
        actual = functions.spell_number(num=10000.2003)
        self.assertMultiLineEqual(expected, actual)
        
    def test_OneHundredThousandths(self):
        expected = 'one thousand and twenty thousand three one hundred thousandths'
        actual = functions.spell_number(num=1000.20003)
        self.assertMultiLineEqual(expected, actual)
