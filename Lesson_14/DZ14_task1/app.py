from flask import Flask, request, render_template, flash
from flask_sqlalchemy import SQLAlchemy
import config as config
app = Flask(__name__, template_folder='templates')
app.config.from_object(config)
 # http://flask-sqlalchemy.pocoo.org/2.1/quickstart/#a-minimal-application
db = SQLAlchemy(app)
@app.route('/', methods=['GET', 'POST'])
def index():
    from forms import PostForm

    if request.method == 'POST':
        print(request.form)
        form = PostForm(request.form)
        if form.validate():
            post = Post(**form.data)
            db.session.add(post)
            db.session.commit()
            flash('Post created!')
        else:
            flash('Form is not valid! Post was not created.')
            flash(str(form.errors))

    posts = Post.query.all()
    # user = User.query.filter(id=posts[0].user_id)
    # user = posts[0].user

    for post in posts:
        user_id = post.user_id
        user = User.query.filter_by(id=user_id).first()
        print(user)
        #user = post.user

    return render_template('home.txt', posts=posts)

@app.route('/comment', methods=['GET', 'POST'])
def index2():
    from forms import CommentForm
    if request.method == 'POST':
        print(request.form)
        form = CommentForm(request.form)
        if form.validate():
            comment = Comment(**form.data)
            db.session.add(comment)
            db.session.commit()
            flash('Comment created!')
        else:
            flash('Form is not valid! Comment was not created.')
            flash(str(form.errors))

    comments = Comment.query.all()
    # user = User.query.filter(id=posts[0].user_id)
    # user = posts[0].user

    for comment in comments:
        user_id = comment.user_id
        post_id = comment.post_id
        user = User.query.filter_by(id=user_id).first()
        post = Post.query.filter_by(id=post_id).first()
        print(user, post)

    return render_template('home.txt', comments=comments)


def populate_db():
    print('Creating default user')
    # Creating new ones:
    ivan = User(username='Ivan', email='p@p.com')
    misha = User(username='Misha', email='mi.com')
    sasha = User(username='Sasha', email='sa.com')

    db.session.add(ivan)
    db.session.add(misha)
    db.session.add(sasha)
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