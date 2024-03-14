#!/usr/bin/python3
"""
square class
"""


class Square:
    """Documentation"""

    width = 0

    def __init__(self, width):
        """Documentation"""
        self.width = width

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
    s = Square(width=12)
    print(s)
    print(s.area_of_my_square())
    print(s.perimeter_of_my_square())
