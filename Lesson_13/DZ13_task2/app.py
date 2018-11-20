# -*- coding: utf-8 -*-

from flask import Flask, request, render_template, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
import config as config
from forms import *


app = Flask(__name__, template_folder='templates')
app.config.from_object(config)

# http://flask-sqlalchemy.pocoo.org/2.1/quickstart/#a-minimal-application
db = SQLAlchemy(app)


@app.route('/items', methods=['GET', 'POST'])
def index():

    # user = User.query.filter(id=posts[0].user_id)
    # user = posts[0].user

    if request.method == 'POST':
        print(request.form)
        form = GuestBookForm(request.form)

        if form.validate():
            note = GuestBookItem(**form.data)
            db.session.add(note)
            db.session.commit()

            print('Note created!')
        else:
            print('Form is not valid! Note was not created.')
            print(str(form.errors))


    notes = GuestBookItem.query.all()
    for note in notes:
        #note = GuestBookItem.query.filter_by(id=note.id).first()
        print(note.id, note)

    return jsonify([n.to_dict() for n in notes])
    #     jsonify({
    #     'people': [p.to_json() for p in people],
    #     'by_name': by_name.to_json(),
    #     'by_age': [p.to_json() for p in by_age],
    #     'by_job': [p.to_json() for p in by_job],
    #
    #     'youngest': youngest.to_json(),
    # })




if __name__ == '__main__':

    from models import *
    db.create_all()

    notes = GuestBookItem.query.all()
    print(list(map(str, notes)))

    # Running app:
    app.run()
