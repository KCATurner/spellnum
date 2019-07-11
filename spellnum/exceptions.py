"""
Separate home for custom exceptions raised by spellnum functions.
"""


class InvalidPeriodName(ValueError):
    """
    Custom exception type for readperiod function
    """
    
    def __init__(self, name, prefix, *args):
        super(InvalidPeriodName, self).__init__(
            '"{}" is not a valid Conway-Wechsler period name; '
            'specifically, prefix "{}" not found'.format(name, prefix),
            *args
        )
        
        
class InvalidNumericalFormat(ValueError):
    """
    Custom exception type for number2text function
    """
    
    def __init__(self, number, *args):
        super(InvalidNumericalFormat, self).__init__(
            "we gave it our best, but we don't "
            "understand what you meant by {}".format(number),
            *args
        )
        
        
class InvalidLexicalFormat(ValueError):
    """
    Custom exception for text2number function
    """
    
    def __init__(self, text, *args):
        super(InvalidLexicalFormat, self).__init__(
            '"{}" does not follow lexical expected lexical pattern: '
            '<whole_number_text> and <decimal_numerator_text> <decimal_denominator_text>th(s)'
            '\nsee module documentation for more detail'.format(text),
            *args
        )
        
        
class InvalidPeriodValue(ValueError):
    """
    Custom exception for text2number function
    """
    
    def __init__(self, value, period, *args):
        super(InvalidPeriodValue, self).__init__(
            'could not understand "{}" for {} period'.format(value, period),
            *args
        )
        
        
class InvalidPeriodOrder(ValueError):
    """
    Custom exception for text2number function
    """
    
    def __init__(self, larger, smaller, *args):
        super(InvalidPeriodOrder, self).__init__(
            '"{}" must be followed by a smaller period, '
            'not "{}"'.format(larger, smaller),
            *args
        )
        
        
class ImproperFractionText(ValueError):
    """
    Custom exception for text2number function
    """
    
    def __init__(self, numerator, denominator, *args):
        super(ImproperFractionText, self).__init__(
            '~{} / {} is not a proper fraction'.format(numerator, denominator),
            *args
        )
