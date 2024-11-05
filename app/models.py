from datetime import datetime as dt

from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(80), unique = True, nullable = False)
    email = db.Column(db.String(120), unique = True, nullable = False)
    password = db.Column(db.String(200), nullable = False)
    orders = db.relationship('Order', backref = 'user', lazy = True)

class Restaurant(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(120), nullable = False)
    menu_items = db.relationship('MenuItem', backref = 'restaurant', lazy = True)

class MenuItem(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(120), nullable = False)
    description = db.Column(db.String(500))
    price = db.Column(db.Float, nullable = False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'), nullable = False)

class Order(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    status = db.Column(db.String(20), nullable = False, default = 'Pending')
    timestamp = db.Column(db.DateTime, default = dt.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
    items = db.relationship('OrderItem', backref = 'order', lazy = True)

class OrderItem(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    quantity = db.Column(db.Integer, nullable = False)
    menu_item_id = db.Column(db.Integer, db.ForeignKey('menu_item.id'), nullable = False)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable = False)