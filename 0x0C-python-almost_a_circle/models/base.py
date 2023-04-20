#!/usr/bin/python3
"""Module defining Base class"""

class Base:
    """Base class for all objects in this project"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new instance of the Base class"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects


import json

class Base:
    """ Base class """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Constructor method """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returns the JSON string representation of a list of dictionaries """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Writes the JSON string representation of a list of objects to a file """
        filename = cls.__name__ + ".json"
        list_dicts = []
        if list_objs is not None:
            list_dicts = [obj.to_dictionary() for obj in list_objs]
        with open(filename, mode="w", encoding="utf-8") as myFile:
            myFile.write(cls.to_json_string(list_dicts))


"""base module"""


import json


class Base:
    """Base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """initialization method"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of a list of dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        with open(filename, mode="w") as file:
            json_str = cls.to_json_string([obj.to_dictionary() for obj in list_objs])
            file.write(json_str)


""" Module defining the Base class. """
import json


class Base:
    """ Class with a private class attribute __nb_objects. """

    __nb_objects = 0

    def __init__(self, id=None):
        """ Constructor method. """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Static method that returns the JSON string representation of a list of dictionaries. """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """ Static method that returns the list of the JSON string representation json_string. """
        if json_string is None or json_string == '':
            return []
        else:
            return json.loads(json_string)



class Base:
    """ This class will be the “base” of all other classes in this project """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Constructor of the class """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Static method that returns the JSON string representation
        of list_dictionaries """
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Class method that writes the JSON string representation of
        list_objs to a file """
        filename = cls.__name__ + ".json"
        if list_objs is None:
            json_list = []
        else:
            json_list = [obj.to_dictionary() for obj in list_objs]
        with open(filename, mode="w", encoding="utf-8") as f:
            f.write(cls.to_json_string(json_list))

    @staticmethod
    def from_json_string(json_string):
        """ Static method that returns the list of the JSON string
        representation json_string """
        if json_string is None or not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Class method that returns an instance with all attributes
        already set """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = cls()
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ Class method that returns a list of instances """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, mode="r", encoding="utf-8") as f:
                json_list = cls.from_json_string(f.read())
                return [cls.create(**d) for d in json_list]
        except FileNotFoundError:
            return []

    @classmethod
    def load_from_file_csv(cls):
        """ Class method that returns a list of instances """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, mode="r", encoding="utf-8") as f:
                csv_list = csv.reader(f)
                header = next(csv_list)
                attributes = [attr.strip() for attr in header]
                obj_list = []
                for row in csv_list:
                    values = [int(value) for value in row]
                    obj_dict = dict(zip(attributes, values))
                    obj_list.append(cls.create(**obj_dict))
                return obj_list
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ Class method that writes the CSV string representation of
        list_objs to a file """
        filename = cls.__name__ + ".csv"
        if list_objs is None:
            csv_list = []
        else:
            csv_list = [[getattr(obj, attr) for attr in
                         ["id", "size", "height", "width", "x", "y"][:len


#!/usr/bin/python3
"""base.py module"""

import json


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base instance"""
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of a list of dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save a list of instances to a JSON file"""
        filename = cls.__name__ + ".json"
        with open(filename, mode="w", encoding="utf-8") as f:
            if list_objs is None:
                f.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                f.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Return the list of instances represented by a JSON string"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return a new instance with the attributes set from a dictionary"""
        if cls.__name__ == "Rectangle":
            obj = cls(1, 1)
        elif cls.__name__ == "Square":
            obj = cls(1)
        else:
            obj = None
        obj.update(**dictionary)
        return obj

    @classmethod
    def load_from_file(cls):
        """Return a list of instances from a JSON file"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, mode="r", encoding="utf-8") as f:
                list_dicts = cls.from_json_string(f.read())
                return [cls.create(**d) for d in list_dicts]
        except FileNotFoundError:
            return []


import csv

class Base:
    """The base class for all shapes"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new shape instance"""

        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes a list of objects to a CSV file"""

        filename = cls.__name__ + ".csv"
        with open(filename, mode="w", newline="") as file:
            writer = csv.writer(file)
            for obj in list_objs:
                if type(obj) == Rectangle:
                    writer.writerow([obj.id, obj.width, obj.height, obj.x, obj.y])
                elif type(obj) == Square:
                    writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes a list of objects from a CSV file"""

        filename = cls.__name__ + ".csv"
        objs = []
        try:
            with open(filename, mode="r") as file:
                reader = csv.reader(file)
                for row in reader:
                    if cls.__name__ == "Rectangle":
                        obj = cls(int(row[1]), int(row[2]), int(row[3]), int(row[4]), int(row[0]))
                    elif cls.__name__ == "Square":
                        obj = cls(int(row[1]), int(row[2]), int(row[3]), int(row[0]))
                    objs.append(obj)
        except FileNotFoundError:
            pass
        return objs



@staticmethod
    def draw(list_rectangles, list_squares):
        """Draw Rectangles and Squares using the turtle module.
        Args:
            list_rectangles (list): A list of Rectangle objects to draw.
            list_squares (list): A list of Square objects to draw.
        """
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#ffffff")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#b5e3d8")
        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for i in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()
