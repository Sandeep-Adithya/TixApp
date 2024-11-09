from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Mtag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'), nullable=True)
    tag_id = db.Column(db.Integer, db.ForeignKey('tag.id'), nullable=True)

class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    #mtag = db.relationship('Mtag', backref='tag')


class Venue(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    address = db.Column(db.String(150))
    city = db.Column(db.String(150))
    capacity = db.Column(db.Integer)
    show = db.relationship('Show', backref='venue')
    ticket = db.relationship('Ticket', backref='venue')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'address': self.address,
            'city': self.city,
            'capacity': self.capacity
        }

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    rating = db.Column(db.Float)
    tags = db.relationship('Tag', secondary='mtag', backref='movies')
    show = db.relationship('Show', backref='movie')
    description = db.Column(db.String(10000), default = "No description available")
    poster = db.Column(db.String(10000), default="/static/assets/img/poster.jpg")

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'rating': self.rating,
            'description': self.description,
            'poster': self.poster
        }

class Show(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'), nullable=False)
    venue_id = db.Column(db.Integer, db.ForeignKey('venue.id'), nullable=False)
    time = db.Column(db.DateTime(timezone=True), default=func.now())
    ticket = db.relationship('Ticket', backref='show')
    tickets_booked = db.Column(db.Integer, default=0)
    ticket_price = db.Column(db.Float, nullable=False)


class Ticket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    show_id = db.Column(db.Integer, db.ForeignKey('show.id'), nullable=False)
    venue_id = db.Column(db.Integer, db.ForeignKey('venue.id'), nullable=False)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    username = db.Column(db.String(150))
    city = db.Column(db.String(150))
    tickets = db.relationship('Ticket', backref='user')
    role = db.Column(db.String(20), default='user')

    