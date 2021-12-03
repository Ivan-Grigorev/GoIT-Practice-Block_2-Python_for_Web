from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length


class NoteForm(FlaskForm):
    note = TextAreaField("Note something to do", validators=[DataRequired(), Length(min=2, max=140)])
    submit = SubmitField('Submit')
