#!/usr/bin/python3
"""Unittest for class BaseModel
"""
import unittest
import datetime
import os

from models.base_model import BaseModel



class TestBase(unittest.TestCase):
    """
    Test case class to validate the ID generation of BaseModel class.
    """

    def test_idType(self):
        b1 = BaseModel()
        self.assertEqual(type(b1.id), str)

    def test_id0(self):
        b1 = BaseModel()
        b2 = BaseModel()
        self.assertNotEqual(b1.id, b2.id)

    def test_created_atType(self):
        b1 = BaseModel()
        self.assertEqual(type(b1.created_at), datetime.datetime)

    def test_created_at0(self):
        b1 = BaseModel()
        b2 = BaseModel()
        self.assertNotEqual(b1.created_at, b2.created_at)

    def test_updated_atType(self):
        b1 = BaseModel()
        self.assertEqual(type(b1.updated_at), datetime.datetime)

    def test_updated_at0(self):
        b1 = BaseModel()
        b2 = BaseModel()
        self.assertNotEqual(b1.updated_at, b2.updated_at)

    def test_upd_created_at(self):
        b1 = BaseModel()
        b2 = BaseModel()
        self.assertNotEqual(b1.created_at, b2.updated_at)
    
    def test_kwargs(self):
        b = BaseModel()
        c = b.to_dict()
        c_new = BaseModel(**c)
        self.assertEqual(c_new.__str__(), b.__str__())

    def test_kwargsType(self):
        b = BaseModel()
        c = b.to_dict()
        c_new = BaseModel(**c)
        self.assertEqual(type(c_new.updated_at), datetime.datetime)

    def test_kwargsType2(self):
        b = BaseModel()
        c = b.to_dict()
        c_new = BaseModel(**c)
        self.assertEqual(type(c_new.created_at), datetime.datetime)

    def test_kwargsbool(self):
        b = BaseModel()
        c = b.to_dict()
        c_new = BaseModel(**c)
        self.assertFalse(b is c_new)

class TestBase_str(unittest.TestCase):
    """
    Test case class to validate the __str__ method of BaseModel class.
    """
    def test_str1(self):
        b = BaseModel()
        self.assertEqual(b.__str__(), f"[{b.__class__.__name__}] ({b.id}) {b.__dict__}")

    def test_str2(self):
        b = BaseModel()
        b.name = "My First Model"
        b.my_number = 89
        self.assertEqual(b.__str__(), f"[{b.__class__.__name__}] ({b.id}) {b.__dict__}")

    def test_strErr(self):
        b = BaseModel()
        with self.assertRaises(TypeError):
            b.__str__(4)

    
class TestBase_save(unittest.TestCase):
    """
    Test case class to validate the save method of BaseModel class.
    """

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_save_update(self):
        b = BaseModel()
        b.name = "My First Model"
        b.my_number = 89
        updated_at_before_save = b.updated_at
        b.save()
        updated_at_after_save = b.updated_at
        self.assertNotEqual(updated_at_before_save, updated_at_after_save)

    def test_save_create(self):
        b = BaseModel()
        b.name = "My First Model"
        b.my_number = 89
        created_at_before_save = b.created_at
        b.save()
        created_at_after_save = b.created_at
        self.assertEqual(created_at_before_save, created_at_after_save)

    def test_save_str(self):
        b = BaseModel()
        b.name = "My First Model"
        b.my_number = 89
        str_before_save = b.__str__()
        b.save()
        str_after_save = b.__str__()
        self.assertNotEqual(str_before_save, str_after_save)
    
class TestBase_todict(unittest.TestCase):
    """
    Test case class to validate the to_dict method of BaseModel class.
    """

    def test_todict(self):
        b = BaseModel()
        
        dict = dict = {
            'id': b.id,
            'created_at': b.created_at.isoformat(),
            'updated_at': b.updated_at.isoformat(),
            '__class__': b.__class__.__name__,
        }
        self.assertEqual(b.to_dict(), dict)

    def test_todictType(self):
        b = BaseModel()
        c = b.to_dict()
        self.assertEqual(type(c["created_at"]), str)

    def test_todictType2(self):
        b = BaseModel()
        c = b.to_dict()
        self.assertEqual(type(c["updated_at"]), str)
    
    def test_dictErr(self):
        b = BaseModel()
        with self.assertRaises(TypeError):
            b.to_dict(5)
