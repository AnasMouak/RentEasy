#!/usr/bin/python3
"""Unittest for class FileStorage
"""
import unittest
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage


class TestFileStorage_all_new(unittest.TestCase):
    """
    Test case class to validate the methods of FileStorage class.
    """

    @classmethod
    def setUpClass(cls):
        cls.storage = FileStorage()

    def setUp(self):
        self.storage.reload()  

    def tearDown(self):
        """Delete any created files."""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
    
    def test_type_path(self):
        self.assertEqual(type(storage._FileStorage__file_path), str)

    def test_allType(self):
        all_objs = storage.all()
        self.assertEqual(type(all_objs), dict)

    def test_all(self):
        self.assertEqual(len(storage.all()), 0)

    def test_new_and_all(self):
        obj = BaseModel()
        self.storage.new(obj)
        self.assertEqual(len(self.storage.all()), 1)

    def test_savejsonStrFile_BaseModel(self):
        storage.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_reloadjsonStrFile_BaseModel(self):
        b = BaseModel()
        storage.save()
        storage.reload()
        self.assertEqual(storage.save(), storage.reload())

    def test_reloadjsonStrFile_BaseModel1(self):
        b = BaseModel()
        storage.save()
        storage.reload()
        for obj in storage.all().values():
            reloaded_obj = obj
        self.assertEqual(b.to_dict(), reloaded_obj.to_dict())

    def test_reloadjsonStrFile_BaseModel2(self):
        b = BaseModel()
        storage.save()
        storage.reload()
        for obj in storage.all().values():
            reloaded_obj = obj
        self.assertEqual(b.id, reloaded_obj.id)

    def test_reload_from_nonexistent(self):
        self.assertEqual(storage.reload(), None)
