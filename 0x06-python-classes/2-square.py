#!/usr/bin/python3
"""Creating an empty Class"""


class Square:
    """Defines an square

    Attributes:
        __size (int): Defines square size

    """
    def __init__(self, size=0):
        """Making size private

        Args:
            size (int): Defines square size

        Returns: None, if it is not int the method raise the mistake
        """
        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
