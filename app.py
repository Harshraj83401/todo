from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# Initialize Flask App
app = Flask(__name__)

# Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todos.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize Database and Marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Define Todo Model
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(500))
    completed = db.Column(db.Boolean, default=False)

# Define Todo Schema for Serialization
class TodoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Todo

todo_schema = TodoSchema()
todos_schema = TodoSchema(many=True)

# Create Database Tables
with app.app_context():
    db.create_all()

# Home Route
@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Todo API"}), 200
