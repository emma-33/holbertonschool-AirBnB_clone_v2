#!/usr/bin/python3
""" """
from re import T
from tests.test_models.test_base_model import TestBaseModel
from models.review import Review


class test_review(TestBaseModel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.text), str)
#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class test_review(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.text), str)

    def test_table_name(self):
        """ """
        new = self.value()
        self.assertEqual(new.__tablename__, "reviews")

    def test_place_id_column(self):
        """ """
        new = self.value()
        self.assertTrue(hasattr(new, "place_id"))
        self.assertEqual(type(new.place_id), Column)
        self.assertEqual(new.place_id.type, String(60))
        self.assertFalse(new.place_id.nullable)
        self.assertEqual(new.place_id.foreign_keys, {ForeignKey('places.id')})

    def test_user_id_column(self):
        """ """
        new = self.value()
        self.assertTrue(hasattr(new, "user_id"))
        self.assertEqual(type(new.user_id), Column)
        self.assertEqual(new.user_id.type, String(60))
        self.assertFalse(new.user_id.nullable)
        self.assertEqual(new.user_id.foreign_keys, {ForeignKey('users.id')})

    def test_text_column(self):
        """ """
        new = self.value()
        self.assertTrue(hasattr(new, "text"))
        self.assertEqual(type(new.text), Column)
        self.assertEqual(new.text.type, String(1024))
        self.assertFalse(new.text.nullable)