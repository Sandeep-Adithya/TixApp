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


# class Note(db.Model):
    # id = db.Column(db.Integer, primary_key=True)
    # data = db.Column(db.String(10000))
    # date = db.Column(db.DateTime(timezone=True), default=func.now())
    # user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class Venue(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    address = db.Column(db.String(150))
    city = db.Column(db.String(150))
    capacity = db.Column(db.Integer)
    show = db.relationship('Show', backref='venue')
    ticket = db.relationship('Ticket', backref='venue')

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    rating = db.Column(db.Float)
    tags = db.relationship('Tag', secondary='mtag', backref='movies')
    show = db.relationship('Show', backref='movie')
    description = db.Column(db.String(10000), default = "No description available")
    poster = db.Column(db.String(10000), default="/static/assets/img/poster.jpg")

class Show(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'), nullable=False)
    venue_id = db.Column(db.Integer, db.ForeignKey('venue.id'), nullable=False)
    time = db.Column(db.DateTime(timezone=True), default=func.now())
    ticket = db.relationship('Ticket', backref='show')

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
    # notes = db.relationship('Note')
    


# class Dummy(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(150))
#     venue_id = db.Column(db.Integer, db.ForeignKey('venue.id'))


    # venue = db.relationship('Venue', backref=db.backref('tickets_venue', lazy='dynamic'))
    # show = db.relationship('Show', backref=db.backref('tickets_show', lazy='dynamic'))
    # user = db.relationship('User', backref=db.backref('tickets_user', lazy='dynamic'))

    # def __repr__(self):
    #     return f"Ticket {self.id} - {self.show.name} at {self.venue.name} for {self.user.email}"