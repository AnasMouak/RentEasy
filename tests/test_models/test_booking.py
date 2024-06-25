#!/usr/bin/python3
"""Unittest for class Booking
"""
import unittest
import datetime
import os


from models.booking import Booking



class TestBooking(unittest.TestCase):
    """
    Test case class to validate the ID generation of Booking class.
    """

    def test_car_model_id(self):
        r = Booking()
        self.assertEqual(type(r.car_model_id), str)

    def test_user_id(self):
        r = Booking()
        self.assertEqual(type(r.user_id), str)

    def test_start_date(self):
        r = Booking()
        self.assertEqual(type(r.start_date), datetime.datetime)

    def test_end_date(self):
        r = Booking()
        self.assertEqual(type(r.end_date), datetime.datetime)

    def test_total_price(self):
        r = Booking()
        self.assertEqual(type(r.total_price), float)

    def test_idType(self):
        r1 = Booking()
        self.assertEqual(type(r1.id), str)

    def test_id0(self):
        r1 = Booking()
        r2 = Booking()
        self.assertNotEqual(r1.id, r2.id)

    def test_created_atType(self):
        r1 = Booking()
        self.assertEqual(type(r1.created_at), datetime.datetime)

    def test_created_at0(self):
        r1 = Booking()
        r2 = Booking()
        self.assertNotEqual(r1.created_at, r2.created_at)

    def test_updated_atType(self):
        r1 = Booking()
        self.assertEqual(type(r1.updated_at), datetime.datetime)

    def test_updated_at0(self):
        r1 = Booking()
        r2 = Booking()
        self.assertNotEqual(r1.updated_at, r2.updated_at)

    def test_upd_created_at(self):
        r1 = Booking()
        r2 = Booking()
        self.assertNotEqual(r1.created_at, r2.updated_at)
    
    def test_kwargs(self):
        r = Booking()
        c = r.to_dict()
        c_new = Booking(**c)
        self.assertEqual(c_new.__str__(), r.__str__())

    def test_kwargsType(self):
        r = Booking()
        c = r.to_dict()
        c_new = Booking(**c)
        self.assertEqual(type(c_new.updated_at), datetime.datetime)

    def test_kwargsType2(self):
        r = Booking()
        c = r.to_dict()
        c_new = Booking(**c)
        self.assertEqual(type(c_new.created_at), datetime.datetime)

    def test_kwargsbool(self):
        r = Booking()
        c = r.to_dict()
        c_new = Booking(**c)
        self.assertFalse(r is c_new)

class TestBooking_str(unittest.TestCase):
    """
    Test case class to validate the __str__ method of Booking class.
    """

    def test_str1(self):
        r = Booking()
        self.assertEqual(r.__str__(), f"[{r.__class__.__name__}] ({r.id}) {r.__dict__}")

    def test_str2(self):
        r = Booking()
        r.name = "My First Model"
        r.my_number = 89
        self.assertEqual(r.__str__(), f"[{r.__class__.__name__}] ({r.id}) {r.__dict__}")

    def test_strErr(self):
        r = Booking()
        with self.assertRaises(TypeError):
            r.__str__(4)

    
class TestBooking_save(unittest.TestCase):
    """
    Test case class to validate the save method of Booking class.
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
        r = Booking()
        r.name = "My First Model"
        r.my_number = 89
        updated_at_before_save = r.updated_at
        r.save()
        updated_at_after_save = r.updated_at
        self.assertNotEqual(updated_at_before_save, updated_at_after_save)

    def test_save_create(self):
        r = Booking()
        r.name = "My First Model"
        r.my_number = 89
        created_at_before_save = r.created_at
        r.save()
        created_at_after_save = r.created_at
        self.assertEqual(created_at_before_save, created_at_after_save)

    def test_save_str(self):
        r = Booking()
        r.name = "My First Model"
        r.my_number = 89
        str_before_save = r.__str__()
        r.save()
        str_after_save = r.__str__()
        self.assertNotEqual(str_before_save, str_after_save)
    
class TestBooking_todict(unittest.TestCase):
    """
    Test case class to validate the to_dict method of Booking class.
    """

    def test_todict(self):
        r = Booking()
        
        dict = dict = {
            'id': r.id,
            'created_at': r.created_at.isoformat(),
            'updated_at': r.updated_at.isoformat(),
            '__class__': r.__class__.__name__,
        }
        self.assertEqual(r.to_dict(), dict)

    def test_todictType(self):
        r = Booking()
        c = r.to_dict()
        self.assertEqual(type(c["created_at"]), str)

    def test_todictType2(self):
        r = Booking()
        c = r.to_dict()
        self.assertEqual(type(c["updated_at"]), str)
    
    def test_dictErr(self):
        r = Booking()
        with self.assertRaises(TypeError):
            r.to_dict(5)