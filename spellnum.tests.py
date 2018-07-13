import unittest
import spellnum


class SpellPeriodTest(unittest.TestCase):
    
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    def testLTMinimumInput(self):
        self.assertRaises(ValueError, spellnum._spell_period, period=-1)
        
    def testGTMaximumInput(self):
        self.assertRaises(ValueError, spellnum._spell_period, period=1000)
        
    def testTypeStringInput(self):
        self.assertRaises(ValueError, spellnum._spell_period, period='500')
        
    def testTypeFloatInput(self):
        self.assertRaises(ValueError, spellnum._spell_period, period=500.5)
        
    def test000(self):
        expected = ''
        actual = spellnum._spell_period(period=0)
        self.assertMultiLineEqual(expected, actual)
        
    def test001(self):
        expected = 'one'
        actual = spellnum._spell_period(period=1)
        self.assertMultiLineEqual(expected, actual)
        
    def test002(self):
        expected = 'two'
        actual = spellnum._spell_period(period=2)
        self.assertMultiLineEqual(expected, actual)
        
    def test003(self):
        expected = 'three'
        actual = spellnum._spell_period(period=3)
        self.assertMultiLineEqual(expected, actual)
        
    def test004(self):
        expected = 'four'
        actual = spellnum._spell_period(period=4)
        self.assertMultiLineEqual(expected, actual)
        
    def test005(self):
        expected = 'five'
        actual = spellnum._spell_period(period=5)
        self.assertMultiLineEqual(expected, actual)

    def test006(self):
        expected = 'six'
        actual = spellnum._spell_period(period=6)
        self.assertMultiLineEqual(expected, actual)

    def test007(self):
        expected = 'seven'
        actual = spellnum._spell_period(period=7)
        self.assertMultiLineEqual(expected, actual)
        
    def test008(self):
        expected = 'eight'
        actual = spellnum._spell_period(period=8)
        self.assertMultiLineEqual(expected, actual)
        
    def test009(self):
        expected = 'nine'
        actual = spellnum._spell_period(period=9)
        self.assertMultiLineEqual(expected, actual)
        
    def test010(self):
        expected = 'ten'
        actual = spellnum._spell_period(period=10)
        self.assertMultiLineEqual(expected, actual)
        
    def test011(self):
        expected = 'eleven'
        actual = spellnum._spell_period(period=11)
        self.assertMultiLineEqual(expected, actual)
        
    def test012(self):
        expected = 'twelve'
        actual = spellnum._spell_period(period=12)
        self.assertMultiLineEqual(expected, actual)
        
    def test013(self):
        expected = 'thirteen'
        actual = spellnum._spell_period(period=13)
        self.assertMultiLineEqual(expected, actual)
        
    def test014(self):
        expected = 'fourteen'
        actual = spellnum._spell_period(period=14)
        self.assertMultiLineEqual(expected, actual)
        
    def test015(self):
        expected = 'fifteen'
        actual = spellnum._spell_period(period=15)
        self.assertMultiLineEqual(expected, actual)
        
    def test016(self):
        expected = 'sixteen'
        actual = spellnum._spell_period(period=16)
        self.assertMultiLineEqual(expected, actual)
        
    def test017(self):
        expected = 'seventeen'
        actual = spellnum._spell_period(period=17)
        self.assertMultiLineEqual(expected, actual)
        
    def test018(self):
        expected = 'eighteen'
        actual = spellnum._spell_period(period=18)
        self.assertMultiLineEqual(expected, actual)
        
    def test019(self):
        expected = 'nineteen'
        actual = spellnum._spell_period(period=19)
        self.assertMultiLineEqual(expected, actual)
        
    def test100(self):
        expected = 'one hundred'
        actual = spellnum._spell_period(period=100)
        self.assertMultiLineEqual(expected, actual)
        
    def test200(self):
        expected = 'two hundred'
        actual = spellnum._spell_period(period=200)
        self.assertMultiLineEqual(expected, actual)
        
    def test300(self):
        expected = 'three hundred'
        actual = spellnum._spell_period(period=300)
        self.assertMultiLineEqual(expected, actual)
        
    def test400(self):
        expected = 'four hundred'
        actual = spellnum._spell_period(period=400)
        self.assertMultiLineEqual(expected, actual)
        
    def test500(self):
        expected = 'five hundred'
        actual = spellnum._spell_period(period=500)
        self.assertMultiLineEqual(expected, actual)
        
    def test600(self):
        expected = 'six hundred'
        actual = spellnum._spell_period(period=600)
        self.assertMultiLineEqual(expected, actual)
        
    def test700(self):
        expected = 'seven hundred'
        actual = spellnum._spell_period(period=700)
        self.assertMultiLineEqual(expected, actual)
        
    def test800(self):
        expected = 'eight hundred'
        actual = spellnum._spell_period(period=800)
        self.assertMultiLineEqual(expected, actual)
        
    def test900(self):
        expected = 'nine hundred'
        actual = spellnum._spell_period(period=900)
        self.assertMultiLineEqual(expected, actual)
        
    def test999(self):
        expected = 'nine hundred ninety-nine'
        actual = spellnum._spell_period(period=999)
        self.assertMultiLineEqual(expected, actual)
        
        
class PeriodNameTest(unittest.TestCase):
    
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    def testLTZeroInput(self):
        expected = ''
        actual = spellnum._period_name(baseillion=-1)
        self.assertMultiLineEqual(expected, actual)
        
    def test_000(self):
        expected = 'thousand'
        actual = spellnum._period_name(baseillion=0)
        self.assertMultiLineEqual(expected, actual)
        
    def test_001(self):
        expected = 'million'
        actual = spellnum._period_name(baseillion=1)
        self.assertMultiLineEqual(expected, actual)
        
    def test_002(self):
        expected = 'billion'
        actual = spellnum._period_name(baseillion=2)
        self.assertMultiLineEqual(expected, actual)
        
    def test_487(self):
        expected = 'septemoctogintaquadringentillion'
        actual = spellnum._period_name(baseillion=487)
        self.assertMultiLineEqual(expected, actual)
        
    
class SpellIntegerTest(unittest.TestCase):
    
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
