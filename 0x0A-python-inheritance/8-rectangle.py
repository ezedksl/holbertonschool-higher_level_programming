#!/usr/bin/python3
"""Defines a class inherited from BaseGeometry"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Defines Rectangle class inherited from BaseGeometry"""

    def __init__(self, width, height):
        """Creates a new Rectangle object

        Args:
            width (int) = width of the rectangle
            height (int) = height of the rectangle
        """

        if (self.integer_validator("width", width) and
                self.integer_validator("height", height)):
            self.__width = width
            self.__height = height