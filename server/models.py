from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates
from sqlalchemy.ext.hybrid import hybrid_property
from config import db, bcrypt
# db = SQLAlchemy()

# class Trainer(db.Model, SerializerMixin):
#     __tablename__ = 'trainers'

#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String)

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    workout_id = db.Column(db.Integer, db.ForeignKey('workouts.id'))
    name = db.Column(db.String)
    email = db.Column(db.String)
    _password_hash = db.Column(db.String)
    # admin = db.Column(db.String, default=False)

    @hybrid_property 
    def password_hash(self):
        return self._password_hash
    
    @password_hash.setter
    def password_hash(self, password):
        password_hash = bcrypt.generate_password_hash(password.encode('utf-8'))
        self._password_hash = password_hash.decode('utf-8')
    
    def authenticate(self, password):
        return bcrypt.check_password_hash(self._password_hash, password.encode('utf-8'))

# from app import bcrypt 
class Trainer(db.Model, SerializerMixin):
    __tablename__ = "trainers"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    image = db.Column(db.String)
    bio = db.Column(db.String)

class Workout(db.Model, SerializerMixin):
    __tablename__ = 'workouts'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    time = db.Column(db.DateTime, server_default=db.func.now())
    description = db.Column(db.String)
    trainer_id = db.Column(db.Integer, db.ForeignKey('trainers.id'))

    # trainers = db.relationship('Trainer', backref='workout')
