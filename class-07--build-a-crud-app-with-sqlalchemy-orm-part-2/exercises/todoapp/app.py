from flask import Flask, render_template, request, redirect, url_for, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
import sys
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://todoapp:todoapp@localhost:5432/todoapp'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Todo(db.Model):
    __tablename__ = 'todos'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(), nullable=False)
    completed = db.Column(db.Boolean, nullable=False, default=False)

    def __repr__(self):
        return f'Todo (id={self.id},  description={self.description})'


@app.route('/')
@app.route('/todos')
def index():
    return render_template('index.html', data=Todo.query.order_by('id').all())


@app.route('/todos/create', methods=['POST'])
def create():
    description = request.get_json().get('description')
    if description:
        error = False
        response = {}
        try:
            new_todo = Todo(description=description)
            db.session.add(new_todo)
            db.session.commit()
            response['description'] = new_todo.description
        except:
            db.session.rollback()
            error = True
            print(sys.exc_info)
        finally:
            db.session.close()

        if error:
            abort(make_error('Sorry, we can\'t process your request', 500))
        else:
            return jsonify(response)
    else:
        abort(make_error('Description is required', 400))


@app.route('/todos/<todo_id>/set-completed', methods=['POST'])
def set_completed(todo_id):
    try:
        completed = request.get_json()['completed']
        todo = Todo.query.get(todo_id)
        todo.completed = completed
        db.session.commit()
    except:
        db.session.rollback()
    finally:
        db.session.close()
    return redirect(url_for('index'))


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


def make_error(message, code):
    json_error = jsonify({
        'code': code,
        'message': message
    })
    json_error.status_code = code
    return json_error


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')