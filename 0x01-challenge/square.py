#!/usr/bin/python3
"""
square class
"""


class Square():
    """Documentation : the square class"""

    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """Documentation: the init method"""

        if 'width' not in kwargs or 'height' not in kwargs:
            raise ValueError("Both width and height must be provided.")

        for key, value in kwargs.items():
            if key in kwargs:
                if not isinstance(value, (int, float)):
                    raise TypeError("{} must be a number".format(key))
                if value <= 0:
                    raise ValueError("{} must be a positive number"
                                     .format(key))
                setattr(self, key, value)

    def area_of_my_square(self):
        """Documentation: Area of the square"""
        return self.width * self.height

    def perimeter_of_my_square(self):
        """Documentation: the perimeter of the square"""
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """Documentation: the string representation of the square"""
        return "{0}/{1}".format(self.width, self.height)


if __name__ == "__main__":
    """entry point to this module"""

    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.perimeter_of_my_square())

    ss = Square(width=12)
    print(ss)
    print(ss.area_of_my_square())
    print(ss.perimeter_of_my_square())
