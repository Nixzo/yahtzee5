"""error.py"""


class MissingIndex(Exception):
    """
    Exception när ett index inte finns i en lista.
    """

    def __init__(self, message="Index out of range."):
        self.message = message
        super().__init__(self.message)


class MissingValue(Exception):
    """
    Exception när ett värde inte finns i en lista.
    """

    def __init__(self, message="Value not found in list."):
        self.message = message
        super().__init__(self.message)
