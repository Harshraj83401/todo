from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()

# Define Todo model
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(500), nullable=True)
    completed = db.Column(db.Boolean, default=False)

# Define Todo schema for serialization
class TodoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Todo

todo_schema = TodoSchema()
todos_schema = TodoSchema(many=True)
