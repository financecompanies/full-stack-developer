# SQLAlchemy Basics

## Introduction

### Takeaways

**SQLAlchemy**
SQLAlchemy is the most popular open-source library for working with relational databases from Python.

SQLAlchemy:
* Features function-based query construction: allows SQL clauses to be built via Python functions and expressions.
* Avoid writing raw SQL. Generate SQL and Python code for you to access tables.
* Moreover, you can avoid sending SQL to the database on every call. The SQLAlchemy ORM library features automatic caching, caching collections and references between objects once initially loaded.

## Layers of Abstraction

### Takeaways
* Without SQLAlchemy, we'd only use a DBAPI to establish connections and execute SQL statements. Simple, but not scalable as complexity grows.
* SQLAlchemy offers several layers of abstraction and convenient tools for interacting with a database.

#### SQLALchemy lets you traverse through all 3 layers of abstraction to interact with your database.
* Can stay on the ORM level
* Can dive into database operations to run customized SQL code specific to the database, on the Expressions level.
* Can write raw SQL to execute, when needed, on the Engine level.
    * Can more simply use `psycopg2` in this case

#### Good Design Practice (Opinion)
Here's my opinion on interacting with databases using good design practice.

* Keep your code Pythonic. Work in classes and objects as much as possible.
    * Makes switching to a different backend easy in the feature.
* Avoid writing raw SQL until absolutely necessary

<img src="https://video.udacity-data.com/topher/2019/August/5d5a1ede_sqla/sqla.png" alt="" width="800px" class="index--image--1wh9w">

**Layers of SQLAlchemy**
* DBAPI
* The Dialect
* The Connection Pool
* The Engine
* SQL Expressions
* SQLAlchemy ORM (optional)

## The Dialect

### Resources
* [SQLAlchemy Docs on the Dialect](https://docs.sqlalchemy.org/en/latest/dialects/)

## The Connection Pool

### Resources
* [SQLAlchemy Docs on its Connection Pooling](https://docs.sqlalchemy.org/en/latest/core/pooling.html)

## The Engine

### Takeaways

#### The Engine
* 1 of 3 main layers for how you may choose to interact with the database.
* Is the lowest level layer of interacting with the database, and is much like using the DBAPI directly. Very similar to using psycopg2, managing a connection directly.

Moreover,
* The Engine in SQLAlchemy refers to both itself, the Dialect and the Connection Pool, which all work together to interface with our database.
* A connection pool gets automatically created when we create a SQLAlchemy engine.
Resources

### Resources
* [SQLAlchemy Docs on the Engine.](https://docs.sqlalchemy.org/en/latest/core/engines.html)

## SQL Expressions

### Takeaways
* Instead of sending raw SQL (using the Engine), we can compose python objects to compose SQL expressions, instead.
* SQL Expressions still involves using and knowing SQL to interact with the database.

## SQLAlchemy ORM

### Takeaways

### SQLAlchemy ORM
* Lets you compose SQL expressions by mapping python classes of objects to tables in the database
* Is the highest layer of abstraction in SQLALchemy.
* Wraps the SQL Expressions and Engine to work together to interact with the database
* Will be used in this course, so we can know how to use ORM libraries in general.

Moreover, SQLAlchemy is split into two libraries:
* SQLAlchemy Core
* SQLAlchemy ORM (Object Relational Mapping library). SQLALchemy ORM is offered as an optional library, so you don't have to use the ORM in order to use the rest of SQLAlchemy.
    * The ORM uses the Core library inside
    * The ORM lets you map from the database schema to the application's Python objects
    * The ORM persists objects into corresponding database tables

#### SQLAlchemy Layers of Abstraction Overview (Diagram)

<img src="https://video.udacity-data.com/topher/2019/August/5d4de779_sqlalchemy-layers-of-abstraction/sqlalchemy-layers-of-abstraction.png" alt="Diagram showing SQLAlchemy layers of abstraction" width="880px" class="index--image--1wh9w">

## Flask-SQLAlchemy

### Resources
* [Flask Docs](https://flask.palletsprojects.com/) under "Quickstart"
* [Flask-SQLAlchemy Docs](http://flask-sqlalchemy.palletsprojects.com/) under "Quickstart"

### Initializing the app
`app = Flask(__name__)` sets the name of your app to the name of your module ("app" if "app.py" is the name of your file).

### Using `@app.route`
```python
@app.route('/')
def index():
  ...
```

In this case, `@app.route` is a Python decorator. Decorators take functions and returns another function, usually extending the input function with additional ("decorated") functionality. `@app.route` is a decorator that takes an input function `index()` as the callback that gets invoked when a request to route `/` comes in from a client.

See: [this primer on decorators from Real Python.](https://realpython.com/primer-on-python-decorators/#decorators-with-arguments)

### Running the flask app

To start the server,
* We run a flask app defined at app.py with FLASK_APP=app.py flask run
    * FLASK_APP must be set to the server file path with an equal sign in between. No spaces. FLASK_APP = app.py will not work. These flags have to be set exactly as expected, as FLAG=value.
* To enable live reload, set export FLASK_ENV=development in your terminal session to enable debug mode, prior to running flask run. Or call it together with flask run:

```python
FLASK_APP=app.py FLASK_DEBUG=true flask run
```

Alternative approach to run a Flask app: using `__main__`
Instead of using $ flask run, we could have also defined a method

```python
if __name__ == '__main__':
  app.run()
```

at the bottom of our `app.py` script, and then called `$ python3 app.py` in our terminal to invoke `app.run()` and run the flask app this way.

When we call a script this way, using `$ python script.py`, the script's `__name__` gets set to `__main__` by the Python interpreter, which then runs through executing all code found in the script. When it reaches the end, and finds `if __name__ == 'main'`, it evaluates this to True and therefore calls `app.run()` at the end, running the Flask app.

Both approaches to running your server are valid and neither way is better than the other.

**Note: different versions of flask take `FLASK_APP=app.py` versus `FLASK_APP=app`, etc.**
Check out the docs on the [Flask CLI](https://flask.palletsprojects.com/en/1.0.x/cli/) to understand the various options for pointing `FLASK_APP` to your flask application.

## db.Model and defining models

### Takeaways

Given an instance of the SQLAlchemy class from Flask-SQLAlchemy,

```python
db = SQLAlchemy(app)
```

* db is an interface for interacting with our database
* `db.Model` lets us create and manipulate **data models**
* `db.session` lets us create and manipulate **database transactions**

### Declaring classes

* `class MyModel(db.Model)` will inherit from db.Model
* By inheriting from `db.Model`, we map from our classes to tables via SQLAlchemy ORM

### Defining columns

* Within our class, we declare attributes equal to `db.Column(...)`
* db.Column takes `<datatype>, <primary_key?>, <constraint?>, <default?>`

### Table naming

* By default, SQLAlchemy will pick the name of the table for you, setting it equal to the lower-case version of your class's name. Otherwise, we set the name of the table using `__tablename__ = 'my_custom_table_name'`.

