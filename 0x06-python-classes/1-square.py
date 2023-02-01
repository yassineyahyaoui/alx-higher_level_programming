#!/usr/bin/python3
"""Creating an empty Class"""


class Square:
    """Defines an square

    Attributes:
        __size (int): Defines square size

    """
    def __init__(self, size):
        """Making size private

        Args:
            size (int): Defines square size

        Returns: None
        """
        self.__size = size
