#!/usr/bin/python3
"""A set of unittests for the ``Square`` class"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models import square
Square = square.Square


class TestSquare(unittest.TestCase):
    """A class to test the Square class"""
    def setUp(self):
        """makes instances for each test case"""
        Base._Base__nb_objects = 0
        self.r1 = Square(2)
        self.r2 = Square(2, 2)
        self.r3 = Square(3, 1, 3, 12)
        self.r4 = Square(2, 1, 1, -1)
        self.r5 = Square(3, 2, 2, 0)
        self.r6 = Square(3, 0, 0)

    def test_square_mod_doc(self):
        """test for doc in the square module"""
        self.assertTrue(len(square.__doc__) > 1)

    def test_Square_class_doc(self):
        """test for doc in the Square class"""
        self.assertTrue(len(Square.__doc__) > 1)

    def test_Square_method_doc(self):
        """test for doc in the Square class methods"""
        self.assertTrue(len(Square.__init__.__doc__) > 1)
        self.assertTrue(len(Square.area.__doc__) > 1)
        self.assertTrue(len(Square.display.__doc__) > 1)
        self.assertTrue(len(Square.__str__.__doc__) > 1)
        self.assertTrue(len(Square.update.__doc__) > 1)
        self.assertTrue(len(Square.width.__doc__) > 1)
        self.assertTrue(len(Square.width.fset.__doc__) > 1)
        self.assertTrue(len(Square.height.__doc__) > 1)
        self.assertTrue(len(Square.height.fset.__doc__) > 1)
        self.assertTrue(len(Square.x.__doc__) > 1)
        self.assertTrue(len(Square.x.fset.__doc__) > 1)
        self.assertTrue(len(Square.y.__doc__) > 1)
        self.assertTrue(len(Square.y.fset.__doc__) > 1)
        self.assertTrue(len(Square.to_dictionary.__doc__) > 1)

    def test_invalid_number_of_arguments(self):
        """test the number of arguments passed at instantiation"""
        with self.assertRaises(TypeError):
            r1 = Square()

    def test_Square_inheritance_from_Rectangle(self):
        """tests whether Square is a subclass of Rectangle"""
        self.assertTrue(issubclass(Square, Rectangle))

    def test_Square_attributes(self):
        """tests for the attributes in Square class"""
        self.assertFalse("width" in Square.__dict__)
        self.assertFalse("height" in Square.__dict__)
        self.assertFalse("x" in Square.__dict__)
        self.assertFalse("y" in Square.__dict__)
        self.assertFalse("id" in Square.__dict__)
        self.assertTrue("_Rectangle__width" in self.r1.__dict__)
        self.assertTrue("_Rectangle__height" in self.r1.__dict__)
        self.assertTrue("_Rectangle__x" in self.r1.__dict__)
        self.assertTrue("_Rectangle__y" in self.r1.__dict__)
        self.assertTrue("id" in self.r1.__dict__)

    def test_Square_id(self):
        """test the id values"""
        self.assertTrue(self.r1.id == 1)
        self.assertTrue(self.r2.id == 2)
        self.assertTrue(self.r3.id == 12)
        self.assertTrue(self.r4.id == -1)
        self.assertTrue(self.r5.id == 0)
        self.assertTrue(self.r6.id == 3)

    def test_values(self):
        """test the values in the instance attributes"""
        self.assertEqual(self.r1.size, 2)
        self.assertEqual(self.r1.x, 0)
        self.assertEqual(self.r1.y, 0)
        self.r1.width = 3
        self.r1.x = 3
        self.r1.y = 4
        self.assertEqual(self.r1.width, 3)
        self.assertEqual(self.r1.x, 3)
        self.assertEqual(self.r1.y, 4)

    def test_size_for_validation(self):
        """test whether size gets the proper type or value"""
        r1 = Square(10)
        self.assertTrue(type(r1.size) is int)
        with self.assertRaises(TypeError, msg="width must be an integer"):
            r2 = Square("10")
        with self.assertRaises(ValueError, msg="width must be > 0"):
            r2 = Square(0)
        with self.assertRaises(TypeError, msg="width must be an integer"):
            r1.size = 10.0
        with self.assertRaises(ValueError, msg="width must be > 0"):
            r1.size = -1

    def test_x_y_for_validation(self):
        """test whether x and y get the proper type or value"""
        r1 = Square(10, 2, 1, 1)
        self.assertTrue(type(r1.x) is int and type(r1.y) is int)
        with self.assertRaises(TypeError, msg="x must be an integer"):
            r2 = Square(10, "wrong", 2)
        with self.assertRaises(ValueError, msg="x must be >= 0"):
            r2 = Square(10, -1, 2)
        with self.assertRaises(TypeError, msg="y must be an integer"):
            r2 = Square(10, 2, "wrong")
        with self.assertRaises(ValueError, msg="y must be >= 0"):
            r2 = Square(10, 2, -1)
        with self.assertRaises(TypeError, msg="x must be an integer"):
            r1.x = 10.0
        with self.assertRaises(ValueError, msg="x must be >= 0"):
            r1.x = -1
        with self.assertRaises(TypeError, msg="y must be an integer"):
            r1.y = 10.0
        with self.assertRaises(ValueError, msg="y must be >= 0"):
            r1.y = -1

    def test_area(self):
        """test the area method"""
        self.assertEqual(self.r1.area(), 4)
        self.assertEqual(self.r3.area(), 9)

    def test_display(self):
        """test the dimension printed for a rectangle"""
        r1 = Square(2)
        self.assertEqual(r1.display(), print("##\n##"))
        r2 = Square(2, 2, 1, 2)
        self.assertEqual(r2.display(), print("\n  ##\n  ##"))

    def test___str___override(self):
        """test the string representation of an instance"""
        r1 = Square(4, 2, 1, 12)
        self.assertEqual(str(r1), "[Square] (12) 2/1 - 4")

    def test_update_arg(self):
        """test the update method to change instance values"""
        r1 = Square(5)
        self.assertEqual(str(r1), "[Square] (4) 0/0 - 5")
        r1.update(10)
        self.assertEqual(str(r1), "[Square] (10) 0/0 - 5")
        r1.update(89, 2)
        self.assertEqual(str(r1), "[Square] (89) 0/0 - 2")
        r1.update(89, 2, 3)
        self.assertEqual(str(r1), "[Square] (89) 3/0 - 2")
        r1.update(89, 2, 3, 4)
        self.assertEqual(str(r1), "[Square] (89) 3/4 - 2")

    def test_update_kwarg(self):
        """test the update method to change instance values"""
        r1 = Square(10, 10, 10, 10)
        self.assertEqual(str(r1), "[Square] (10) 10/10 - 10")
        r1.update(size=1)
        self.assertEqual(str(r1), "[Square] (10) 10/10 - 1")
        r1.update(size=1, x=2)
        self.assertEqual(str(r1), "[Square] (10) 2/10 - 1")
        r1.update(y=1, size=2, x=3, id=89)
        self.assertEqual(str(r1), "[Square] (89) 3/1 - 2")
        r1.update(x=1, size=2, y=3)
        self.assertEqual(str(r1), "[Square] (89) 1/3 - 2")

    def test_to_dictionary(self):
        """test conversion of an instance to a dictionary"""
        expected = {'id': 12, 'size': 3, 'x': 1, 'y': 3}
        r3_dict = self.r3.to_dictionary()
        self.assertTrue(type(r3_dict) is dict)
        self.assertEqual(dict(sorted(r3_dict.items())), expected)
        self.r1.update(**r3_dict)
        self.assertEqual(str(self.r3), str(self.r1))
        self.assertFalse(self.r3 == self.r1)
