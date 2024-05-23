from flask import Blueprint, request
from services.order_service_handler import handle_new_order, handle_get_all_orders
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask import jsonify
from utils.logging import logger
import os

order_blueprint = Blueprint('order_blueprint', __name__)

auth = HTTPBasicAuth()

# Verification callback
@auth.verify_password
def verify_password(username, password):
    if username == os.getenv('API_USERNAME') and password == os.getenv('API_PASSWORD'):
        return True
    logger.error("Username or password is incorrect")  # This is just for debugging purposes
    return False


@auth.error_handler
def auth_error(status):
    return jsonify({"error": "Unauthorized access", "message": "Username or password is incorrect"}), 401


@order_blueprint.route("/", methods=['POST'])
@auth.login_required
def new_order():
    return handle_new_order(request)

@order_blueprint.route("/allOrders", methods=['GET'])
@auth.login_required
def get_all_orders():
    return handle_get_all_orders()


@order_blueprint.route("/test", methods=['GET'])
def get_test():
    return "test passed"