from flask import Flask, request, render_template
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite'

# initialize the database connection
database = SQLAlchemy(app)

# initialize database migration management
MIGRATE = Migrate(app, database)

from models import *

@app.route('/')
def view_registered_guests():
    guests = Guest.query.all()
    return render_template('guest_list.html', guests=guests)


@app.route('/register', methods = ['GET'])
def view_registration_form():
    return render_template('guest_registration.html')


@app.route('/register', methods = ['POST'])
def register_guest():
    name = request.form.get('name')
    email = request.form.get('email')
    group_size = request.form.get('group_size')
    if not group_size or group_size=='':
        group_size = 1

    guest = Guest(name, email, group_size)
    database.session.add(guest)
    database.session.commit()

    return render_template('guest_confirmation.html',
        name=name, email=email, group_size=group_size)
