import unittest
import spellnum


class SpellPeriodTests(unittest.TestCase):
    
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    def test_LTMinimumInput(self):
        self.assertRaises(ValueError, spellnum._spell_period, period=-1)
        
    def test_GTMaximumInput(self):
        self.assertRaises(ValueError, spellnum._spell_period, period=1000)
        
    def test_TypeStringInput(self):
        self.assertRaises(ValueError, spellnum._spell_period, period='500')
        
    def test_TypeFloatInput(self):
        self.assertRaises(ValueError, spellnum._spell_period, period=500.5)
        
    def test_000(self):
        expected = ''
        actual = spellnum._spell_period(period=0)
        self.assertMultiLineEqual(expected, actual)
        
    def test_001(self):
        expected = 'one'
        actual = spellnum._spell_period(period=1)
        self.assertMultiLineEqual(expected, actual)
        
    def test_002(self):
        expected = 'two'
        actual = spellnum._spell_period(period=2)
        self.assertMultiLineEqual(expected, actual)
        
    def test_003(self):
        expected = 'three'
        actual = spellnum._spell_period(period=3)
        self.assertMultiLineEqual(expected, actual)
        
    def test_004(self):
        expected = 'four'
        actual = spellnum._spell_period(period=4)
        self.assertMultiLineEqual(expected, actual)
        
    def test_005(self):
        expected = 'five'
        actual = spellnum._spell_period(period=5)
        self.assertMultiLineEqual(expected, actual)

    def test_006(self):
        expected = 'six'
        actual = spellnum._spell_period(period=6)
        self.assertMultiLineEqual(expected, actual)

    def test_007(self):
        expected = 'seven'
        actual = spellnum._spell_period(period=7)
        self.assertMultiLineEqual(expected, actual)
        
    def test_008(self):
        expected = 'eight'
        actual = spellnum._spell_period(period=8)
        self.assertMultiLineEqual(expected, actual)
        
    def test_009(self):
        expected = 'nine'
        actual = spellnum._spell_period(period=9)
        self.assertMultiLineEqual(expected, actual)
        
    def test_010(self):
        expected = 'ten'
        actual = spellnum._spell_period(period=10)
        self.assertMultiLineEqual(expected, actual)
        
    def test_011(self):
        expected = 'eleven'
        actual = spellnum._spell_period(period=11)
        self.assertMultiLineEqual(expected, actual)
        
    def test_012(self):
        expected = 'twelve'
        actual = spellnum._spell_period(period=12)
        self.assertMultiLineEqual(expected, actual)
        
    def test_013(self):
        expected = 'thirteen'
        actual = spellnum._spell_period(period=13)
        self.assertMultiLineEqual(expected, actual)
        
    def test_014(self):
        expected = 'fourteen'
        actual = spellnum._spell_period(period=14)
        self.assertMultiLineEqual(expected, actual)
        
    def test_015(self):
        expected = 'fifteen'
        actual = spellnum._spell_period(period=15)
        self.assertMultiLineEqual(expected, actual)
        
    def test_016(self):
        expected = 'sixteen'
        actual = spellnum._spell_period(period=16)
        self.assertMultiLineEqual(expected, actual)
        
    def test_017(self):
        expected = 'seventeen'
        actual = spellnum._spell_period(period=17)
        self.assertMultiLineEqual(expected, actual)
        
    def test_018(self):
        expected = 'eighteen'
        actual = spellnum._spell_period(period=18)
        self.assertMultiLineEqual(expected, actual)
        
    def test_019(self):
        expected = 'nineteen'
        actual = spellnum._spell_period(period=19)
        self.assertMultiLineEqual(expected, actual)
        
    def test_100(self):
        expected = 'one hundred'
        actual = spellnum._spell_period(period=100)
        self.assertMultiLineEqual(expected, actual)
        
    def test_200(self):
        expected = 'two hundred'
        actual = spellnum._spell_period(period=200)
        self.assertMultiLineEqual(expected, actual)
        
    def test_300(self):
        expected = 'three hundred'
        actual = spellnum._spell_period(period=300)
        self.assertMultiLineEqual(expected, actual)
        
    def test_400(self):
        expected = 'four hundred'
        actual = spellnum._spell_period(period=400)
        self.assertMultiLineEqual(expected, actual)
        
    def test_500(self):
        expected = 'five hundred'
        actual = spellnum._spell_period(period=500)
        self.assertMultiLineEqual(expected, actual)
        
    def test_600(self):
        expected = 'six hundred'
        actual = spellnum._spell_period(period=600)
        self.assertMultiLineEqual(expected, actual)
        
    def test_700(self):
        expected = 'seven hundred'
        actual = spellnum._spell_period(period=700)
        self.assertMultiLineEqual(expected, actual)
        
    def test_800(self):
        expected = 'eight hundred'
        actual = spellnum._spell_period(period=800)
        self.assertMultiLineEqual(expected, actual)
        
    def test_900(self):
        expected = 'nine hundred'
        actual = spellnum._spell_period(period=900)
        self.assertMultiLineEqual(expected, actual)
        
    def test_999(self):
        expected = 'nine hundred ninety-nine'
        actual = spellnum._spell_period(period=999)
        self.assertMultiLineEqual(expected, actual)
        
        
class PeriodNameTests(unittest.TestCase):
    
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    def test_LTZeroInput(self):
        expected = ''
        actual = spellnum._get_period_suffix(baseillion=-1)
        self.assertMultiLineEqual(expected, actual)
        
    def test_000(self):
        expected = 'thousand'
        actual = spellnum._get_period_suffix(baseillion=0)
        self.assertMultiLineEqual(expected, actual)
        
    def test_001(self):
        expected = 'million'
        actual = spellnum._get_period_suffix(baseillion=1)
        self.assertMultiLineEqual(expected, actual)
        
    def test_002(self):
        expected = 'billion'
        actual = spellnum._get_period_suffix(baseillion=2)
        self.assertMultiLineEqual(expected, actual)
        
    def test_023(self):
        expected = 'tresvigintillion'
        actual = spellnum._get_period_suffix(baseillion=23)
        self.assertMultiLineEqual(expected, actual)
        
    def test_026(self):
        expected = 'sesvigintillion'
        actual = spellnum._get_period_suffix(baseillion=26)
        self.assertMultiLineEqual(expected, actual)
        
    def test_027(self):
        expected = 'septemvigintillion'
        actual = spellnum._get_period_suffix(baseillion=27)
        self.assertMultiLineEqual(expected, actual)
        
    def test_029(self):
        expected = 'novemvigintillion'
        actual = spellnum._get_period_suffix(baseillion=29)
        self.assertMultiLineEqual(expected, actual)
        
    def test_033(self):
        expected = 'trestrigintillion'
        actual = spellnum._get_period_suffix(baseillion=33)
        self.assertMultiLineEqual(expected, actual)
        
    def test_036(self):
        expected = 'sestrigintillion'
        actual = spellnum._get_period_suffix(baseillion=36)
        self.assertMultiLineEqual(expected, actual)
        
    def test_037(self):
        expected = 'septentrigintillion'
        actual = spellnum._get_period_suffix(baseillion=37)
        self.assertMultiLineEqual(expected, actual)
        
    def test_039(self):
        expected = 'noventrigintillion'
        actual = spellnum._get_period_suffix(baseillion=39)
        self.assertMultiLineEqual(expected, actual)
        
    def test_043(self):
        expected = 'tresquadragintillion'
        actual = spellnum._get_period_suffix(baseillion=43)
        self.assertMultiLineEqual(expected, actual)
        
    def test_046(self):
        expected = 'sesquadragintillion'
        actual = spellnum._get_period_suffix(baseillion=46)
        self.assertMultiLineEqual(expected, actual)
        
    def test_047(self):
        expected = 'septenquadragintillion'
        actual = spellnum._get_period_suffix(baseillion=47)
        self.assertMultiLineEqual(expected, actual)
        
    def test_049(self):
        expected = 'novenquadragintillion'
        actual = spellnum._get_period_suffix(baseillion=49)
        self.assertMultiLineEqual(expected, actual)
        
    def test_053(self):
        expected = 'tresquinquagintillion'
        actual = spellnum._get_period_suffix(baseillion=53)
        self.assertMultiLineEqual(expected, actual)
        
    def test_056(self):
        expected = 'sesquinquagintillion'
        actual = spellnum._get_period_suffix(baseillion=56)
        self.assertMultiLineEqual(expected, actual)
        
    def test_057(self):
        expected = 'septenquinquagintillion'
        actual = spellnum._get_period_suffix(baseillion=57)
        self.assertMultiLineEqual(expected, actual)
        
    def test_059(self):
        expected = 'novenquinquagintillion'
        actual = spellnum._get_period_suffix(baseillion=59)
        self.assertMultiLineEqual(expected, actual)
        
    def test_067(self):
        expected = 'septensexagintillion'
        actual = spellnum._get_period_suffix(baseillion=67)
        self.assertMultiLineEqual(expected, actual)
        
    def test_069(self):
        expected = 'novensexagintillion'
        actual = spellnum._get_period_suffix(baseillion=69)
        self.assertMultiLineEqual(expected, actual)
        
    def test_077(self):
        expected = 'septenseptuagintillion'
        actual = spellnum._get_period_suffix(baseillion=77)
        self.assertMultiLineEqual(expected, actual)
        
    def test_079(self):
        expected = 'novenseptuagintillion'
        actual = spellnum._get_period_suffix(baseillion=79)
        self.assertMultiLineEqual(expected, actual)
        
    def test_086(self):
        expected = 'sexoctogintillion'
        actual = spellnum._get_period_suffix(baseillion=86)
        self.assertMultiLineEqual(expected, actual)
        
    def test_087(self):
        expected = 'septemoctogintillion'
        actual = spellnum._get_period_suffix(baseillion=87)
        self.assertMultiLineEqual(expected, actual)
        
    def test_089(self):
        expected = 'novemoctogintillion'
        actual = spellnum._get_period_suffix(baseillion=89)
        self.assertMultiLineEqual(expected, actual)
        
    def test_106(self):
        expected = 'sexcentillion'
        actual = spellnum._get_period_suffix(baseillion=106)
        self.assertMultiLineEqual(expected, actual)
        
    def test_107(self):
        expected = 'septencentillion'
        actual = spellnum._get_period_suffix(baseillion=107)
        self.assertMultiLineEqual(expected, actual)
        
    def test_109(self):
        expected = 'novencentillion'
        actual = spellnum._get_period_suffix(baseillion=109)
        self.assertMultiLineEqual(expected, actual)
        
    def test_207(self):
        expected = 'septenducentillion'
        actual = spellnum._get_period_suffix(baseillion=207)
        self.assertMultiLineEqual(expected, actual)
        
    def test_209(self):
        expected = 'novenducentillion'
        actual = spellnum._get_period_suffix(baseillion=209)
        self.assertMultiLineEqual(expected, actual)
        
    def test_303(self):
        expected = 'trestrecentillion'
        actual = spellnum._get_period_suffix(baseillion=303)
        self.assertMultiLineEqual(expected, actual)
        
    def test_306(self):
        expected = 'sestrecentillion'
        actual = spellnum._get_period_suffix(baseillion=306)
        self.assertMultiLineEqual(expected, actual)
        
    def test_307(self):
        expected = 'septentrecentillion'
        actual = spellnum._get_period_suffix(baseillion=307)
        self.assertMultiLineEqual(expected, actual)
        
    def test_309(self):
        expected = 'noventrecentillion'
        actual = spellnum._get_period_suffix(baseillion=309)
        self.assertMultiLineEqual(expected, actual)
        
    def test_403(self):
        expected = 'tresquadringentillion'
        actual = spellnum._get_period_suffix(baseillion=403)
        self.assertMultiLineEqual(expected, actual)
        
    def test_406(self):
        expected = 'sesquadringentillion'
        actual = spellnum._get_period_suffix(baseillion=406)
        self.assertMultiLineEqual(expected, actual)
        
    def test_407(self):
        expected = 'septenquadringentillion'
        actual = spellnum._get_period_suffix(baseillion=407)
        self.assertMultiLineEqual(expected, actual)
        
    def test_409(self):
        expected = 'novenquadringentillion'
        actual = spellnum._get_period_suffix(baseillion=409)
        self.assertMultiLineEqual(expected, actual)
        
    def test_503(self):
        expected = 'tresquingentillion'
        actual = spellnum._get_period_suffix(baseillion=503)
        self.assertMultiLineEqual(expected, actual)
        
    def test_506(self):
        expected = 'sesquingentillion'
        actual = spellnum._get_period_suffix(baseillion=506)
        self.assertMultiLineEqual(expected, actual)
        
    def test_507(self):
        expected = 'septenquingentillion'
        actual = spellnum._get_period_suffix(baseillion=507)
        self.assertMultiLineEqual(expected, actual)
        
    def test_509(self):
        expected = 'novenquingentillion'
        actual = spellnum._get_period_suffix(baseillion=509)
        self.assertMultiLineEqual(expected, actual)
        
    def test_607(self):
        expected = 'septensescentillion'
        actual = spellnum._get_period_suffix(baseillion=607)
        self.assertMultiLineEqual(expected, actual)
        
    def test_609(self):
        expected = 'novensescentillion'
        actual = spellnum._get_period_suffix(baseillion=609)
        self.assertMultiLineEqual(expected, actual)
        
    def test_707(self):
        expected = 'septenseptingentillion'
        actual = spellnum._get_period_suffix(baseillion=707)
        self.assertMultiLineEqual(expected, actual)
        
    def test_709(self):
        expected = 'novenseptingentillion'
        actual = spellnum._get_period_suffix(baseillion=709)
        self.assertMultiLineEqual(expected, actual)
        
    def test_806(self):
        expected = 'sexoctingentillion'
        actual = spellnum._get_period_suffix(baseillion=806)
        self.assertMultiLineEqual(expected, actual)
        
    def test_807(self):
        expected = 'septemoctingentillion'
        actual = spellnum._get_period_suffix(baseillion=807)
        self.assertMultiLineEqual(expected, actual)
        
    def test_809(self):
        expected = 'novemoctingentillion'
        actual = spellnum._get_period_suffix(baseillion=809)
        self.assertMultiLineEqual(expected, actual)
        
        
class SpellIntegerTests(unittest.TestCase):
    
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    def test_000000(self):
        expected = 'zero'
        actual = spellnum.spell_integer(number=0)
        self.assertMultiLineEqual(expected, actual)
        
    def test_001000(self):
        expected = 'one thousand'
        actual = spellnum.spell_integer(number=1000)
        self.assertMultiLineEqual(expected, actual)
        
    def test_001111(self):
        expected = 'one thousand one hundred eleven'
        actual = spellnum.spell_integer(number=1111)
        self.assertMultiLineEqual(expected, actual)
        
    def test_001Million(self):
        expected = 'one million'
        actual = spellnum.spell_integer(number=1000000)
        self.assertMultiLineEqual(expected, actual)
        
    def test_010Million(self):
        expected = 'ten million'
        actual = spellnum.spell_integer(number=10000000)
        self.assertMultiLineEqual(expected, actual)
        
    def test_100Million(self):
        expected = 'one hundred million'
        actual = spellnum.spell_integer(number=100000000)
        self.assertMultiLineEqual(expected, actual)
