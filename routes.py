from flask import Blueprint, request, jsonify
from models import db, Todo, todo_schema, todos_schema

todo_routes = Blueprint('todo_routes', __name__)

# CREATE a new Todo
@todo_routes.route('/todos', methods=['POST'])
def add_todo():
    data = request.get_json()
    
    if not data or 'title' not in data:
        return jsonify({"error": "Title is required"}), 400

    new_todo = Todo(
        title=data['title'],
        description=data.get('description', ''),
        completed=data.get('completed', False)
    )
    
    db.session.add(new_todo)
    db.session.commit()
    
    return todo_schema.jsonify(new_todo), 201

# READ all Todos
@todo_routes.route('/todos', methods=['GET'])
def get_todos():
    todos = Todo.query.all()
    return todos_schema.jsonify(todos), 200

# READ a single Todo
@todo_routes.route('/todos/<int:id>', methods=['GET'])
def get_todo(id):
    todo = Todo.query.get_or_404(id)
    return todo_schema.jsonify(todo), 200

# UPDATE an existing Todo
@todo_routes.route('/todos/<int:id>', methods=['PUT'])
def update_todo(id):
    todo = Todo.query.get_or_404(id)
    data = request.get_json()

    todo.title = data.get('title', todo.title)
    todo.description = data.get('description', todo.description)
    todo.completed = data.get('completed', todo.completed)

    db.session.commit()
    return todo_schema.jsonify(todo), 200

# DELETE a Todo
@todo_routes.route('/todos/<int:id>', methods=['DELETE'])
def delete_todo(id):
    todo = Todo.query.get_or_404(id)
    db.session.delete(todo)
    db.session.commit()
    return jsonify({"message": "Todo item deleted"}), 200
