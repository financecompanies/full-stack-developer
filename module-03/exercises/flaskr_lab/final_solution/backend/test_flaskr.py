import unittest
import json
from flaskr import create_app
from models import setup_db, Book
# from flask_sqlalchemy import SQLAlchemy


class BookTestCase(unittest.TestCase):
    """This class represents the bookshelf test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = 'bookshelf_test'
        self.database_path = 'postgres://{}:{}@{}/{}'.format(
            'student', 'student', 'localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        self.new_book = {
            'title': 'Programming with Types',
            'author': 'Vlad Riscutia',
            'rating': 4
        }

        # with self.app.app_context():
        #     self.db = SQLAlchemy()
        #     self.db.init_app(self.db)
        #     self.db.create_all()

    def test_can_get_all_books(self):
        response = self.client().get('/books')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(data['success'])
        self.assertTrue('total_books' in data)
        self.assertTrue('books' in data)

    def tearDown(self):
        """teardown all initialized variables."""
        pass


if __name__ == "__main__":
    unittest.main()
