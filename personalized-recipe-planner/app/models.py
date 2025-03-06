from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class UserPreference(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dietary_restrictions = db.Column(db.String(200))
    favorite_cuisine = db.Column(db.String(100))
    meals_per_week = db.Column(db.Integer)

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    ingredients = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user_preference.id'), nullable=False)

    user_preference = db.relationship('UserPreference', backref=db.backref('recipes', lazy=True))