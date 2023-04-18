from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)


class User(db.Model):
    """User."""

    __tablename__ = "users"

    username = db.Column(db.Integer,
                         primary_key=True,
                         nullable=False,
                         unique=True)
    password = db.Column(db.Text,
                         nullable=False)
    first_name = db.Column(db.String,
                           nullable=False)
    last_name = db.Column(db.String,
                          nullable=False)
    email = db.Column(db.Text, nullable=False)

    class Feedback(db.Model):
        """Feedback."""

    __tablename__ = "feedback"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    title = db.Column(db.String,
                      nullable=False)
    content = db.Column(db.Text,
                        nullable=False)
    username = db.Column(db.String,
                         nullable=False)
