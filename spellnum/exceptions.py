"""
Separate home for custom exceptions raised by spellnum functions.
"""


class InvalidNumericalFormat(ValueError):
    """
    Custom exception type for spell_number function
    """
    
    def __init__(self, number, *args):
        super(InvalidNumericalFormat, self).__init__(
            "we gave it our best, but we don't understand what you meant by {}".format(number),
            *args
        )
