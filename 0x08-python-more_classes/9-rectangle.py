#!/usr/bin/python3
"""
Class:
    Rectangle: Defines a rectangle.

"""


class Rectangle:
    """Class to define a Rectangle."""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialization of a rectangle object.

        Args:
        __width (int): Width of the rectangle.
        __height (int): Height of the rectangle.

        """

        Rectangle.number_of_instances += 1
        self.__width = width
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
                sqrstr += str(self.print_symbol)
            if h != self.__height - 1:
                sqrstr += "\n"
        return sqrstr

    def __repr__(self):
        """Returns formal version of the rectangle
        --This task actually makes no sense--(bold)

        """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """Print "Bye rectangle..." when an object is destroyed."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Checks which of the two Rectangles is bigger.

        Args:
            rect_1: First rectangle to compare
            rect_2: Second rectangle to compare

        Returns:
            The bigger rectangle, or rect_1 if both are equal

        Raises:
            TypeError: When arguments are not of type 'Rectangle'
        """

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        return (rect_1 if rect_1.area() >= rect_2.area() else rect_2)

    @classmethod
    def square(cls, size=0):
        """Returns a new square.

        Args:
            size: Size of the square
        Returns:
            A square

        """
        return Rectangle(size, size)