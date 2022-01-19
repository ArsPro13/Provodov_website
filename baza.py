from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__) # объект приложения Flask
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///testdb.db' # привязываем базу данных
db = SQLAlchemy(app) # создаем объект SQLAlchemy

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True, unique=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=True, nullable=False)
    first_name = db.Column(db.String(80), unique=True, nullable=False)
    last_name = db.Column(db.String(80), unique=True, nullable=False)
    adress = db.Column(db.String(80), unique=True, nullable=False)
    phone_number = db.Column(db.String(80), unique=True, nullable=False)
    created_at = db.Column(db.String(80), unique=True, nullable=False)
    lesson_amount = db.Column(db.Integer, nullable=False)
    
    def __repr__(self):
        return f'{self.id} {self.username}'

class cart_item(db.Model):
    cart_item_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    ord_id = db.Column(db.Integer)
    number = db.Column(db.Integer)
    price = db.Column(db.Integer)
    item_id_cart = db.Column(db.Integer)
    lesson_amount = db.Column(db.Integer, nullable=False)
    
    def __repr__(self):
        return f'{self.cart_item_id} {self.item_id_cart} {self.number} {self.price}'

class Item(db.Model):
    item_id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(80), unique=True, nullable=False)
    category = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(80), nullable=False)
    
    def __repr__(self):
        return f'{self.item_id} {self.item_name}'

class orders(db.Model):
    order_id = db.Column(db.Integer, primary_key=True)
    user_id_ord = db.Column(db.Integer)
    amount = db.Column(db.Integer)
    status = db.Column(db.Integer)
    created_at = db.Column(db.String(80), nullable=False)
    
    def __repr__(self):
        return f'{order.id} {self.amount}'



db.create_all()



