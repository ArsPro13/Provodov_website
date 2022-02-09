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
    
    def __repr__(self):
        return f'{self.user_id} {self.username}'

class cart_item(db.Model):
    cart_item_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    ord_id = db.Column(db.Integer)
    number = db.Column(db.Integer)
    price = db.Column(db.Integer)
    item_id_cart = db.Column(db.Integer)
    
    def __repr__(self):
        return f'{self.cart_item_id} {self.item_id_cart} {self.number} {self.price}'

class Item(db.Model):
    item_id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer)
    item_name = db.Column(db.String(80), unique=True, nullable=False)
    category = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(80), nullable=False)
    
    def __repr__(self):
        return f'{self.item_id} {self.item_name}'

class Orders(db.Model):
    order_id = db.Column(db.Integer, primary_key=True)
    user_id_ord = db.Column(db.Integer)
    amount = db.Column(db.Integer)
    status = db.Column(db.Integer)
    created_at = db.Column(db.String(80), nullable=False)
    
    def __repr__(self):
        return f'{self.order_id} {self.amount}'



db.create_all()

Arseniy = User(username='Ars13', password='Qwerty123', first_name='Arseniy', last_name='Provodov', adress='Moscow', phone_number='891347584', created_at='13.06.2021')
Pavel = User(username='Paul223242', password='Qwerty123658', first_name='Paul', last_name='Linuxov', adress='SPB', phone_number='892464844', created_at='25.01.2020')
Anthony = User(username='Kark', password='Qwerty1232343', first_name='Tony', last_name='Stark', adress='New York City', phone_number='8913657433', created_at='03.09.2021')
Shirt = Item(item_name='T-shirt#1', category='T-shirts', description='Perfect pink t-shirt', price=34)
Mouse = Item(item_name='Mouse#1', category='PC', description='A great mouse', price=50)
Pen = Item(item_name='Pen#1', category='Pens', description="The best pen you've ever used", price=5)
order1 = Orders(user_id_ord=1, amount=100, status=1, created_at='13.01.2022')
order2 = Orders(user_id_ord=3, amount=34, status=1, created_at='14.01.2022')
order3 = Orders(user_id_ord=2, amount=55, status=1, created_at='01.02.2022')

db.session.add(Arseniy)
db.session.add(Pavel)
db.session.add(Anthony)
db.session.add(Shirt)
db.session.add(Mouse)
db.session.add(Pen)
db.session.add(order1)
db.session.add(order2)
db.session.add(order3)

print(User.query.all())
print(Item.query.all())
print(Orders.query.all())


