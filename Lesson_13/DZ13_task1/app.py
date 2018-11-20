# -*- coding: utf-8 -*-

from flask import Flask, request, render_template, flash
from flask_sqlalchemy import SQLAlchemy
import config as config
from forms import *


app = Flask(__name__, template_folder='templates')
app.config.from_object(config)

# http://flask-sqlalchemy.pocoo.org/2.1/quickstart/#a-minimal-application
db = SQLAlchemy(app)


@app.route('/', methods=['GET'])
def index():

    # user = User.query.filter(id=posts[0].user_id)
    # user = posts[0].user
    users = User.query.all()

    for user in users:
        user = User.query.filter_by(id=user.id).first()
        print(user, user.message)
        #user = post.user
    print(users)
    return render_template('home.txt', users=users)


@app.route('/create', methods=['POST'])
def add_user():

    print(request.form)
    form = UserForm(request.form)

    if form.validate():
        user = User(**form.data)
        db.session.add(user)
        db.session.commit()
        #flash('Post created!')
        print('Post creaated')
    else:
        print('Form is not valid! Post was not created.')
        #flash('Form is not valid! Post was not created.')
        #flash(str(form.errors))

    # user = User.query.filter(id=posts[0].user_id)
    # user = posts[0].user


def populate_db():
    print('Creating default user')
    # Creating new ones:
    ivan = User(username='Ivan', message='Lalala 5 chars')
    misha = User(username='Misha', message='Second letter')

    db.session.add(ivan)
    db.session.add(misha)
    db.session.commit()  # note


if __name__ == '__main__':

    from models import *
    db.create_all()
    if User.query.count() == 0:
        populate_db()


    users = User.query.all()
    print(list(map(str, users)))

    # Running app:
    app.run()
