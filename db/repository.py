from .db import db
from .models import Order, CandleItem
from flask import jsonify


def add_order(order):
    db.session.add(order)
    db.session.commit()

def get_order_by_id(order_id):
    return Order.query.get(order_id)

def get_all_orders():
    try:
        orders = Order.query.all()
        if not orders:
            return jsonify({"message": "There are no orders."}), 400
        return jsonify([order.to_dict() for order in orders]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    



# local tests
# order_data_json = '''{
#     "phoneNo": "0543333333",
#     "customerName": "Yonatan Kalma",
#     "address": "Tel Aviv",
#     "candleItem": [
#         {
#             "candleName": "Red velvet",
            
#             "quantity": 2,
#             "price": 100
#         },
#         {
#             "candleName": "Red velvet2",
#             "quantity": 1,
#             "price": 200
#         }
#     ]
# }'''
# sample order for testing
# order_data = json.loads(order_data_json)

# # Create an Order instance
# orderddd = Order(phoneNo=order_data['phoneNo'], customerName=order_data['customerName'], address=order_data['address'])
# ordercc = Order(
#     phoneNo=order_data['phoneNo'],
#     customerName=order_data['customerName'],
#     address=order_data['address']
# )