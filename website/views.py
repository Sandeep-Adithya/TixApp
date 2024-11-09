from flask import Blueprint, render_template, request, flash, jsonify, abort, redirect, url_for, jsonify
from flask_login import login_required, current_user, set_login_view
from .models import *
#from . import db
import json
from functools import wraps
from datetime import datetime

views = Blueprint('views', __name__)

# def admin_login_required(func):
#     @wraps(func)
#     def decorated_view(*args, **kwargs):
#         if not current_user.is_authenticated or not current_user.is_admin:
#             abort(403)  # return a 403 Forbidden error if the user is not an admin
#         return func(*args, **kwargs)
#     return login_required(decorated_view)



@views.route('/', methods=['GET', 'POST'])
def home():
    movies = Movie.query.all()
    if current_user.is_authenticated:
        if current_user.role == 'user':
            return render_template("home.html", user=current_user, movies=movies)
        else:
            return redirect(url_for('admin.index'))
    else:
        return render_template('index.html',user=current_user, movies=movies)

@views.route('/movies', methods=['GET'])
@login_required
def movies():
    movies = Movie.query.all()
    return render_template("movies.html", user=current_user, movies=movies)

@views.route('/movies/<int:movie_id>', methods=['GET'])
@login_required
def movie(movie_id):
    movie = Movie.query.filter_by(id=movie_id).first()
    return render_template("movie.html", user=current_user, movie=movie)

@views.route('/venues/', methods=['GET'])
@login_required
def venues():
    venue = Venue.query.all()
    return render_template("venue.html", user=current_user, venues=venue)

@views.route('/venues/<int:venue_id>', methods=['GET', 'POST'])
@login_required
def venue(venue_id):

    if request.method == "POST":
        data=request.form
        print(data)

        show_id = data.get('show-id')
        ticket_count = data.get('ticket-count')
        show = Show.query.filter_by(id=show_id).first()

        for i in range(int(ticket_count)):
            if show.venue.capacity > show.tickets_booked :
                ticket = Ticket(user_id=current_user.id, show_id=show.id, venue_id=show.venue.id)
                show.tickets_booked += 1
                db.session.add(ticket)    
        db.session.commit()

    venue = Venue.query.filter_by(id=venue_id).first()
    shows = Show.query.filter_by(venue_id=venue_id).order_by(Show.movie_id).all()
    movie = Show.query.filter_by(venue_id=venue_id).group_by(Show.movie_id).all()
    return render_template("show.html", user=current_user, venue=venue, shows=shows, movie=movie)

@views.route('/movies/<int:movie_id>/book', methods=['GET', 'POST'])
@login_required
def book_movie(movie_id):

    movie = Movie.query.filter_by(id=movie_id).first()
    shows = Show.query.filter_by(movie_id=movie_id).order_by(Show.venue_id).all()
    venue = Show.query.filter_by(movie_id=movie_id).group_by(Show.venue_id).all()

    if request.method == "POST":
        data=request.form
        print(data)

        show_id = data.get('show-id')
        ticket_count = data.get('ticket-count')
        show = Show.query.filter_by(id=show_id).first()

        if int(ticket_count) < (show.venue.capacity-show.tickets_booked):
            for i in range(int(ticket_count)):
                if show.venue.capacity > show.tickets_booked :
                    ticket = Ticket(user_id=current_user.id, show_id=show.id, venue_id=show.venue.id)
                    show.tickets_booked += 1
                    db.session.add(ticket)
        else:
            flash('Request exceeds available amount', category='error')
        db.session.commit()

    
    
    return render_template("book-movie.html", user=current_user, shows=shows, movie=movie, venue=venue)

@views.route('/bookings', methods=['GET'])
@login_required
def bookings():
    tickets = Ticket.query.filter_by(user_id=current_user.id)
    shows = Show.query.all()
    venues = Venue.query.all()
    print(venues)
    print(shows)
    return render_template("bookings.html", user=current_user, tickets=tickets, shows=shows, venues=venues)

@views.route('/api/venues', methods=['GET'])
def get_venues():
    venues = Venue.query.all()
    return jsonify([venue.to_dict() for venue in venues])

@views.route('/api/venues/<int:id>', methods=['GET'])
def get_venue(id):
    venue = Venue.query.get(id)
    if not venue:
        return jsonify({'error': 'Venue not found'}), 404
    return jsonify(venue.to_dict())

@views.route('/api/venues/create', methods=['POST'])
def create_venue():
    data = request.json
    venue = Venue(name=data.get('name'), address=data.get('address'), city=data.get('city'), capacity=data.get('capacity'))
    db.session.add(venue)
    db.session.commit()
    return jsonify(venue.to_dict())

@views.route('/api/venues/<int:id>', methods=['PUT'])
def update_venue(id):
    venue = Venue.query.get(id)
    if not venue:
        return jsonify({'error': 'Venue not found'}), 404
    data = request.json
    venue.name = data.get('name', venue.name)
    venue.address = data.get('address', venue.address)
    venue.city = data.get('city', venue.city)
    venue.capacity = data.get('capacity', venue.capacity)
    db.session.commit()
    return jsonify(venue.to_dict())

@views.route('/api/venues/<int:id>', methods=['DELETE'])
def delete_venue(id):
    venue = Venue.query.get(id)
    if not venue:
        return jsonify({'error': 'Venue not found'}), 404
    db.session.delete(venue)
    db.session.commit()
    return '', 204

@views.route('/api/movies', methods=['GET'])
def get_movies():
    movies = Movie.query.all()
    return jsonify([movie.to_dict() for movie in movies])

@views.route('/api/movies/<int:id>', methods=['GET'])
def get_movie(id):
    movie = Movie.query.get(id)
    if not movie:
        return jsonify({'error': 'Movie not found'}), 404
    return jsonify(movie.to_dict())

@views.route('/api/movies/create', methods=['POST'])
def create_movie():
    data = request.json
    movie = Movie(name=data.get('name'), rating=data.get('rating'), description=data.get('description'), poster=data.get('poster'))
    db.session.add(movie)
    db.session.commit()
    return jsonify(movie.to_dict())

@views.route('/api/movies/<int:id>', methods=['PUT'])
def update_movie(id):
    movie = Movie.query.get(id)
    if not movie:
        return jsonify({'error': 'Movie not found'}), 404
    data = request.json
    movie.name = data.get('name', movie.name)
    movie.rating = data.get('rating', movie.rating)
    movie.description = data.get('description', movie.description)
    movie.poster = data.get('poster', movie.poster)
    db.session.commit()
    return jsonify(movie.to_dict())

@views.route('/api/movies/<int:id>', methods=['DELETE'])
def delete_movie(id):
    movie = Movie.query.get(id)
    if not movie:
        return jsonify({'error': 'Movie not found'}), 404
    db.session.delete(movie)
    db.session.commit()
    return '', 204
