# Build a CRUD App with SQLAlchemy ORM - Part 2

## Updating a Todo Item: Part I

### Implement Updating a Todo Item

[![](https://img.youtube.com/vi/0Xm2VnXRzVk/0.jpg)](https://youtu.be/0Xm2VnXRzVk)

### Takeaways
An update involves setting the attributes of an existing object in the database.

In SQL:

```postgres
UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition;
```

In SQLAlchemy ORM:

```python
user = User.query.get(some_id)
user.name = 'Some new name'
db.session.commit()
```

### Using the Jinja if statement

#### Check out the Jinja Docs
[Click here for the Jinja Docs](http://jinja.pocoo.org/docs/2.10/templates/#if)

#### Starter Code
[Click here: todoapp-migrations.zip](https://video.udacity-data.com/topher/2019/August/5d5dec79_todoapp-migrations/todoapp-migrations.zip)

## Updating a Todo Item: Part II

### Final Code

**app.py**

```python
@app.route('/todos/<todo_id>/set-completed', methods=['POST'])
def set_completed_todo(todo_id):
  try:
    completed = request.get_json()['completed']
    print('completed', completed)
    todo = Todo.query.get(todo_id)
    todo.completed = completed
    db.session.commit()
  except:
    db.session.rollback()
  finally:
    db.session.close()
  return redirect(url_for('index'))
```

**index.html**

```html
<html>
  <head>
    <title>Todo App</title>
    <style>
      .hidden {
        display: none;
      }
      ul {
        list-style: none;
        padding: 0;
        margin: 0;
        width: 300px;
      }
      li {
        clear: both;
      }
      li button {
        -webkit-appearance: none;
        border: none;
        outline: none;
        color: red;
        float: right;
        cursor: pointer;
        font-size: 20px;
      }
      .lists-wrapper, .todos-wrapper {
        display: inline-block;
        vertical-align: top;
      }
    </style>
  </head>
  <body>
    <div class="lists-wrapper">
      <ul id="lists">
        {% for list in lists %}
        <li>
          <a href="/lists/{{ list.id }}">
            {{ list.name }}
          </a>
        </li>
        {% endfor %}
      </ul>
    </div>
    <div class="todos-wrapper">
      <h4>{{ active_list.name }}</h4>
      <form id="form">
        <input type="text" id="description" name="description" />
        <input type="submit" value="Create" />
      </form>
      <div id="error" class="hidden">Something went wrong!</div>
      <ul id="todos">
        {% for todo in todos %}
        <li>
          <input class="check-completed" data-id="{{ todo.id }}" type="checkbox" {% if todo.completed %} checked {% endif %} />
          {{ todo.description }}
        </li>
        {% endfor %}
      </ul>
    </div>
    <script>
      const checkboxes = document.querySelectorAll('.check-completed');
      for (let i = 0; i < checkboxes.length; i++) {
        const checkbox = checkboxes[i];
        checkbox.onchange = function(e) {
          const newCompleted = e.target.checked;
          const todoId = e.target.dataset['id'];
          fetch('/todos/' + todoId + '/set-completed', {
            method: 'POST',
            body: JSON.stringify({
              'completed': newCompleted
            }),
            headers: {
              'Content-Type': 'application/json'
            }
          })
          .then(function() {
            document.getElementById('error').className = 'hidden';
          })
          .catch(function() {
            document.getElementById('error').className = '';
          })
        }
      }
      document.getElementById('form').onsubmit = function(e) {
        e.preventDefault();
        fetch('/todos/create', {
          method: 'POST',
          body: JSON.stringify({
            'description': document.getElementById('description').value
          }),
          headers: {
            'Content-Type': 'application/json'
          }
        })
        .then(function(response) {
          return response.json();
        })
        .then(function(jsonResponse) {
          console.log(jsonResponse);
          const liItem = document.createElement('LI');
          liItem.innerHTML = jsonResponse['description'];
          document.getElementById('todos').appendChild(liItem);
          document.getElementById('error').className = 'hidden';
        })
        .catch(function() {
          document.getElementById('error').className = '';
        })
      }
    </script>
  </body>
</html>
```

### Solution Code
[Download by clicking here: todoapp-updates.zip](https://video.udacity-data.com/topher/2019/August/5d5fc559_todoapp-updates/todoapp-updates.zip)

## DELETE a Todo item - Exercise

### DELETE a todo item: The "D" in CRUD
We're almost done with CRUD!

Learning how to handle deletes in our application implements the last operation of the 4 operations in CRUD.

[![](https://img.youtube.com/vi/23WUhMIaP9c/0.jpg)](https://youtu.be/23WUhMIaP9c)

### Takeaways
**Deletes** deal with removing existing objects in our database

In SQL:

```postgres
DELETE FROM table_name
WHERE condition;
```

In SQLAlchemy ORM:

```python
todo = Todo.query.get(todo_id)
db.session.delete(todo) # or...
Todo.query.filter_by(id=todo_id).delete()
db.session.commit()
```

### Steps we'll implement:
* Loop through every To-Do item and show a delete button
* Pressing the delete button sends a request that includes which to-do item to delete
* The controller takes the user input, and notifies the models to delete the To-Do object by ID
* On successful deletion by the models, the controller should notify the view to refresh the page and redirect to our homepage, showing a fresh fetch of all To-Do items to now exclude the removed item.

### Using the DELETE method
Requests that delete objects should use the method DELETE, as opposed to POST, GET, etc. when sending requests to the server.

## DELETE a Todo item - Solution

### Delete a Todo Item - Solution

**index.html**

```html
<ul id="todos">
  {% for todo in todos %}
  <li>
    <input class="check-completed" data-id="{{ todo.id }}" type="checkbox" {% if todo.completed %} checked {% endif %} />
    {{ todo.description }}
    <button class="delete-button" data-id="{{ todo.id }}">&cross;</button>
  </li>
  {% endfor %}
</ul>
```

In `<script>...</script>` located near the end of the `body`,

```javascript
const deleteBtns = document.querySelectorAll('.delete-button');
  for (let i = 0; i < deleteBtns.length; i++) {
    const btn = deleteBtns[i];
    btn.onclick = function(e) {
      const todoId = e.target.dataset['id'];
      fetch('/todos/' + todoId, {
        method: 'DELETE'
      });
    }
  }
```

**app.py**

```python
@app.route('/todos/<todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
  try:
    Todo.query.filter_by(id=todo_id).delete()
    db.session.commit()
  except:
    db.session.rollback()
  finally:
    db.session.close()
  return jsonify({ 'success': True })
```

### Solution Code
[Download the solution by clicking here: todoapp-updates-deletes.zip](https://video.udacity-data.com/topher/2019/August/5d5fc44f_todoapp-updates-deletes/todoapp-updates-deletes.zip)
To run it:

```bash
$ pip3 install -r requirements.txt
$ FLASK_APP=app.py FLASK_DEBUG=true flask run
```

## db.relationship

[![](https://img.youtube.com/vi/WULi0shD61Q/0.jpg)](https://youtu.be/WULi0shD61Q)

### Takeaways
* SQLAlchemy configures the settings between model relationships once, and generates JOIN statements for us whenever we need them.
* `db.relationship` is an interface offered in SQLAlchemy to provide and configure a mapped relationship between two models.
* `db.relationship` is defined on the parent model, and it sets:
    * the name of its children (e.g. children), for example parent1.children
    * the name of a parent on a child using the backref, for example child1.my_amazing_parent


### Resources
* [Flask-SQLAlchemy - Simple Relationships](https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/#simple-relationships)
* [SQLAlchemy Docs: Relationship API](https://docs.sqlalchemy.org/en/latest/orm/relationship_api.html#sqlalchemy.orm.relationship)

<img src="https://video.udacity-data.com/topher/2019/August/5d5f5ed0_screen-shot-2019-08-22-at-8.34.29-pm/screen-shot-2019-08-22-at-8.34.29-pm.png" alt="" width="705px" class="index--image--1wh9w">

## Configuring Relationships

[![](https://img.youtube.com/vi/QATpsBELc8s/0.jpg)](https://youtu.be/QATpsBELc8s)

### Takeaways
* When calling `child1.some_parent`, SQLAlchemy determines when we load the parent from the database.

#### Why is it important to care about when we load parents?
* Joins are expensive.
* We should avoid having the user idling. **Delays more than 150ms are noticeable**, so milliseconds of performance matter!
* We should make sure the joins happen during a time and place in the UX that doesn't negatively impact the experience too much.

### Lazy loading vs. Eager loading

[![](https://img.youtube.com/vi/oq-Wqp_BSps/0.jpg)](https://youtu.be/oq-Wqp_BSps)

#### Takeaways

**Lazy loading**
* Load needed joined data only as needed. **Default** in SQLAlchemy.
    * Pro: no initial wait time. Load only what you need.
    * Con: produces a join SQL call every time there is a request for a joined asset. Bad if you do this a lot.

**Eager loading**
* Load all needed joined data objects, all at once.
    * Pro: reduces further queries to the database. Subsequent SQL calls read existing data
    * Con: loading the joined table has a long upfront initial load time.

`lazy=True` (lazy loading) is the default option in `db.relationship`:

```python
children = db.relationship('ChildModel', backref='some_parent', lazy=True)
```

#### Other loading options we can use
See [the SQLAlchemy Docs on Relationship Loading Techniques(https://docs.sqlalchemy.org/en/latest/orm/loading_relationships.html)] for more loading options.

### Other relationship options: `collection_class` and `cascade`

[![](https://img.youtube.com/vi/qywsiQi6lvk/0.jpg)](https://youtu.be/qywsiQi6lvk)

#### SQLAlchemy Docs on Relationship Options
* [SQLALchemy ORM Relationship Docs](https://docs.sqlalchemy.org/en/13/orm/relationship_api.html#sqlalchemy.orm.relationship)


#### Takeaways

**`db.relationship`**
* Allows SQLAlchemy to identity relationships between models
* Links relationships with backrefs (`child1.some_parent`)
* Configures relationship dynamics between parents and children, including options like `lazy`, `collection_class`, and `cascade`

## Foreign Key Constraint Setup

### Setting up the Foreign Key Constraint

[![](https://img.youtube.com/vi/ovI5b7j-Oqc/0.jpg)](https://youtu.be/ovI5b7j-Oqc)

#### Takeaways
* `db.relationship` does not set up foreign key constraints for you. We need to add a column, `some_parent_id`, on the **child** model that has a foreign key constraint
* Whereas we set ``db.relationship`` on the **parent** model, we set the foreign key constraint on the child model.
* A foreign key constraint prefers **referential integrity** from one table to another, by ensuring that the foreign key column always maps a primary key in the foreign table.

<img src="https://video.udacity-data.com/topher/2019/August/5d5f62cd_screen-shot-2019-08-22-at-8.51.27-pm/screen-shot-2019-08-22-at-8.51.27-pm.png" alt="" width="774px" class="index--image--1wh9w">

### `db.ForeignKey` question

[![](https://img.youtube.com/vi/oVuHm3rNxKI/0.jpg)](https://youtu.be/oVuHm3rNxKI)

#### `db.ForeignKey`
* Option in db.column to specify a foreign key constraint, referring to the primary key of the other table / model
* Gets defined on the Child model

<img src="https://video.udacity-data.com/topher/2019/August/5d5faa19_screen-shot-2019-08-23-at-1.55.35-am/screen-shot-2019-08-23-at-1.55.35-am.png" alt="" width="716px" class="index--image--1wh9w">

### Resources
* [SQLAlchemy Docs on Defining Constraints](https://docs.sqlalchemy.org/en/latest/core/constraints.html)

### Applying what we learned to an example

[![](https://img.youtube.com/vi/XXy8hL0d30c/0.jpg)](https://youtu.be/XXy8hL0d30c)

#### Solution

```python
class Driver(db.Model):
    __tablename__ = 'drivers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    state = db.Column(db.String(2), nullable=False)
    issued = db.Column(db.Date, nullable=False)
    vehicles = db.relationship('Vehicle', back_ref='driver', lazy=True)

class Vehicle(db.Model):
    __tablename__ = 'vehicles'
    id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String(), nullable=False)
    model = db.Column(db.String(), nullable=False)
    year = db.Column(db.Integer), nullable=False)
    driver_id = db.Column(db.Integer, db.ForeignKey('drivers.id'), nullable=False)
```