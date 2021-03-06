#!/usr/bin/python3
"""
Class:
    Rectangle: Defines a rectangle.

"""


class Rectangle:
    """Class to define a Rectangle."""

    def __init__(self, width=0, height=0):
        """Initialization of a rectangle object.

        Args:
        __width (int): Width of the rectangle.
        __height (int): Height of the rectangle.

        """

        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the value of width for the rectangle."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets a height for the rectangle."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Gets the area of a rectangle."""
        return (self.__height * self.__width)

    def perimeter(self):
        """Gets the perimeter of a rectangle."""
        if ((self.__width == 0) or (self.__height == 0)):
            return 0
        else:
            return ((self.__width + self.__height) * 2)

    def __str__(self):
        """Prints a rectangle with numeral characters."""
        if ((self.__width == 0) or (self.__height == 0)):
            return ""

        sqrstr = ""
        for h in range(self.__height):
            for w in range(self.__width):
                sqrstr += "#"
            if h != self.__height - 1:
                sqrstr += "\n"
        return sqrstr

    def __repr__(self):
        """Returns formal version of the rectangle
        --This task actually makes no sense--(bold)

        """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
