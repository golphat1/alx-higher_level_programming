#!/usr/bin/python3
"""Module defines a Square class that inherits from Rectangle"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a square, which is a special rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes a Square instance

        Args:
            size (int): the size of the square
            x (int, optional): the x-coordinate of the square's position. Defaults to 0.
            y (int, optional): the y-coordinate of the square's position. Defaults to 0.
            id (int, optional): the ID of the square. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Returns the size of the square"""
        return self.width

    @size.setter
    def size(self, value):
        """Sets the size of the square"""
        self.width = value
        self.height = value

    def __str__(self):
        """Returns a string representation of the square"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """Updates the attributes of the square

        Args:
            *args: list of arguments
            **kwargs: dictionary of arguments
        """
        if args:
            attrs = ["id", "size", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, attrs[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of a square"""
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}


#!/usr/bin/python3
""" Define a Square class """

from models.rectangle import Rectangle


class Square(Rectangle):
    """ Class Square """

    def __init__(self, size, x=0, y=0, id=None):
        """ Initialize a new Square instance """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ Getter for size attribute """
        return self.width

    @size.setter
    def size(self, value):
        """ Setter for size attribute """
        self.width = value
        self.height = value

    def __str__(self):
        """ Return string representation of Square instance """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """ Update attributes of Square instance """
        if args:
            attrs = ["id", "size", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, attrs[i], arg)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ Return dictionary representation of Square instance """
        return {"id": self.id, "size": self.width, "x": self.x, "y": self.y}


class Square:
    def __init__(self, size, x=0, y=0, id=None):
        self.size = size
        self.x = x
        self.y = y
        if id is None:
            self.id = uuid.uuid4()
        else:
            self.id = id

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.size)

    def update(self, *args, **kwargs):
        if args:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                elif key == 'size':
                    self.size = value
                elif key == 'x':
                    self.x = value
                elif key == 'y':
                    self.y = value


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)

    def to_dictionary(self):
        return {'id': self.id, 'size': self.width, 'x': self.x, 'y': self.y}

