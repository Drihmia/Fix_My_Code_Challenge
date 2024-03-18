#!/usr/bin/python3
"""square class"""


class Square():
    """Documentation : the square class"""
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """Documentation: the init method"""
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """Documentation: Area of the square"""
        area = self.width * self.height
        return area

    def perimeter_of_my_square(self):
        """Documentation: the perimeter of the square"""
        perimeter = (self.width * 2) + (self.height * 2)
        return perimeter

    def __str__(self):
        """Documentation: the string representation of the square"""
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    """entry point to this module"""
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.perimeter_of_my_square())
