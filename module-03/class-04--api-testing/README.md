# API Testing

## 1. Overview

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

## 2. Testing in Flask

<figure class="video_container">
<iframe src="https://r848940c899836xJUPYTERiht9hei9.udacity-student-workspaces.com/notebooks/Testing_Prep.ipynb" allow="microphone" frameborder="0" style="height:100%; width:100%;"></iframe>
</figure>

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