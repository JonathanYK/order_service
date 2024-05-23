from .db import db

class CandleItem(db.Model):
    __tablename__ = 'candle_items'
    id = db.Column(db.Integer, primary_key=True)
    candleName = db.Column(db.String(80), nullable=False)
    color = db.Column(db.String(80), nullable=False)
    smell = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(80), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'), nullable=False)  # Ensure FK is correct

    @staticmethod
    def from_dict(data):
        return CandleItem(
            candleName=data.get('candleName'),
            color=data.get('color'),
            smell=data.get('smell'),
            description=data.get('description'),
            quantity=data.get('quantity'),
            price=data.get('price')
        )

    def to_dict(self):
        return {
            "candleName": self.candleName,
            "color": self.color,
            "smell": self.smell,
            "description": self.description,
            "quantity": self.quantity,
            "price": self.price
        }

class Order(db.Model):
    __tablename__ = 'orders'  # Changed to 'orders' to avoid SQL reserved keyword issues
    id = db.Column(db.Integer, primary_key=True)
    phoneNo = db.Column(db.String(120), nullable=False)
    customerName = db.Column(db.String(120), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    candleItems = db.relationship('CandleItem', backref='order', lazy=True)  # Changed to candleItems

    def __init__(self, order_data):
        self.phoneNo = order_data.get('phoneNo')
        self.customerName = order_data.get('customerName')
        self.address = order_data.get('address')
        self.candleItems = [CandleItem.from_dict(item) for item in order_data.get('candleItem', [])]

    def to_dict(self):
        return {
            "phoneNo": self.phoneNo,
            "customerName": self.customerName,
            "address": self.address,
            "candleItems": [item.to_dict() for item in self.candleItems]
        }

    @staticmethod
    def from_dict(data):
        order = Order(
            phoneNo=data['phoneNo'],
            customerName=data['customerName'],
            address=data['address']
        )
        candle_items_data = data.get('candleItem', [])
        order.candleItems = [CandleItem.from_dict(item) for item in candle_items_data]
        return order