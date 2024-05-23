from flask import Flask
from db import db
from routes.order_routes import order_blueprint
from flask import Flask
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import create_engine
from dotenv import load_dotenv


db_session = None

def create_app():

    app = Flask(__name__)

    app.register_blueprint(order_blueprint)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///orders.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])

    db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

    db.init_db(app)
    load_dotenv()
    
    return app