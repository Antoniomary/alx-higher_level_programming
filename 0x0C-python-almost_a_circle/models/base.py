#!/usr/bin/python3
"""
    A module for the class named Base
"""
import json
import csv
import turtle


class Base:
    """A class which serves as base of other classes"""
    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or not list_dictionaries:
            return "[]"

        err_msg = "list_dictionaries must be a list of dictionaries"
        if type(list_dictionaries) is not list:
            raise TypeError(err_msg)

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        filename = cls.__name__ + ".json"
        with open(filename, 'w') as f:
            objs_to_dicts = []
            if list_objs:
                objs_to_dicts = [each.to_dictionary() for each in list_objs]
            f.write(Base.to_json_string(objs_to_dicts))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if not json_string:
            return []
        if type(json_string) is not str:
            err_msg = "json_string must be a string of list of dictionaries"
            raise TypeError(err_msg)
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        obj_class = cls.__name__
        if obj_class == "Rectangle":
            obj = cls(1, 1)
        elif obj_class == "Square":
            obj = cls(1)

        obj.update(**dictionary)
        return obj

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r') as file:
                instances = []
                for line in file:
                    obj = cls.from_json_string(line)
                    for each in obj:
                        instances.append(cls.create(**each))
                return instances
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """writes the csc string representation of list_objs to a file"""
        filename = cls.__name__ + ".csv"
        with open(filename, 'w') as f:
            f_writer = csv.writer(f)
            if list_objs:
                instance = []
                for each in list_objs:
                    instance.append(each.to_dictionary())
                    f_writer.writerow(instance)
                    instance.clear()
            else:
                f_writer.writerow([])

    @classmethod
    def load_from_file_csv(cls):
        """returns a list of instances"""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, 'r') as f:
                f_reader = csv.reader(f)
                f_data = list(f_reader)
                instances = []
                for obj in f_data:
                    obj_to_dict = {}
                    obj = obj[0].split()
                    parsed_data = [piece.strip("{'': ,}") for piece in obj]
                    obj_to_dict[parsed_data[0]] = int(parsed_data[1])
                    obj_to_dict[parsed_data[2]] = int(parsed_data[3])
                    if cls.__name__ == "Rectangle":
                        obj_to_dict[parsed_data[4]] = int(parsed_data[5])
                    obj_to_dict[parsed_data[-4]] = int(parsed_data[-3])
                    obj_to_dict[parsed_data[-2]] = int(parsed_data[-1])
                    instances.append(cls.create(**obj_to_dict))
                return instances
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """opens a window and draws all the Rectangles and Squares"""
        if list_rectangles is None and list_squares is None:
            return

        rect_err = "list_rectangles must be a list of Rectangle objects only"
        square_err = "list_squares must be a list of Square ibjects only"
        for each in list_rectangles:
            if type(each).__name__ != "Rectangle":
                raise TypeError(rect_err)

        for each in list_squares:
            if type(each).__name__ != "Square":
                raise TypeError(square_err)

        shape = turtle.Turtle()
        shape.hideturtle()
        shape.speed(1)

        shape.color("blue", "cyan")
        for rect in list_rectangles:
            shape.penup()
            shape.goto(rect.x, rect.y)
            shape.pendown()
            shape.begin_fill()
            for i in range(2):
                shape.forward(rect.width)
                shape.left(90)
                shape.forward(rect.height)
                shape.left(90)
            shape.end_fill()

        shape.color("red", "cyan")
        for square in list_squares:
            shape.penup()
            shape.goto(square.x, square.y)
            shape.pendown()
            shape.begin_fill()
            for i in range(4):
                shape.forward(square.size)
                shape.left(90)
            shape.end_fill()

        turtle.done()
