#!/usr/bin/python3
"""A set of unittests for the ``Rectangle`` class"""
import unittest
from models.base import Base
from models import rectangle
Rectangle = rectangle.Rectangle


class TestRectangle(unittest.TestCase):
    """A class to test the Rectangle class"""
    def setUp(self):
        """makes instances for each test case"""
        Base._Base__nb_objects = 0
        self.r1 = Rectangle(10, 2)
        self.r2 = Rectangle(2, 10)
        self.r3 = Rectangle(10, 2, 0, 0, 12)
        self.r4 = Rectangle(5, 3, 0, 0, -1)
        self.r5 = Rectangle(3, 5, 0, 0, 0)
        self.r6 = Rectangle(7, 4)

    def test_rectangle_mod_doc(self):
        """test for doc in the rectangle module"""
        self.assertTrue(len(rectangle.__doc__) > 1)

    def test_Rectangle_class_doc(self):
        """test for doc in the Rectangle class"""
        self.assertTrue(len(Rectangle.__doc__) > 1)

    def test_Rectangle_method_doc(self):
        """test for doc in the Rectangle class methods"""
        self.assertTrue(len(Rectangle.__init__.__doc__) > 1)
        self.assertTrue(len(Rectangle.area.__doc__) > 1)
        self.assertTrue(len(Rectangle.display.__doc__) > 1)
        self.assertTrue(len(Rectangle.__str__.__doc__) > 1)
        self.assertTrue(len(Rectangle.update.__doc__) > 1)
        self.assertTrue(len(Rectangle.width.__doc__) > 1)
        self.assertTrue(len(Rectangle.width.fset.__doc__) > 1)
        self.assertTrue(len(Rectangle.height.__doc__) > 1)
        self.assertTrue(len(Rectangle.height.fset.__doc__) > 1)
        self.assertTrue(len(Rectangle.x.__doc__) > 1)
        self.assertTrue(len(Rectangle.x.fset.__doc__) > 1)
        self.assertTrue(len(Rectangle.y.__doc__) > 1)
        self.assertTrue(len(Rectangle.y.fset.__doc__) > 1)
        self.assertTrue(len(Rectangle.to_dictionary.__doc__) > 1)

    def test_Rectangle_inheritance_from_Base(self):
        """tests whether Rectangle is a subclass of Base"""
        self.assertTrue(issubclass(Rectangle, Base))

    def test_Rectangle_attributes(self):
        """tests for the attributes in Rectangle class"""
        self.assertTrue("width" in Rectangle.__dict__)
        self.assertTrue("height" in Rectangle.__dict__)
        self.assertTrue("x" in Rectangle.__dict__)
        self.assertTrue("y" in Rectangle.__dict__)
        self.assertFalse("id" in Rectangle.__dict__)
        self.assertTrue("id" in self.r1.__dict__)

    def test_Rectangle_id(self):
        """test the id values"""
        self.assertTrue(self.r1.id == 1)
        self.assertTrue(self.r2.id == 2)
        self.assertTrue(self.r3.id == 12)
        self.assertTrue(self.r4.id == -1)
        self.assertTrue(self.r5.id == 0)
        self.assertTrue(self.r6.id == 3)

    def test_values(self):
        """test the values in the instance attributes"""
        self.assertEqual(self.r1.width, 10)
        self.assertEqual(self.r1.height, 2)
        self.assertEqual(self.r1.x, 0)
        self.assertEqual(self.r1.y, 0)
        self.r1.width = 2
        self.r1.height = 10
        self.r1.x = 3
        self.r1.y = 4
        self.assertEqual(self.r1.width, 2)
        self.assertEqual(self.r1.height, 10)
        self.assertEqual(self.r1.x, 3)
        self.assertEqual(self.r1.y, 4)

    def test_width_for_validation(self):
        """test whether width gets the proper type or value"""
        r1 = Rectangle(10, 2)
        self.assertTrue(type(r1.width) is int)
        with self.assertRaises(TypeError, msg="width must be an integer"):
            r2 = Rectangle("10", 2)
        with self.assertRaises(ValueError, msg="width must be > 0"):
            r2 = Rectangle(0, 2)
        with self.assertRaises(TypeError, msg="width must be an integer"):
            r1.width = 10.0
        with self.assertRaises(ValueError, msg="width must be > 0"):
            r1.width = -1

    def test_height_for_validation(self):
        """test whether height gets the proper type or value"""
        r1 = Rectangle(10, 2)
        self.assertTrue(type(r1.height) is int)
        with self.assertRaises(TypeError, msg="height must be an integer"):
            r2 = Rectangle(10, '2')
        with self.assertRaises(ValueError, msg="height must be > 0"):
            r2 = Rectangle(10, 0)
        with self.assertRaises(TypeError, msg="height must be an integer"):
            r1.height = 10.0
        with self.assertRaises(ValueError, msg="height must be > 0"):
            r1.height = -1

    def test_x_y_for_validation(self):
        """test whether x and y get the proper type or value"""
        r1 = Rectangle(10, 2, 1, 1)
        self.assertTrue(type(r1.x) is int and type(r1.y) is int)
        with self.assertRaises(TypeError, msg="x must be an integer"):
            r2 = Rectangle(10, 2, "wrong", 1)
        with self.assertRaises(ValueError, msg="x must be >= 0"):
            r2 = Rectangle(10, 2, -1, 1)
        with self.assertRaises(TypeError, msg="y must be an integer"):
            r2 = Rectangle(10, 2, 1, "wrong")
        with self.assertRaises(ValueError, msg="y must be >= 0"):
            r2 = Rectangle(10, 2, 1, -1)
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
        self.assertEqual(self.r1.area(), 20)
        self.assertEqual(self.r4.area(), 15)
        self.assertEqual(self.r6.area(), 28)

    def test_display(self):
        """test the dimension printed for a rectangle"""
        r1 = Rectangle(2, 3)
        self.assertEqual(r1.display(), print("##\n##\n##"))
        r2 = Rectangle(2, 3, 2, 2)
        self.assertEqual(r2.display(), print("\n\n  ##\n  ##\n  ##"))

    def test___str___override(self):
        """test the string representation of an instance"""
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r1), "[Rectangle] (12) 2/1 - 4/6")

    def test_update_arg(self):
        """test the update method to change instance values"""
        r1 = Rectangle(10, 10, 10, 10)
        self.assertEqual(str(r1), "[Rectangle] (4) 10/10 - 10/10")
        r1.update(89)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 10/10")
        r1.update(89, 2)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 2/10")
        r1.update(89, 2, 3)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 2/3")
        r1.update(89, 2, 3, 4)
        self.assertEqual(str(r1), "[Rectangle] (89) 4/10 - 2/3")
        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r1), "[Rectangle] (89) 4/5 - 2/3")

    def test_update_kwarg(self):
        """test the update method to change instance values"""
        r1 = Rectangle(10, 10, 10, 10)
        self.assertEqual(str(r1), "[Rectangle] (4) 10/10 - 10/10")
        r1.update(height=1)
        self.assertEqual(str(r1), "[Rectangle] (4) 10/10 - 10/1")
        r1.update(width=1, x=2)
        self.assertEqual(str(r1), "[Rectangle] (4) 2/10 - 1/1")
        r1.update(y=1, width=2, x=3, id=89)
        self.assertEqual(str(r1), "[Rectangle] (89) 3/1 - 2/1")
        r1.update(x=1, height=2, y=3, width=4)
        self.assertEqual(str(r1), "[Rectangle] (89) 1/3 - 4/2")

    def test_to_dictionary(self):
        """test conversion of an instance to a dictionary"""
        expected = {'height': 2, 'id': 12, 'width': 10, 'x': 0, 'y': 0}
        r3_dict = self.r3.to_dictionary()
        self.assertTrue(type(r3_dict) is dict)
        self.assertEqual(dict(sorted(r3_dict.items())), expected)
        self.r1.update(**r3_dict)
        self.assertEqual(str(self.r3), str(self.r1))
        self.assertFalse(self.r3 == self.r1)
