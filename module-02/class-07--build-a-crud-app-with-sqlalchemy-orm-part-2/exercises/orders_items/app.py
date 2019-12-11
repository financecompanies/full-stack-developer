from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://orders_items:orders_items@localhost:5432/orders_items'
db = SQLAlchemy(app)

orders_items = db.Table('orders_items',
    db.Column('order_id', db.Integer, db.ForeignKey('orders.id'), primary_key=True),
    db.Column('product_id', db.Integer, db.ForeignKey('products.id'), primary_key=True)
)

class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(), nullable=False, unique=True)
    price = db.Column(db.Numeric(precision=16, scale=2), nullable=False)

    def __repr__(self):
        return f'Product( description={self.description}, price={self.price} )'

class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)
    status = db.Column(db.String(), nullable=False, default='created')
    products = db.relationship('Product', secondary=orders_items, backref=db.backref('orders', lazy=True))

    def __repr__(self):
        return f'Order( status={self.status}, products={self.products} )'
