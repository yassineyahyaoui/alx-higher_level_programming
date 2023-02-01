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

    def __lt__(self, other):
        """ Compare if our square is less than the other one

        Args:
            other (Square): the square which we are comparing

        Returns:
            True or False
        """
        return self.area() < other.area()

    def __le__(self, other):
        """ Compare if our square is less ot equal than the other one

        Args:
            other (Square): the square which we are comparing

        Returns:
            True or False
        """
        return self.area() <= other.area()

    def __eq__(self, other):
        """ Compare if our square is equal than the other one

        Args:
            other (Square): the square which we are comparing

        Returns:
            True or False
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """ Compare if our square is different than the other one

        Args:
            other (Square): the square which we are comparing

        Returns:
            True or False
        """
        return self.area() != other.area()

    def __gt__(self, other):
        """ Compare if our square is greater than the other one

        Args:
            other (Square): the square which we are comparing

        Returns:
            True or False
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """ Compare if our square is less than the other one

        Args:
            other (Square): the square which we are comparing

        Returns:
            True or False
        """
        return self.area() >= other.area()
