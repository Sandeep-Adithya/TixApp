from flask import Flask, redirect, url_for
from flask_sqlalchemy import SQLAlchemy 
from os import path
from flask_login import LoginManager, current_user
from flask_admin import Admin,  AdminIndexView, expose
from flask_admin.contrib.sqla import ModelView
from flask_wtf import FlaskForm
import requests
from wtforms import StringField, DateTimeField
from wtforms_sqlalchemy.fields import QuerySelectField, QuerySelectMultipleField
from wtforms.validators import DataRequired
from datetime import datetime
from requests import request
from sqlalchemy import func


db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .views import views
    from .auth import auth
    from .models import User, Venue, Ticket, Show ,Movie, Tag, Mtag

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    
    with app.app_context():
        db.create_all()

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    try:
        if not current_user.is_authenticated:
            return app.login_manager.unauthorized()
    except:
        pass

    # admin_login_manager = LoginManager()
    # admin_login_manager.init_app(app)
    # admin_login_manager.login_view = 'admin.login'

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    
    class HomeView(AdminIndexView):
        @expose('/')
        def index(self):
            movie= db.session.query(Movie.name, func.count(Ticket.id)).join(Show, Movie.id == Show.movie_id).join(Ticket, Show.id == Ticket.show_id).group_by(Movie.name).order_by(Movie.name.asc()).all()
            venue= db.session.query(Venue.name, func.count(Ticket.id)).join(Ticket, Venue.id == Ticket.venue_id).group_by(Venue.name).order_by(Venue.name.asc()).all()
            return self.render('admin_home.html',movie=movie, venue=venue)

    admin = Admin(app, base_template='baseadmin.html', template_mode='bootstrap4', index_view=HomeView())

    class BaseForm(FlaskForm):
        class Meta:
            csrf = False
        
    class BaseView(ModelView):
        
        can_select_all=True
        column_editable_list=[]
        def is_accessible(self):
            if not current_user.is_authenticated:
                return False
            if current_user.role != 'admin':
                print('not admin')
                return False
            return True
        form_base_class = BaseForm
        def inaccessible_callback(self, name, **kwargs):
            return redirect(url_for('auth.login'))

    class MovieForm(BaseForm):
        name = StringField('Name', validators=[DataRequired()])
        rating = StringField('Rating', validators=[DataRequired()])
        poster = StringField('Poster',default="/static/assets/img/poster.jpg")
        desc = StringField('Description',default = "No description available")
        tags = QuerySelectMultipleField('Tags', query_factory=lambda: Tag.query.all(), get_label='name')

    class MovieView(BaseView):
        form = MovieForm

    class UserForm(BaseForm):
        email = StringField('Email', validators=[DataRequired()])
        password = StringField('Password', validators=[DataRequired()])
        username = StringField('Username', validators=[DataRequired()])
        role = StringField('Role', validators=[DataRequired()])

    class UserView(BaseView):
        form = UserForm

    class VenueForm(BaseForm):
        name = StringField('Name', validators=[DataRequired()])
        address = StringField('Address', validators=[DataRequired()])
        city = StringField('City', validators=[DataRequired()])
        capacity = StringField('Capacity', validators=[DataRequired()])

    class VenueView(BaseView):
        form = VenueForm

    class TagForm(BaseForm):
        name = StringField('Name', validators=[DataRequired()])

    class TagView(BaseView):
        form = TagForm
        
    class ShowForm(BaseForm):
        movie = QuerySelectField('Movie', query_factory=lambda: Movie.query.all(), get_label='name')
        venue = QuerySelectField('Venue', query_factory=lambda: Venue.query.all(), get_label='name')
        time = DateTimeField('Time',validators=[DataRequired()], format='%d-%m-%y %H:%M:00', default=datetime.now().replace(year=datetime.now().year)
    )

    class ShowView(BaseView):
        form = ShowForm
        column_display_pk = True
        column_hide_backrefs = False
        column_list = ('id', 'venue.name', 'movie.name', 'time')
        column_labels = { 'id' : 'ID' , 'venue.name' : 'Venue', 'movie.name' : 'Movie', 'time' : 'Time'}
    
    class TicketView(BaseView):
        can_create = False
        can_edit = False
        column_display_pk = True
        column_hide_backrefs = False
        column_list = ('id', 'venue.name', 'show.movie.name', 'user.username')
        column_labels = { 'id' : 'ID' , 'venue.name' : 'Venue', 'show.movie.name' : 'Movie', 'user.username' : 'User'}

    admin.add_view(UserView(User, db.session))
    admin.add_view(VenueView(Venue, db.session))
    admin.add_view(MovieView(Movie, db.session))
    admin.add_view(ShowView(Show, db.session))
    admin.add_view(TagView(Tag, db.session))
    admin.add_view(TicketView(Ticket, db.session))

    return app

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')

