#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.city import City


class test_City(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """ """
        fresh = self.value()
        self.assertNotEqual(type(fresh.state_id), str)

    def test_name(self):
        """ """
        fresh = self.value()
        self.assertNotEqual(type(fresh.name), str)