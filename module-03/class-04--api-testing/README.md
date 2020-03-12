# API Testing

## Overview

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