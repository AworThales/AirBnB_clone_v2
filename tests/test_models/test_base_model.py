#!/usr/bin/python3
""" """
from models.base_model import BaseModel
import datetime
from uuid import UUID
import unittest
import json
import os

class test_basemodel(unittest.TestCase):
    """ """
    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def setUp(self):
        """ """
        pass

    def tearDown(self):
        try:
            os.remove('file.json')
        except:
            pass

    def test_default(self):
        """ """
        t = self.value()
        self.assertEqual(type(t), self.value)

    def test_kwargs(self):
        """ """
        t = self.value()
        copy = t.to_dict()
        fresh = BaseModel(**copy)
        self.assertFalse(fresh is t)

    def test_kwargs_int(self):
        """ """
        t = self.value()
        copy = t.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            fresh = BaseModel(**copy)

    def test_save(self):
        """ Testing save """
        t = self.value()
        t.save()
        key = self.name + "." + t.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], t.to_dict())

    def test_str(self):
        """ """
        t = self.value()
        self.assertEqual(str(t), '[{}] ({}) {}'.format(self.name, t.id,
                         t.__dict__))

    def test_todict(self):
        """ """
        t = self.value()
        n = t.to_dict()
        self.assertEqual(t.to_dict(), n)

    def test_kwargs_none(self):
        """ """
        n = {None: None}
        with self.assertRaises(TypeError):
            fresh = self.value(**n)

    def test_id(self):
        """ """
        fresh = self.value()
        self.assertEqual(type(fresh.id), str)

    def test_created_at(self):
        """ """
        fresh = self.value()
        self.assertEqual(type(fresh.created_at), datetime.datetime)

    def test_updated_at(self):
        """ """
        fresh = self.value()
        self.assertEqual(type(fresh.updated_at), datetime.datetime)
        n = fresh.to_dict()
        fresh = BaseModel(**n)
        self.assertNotEqual(fresh.created_at, fresh.updated_at)
