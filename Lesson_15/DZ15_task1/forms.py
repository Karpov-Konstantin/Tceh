from flask_wtf import FlaskForm
from wtforms import fields, validators, SubmitField
from wtforms_alchemy import ModelForm
from models import *


class UserForm(ModelForm):
    class Meta:
        model = User


class PostForm(ModelForm):
    class Meta:
        model = Post
        include = [
            'user_id',
        ]


class CommentForm(ModelForm):
    submit = SubmitField('Submit')

    class Meta:
        model = Comment
        include = [
            'user_id',
            'post_id',
        ]

