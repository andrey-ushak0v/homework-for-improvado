from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField
from wtforms.validators import DataRequired


class QuestionForm(FlaskForm):
    question = TextAreaField('question text',
                             validators=[DataRequired(
                              message="field don't can be null")])
    submit = SubmitField('send')
