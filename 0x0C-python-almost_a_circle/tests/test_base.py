#!/usr/bin/python3
"""A set of unittests for the ``Base`` class"""
import unittest
import json
from models import base
from models.rectangle import Rectangle
from models.square import Square
Base = base.Base


class TestBase(unittest.TestCase):
    """A class to test the Base class"""
    def setUp(self):
        """setup method for tests"""
        Base._Base__nb_objects = 0

    def test_base_mod_doc(self):
        """test for doc in the base module"""
        self.assertTrue(len(base.__doc__) > 1)

    def test_Base_class_doc(self):
        """test for doc in the Base class"""
        self.assertTrue(len(Base.__doc__) > 1)

    def test_Base_method_doc(self):
        """test for doc in the Base class methods"""
        self.assertTrue(len(Base.__init__.__doc__) > 1)
        self.assertTrue(len(Base.to_json_string.__doc__) > 1)
        self.assertTrue(len(Base.save_to_file.__doc__) > 1)
        self.assertTrue(len(Base.from_json_string.__doc__) > 1)
        self.assertTrue(len(Base.create.__doc__) > 1)
        self.assertTrue(len(Base.load_from_file.__doc__) > 1)
        self.assertTrue(len(Base.save_to_file_csv.__doc__) > 1)
        self.assertTrue(len(Base.load_from_file_csv.__doc__) > 1)
        self.assertTrue(len(Base.draw.__doc__) > 1)

    def test_Base_attribute__no_objects(self):
        """test for the existence of __nb_objects in Base class"""
        self.assertTrue("_Base__nb_objects" in Base.__dict__)

    def test_Base_instances(self):
        """test the value of id when instance is made"""
        self.b1 = Base()  # with None
        self.assertEqual(self.b1.id, 1)
        self.b2 = Base()  # with None to assert increment
        self.assertEqual(self.b2.id, 2)
        self.b3 = Base(12)  # with positive number
        self.assertEqual(self.b3.id, 12)
        self.b4 = Base()  # with None after id 12 was assigned
        self.assertEqual(self.b4.id, 3)
        self.b5 = Base(0)  # with zero
        self.assertEqual(self.b5.id, 0)
        self.b5 = Base(-1)  # with negative number
        self.assertEqual(self.b5.id, -1)

    def test_to_json_string(self):
        """test the to_json_string method"""
        sample1 = []
        sample2 = None
        self.assertTrue(Base.to_json_string(sample1) == "[]")
        self.assertTrue(Base.to_json_string(sample2) == "[]")
        with self.assertRaises(TypeError):
            Base.to_json_string("wrong type")
        sample1 = Rectangle(2, 3)
        self.assertEqual(type(sample1), Rectangle)
        sample1_dict = sample1.to_dictionary()
        self.assertTrue(type(sample1_dict) is dict)
        sorted1 = dict(sorted(sample1_dict.items()))
        expected1 = '[{"height": 3, "id": 1, "width": 2, "x": 0, "y": 0}]'
        self.assertEqual(Base.to_json_string([sorted1]), expected1)
        self.assertTrue(type(expected1) is str)
        sample1 = Square(3)
        self.assertEqual(type(sample1), Square)
        sample1_dict = sample1.to_dictionary()
        self.assertTrue(type(sample1_dict) is dict)
        sorted2 = dict(sorted(sample1_dict.items()))
        expected2 = '[{"id": 2, "size": 3, "x": 0, "y": 0}]'
        self.assertEqual(Base.to_json_string([sorted2]), expected2)
        expected = '[{"height": 3, "id": 1, "width": 2, "x": 0, "y": 0}'
        expected += ', ' + '{"id": 2, "size": 3, "x": 0, "y": 0}]'
        self.assertEqual(Base.to_json_string([sorted1, sorted2]), expected)
        self.assertTrue(type(expected) is str)

    def test_save_to_file(self):
        """test the save_to_file class method"""
        with self.assertRaises(AttributeError):
            Rectangle.save_to_file(["wrong"])

        r1 = Rectangle(4, 5, 0, 0, 3)
        wrong = "wrong type"

        with self.assertRaises(AttributeError):
            Rectangle.save_to_file([r1, wrong])

        Rectangle.save_to_file([r1])
        with open("Rectangle.json", 'r') as f:
            content = f.read()
        expected = [{"x": 0, "y": 0, "id": 3, "height": 5, "width": 4}]
        self.assertEqual(json.loads(content), expected)

        Rectangle.save_to_file(None)
        with open("Rectangle.json", 'r') as f:
            content = f.read()
        self.assertEqual(json.loads(content), [])

        Rectangle.save_to_file([])
        with open("Rectangle.json", 'r') as f:
            content = f.read()
        self.assertEqual(json.loads(content), [])

    def test_from_json_string(self):
        """test the from_json_string static method"""
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        list_input2 = []
        list_input3 = None
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        json_list_input2 = Rectangle.to_json_string(list_input2)
        list_output2 = Rectangle.from_json_string(json_list_input2)
        json_list_input3 = Rectangle.to_json_string(list_input3)
        list_output3 = Rectangle.from_json_string(json_list_input3)
        self.assertEqual(list_output3, [])
        self.assertEqual(list_output2, [])
        self.assertTrue(type(list_output), list)
        self.assertTrue(type(json_list_input), str)
        self.assertTrue(type(list_output), list)
        self.assertEqual(list_output, list_input)

    def test_create(self):
        """test the create class method used to create
           an instance from a dictionary
        """
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(str(r1), "[Rectangle] (1) 1/0 - 3/5")
        self.assertEqual(str(r2), "[Rectangle] (1) 1/0 - 3/5")
        self.assertFalse(r1 is r2)
        self.assertFalse(r1 == r2)

        s1 = Square(3)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual(str(s1), "[Square] (3) 0/0 - 3")
        self.assertEqual(str(s2), "[Square] (3) 0/0 - 3")
        self.assertFalse(s1 is s2)
        self.assertFalse(s1 == s2)

    def test_load_from_file(self):
        """test the load_from_file class method
           It should returns a list of instances.
        """
        pass

    def test_save_to_file_cvs(self):
        """test the save_to_file_cvs class method"""
        pass

    def test_load_from_file(self):
        """test the load_from_file class method
           It should returns a list of instances.
        """
        pass


if __name__ == "__main__":
    unittest.main()
