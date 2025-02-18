import unittest
from app import app, db

class TodoTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_create_todo(self):
        response = self.app.post('/api/todos', json={'title': 'Test Task'})
        self.assertEqual(response.status_code, 201)

if __name__ == '__main__':
    unittest.main()
