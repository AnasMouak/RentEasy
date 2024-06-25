#!/usr/bin/python3
"""Unittest for class CarModel
"""
import unittest
import datetime
import os


from models.car_model import CarModel



class TestCarModel(unittest.TestCase):
    """
    Test case class to validate the ID generation of CarModel class.
    """

    def test_name(self):
        c = CarModel()
        self.assertEqual(type(c.name), str)
    
    def test_car_maker_id(self):
        c = CarModel()
        self.assertEqual(type(c.car_maker_id), str)

    def test_idType(self):
        c = CarModel()
        self.assertEqual(type(c.id), str)

    def test_price_per_day(self):
        c = CarModel()
        self.assertEqual(type(c.price_per_day), float)

    def test_kilometers(self):
        c = CarModel()
        self.assertEqual(type(c.kilometers), float)

    def test_year(self):
        c = CarModel()
        self.assertEqual(type(c.year), int)
    
    def test_color(self):
        c = CarModel()
        self.assertEqual(type(c.color), str)

    def test_passengers(self):
        c = CarModel()
        self.assertEqual(type(c.passengers), int)

    def test_doors(self):
        c = CarModel()
        self.assertEqual(type(c.doors), int)
    
    def test_transmission(self):
        c = CarModel()
        self.assertEqual(type(c.transmission), str)

    def test_fuel(self):
        c = CarModel()
        self.assertEqual(type(c.fuel), str)
    
    def test_air_conditioning(self):
        c = CarModel()
        self.assertEqual(type(c.air_conditioning), bool)

    def test_id0(self):
        c1 = CarModel()
        c2 = CarModel()
        self.assertNotEqual(c1.id, c2.id)

    def test_created_atType(self):
        c1 = CarModel()
        self.assertEqual(type(c1.created_at), datetime.datetime)

    def test_created_at0(self):
        c1 = CarModel()
        c2 = CarModel()
        self.assertNotEqual(c1.created_at, c2.created_at)

    def test_updated_atType(self):
        c1 = CarModel()
        self.assertEqual(type(c1.updated_at), datetime.datetime)

    def test_updated_at0(self):
        c1 = CarModel()
        c2 = CarModel()
        self.assertNotEqual(c1.updated_at, c2.updated_at)

    def test_upd_created_at(self):
        c1 = CarModel()
        c2 = CarModel()
        self.assertNotEqual(c1.created_at, c2.updated_at)
    
    def test_kwargs(self):
        c = CarModel()
        cc = c.to_dict()
        c_new = CarModel(**cc)
        self.assertEqual(c_new.__str__(), c.__str__())

    def test_kwargsType(self):
        c = CarModel()
        cc = c.to_dict()
        c_new = CarModel(**cc)
        self.assertEqual(type(c_new.updated_at), datetime.datetime)

    def test_kwargsType2(self):
        c = CarModel()
        cc = c.to_dict()
        c_new = CarModel(**cc)
        self.assertEqual(type(c_new.created_at), datetime.datetime)

    def test_kwargsbool(self):
        c = CarModel()
        cc = c.to_dict()
        c_new = CarModel(**cc)
        self.assertFalse(c is c_new)

class TestCarModel_str(unittest.TestCase):
    """
    Test case class to validate the __str__ method of CarModel class.
    """

    def test_str1(self):
        c = CarModel()
        self.assertEqual(c.__str__(), f"[{c.__class__.__name__}] ({c.id}) {c.__dict__}")

    def test_str2(self):
        c = CarModel()
        c.name = "CarModelName"
        c.my_number = 89
        self.assertEqual(c.__str__(), f"[{c.__class__.__name__}] ({c.id}) {c.__dict__}")

    def test_strErr(self):
        c = CarModel()
        with self.assertRaises(TypeError):
            c.__str__(4)

    
class TestCarModel_save(unittest.TestCase):
    """
    Test case class to validate the save method of CarModel class.
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
        c = CarModel()
        c.name = "CarModelName"
        c.my_number = 89
        updated_at_before_save = c.updated_at
        c.save()
        updated_at_after_save = c.updated_at
        self.assertNotEqual(updated_at_before_save, updated_at_after_save)

    def test_save_create(self):
        c = CarModel()
        c.name = "CarModelName"
        c.my_number = 89
        created_at_before_save = c.created_at
        c.save()
        created_at_after_save = c.created_at
        self.assertEqual(created_at_before_save, created_at_after_save)

    def test_save_str(self):
        c = CarModel()
        c.name = "CarModelName"
        c.my_number = 89
        str_before_save = c.__str__()
        c.save()
        str_after_save = c.__str__()
        self.assertNotEqual(str_before_save, str_after_save)
    
class TestCarModel_todict(unittest.TestCase):
    """
    Test case class to validate the to_dict method of CarModel class.
    """

    def test_todict(self):
        c = CarModel()
        
        dict = dict = {
            'id': c.id,
            'created_at': c.created_at.isoformat(),
            'updated_at': c.updated_at.isoformat(),
            '__class__': c.__class__.__name__,
        }
        self.assertEqual(c.to_dict(), dict)

    def test_todictType(self):
        c = CarModel()
        cc = c.to_dict()
        self.assertEqual(type(cc["created_at"]), str)

    def test_todictType2(self):
        c = CarModel()
        cc = c.to_dict()
        self.assertEqual(type(cc["updated_at"]), str)
    
    def test_dictErr(self):
        c = CarModel()
        with self.assertRaises(TypeError):
            c.to_dict(5)
