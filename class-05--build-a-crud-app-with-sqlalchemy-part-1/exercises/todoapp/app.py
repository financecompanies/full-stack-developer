from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://todoapp:todoapp@localhost:5432/todoapp'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Todo(db.Model):
    __tablename__ = 'todos'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return f'Todo (id={self.id},  description={self.description})'

db.create_all()

@app.route('/')
@app.route('/todos')
def index():
    return render_template('index.html', data=Todo.query.all())


@app.route('/todos/create', methods=['POST'])
def create():
    description = request.get_json().get('description')
    if description:
        new_todo = Todo(description=description)
        db.session.add(new_todo)
        db.session.commit()
        return jsonify({
            'description': new_todo.description
        })

if __name__ == '__main__':
    app.run(debug=True)