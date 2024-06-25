#!/usr/bin/python3
"""Unittest for class User
"""
import unittest
import datetime
import os


from models.user import User


class TestUser(unittest.TestCase):
    """
    Test case class to validate the ID generation of User class.
    """

    def test_first_name(self):
        u = User()
        self.assertEqual(type(u.first_name), str)

    def test_last_name(self):
        u = User()
        self.assertEqual(type(u.last_name), str)

    def test_email(self):
        u = User()
        self.assertEqual(type(u.email), str)

    def test_password(self):
        u = User()
        self.assertEqual(type(u.password), str)

    def test_idType(self):
        u1 = User()
        self.assertEqual(type(u1.id), str)

    def test_id0(self):
        u1 = User()
        u2 = User()
        self.assertNotEqual(u1.id, u2.id)

    def test_created_atType(self):
        u1 = User()
        self.assertEqual(type(u1.created_at), datetime.datetime)

    def test_created_at0(self):
        u1 = User()
        u2 = User()
        self.assertNotEqual(u1.created_at, u2.created_at)

    def test_updated_atType(self):
        u1 = User()
        self.assertEqual(type(u1.updated_at), datetime.datetime)

    def test_updated_at0(self):
        u1 = User()
        u2 = User()
        self.assertNotEqual(u1.updated_at, u2.updated_at)

    def test_upd_created_at(self):
        u1 = User()
        u2 = User()
        self.assertNotEqual(u1.created_at, u2.updated_at)
    
    def test_kwargs(self):
        u = User()
        c = u.to_dict()
        c_new = User(**c)
        self.assertEqual(c_new.__str__(), u.__str__())

    def test_kwargsType(self):
        u = User()
        c = u.to_dict()
        c_new = User(**c)
        self.assertEqual(type(c_new.updated_at), datetime.datetime)

    def test_kwargsType2(self):
        u = User()
        c = u.to_dict()
        c_new = User(**c)
        self.assertEqual(type(c_new.created_at), datetime.datetime)

    def test_kwargsbool(self):
        u = User()
        c = u.to_dict()
        c_new = User(**c)
        self.assertFalse(u is c_new)

class TestUser_str(unittest.TestCase):
    """
    Test case class to validate the __str__ method of User class.
    """

    def test_str1(self):
        u = User()
        self.assertEqual(u.__str__(), f"[{u.__class__.__name__}] ({u.id}) {u.__dict__}")

    def test_str2(self):
        u = User()
        u.name = "My First Model"
        u.my_number = 89
        self.assertEqual(u.__str__(), f"[{u.__class__.__name__}] ({u.id}) {u.__dict__}")
    

    def test_strErr(self):
        u = User()
        with self.assertRaises(TypeError):
            u.__str__(4)

    
class TestUser_save(unittest.TestCase):
    """
    Test case class to validate the save method of User class.
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
        u = User()
        u.name = "My First Model"
        u.my_number = 89
        updated_at_before_save = u.updated_at
        u.save()
        updated_at_after_save = u.updated_at
        self.assertNotEqual(updated_at_before_save, updated_at_after_save)

    def test_save_create(self):
        u = User()
        u.name = "My First Model"
        u.my_number = 89
        created_at_before_save = u.created_at
        u.save()
        created_at_after_save = u.created_at
        self.assertEqual(created_at_before_save, created_at_after_save)

    def test_save_str(self):
        u = User()
        u.name = "My First Model"
        u.my_number = 89
        str_before_save = u.__str__()
        u.save()
        str_after_save = u.__str__()
        self.assertNotEqual(str_before_save, str_after_save)
    
class TestUser_todict(unittest.TestCase):
    """
    Test case class to validate the to_dict method of User class.
    """

    def test_todict(self):
        u = User()
        
        dict = dict = {
            'id': u.id,
            'created_at': u.created_at.isoformat(),
            'updated_at': u.updated_at.isoformat(),
            '__class__': u.__class__.__name__,
        }
        self.assertEqual(u.to_dict(), dict)

    def test_todictType(self):
        u = User()
        c = u.to_dict()
        self.assertEqual(type(c["created_at"]), str)

    def test_todictType2(self):
        u = User()
        c = u.to_dict()
        self.assertEqual(type(c["updated_at"]), str)
    
    def test_dictErr(self):
        u = User()
        with self.assertRaises(TypeError):
            u.to_dict(5)
