from flask import jsonify
import json
from db.models import Order
from utils.logging import logger
from db.repository import add_order, get_all_orders
from .send_order_handler import handle_send_order_by_whatsapp
import json
from bidi.algorithm import get_display

def handle_new_order(request):
    order_data = request.get_json()

    order_details = json.dumps(order_data, indent=4, ensure_ascii=False)
    log_message = f'\nOrder received from url: {request.base_url}\nDetails:\n{order_details.encode('utf-8').decode('utf-8')}'

    # Apply bidirectional algorithm to correctly format the text
    logger.info(get_display(log_message))


    try:
        new_order = Order(order_data)
        # save order to database
        add_order(new_order)

        # send the order using greenAPI
        handle_send_order_by_whatsapp(new_order)

    except KeyError as e:
        return jsonify({'error': f'Missing data for {str(e)}'}), 400
    
    return jsonify(new_order.to_dict()), 200


def handle_get_all_orders():
    return get_all_orders()