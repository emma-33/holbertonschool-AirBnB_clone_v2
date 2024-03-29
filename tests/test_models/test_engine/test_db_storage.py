import unittest
from models.engine.db_storage import DBStorage
from models.base_model import BaseModel
from models.user import User

class TestDBStorage(unittest.TestCase):
    def setUp(self):
        self.db = DBStorage()
        self.db.reload()

    def tearDown(self):
        pass

    def test_all(self):
        # Test all() method with specific class
        all_objects = self.db.all(User)
        self.assertIsInstance(all_objects, dict)
        self.assertEqual(len(all_objects), 0)

        # Test all() method without specific class
        all_objects = self.db.all()
        self.assertIsInstance(all_objects, dict)
        self.assertEqual(len(all_objects), 0)

    def test_new(self):
        # Test new() method
        user = User()
        self.db.new(user)
        self.assertIn(user, self.db._DBStorage__session.new)

    def test_save(self):
        # Test save() method
        user = User()
        self.db.new(user)
        self.db.save()
        self.assertIn(user, self.db._DBStorage__session)

    def test_delete(self):
        # Test delete() method
        user = User()
        self.db.new(user)
        self.db.delete(user)
        self.assertNotIn(user, self.db._DBStorage__session)

    def test_reload(self):
        # Test reload() method
        self.db.reload()
        self.assertIsNotNone(self.db._DBStorage__session)

if __name__ == '__main__':
    unittest.main()