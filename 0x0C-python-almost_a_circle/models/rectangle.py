#!/usr/bin/python3
from models.base import Base


class Rectangle(Base):
    """Class Rectangle"""
    @property
    def width(self):
        """Property width"""
        return self.__width

    @width.setter
    def width(self, width):
        """setter"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width

    @property
    def height(self):
        """Property height"""
        return self.__height

    @height.setter
    def height(self, height):
        """setter"""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = height

    @property
    def x(self):
        """Property x"""
        return self.__x

    @x.setter
    def x(self, x):
        """setter"""
        if type(x) is not int:
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x

    @property
    def y(self):
        """Property y"""
        return self.__y

    @y.setter
    def y(self, y):
        """setter"""
        if type(y) is not int:
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y

    def area(self):
        """area"""
        return self.__width * self.__height

    def display(self):
        """Public method dispaly"""
        str_y = "\n" * self.y
        print(str_y, end="")
        for i in range(self.height):
            str_x = " " * self.x
            print(str_x, end="")
            str_width = "#" * self.width
            print(str_width)

    def __init__(self, width, height, x=0, y=0, id=None):
        """constructor"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        """str method"""
        return f"[Rectangle] ({self.id}) \
{self.__x}/{self.__y} - {self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """Public method update"""
        arg = {0: "id", 1: "width", 2: "height", 3: "x", 4: "y"}
        if args:
            if len(args) < 6:
                for i in range(len(args)):
                    setattr(self, arg[i], args[i])
        elif kwargs:
            for key in kwargs:
                setattr(self, key, kwargs[key])

    def to_dictionary(self):
        """return dictionary"""
        my_dict = {
            'x': self.x,
            'y': self.y,
            'id': self.id,
            'width': self.width,
            'height': self.height
        }
        return my_dict
