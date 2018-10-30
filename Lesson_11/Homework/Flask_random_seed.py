from flask import Flask, request
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, validators

import os
import random


class ContactForm(FlaskForm):
    try_answer = IntegerField(label='Try_answer', validators=[])
#print(type(ContactForm.try_answer))


app = Flask(__name__)
app.config.update(
    DEBUG=True,
    WTF_CSRF_ENABLED=False
)

val_seed = os.environ['FLASK_RANDOM_SEED'],

random.seed(val_seed)
REAL_ANSWER = random.randint(0, 10)


@app.route('/', methods=['GET'])
def home():
    if request.method == 'GET':
        return 'Число загадано'


@app.route('/gues', methods=['POST'])
def quiz():

    if request.method == 'POST':
        print(request.form)
        form = ContactForm(request.form)
        print(form.validate())

        if form.validate():
            if form.try_answer.data == quiz.local_real_answer:
                quiz.local_real_answer = random.randint(0,10)
                return ('Число угадано')
            elif form.try_answer.data > REAL_ANSWER:
                print(quiz.local_real_answer)
                return ('Число меньше')
            else:
                print(quiz.local_real_answer)
                return ('Число больше')
        else:
            return ('invalid', 400)

quiz.local_real_answer = REAL_ANSWER

if __name__ == '__main__':
    app.run()

