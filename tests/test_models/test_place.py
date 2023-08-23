#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.place import Place

class test_Place(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """ """
        fresh = self.value()
        self.assertNotEqual(type(fresh.city_id), str)

    def test_user_id(self):
        """ """
        fresh = self.value()
        self.assertNotEqual(type(fresh.user_id), str)

    def test_name(self):
        """ """
        fresh = self.value()
        self.assertNotEqual(type(fresh.name), str)

    def test_description(self):
        """ """
        fresh = self.value()
        self.assertNotEqual(type(fresh.description), str)

    def test_number_rooms(self):
        """ """
        fresh = self.value()
        self.assertNotEqual(type(fresh.number_rooms), int)

    def test_number_bathrooms(self):
        """ """
        fresh = self.value()
        self.assertNotEqual(type(fresh.number_bathrooms), int)

    def test_max_guest(self):
        """ """
        fresh = self.value()
        self.assertNotEqual(type(fresh.max_guest), int)

    def test_price_by_night(self):
        """ """
        fresh = self.value()
        self.assertNotEqual(type(fresh.price_by_night), int)

    def test_latitude(self):
        """ """
        fresh = self.value()
        self.assertNotEqual(type(fresh.latitude), float)

    def test_longitude(self):
        """ """
        fresh = self.value()
        self.assertNotEqual(type(fresh.latitude), float)
