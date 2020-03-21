# API Testing

## [1. Overview](https://classroom.udacity.com/nanodegrees/nd0044/parts/838df8a7-4694-4982-a9a5-a5ab20247776/modules/afbae13a-a91a-4d5e-9f98-4fe13c415f7a/lessons/123d0a0a-8137-4e21-881f-8d03fb371209/concepts/0ae8c4ed-e895-4f9e-8669-e8a8d8125811)

[![](https://img.youtube.com/vi/Q_Jh4bsLUJ8/0.jpg)](https://youtu.be/Q_Jh4bsLUJ8)

In this lesson we'll cover:
* Purpose and Benefits of API Testing
* Testing a Flask Api with Unittest
* Test-Driven Development for APIs

### Why Testing?
As with all tests, writing unittests for your API verifies the behavior. For APIs, test should be written:
* To confirm expected request handling behavior
* To confirm success-response structure is correct
* To confirm expected errors are handled appropriately
* To confirm CRUD operations persist
* In addition to verifying behavior, having a thorough test suite ensures that when you update your API, you can easily test all previous functionality.

If bugs are discovered while in development, they cost next to nothing to fix and don't have any negative impact on business outcomes or client experience. But if bugs make it to production, their cost can be quite large—they can impact performance, and fixing bugs can take large amounts of time for big, production applications.

The order of operations for app development should always be:
* Development
* Unit Testing
* Quality Assurance
* Production

Step 2 is essential to ensuring the application is production-ready and time-to-production is used efficiently

## [2. Testing in Flask](https://classroom.udacity.com/nanodegrees/nd0044/parts/838df8a7-4694-4982-a9a5-a5ab20247776/modules/afbae13a-a91a-4d5e-9f98-4fe13c415f7a/lessons/123d0a0a-8137-4e21-881f-8d03fb371209/concepts/c8bce42a-c8a6-4a4f-bbd2-b5ace422a575)

### Exercise [Testing Prep](https://r848940c899836xjupyteriht9hei9.udacity-student-workspaces.com/notebooks/Testing_Prep.ipynb)

[![](https://img.youtube.com/vi/EiwiF5Mqz0E/0.jpg)](https://youtu.be/EiwiF5Mqz0E)

### Unittest Flask Key Structures

As we just saw, all of your Flask application tests will follow the same format:
1. **Define the test case class** for the application (or section of the application, for larger applications).
2. **Define and implement the `setUp` function**. It will be executed before each test and is where you should initialize the app and test client, as well as any other context your tests will need. The Flask library provides a test client for the application, accessed as shown below.
3. **Define the `tearDown` method**, which is implemented after each test. It will run as long as setUp executes successfully, regardless of test success.
4. **Define your tests**. All should begin with `"test_"` and include a doc string about the purpose of the test. In defining the tests, you will need to:
    1. Get the response by having the client make a request
    2. Use `self.assertEqual` to check the status code and all other relevant operations.
5. **Run the test suite**, by running `python test_file_name.py` from the command line.

Here's that same code (from the notebook above), for your reference:

```python
class AppNameTestCase(unittest.TestCase):
    """This class represents the ___ test case"""

    def setUp(self):
        """Executed before each test. Define test variables and initialize app."""
        self.client = app.test_client
        pass

    def tearDown(self):
        """Executed after reach test"""
        pass

    def test_given_behavior(self):
        """Test _____________ """
        res = self.client().get('/')

        self.assertEqual(res.status_code, 200)

# Make the tests conveniently executable
if __name__ == "__main__":
unittest.main()
```

## [3. Practice - Testing in Flask](https://classroom.udacity.com/nanodegrees/nd0044/parts/838df8a7-4694-4982-a9a5-a5ab20247776/modules/afbae13a-a91a-4d5e-9f98-4fe13c415f7a/lessons/123d0a0a-8137-4e21-881f-8d03fb371209/concepts/8d7e8e71-45c7-4730-841e-9821bad16d85)

### Exercise [Writing Your Tests](https://r848940c909323xJUPYTERLo76stdla.udacity-student-workspaces.com/)

### Solution

```python
import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Book

class BookTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client()
        self.database_name = "bookshelf_test"
        self.database_path = "postgres://{}:{}@{}/{}".format('student', 'student','localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        self.new_book = {
            'title': 'Anansi Boys',
            'author': 'Neil Gaiman',
            'rating': 5
        }

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def tearDown(self):
        """Executed after reach test"""
        pass

# @TODO: Write at least two tests for each endpoint - one each for success and error behavior.
#        You can feel free to write additional tests for nuanced functionality,
#        Such as adding a book without a rating, etc.
#        Since there are four routes currently, you should have at least eight tests.
# Optional: Update the book information in setUp to make the test database your own!
    def test_get_books(self):
        response = self.client.post('/books', json=self.new_book)
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/books')
        self.assertEqual(response.status_code, 200)


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
```

## 4. [TDD for APIs](https://classroom.udacity.com/nanodegrees/nd0044/parts/838df8a7-4694-4982-a9a5-a5ab20247776/modules/afbae13a-a91a-4d5e-9f98-4fe13c415f7a/lessons/123d0a0a-8137-4e21-881f-8d03fb371209/concepts/012cae2e-a4ef-429f-aea6-d282da3b7e44)

**Test-Driven Development** (or **TDD**) is a software development paradigm used very commonly in production. It is based on a short, rapid development cycle in which tests are written before the executable code and constantly iterated on.

1. Write test for specific application behavior.
2. Run the tests and watch them fail.
3. Write code to execute the required behavior.
4. Test the code and rewrite as necessary to pass the test
5. Refactor your code.
6. Repeat - write your next test.

## 5. [Practice - TDD for APIs](https://classroom.udacity.com/nanodegrees/nd0044/parts/838df8a7-4694-4982-a9a5-a5ab20247776/modules/afbae13a-a91a-4d5e-9f98-4fe13c415f7a/lessons/123d0a0a-8137-4e21-881f-8d03fb371209/concepts/7529c53d-c671-4ec7-bd7b-81ea374f72e3)

### Exercise [Test with Web App Interface](https://r848940c899834xjupyterlo0b4429b.udacity-student-workspaces.com/lab/workspaces/auto-i)

### Solution

backend/test_flaskr.py

```python
import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Book

class BookTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "bookshelf_test"
        self.database_path = "postgres://{}:{}@{}/{}".format('student', 'student','localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        self.new_book = {
            'title': 'Anansi Boys',
            'author': 'Neil Gaiman',
            'rating': 5
        }

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def tearDown(self):
        """Executed after reach test"""
        pass

    ...

    def test_search_book(self):
        """Tests a successful search for a book with results"""
        res = self.client().post('/books/search', json={'search': 'Anansi Boys'})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertTrue(data['books'])
        self.assertTrue(data['total_books'])


    def test_400_for_failed_search_book(self):
        """Tests when request a search for a book giving no search term"""
        res = self.client().post('/books/search')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 400)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], 'bad request')


    ...

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
```

backend/flaskr/__init__.py
```python
import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy #, or_
from flask_cors import CORS
import random

from models import setup_db, Book

BOOKS_PER_SHELF = 8

def paginate_books(request, selection):
  page = request.args.get('page', 1, type=int)
  start =  (page - 1) * BOOKS_PER_SHELF
  end = start + BOOKS_PER_SHELF

  books = [book.format() for book in selection]
  current_books = books[start:end]

  return current_books

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)
  CORS(app)

  ...

  @app.route('/books/search', methods=['POST'])
  def search_book():
    body = request.get_json()

    if body is None:
        return abort(400)

    search_term = body.get('search', None)

    if search_term is None:
        return abort(400)

    selection = Book.query.order_by(Book.id).filter(Book.title.ilike(f'%{search_term}%')).all()
    books = [book.format() for book in selection]

    return jsonify({
        'success': True,
        'books': books,
        'total_books': len(books)
    })

  ...
```