from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, Optional


class OpinionForm(FlaskForm):
  title = StringField(
      'Название фильма', validators=[DataRequired(), Length(1, 128)]
  )
  text = TextAreaField('Мнение', validators=[DataRequired()])
  source = StringField('Ссылка на источник', validators=[Optional(), Length(1, 256)])
  submit = SubmitField('Добавить')