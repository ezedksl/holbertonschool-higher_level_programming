#!/usr/bin/python3
"""
Class:
    Rectangle: Defines a rectangle.

"""


class Rectangle:
    """Class to define a Rectangle.

    Attributes:
        __width: Width of the rectangle object
        __height: Height of the rectangle object
    """

    def __init__(self, width=0, height=0):
        """Initialization of a rectangle object.

        Args:
        width (int): Width of the rectangle.
        height (int): Height of the rectangle.

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
