#!/usr/bin/python3
"""Creating an empty Class"""


class Rectangle:
    """Print a rectangle"""
    def __init__(self, width=0, height=0):
        """Initialize the object"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Make width private"""
        return self.__width

    @width.setter
    def width(self, value):
        """Handle width errors"""
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """Make height private"""
        return self.__height

    @height.setter
    def height(self, value):
        """Handle height errors"""
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """Calculates area"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Calculates perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * self.__width + 2 * self.__height)
