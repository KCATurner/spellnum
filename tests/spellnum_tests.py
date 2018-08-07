import unittest
from spellnum import functions


class SpellPeriodTests(unittest.TestCase):
    
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    def test_LTMinimumInput(self):
        self.assertRaises(ValueError, functions._get_period_spelling, period=-1)
        
    def test_GTMaximumInput(self):
        self.assertRaises(ValueError, functions._get_period_spelling, period=1000)
        
    def test_TypeStringInput(self):
        self.assertRaises(ValueError, functions._get_period_spelling, period='500')
        
    def test_TypeFloatInput(self):
        self.assertRaises(ValueError, functions._get_period_spelling, period=12.34)
        
    def test_000(self):
        expected = ''
        actual = functions._get_period_spelling(period=0)
        self.assertMultiLineEqual(expected, actual)
        
    def test_001(self):
        expected = 'one'
        actual = functions._get_period_spelling(period=1)
        self.assertMultiLineEqual(expected, actual)
        
    def test_002(self):
        expected = 'two'
        actual = functions._get_period_spelling(period=2)
        self.assertMultiLineEqual(expected, actual)
        
    def test_003(self):
        expected = 'three'
        actual = functions._get_period_spelling(period=3)
        self.assertMultiLineEqual(expected, actual)
        
    def test_004(self):
        expected = 'four'
        actual = functions._get_period_spelling(period=4)
        self.assertMultiLineEqual(expected, actual)
        
    def test_005(self):
        expected = 'five'
        actual = functions._get_period_spelling(period=5)
        self.assertMultiLineEqual(expected, actual)

    def test_006(self):
        expected = 'six'
        actual = functions._get_period_spelling(period=6)
        self.assertMultiLineEqual(expected, actual)

    def test_007(self):
        expected = 'seven'
        actual = functions._get_period_spelling(period=7)
        self.assertMultiLineEqual(expected, actual)
        
    def test_008(self):
        expected = 'eight'
        actual = functions._get_period_spelling(period=8)
        self.assertMultiLineEqual(expected, actual)
        
    def test_009(self):
        expected = 'nine'
        actual = functions._get_period_spelling(period=9)
        self.assertMultiLineEqual(expected, actual)
        
    def test_010(self):
        expected = 'ten'
        actual = functions._get_period_spelling(period=10)
        self.assertMultiLineEqual(expected, actual)
        
    def test_011(self):
        expected = 'eleven'
        actual = functions._get_period_spelling(period=11)
        self.assertMultiLineEqual(expected, actual)
        
    def test_012(self):
        expected = 'twelve'
        actual = functions._get_period_spelling(period=12)
        self.assertMultiLineEqual(expected, actual)
        
    def test_013(self):
        expected = 'thirteen'
        actual = functions._get_period_spelling(period=13)
        self.assertMultiLineEqual(expected, actual)
        
    def test_014(self):
        expected = 'fourteen'
        actual = functions._get_period_spelling(period=14)
        self.assertMultiLineEqual(expected, actual)
        
    def test_015(self):
        expected = 'fifteen'
        actual = functions._get_period_spelling(period=15)
        self.assertMultiLineEqual(expected, actual)
        
    def test_016(self):
        expected = 'sixteen'
        actual = functions._get_period_spelling(period=16)
        self.assertMultiLineEqual(expected, actual)
        
    def test_017(self):
        expected = 'seventeen'
        actual = functions._get_period_spelling(period=17)
        self.assertMultiLineEqual(expected, actual)
        
    def test_018(self):
        expected = 'eighteen'
        actual = functions._get_period_spelling(period=18)
        self.assertMultiLineEqual(expected, actual)
        
    def test_019(self):
        expected = 'nineteen'
        actual = functions._get_period_spelling(period=19)
        self.assertMultiLineEqual(expected, actual)
        
    def test_100(self):
        expected = 'one hundred'
        actual = functions._get_period_spelling(period=100)
        self.assertMultiLineEqual(expected, actual)
        
    def test_200(self):
        expected = 'two hundred'
        actual = functions._get_period_spelling(period=200)
        self.assertMultiLineEqual(expected, actual)
        
    def test_300(self):
        expected = 'three hundred'
        actual = functions._get_period_spelling(period=300)
        self.assertMultiLineEqual(expected, actual)
        
    def test_400(self):
        expected = 'four hundred'
        actual = functions._get_period_spelling(period=400)
        self.assertMultiLineEqual(expected, actual)
        
    def test_500(self):
        expected = 'five hundred'
        actual = functions._get_period_spelling(period=500)
        self.assertMultiLineEqual(expected, actual)
        
    def test_600(self):
        expected = 'six hundred'
        actual = functions._get_period_spelling(period=600)
        self.assertMultiLineEqual(expected, actual)
        
    def test_700(self):
        expected = 'seven hundred'
        actual = functions._get_period_spelling(period=700)
        self.assertMultiLineEqual(expected, actual)
        
    def test_800(self):
        expected = 'eight hundred'
        actual = functions._get_period_spelling(period=800)
        self.assertMultiLineEqual(expected, actual)
        
    def test_900(self):
        expected = 'nine hundred'
        actual = functions._get_period_spelling(period=900)
        self.assertMultiLineEqual(expected, actual)
        
    def test_999(self):
        expected = 'nine hundred ninety-nine'
        actual = functions._get_period_spelling(period=999)
        self.assertMultiLineEqual(expected, actual)
        
        
class PeriodSuffixTests(unittest.TestCase):
    
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    def test_LTMinimumInput(self):
        self.assertRaises(ValueError, functions._get_period_suffix, base_illion=-2)
        
    def test_GTMaximumInput(self):
        self.assertRaises(ValueError, functions._get_period_suffix, base_illion=1000)
        
    def test_TypeStringInput(self):
        self.assertRaises(ValueError, functions._get_period_suffix, base_illion='500')
        
    def test_TypeFloatInput(self):
        self.assertRaises(ValueError, functions._get_period_suffix, base_illion=12.34)
        
    def test_LTZeroInput(self):
        expected = ''
        actual = functions._get_period_suffix(base_illion=-1)
        self.assertMultiLineEqual(expected, actual)
        
    def test_000(self):
        expected = 'thousand'
        actual = functions._get_period_suffix(base_illion=0)
        self.assertMultiLineEqual(expected, actual)
        
    def test_001(self):
        expected = 'million'
        actual = functions._get_period_suffix(base_illion=1)
        self.assertMultiLineEqual(expected, actual)
        
    def test_002(self):
        expected = 'billion'
        actual = functions._get_period_suffix(base_illion=2)
        self.assertMultiLineEqual(expected, actual)
        
    def test_023(self):
        expected = 'tresvigintillion'
        actual = functions._get_period_suffix(base_illion=23)
        self.assertMultiLineEqual(expected, actual)
        
    def test_026(self):
        expected = 'sesvigintillion'
        actual = functions._get_period_suffix(base_illion=26)
        self.assertMultiLineEqual(expected, actual)
        
    def test_027(self):
        expected = 'septemvigintillion'
        actual = functions._get_period_suffix(base_illion=27)
        self.assertMultiLineEqual(expected, actual)
        
    def test_029(self):
        expected = 'novemvigintillion'
        actual = functions._get_period_suffix(base_illion=29)
        self.assertMultiLineEqual(expected, actual)
        
    def test_033(self):
        expected = 'trestrigintillion'
        actual = functions._get_period_suffix(base_illion=33)
        self.assertMultiLineEqual(expected, actual)
        
    def test_036(self):
        expected = 'sestrigintillion'
        actual = functions._get_period_suffix(base_illion=36)
        self.assertMultiLineEqual(expected, actual)
        
    def test_037(self):
        expected = 'septentrigintillion'
        actual = functions._get_period_suffix(base_illion=37)
        self.assertMultiLineEqual(expected, actual)
        
    def test_039(self):
        expected = 'noventrigintillion'
        actual = functions._get_period_suffix(base_illion=39)
        self.assertMultiLineEqual(expected, actual)
        
    def test_043(self):
        expected = 'tresquadragintillion'
        actual = functions._get_period_suffix(base_illion=43)
        self.assertMultiLineEqual(expected, actual)
        
    def test_046(self):
        expected = 'sesquadragintillion'
        actual = functions._get_period_suffix(base_illion=46)
        self.assertMultiLineEqual(expected, actual)
        
    def test_047(self):
        expected = 'septenquadragintillion'
        actual = functions._get_period_suffix(base_illion=47)
        self.assertMultiLineEqual(expected, actual)
        
    def test_049(self):
        expected = 'novenquadragintillion'
        actual = functions._get_period_suffix(base_illion=49)
        self.assertMultiLineEqual(expected, actual)
        
    def test_053(self):
        expected = 'tresquinquagintillion'
        actual = functions._get_period_suffix(base_illion=53)
        self.assertMultiLineEqual(expected, actual)
        
    def test_056(self):
        expected = 'sesquinquagintillion'
        actual = functions._get_period_suffix(base_illion=56)
        self.assertMultiLineEqual(expected, actual)
        
    def test_057(self):
        expected = 'septenquinquagintillion'
        actual = functions._get_period_suffix(base_illion=57)
        self.assertMultiLineEqual(expected, actual)
        
    def test_059(self):
        expected = 'novenquinquagintillion'
        actual = functions._get_period_suffix(base_illion=59)
        self.assertMultiLineEqual(expected, actual)
        
    def test_067(self):
        expected = 'septensexagintillion'
        actual = functions._get_period_suffix(base_illion=67)
        self.assertMultiLineEqual(expected, actual)
        
    def test_069(self):
        expected = 'novensexagintillion'
        actual = functions._get_period_suffix(base_illion=69)
        self.assertMultiLineEqual(expected, actual)
        
    def test_077(self):
        expected = 'septenseptuagintillion'
        actual = functions._get_period_suffix(base_illion=77)
        self.assertMultiLineEqual(expected, actual)
        
    def test_079(self):
        expected = 'novenseptuagintillion'
        actual = functions._get_period_suffix(base_illion=79)
        self.assertMultiLineEqual(expected, actual)
        
    def test_086(self):
        expected = 'sexoctogintillion'
        actual = functions._get_period_suffix(base_illion=86)
        self.assertMultiLineEqual(expected, actual)
        
    def test_087(self):
        expected = 'septemoctogintillion'
        actual = functions._get_period_suffix(base_illion=87)
        self.assertMultiLineEqual(expected, actual)
        
    def test_089(self):
        expected = 'novemoctogintillion'
        actual = functions._get_period_suffix(base_illion=89)
        self.assertMultiLineEqual(expected, actual)
        
    def test_106(self):
        expected = 'sexcentillion'
        actual = functions._get_period_suffix(base_illion=106)
        self.assertMultiLineEqual(expected, actual)
        
    def test_107(self):
        expected = 'septencentillion'
        actual = functions._get_period_suffix(base_illion=107)
        self.assertMultiLineEqual(expected, actual)
        
    def test_109(self):
        expected = 'novencentillion'
        actual = functions._get_period_suffix(base_illion=109)
        self.assertMultiLineEqual(expected, actual)
        
    def test_207(self):
        expected = 'septenducentillion'
        actual = functions._get_period_suffix(base_illion=207)
        self.assertMultiLineEqual(expected, actual)
        
    def test_209(self):
        expected = 'novenducentillion'
        actual = functions._get_period_suffix(base_illion=209)
        self.assertMultiLineEqual(expected, actual)
        
    def test_303(self):
        expected = 'trestrecentillion'
        actual = functions._get_period_suffix(base_illion=303)
        self.assertMultiLineEqual(expected, actual)
        
    def test_306(self):
        expected = 'sestrecentillion'
        actual = functions._get_period_suffix(base_illion=306)
        self.assertMultiLineEqual(expected, actual)
        
    def test_307(self):
        expected = 'septentrecentillion'
        actual = functions._get_period_suffix(base_illion=307)
        self.assertMultiLineEqual(expected, actual)
        
    def test_309(self):
        expected = 'noventrecentillion'
        actual = functions._get_period_suffix(base_illion=309)
        self.assertMultiLineEqual(expected, actual)
        
    def test_403(self):
        expected = 'tresquadringentillion'
        actual = functions._get_period_suffix(base_illion=403)
        self.assertMultiLineEqual(expected, actual)
        
    def test_406(self):
        expected = 'sesquadringentillion'
        actual = functions._get_period_suffix(base_illion=406)
        self.assertMultiLineEqual(expected, actual)
        
    def test_407(self):
        expected = 'septenquadringentillion'
        actual = functions._get_period_suffix(base_illion=407)
        self.assertMultiLineEqual(expected, actual)
        
    def test_409(self):
        expected = 'novenquadringentillion'
        actual = functions._get_period_suffix(base_illion=409)
        self.assertMultiLineEqual(expected, actual)
        
    def test_503(self):
        expected = 'tresquingentillion'
        actual = functions._get_period_suffix(base_illion=503)
        self.assertMultiLineEqual(expected, actual)
        
    def test_506(self):
        expected = 'sesquingentillion'
        actual = functions._get_period_suffix(base_illion=506)
        self.assertMultiLineEqual(expected, actual)
        
    def test_507(self):
        expected = 'septenquingentillion'
        actual = functions._get_period_suffix(base_illion=507)
        self.assertMultiLineEqual(expected, actual)
        
    def test_509(self):
        expected = 'novenquingentillion'
        actual = functions._get_period_suffix(base_illion=509)
        self.assertMultiLineEqual(expected, actual)
        
    def test_607(self):
        expected = 'septensescentillion'
        actual = functions._get_period_suffix(base_illion=607)
        self.assertMultiLineEqual(expected, actual)
        
    def test_609(self):
        expected = 'novensescentillion'
        actual = functions._get_period_suffix(base_illion=609)
        self.assertMultiLineEqual(expected, actual)
        
    def test_707(self):
        expected = 'septenseptingentillion'
        actual = functions._get_period_suffix(base_illion=707)
        self.assertMultiLineEqual(expected, actual)
        
    def test_709(self):
        expected = 'novenseptingentillion'
        actual = functions._get_period_suffix(base_illion=709)
        self.assertMultiLineEqual(expected, actual)
        
    def test_806(self):
        expected = 'sexoctingentillion'
        actual = functions._get_period_suffix(base_illion=806)
        self.assertMultiLineEqual(expected, actual)
        
    def test_807(self):
        expected = 'septemoctingentillion'
        actual = functions._get_period_suffix(base_illion=807)
        self.assertMultiLineEqual(expected, actual)
        
    def test_809(self):
        expected = 'novemoctingentillion'
        actual = functions._get_period_suffix(base_illion=809)
        self.assertMultiLineEqual(expected, actual)
        
        
class SpellIntegerTests(unittest.TestCase):
    
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    def test_SciInputFloat(self):
        expected = 'one hundred twenty-three vigintillion'
        actual = functions.spell_integer(number=1.23e65)
        self.assertMultiLineEqual(expected, actual)
        
    def test_SciInputFloatShifted(self):
        expected = 'one hundred twenty-three vigintillion'
        actual = functions.spell_integer(number=12.3e64)
        self.assertMultiLineEqual(expected, actual)
    
    def test_SciInputString(self):
        expected = 'one hundred twenty-three vigintillion'
        actual = functions.spell_integer(number='1.23e65')
        self.assertMultiLineEqual(expected, actual)
        
    def test_SciInputStringCaps(self):
        expected = 'one hundred twenty-three vigintillion'
        actual = functions.spell_integer(number='1.23E65')
        self.assertMultiLineEqual(expected, actual)
        
    def test_SciInputStringPadded(self):
        expected = 'one hundred twenty-three vigintillion'
        actual = functions.spell_integer(number='01.230e065')
        self.assertMultiLineEqual(expected, actual)
    
    def test_000000(self):
        expected = 'zero'
        actual = functions.spell_integer(number=0)
        self.assertMultiLineEqual(expected, actual)
        
    def test_001000(self):
        expected = 'one thousand'
        actual = functions.spell_integer(number=1000)
        self.assertMultiLineEqual(expected, actual)
        
    def test_001111(self):
        expected = 'one thousand one hundred eleven'
        actual = functions.spell_integer(number=1111)
        self.assertMultiLineEqual(expected, actual)
        
    def test_001Million(self):
        expected = 'one million'
        actual = functions.spell_integer(number=1000000)
        self.assertMultiLineEqual(expected, actual)
        
    def test_010Million(self):
        expected = 'ten million'
        actual = functions.spell_integer(number=10000000)
        self.assertMultiLineEqual(expected, actual)
        
    def test_100Million(self):
        expected = 'one hundred million'
        actual = functions.spell_integer(number=100000000)
        self.assertMultiLineEqual(expected, actual)
