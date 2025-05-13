from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
# from sqlalchemy.ext.declarative import declarative_base

# Base = declarative_base()

db = SQLAlchemy()

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)


def init_db(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()


# class Games(Base):
#     __tablename__ = 'all_games'
#     row_id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String)
#     descp = db.Column(db.String)
#     clean_price = db.Column(db.String)
#     perc_discount = db.Column(db.String)
#     img = db.Column(db.String)
#     store = db.Column(db.String)
#     pass