#!/usr/bin/python3
"""
square class
"""


class square():
    """ Documentation """

    width = 0

    def __init__(self, width=0):
        """ Documentation """
        self.__width = width

    @property
    def width(self):
        """ Documentation """
        return self.__width

    @width.setter
    def width(self, value):
        if value < 0:
            raise ValueError("width must be a positive number")
        if type(value) not in ("int", "float"):
            raise TypeError("with must be a number")
        setattr(self, str(self.__width), int(value))

    def area_of_my_square(self):
        """ Area of the square """
        return self.__width * self.__width

    def PermiterOfMySquare(self):
        """ Documentation """
        return (self.__width * 4)

    def __str__(self):
        """ Documentation """
        return "{0}/{0}".format(self.__width)


if __name__ == "__main__":

    s = square(width=12)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
