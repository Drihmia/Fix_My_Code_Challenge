#!/usr/bin/python3
"""
square class
"""


class Square():
    """Documentation"""

    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """Documentation"""
        for key, value in kwargs.items():
            if key in kwargs:
                if not isinstance(kwargs[key], (int, float)):
                    raise TypeError("{} must be a number".format(key))
                if kwargs[key] < 0:
                    raise ValueError("{} must be a positive number"
                                     .format(key))
                setattr(self, key, value)

    def area_of_my_square(self):
        """Area of the square"""
        return self.width * self.height

    def perimeter_of_my_square(self):
        """Documentation"""
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """Documentation"""
        return "{0}/{1}".format(self.width, self.height)


if __name__ == "__main__":
    """entry point to this module"""
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.perimeter_of_my_square())
