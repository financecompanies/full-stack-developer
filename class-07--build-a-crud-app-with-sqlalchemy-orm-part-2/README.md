# Build a CRUD App with SQLAlchemy ORM - Part 2

## Updating a Todo Item: Part I

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

