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

## Using AJAX to send data to flask

### Takeaways
* Data request are either synchronous or async (asynchronous)
* Async data requests are requests that get sent to the server and back to the client without a page refresh.
* Async requests (AJAX requests) use one of two methods:
  * XMLHttpRequest
  * Fetch (modern way)

### Using `XMLHttpRequest`

#### Code

```javascript
var xhttp = new XMLHttpRequest();

description = document.getElementById("description").value;

xhttp.open("GET", "/todos/create?description=" + description);

xhttp.send();
```

```javascript
xhttp.onreadystatechange = function() {
    if (this.readyState === 4 && this.status === 200) {
      // on successful response
      console.log(xhttp.responseText);
    }
};
```

### Using `fetch`

#### Takeaways
* `fetch` is another window object that lets you send HTTP requests
* `fetch(<url-route>, <object of request parameters>)`

#### Code

```javascript
fetch('/my/request', {
  method: 'POST',
  body: JSON.stringify({
    'description': 'some description here'
  }),
  headers: {
    'Content-Type': 'application/json'
  }
});
```

## Using sessions in controllers

### Takeaways
* Commits can succeed or fail. On fail, we want to rollback the session to avoid potential implicit commits done by the database on closing a connection.
* Good practice is to close connections at the end of every session used in a controller, to return the connection back to the connection pool.

### Pattern (try-except-finally)

 ```python
 import sys

 try:
   todo = Todo(description=description)
   db.session.add(todo)
   db.session.commit()
 except:
   db.session.rollback()
   error=True
   print(sys.exc_info())
 finally:
   db.session.close()
```

### Improving error handling

The route handler should always return something or raise an intentional exception, in the case of an error. To fix this with a simple solution, we can simply import abort from Flask:

`from flask import abort`

and we can call `abort(<status code>)`, e.g. with status code 500, `abort(500)` to rise an HTTPException for an Internal Server Error, in order to abort a request and prevent it from expecting a returned result. Since this is a course on web data modeling, we won't be going into errors in depth, but you can check out resources below.

#### Resources on Error Handling
* [Flask Docs on Application Errors](https://flask.palletsprojects.com/en/1.0.x/errorhandling/)
* [Error Handling in Flask Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-vii-error-handling)

#### Code

```python
from flask import Flask, render_template, abort

# ...

@app.route('/todos/create', method=['POST'])
def create_todo():
  error = False
  body = {}
  try:
    description = request.form.get_json()['description']
    todo = Todo(description=description)
    db.session.add(todo)
    db.session.commit()
    body['description'] = todo.description
  except:
    error = True
    db.session.rollback()
    print(sys.exc_info())
  finally:
    db.session.close()
  if error:
    abort (400)
  else:
    return jsonify(body
```