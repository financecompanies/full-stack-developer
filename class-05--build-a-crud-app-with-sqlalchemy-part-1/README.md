# Build a CRUD App with SQLAlchemy - Part 1

## Introduction

### Takeaways
In summary, here are the skills we'll master over these next 3 lesson as we build out this application:

* Traversing across all layers of our backend stack, from our backend server in Flask to our database in Postgres, by understanding mappings between user operations, to the ORM, to the SQL executed on a database.
* Developing using the MVC Model-View-Controller pattern, for architecting out our application
* Handling changes to our data schema over time
* Modeling relationships between objects in our web application
* Implementing Search

## Implementing Reads: The “R” in CRUD

### Starter Code you can use

**todoapp/app.py**

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html', data=[{
    'description': 'Todo 1'
  }, {
    'description': 'Todo 2'
  }, {
    'description': 'Todo 3'
  }])
```

**todoapp/templates/index.html**

```python
<html>
  <head>
    <title>Todo App</title>
  </head>
  <body>
    <ul>
      {% for d in data %}
      <li>{{ d.description }}</li>
      {% endfor %}
    </ul>
  </body>
</html>
```

### Reset your database anytime

```postgres
dropdb todoapp && createdb todoapp
```

## Model View Controller (MVC)

### Solution Code to the previous section

**todoapp/app.py**

```python
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://udacitystudios@localhost:5432/todoapp'
db = SQLAlchemy(app)

class Todo(db.Model):
  __tablename__ = 'todos'
  id = db.Column(db.Integer, primary_key=True)
  description = db.Column(db.String(), nullable=False)

  def __repr__(self):
    return f'<Todo {self.id} {self.description}>'

db.create_all()

@app.route('/')
def index():
  return render_template('index.html', data=Todo.query.all())
```

**todoapp/templates/index.html**

```html
<html>
  <head>
    <title>Todo App</title>
  </head>
  <body>
    <ul>
      {% for d in data %}
      <li>{{ d.description }}</li>
      {% endfor %}
    </ul>
  </body>
</html>
```

**terminal commands executed**

```bash
$ create todoapp
$ FLASK_APP=app.py FLASK_DEBUG=true flask run
psql todoapp
>>> \dt
>>> \d todos
>>> INSERT INTO todos (description) VALUES ('Do a thing 1');
>>> INSERT INTO todos (description) VALUES ('Do a thing 2');
>>> INSERT INTO todos (description) VALUES ('Do a thing 3');
>>> INSERT INTO todos (description) VALUES ('Do a thing 4');
>>> select * from todos;
```

### Takeaways

* **MVC** stands for Model-View-Controller, a common pattern for architecting web applications
* Describes the 3 layers of the application we are developing

### Layers

* **Models** manage *data and business logic* for us. What happens inside models and database, capturing logical relationships and properties across the web app objects
* **Views** handles *display and representation logic*. What the user sees (HTML, CSS, JS from the user's perspective)
* **Controllers**: routes commands to the models and views, *containing control logic*. Control how commands are sent to models and views, and how models and views wound up interacting with each other.

<img src="https://video.udacity-data.com/topher/2019/August/5d5dc48f_screen-shot-2019-08-21-at-3.23.56-pm/screen-shot-2019-08-21-at-3.23.56-pm.png" alt="MVC" width="784px">

## Getting User Data in Flask — Part 1

### Takeaways
* There are 3 methods of getting user data from a view to a controller. See the image below.
    * URL query parameters
    * Forms
    * JSON

#### URL query parameters
* URL query parameters are listed as key-value pairs at the end of a URL, preceding a "?" question mark. E.g. `www.example.com/hello?my_key=my_value`.

#### Form data
* `request.form.get('<name>')` reads the value from a form input control (text input, number input, password input, etc) by the `name` attribute on the input HTML element.

#### Note: defaults
* request.args.get, request.form.get both accept an optional second parameter, e.g. request.args.get('foo', 'my default'), set to a default value, in case the result is empty.

#### JSON
* request.data retrieves JSON as a string. Then we'd take that string and turn it into python constructs by calling json.loads on the request.data string to turn it into lists and dictionaries in Python.

<img src="https://video.udacity-data.com/topher/2019/August/5d5dcb03_screen-shot-2019-08-21-at-3.51.37-pm/screen-shot-2019-08-21-at-3.51.37-pm.png" alt="" width="534px">