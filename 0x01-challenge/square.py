#!/usr/bin/python3
"""
square class
"""


class square():
    """ Documentation """

    width = 0

    def __init__(self, *args, **kwargs):
        """ Documentation """
        for key, value in kwargs.items():
            if key == "width":
                setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.width

    def PermiterOfMySquare(self):
        """ Documentation """
        return (self.width * 4)

    def __str__(self):
        """ Documentation """
        return "{0}/{0}".format(self.width)


if __name__ == "__main__":

    s = square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
