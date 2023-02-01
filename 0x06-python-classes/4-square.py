#!/usr/bin/python3
"""Creating an empty Class"""


class Square:
    """Defines an square

    Attributes:
        __size (int): Defines square size

    """
    def __init__(self, size=0):
        """initialysing the square

        Args:
            size (int): Defines square size

        Returns: None
        """
        self.size = size

    @property
    def size(self):
        """Taking the size

        Args:
            size (int): Defines square size

        Returns: size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ Handle the size errors

        Args:
            size (int): square size
        """

        if type(value) is not int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """ Calculates area of a square

        Args:
            size (int): size of a side of square

        Returns: Square's area
        """
        return self.__size ** 2
