#!/usr/bin/python3
"""
Rectangle Module
"""
from models.base import Base


class Rectangle(Base):
    """
    Rectangle Class that inherits from Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor method for Rectangle"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter method for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for width"""
        self.__width = value

    @property
    def height(self):
        """Getter method for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for height"""
        self.__height = value

    @property
    def x(self):
        """Getter method for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter method for x"""
        self.__x = value

    @property
    def y(self):
        """Getter method for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter method for y"""
        self.__y = value


"""
Module for the Rectangle class
"""


class Rectangle:
    """
    Class representing a rectangle
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a new Rectangle instance

        Args:
            width (int): the width of the rectangle
            height (int): the height of the rectangle
            x (int): the x-coordinate of the top-left corner of the rectangle
            y (int): the y-coordinate of the top-left corner of the rectangle
            id (int): the unique identifier for the rectangle (default: None)
        """
        self.id = id
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Getter method for width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for width

        Args:
            value (int): the value to set for width
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        Getter method for height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method for height

        Args:
            value (int): the value to set for height
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """
        Getter method for x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Setter method for x

        Args:
            value (int): the value to set for x
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """
        Getter method for y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Setter method for y

        Args:
            value (int): the value to set for y
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value


"""
This module defines a Rectangle class
"""


class Rectangle:
    """
    This class defines a rectangle by its width, height, x and y positions,
    and an optional id
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a new Rectangle instance
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        if id is None:
            self.id = Rectangle.__nb_instances
            Rectangle.__nb_instances += 1
        else:
            self.id = id

    def __str__(self):
        """
        Returns a string representation of a Rectangle instance
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, 
                self.y, self.width, self.height)

    def __repr__(self):
        """
        Returns a string representation of a Rectangle instance that can be
        used to recreate the instance
        """
        return "Rectangle({}, {}, {}, {}, {})".format(self.width, self.height, 
                self.x, self.y, self.id)

    def area(self):
        """
        Returns the area value of the Rectangle instance
        """
        return self.width * self.height

    # rest of the class implementation...


"""Module for Rectangle class"""


class Rectangle:
    """Class that defines a rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor method"""

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.id = id

    def area(self):
        """Method that returns the area of the rectangle"""

        return self.width * self.height

    def perimeter(self):
        """Method that returns the perimeter of the rectangle"""

        return 2 * (self.width + self.height)

    def __str__(self):
        """String representation of the rectangle"""

        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    def display(self):
        """Method that prints the rectangle to stdout"""

        for i in range(self.height):
            print("#" * self.width)

class Rectangle(Base):
    """Class Rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, 
               self.x, self.y, self.width, self.height)


class Rectangle:
    def __init__(self, width, height, x=0, y=0):
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def display(self):
        for i in range(self.y):
            print()
        for i in range(self.height):
            for j in range(self.x):
                print(" ", end="")
            for j in range(self.width):
                print("#", end="")
            print()

class Rectangle:
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        if id is None:
            self.id = uuid.uuid4()
        else:
            self.id = id

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    def update(self, *args):
        if len(args) > 0:
            self.id = args[0]
        if len(args) > 1:
            self.width = args[1]
        if len(args) > 2:
            self.height = args[2]
        if len(args) > 3:
            self.x = args[3]
        if len(args) > 4:
            self.y = args[4]

class Rectangle:
    """ Rectangle Class """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Constructor Method """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        if id is None:
            Rectangle.count += 1
            self.id = Rectangle.count
        else:
            self.id = id

    def update(self, *args, **kwargs):
        """ Update Method """
        if args is not None and len(args) > 0:
            attrs = ["id", "width", "height", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, attrs[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        """ String Representation Method """
        return "[Rectangle] ({}) {}/{} - {}/{}"
    .format(self.id, self.x, self.y, self.width, self.height)

    def area(self):
        """ Area Method """
        return self.width * self.height

    def display(self):
        """ Display Method """
        print("\n" * self.y, end="")
        for i in range(self.height):
            print(" " * self.x, end="")
            print("#" * self.width)

    def __repr__(self):
        """ Representation Method """
        return "Rectangle({}, {}, {}, {}, {})"
    .format(self.width, self.height, self.x, self.y, self.id)

    def __del__(self):
        """ Destructor Method """
        Rectangle.count -= 1
        print("Bye rectangle...")

    count = 0


class Rectangle(Base):
    """Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize rectangle"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        """Return string representation of rectangle"""
        return "[Rectangle] ({}) {}/{} - {}/{}"
    .format(self.id,self.x, self.y, self.width, self.height)

    def area(self):
        """Return the area of the rectangle"""
        return self.width * self.height

    def display(self):
        """Print a visual representation of the rectangle"""
        print("\n" * self.y + 
                (" " * self.x + "#" * self.width + "\n") * self.height, end="")

    def update(self, *args, **kwargs):
        """Update the rectangle"""
        attrs = ["id", "width", "height", "x", "y"]
        if args:
            for i, arg in enumerate(args):
                setattr(self, attrs[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return dictionary representation of rectangle"""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }


class Square:
    def __init__(self, id, size, x=0, y=0):
        self.id = id
        self.size = size
        self.x = x
        self.y = y

    def __str__(self):
        return "Square({}, {}, {}, {})"
    .format(self.id, self.size, self.x, self.y)

    def area(self):
        return self.size ** 2

    def perimeter(self):
        return self.size * 4

    def to_dictionary(self):
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }

