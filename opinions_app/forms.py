from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, Optional


class OpinionForm(FlaskForm):
    title = StringField(
        'Название фильма',
        validators=[DataRequired(), Length(min=1, max=128)]
    )
    text = StringField(
        'Мнение',
        validators=[DataRequired()]
    )
    source = StringField(
        'Источник',
        validators=[Optional(), Length(max=256)]
    )
    submit = SubmitField('Добавить')