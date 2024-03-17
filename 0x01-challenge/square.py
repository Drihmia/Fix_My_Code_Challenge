#!/usr/bin/python3
"""
square class
"""


class Square:
    """Documentation"""

    width = 0

    def __init__(self, *args, **kwargs):
        """Documentation"""
        if "width" in kwargs:
            if not isinstance(kwargs["width"], (int, float)):
                raise TypeError("Width must be a number")
            if kwargs["width"] < 0:
                raise ValueError("Width must be a positive number")
            self.width = kwargs["width"]

    def area_of_my_square(self):
        """Area of the square"""
        return self.width * self.width

    def perimeter_of_my_square(self):
        """Documentation"""
        return self.width * 4

    def __str__(self):
        """Documentation"""
        return "{0}/{0}".format(self.width)


if __name__ == "__main__":
    """entry point to this module"""
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.perimeter_of_my_square())
