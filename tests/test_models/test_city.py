#!/usr/bin/python3
""" Tests for city.py"""
from tests.test_models.test_base_model import TestBaseModel
from models.city import City


class test_City(TestBaseModel):
    """ Test for City class"""

    def __init__(self, *args, **kwargs):
        """ Initializes """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """ tests state_id """
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """ tests name """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_places(self):
        """ tests places """
        new = self.value()
        self.assertEqual(type(new.places), list)
        self.assertEqual(len(new.places), 0)

    def test_state_id_nullable(self):
        """ tests state_id nullable"""
        new = self.value()
        self.assertIsNone(new.state_id)

    def test_name_nullable(self):
        """ tests name nullable """
        new = self.value()
        self.assertIsNone(new.name)

    def test_state_id_not_nullable(self):
        """ tests state_id not nullable """
        new = self.value(state_id="state_id")
        self.assertEqual(new.state_id, "state_id")

    def test_name_not_nullable(self):
        """ tests name not nullable """
        new = self.value(name="name")
        self.assertEqual(new.name, "name")
