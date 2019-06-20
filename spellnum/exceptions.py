"""
Separate home for custom exceptions raised by spellnum functions.
"""


class BaseIllionOutOfBounds(ValueError):
    """
    Custom exception type for get_period_suffix function
    """
    
    def __init__(self, value, *args):
        super(BaseIllionOutOfBounds, self).__init__(
            "{} isn't an integer in the range [-1, 1000)!".format(value),
            *args
        )
        
        
class InvalidNumericalFormat(ValueError):
    """
    Custom exception type for spell_number function
    """
    
    def __init__(self, number, *args):
        super(InvalidNumericalFormat, self).__init__(
            "we gave it our best, but we don't understand what you meant by {}".format(number),
            *args
        )
