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