import os

from flask import Flask, render_template

from app.forms import QuestionForm
from app.ml_model import find_answer, model, open_txt

SECRET_KEY = os.urandom(32)
app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY


@app.route('/', methods=['GET', 'POST'])
def index():
    form = QuestionForm()
    if form.validate_on_submit():
        return (find_answer(form.question.data, open_txt(), model))
    return render_template('index.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)

app.run()
