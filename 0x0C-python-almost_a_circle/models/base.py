#!/usr/bin/python3
"""Module defining Base class"""
import json
import csv
import turtle


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
        """
        Returns the JSON string representation
        of a list of dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation
        of a list of objects to a file
        """
        filename = cls.__name__ + ".json"
        list_dicts = []
        if list_objs is not None:
            list_dicts = [obj.to_dictionary() for obj in list_objs]
        with open(filename, mode="w", encoding="utf-8") as myFile:
            myFile.write(cls.to_json_string(list_dicts))

    @staticmethod
def from_json_string(json_string):
    """
    Static method that returns the list of the
    JSON string representation json_string
    """
    if json_string is None or json_string == '':
        return []
    else:
        return json.loads(json_string)

    @classmethod
def create(cls, **dictionary):
    """
    Class method that returns an instance with all attributes already set
    """
    if cls.__name__ == "Rectangle":
        new = cls(1, 1)
    elif cls.__name__ == "Square":
        new = cls(1)
    else:
        new = cls()
    new.update(**dictionary)
    return new

    @classmethod
    def load_from_file(cls):
        """
        Class method that returns
        a list of instances
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, mode="r", encoding="utf-8") as f:
                json_list = cls.from_json_string(f.read())
                return [cls.create(**d) for d in json_list]
        except FileNotFoundError:
            return []

    @classmethod
    def load_from_file_csv(cls):
        """
        Class method that returns a
        list of instances
        """
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
        """
        Class method that writes the CSV
        string representation of list_objs to a file
        """
        filename = cls.__name__ + ".csv"
        if list_objs is None:
            csv_list = []
        else:
            csv_list = [[getattr(obj, attr) for attr in
                         ["id", "size", "height", "width", "x", "y"][len

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        Draw Rectangles and Squares using the turtle module.
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
