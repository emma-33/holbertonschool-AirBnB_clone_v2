import unittest
from models.base_model import BaseModel
from datetime import datetime

class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.model = BaseModel()

    def test_id(self):
        self.assertIsNotNone(self.model.id)
        self.assertIsInstance(self.model.id, str)

    def test_created_at(self):
        self.assertIsNotNone(self.model.created_at)
        self.assertIsInstance(self.model.created_at, datetime)

    def test_updated_at(self):
        self.assertIsNotNone(self.model.updated_at)
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_init_with_args(self):
        model = BaseModel(id='test_id', created_at=datetime(2022, 1, 1), updated_at=datetime(2022, 1, 1))
        self.assertEqual(model.id, 'test_id')
        self.assertEqual(model.created_at, datetime(2022, 1, 1))
        self.assertEqual(model.updated_at, datetime(2022, 1, 1))

    def test_str(self):
        expected_output = "[BaseModel] ({}) {}".format(self.model.id, self.model.__dict__)
        self.assertEqual(str(self.model), expected_output)

    def test_save(self):
        self.model.save()
        self.assertNotEqual(self.model.updated_at, self.model.created_at)

    def test_to_dict(self):
        dictionary = self.model.to_dict()
        self.assertIsInstance(dictionary, dict)
        self.assertEqual(dictionary['__class__'], 'BaseModel')
        self.assertEqual(dictionary['created_at'], self.model.created_at.isoformat())
        self.assertEqual(dictionary['updated_at'], self.model.updated_at.isoformat())

    def test_delete(self):
        from models.engine.file_storage import FileStorage
        from models.state import State
        
        fs = FileStorage()
        
        all_states = fs.all(State)
        self.assertEqual(len(all_states.keys()), 0)

        new_state = State()
        new_state.name = "California"
        fs.new(new_state)
        fs.save()
        self.assertEqual(new_state.name, "California")
        self.assertEqual(len(all_states.keys()), 1)

        another_state = State()
        another_state.name = "Nevada"
        fs.new(another_state)
        fs.save()
        self.assertEqual(new_state.name, "Nevada")
        self.assertEqual(len(all_states.keys()), 2)
        
        fs.delete(new_state)
        
        self.assertEqual(len(all_states.keys()), 1)

if __name__ == '__main__':
    unittest.main()