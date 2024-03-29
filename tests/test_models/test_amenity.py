#!/usr/bin/python3
""" Tests for amenity.py"""
from tests.test_models.test_base_model import TestBaseModel
from models.amenity import Amenity


class test_Amenity(TestBaseModel):
    """ tests for Amenity class"""

    def __init__(self, *args, **kwargs):
        """initializes"""
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """ tests name"""
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_name_column(self):
        """ tests name column"""
        amenity = self.value()
        self.assertTrue(hasattr(amenity, 'name'))
        self.assertIsInstance(amenity.name, Column)
        self.assertEqual(amenity.name.type, String(128))
        self.assertFalse(amenity.name.nullable)

    def test_place_amenities_relationship(self):
        """ tests place_amenities relationship"""
        amenity = self.value()
        self.assertTrue(hasattr(amenity, 'place_amenities'))
        self.assertIsInstance(amenity.place_amenities, relationship)
        self.assertEqual(amenity.place_amenities.secondary, 'place_amenity')
        self.assertFalse(amenity.place_amenities.viewonly)
