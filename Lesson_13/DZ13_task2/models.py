# -*- coding: utf-8 -*-

from datetime import date

from app import db


class GuestBookItem(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    author = db.Column(db.String(10), unique=True, nullable=False)
    message = db.Column(db.String(120), unique=True, nullable=False)
    date_created = db.Column(db.Date, default=date.today)
    is_visible = db.Column(db.Boolean, default=True, nullable=False)


    def __str__(self):
        return '<User %r id - %s  message:%r>' % (self.author, self.id, self.message )


    def to_dict(self):
        return {
            'id': self.id,
            'author': self.author,
            'message': self.message,
        }

