from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
db.Model.metadata.clear()

def init_db(app):
    db.init_app(app)
    with app.app_context():
        db.drop_all()
        db.create_all()

    