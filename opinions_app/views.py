import random
from flask import Blueprint, abort, flash, redirect, render_template, url_for

from opinions_app import db
from opinions_app.forms import OpinionForm
from opinions_app.models import Opinion

# Создаем Blueprint для маршрутов
main_blueprint = Blueprint('main', __name__)


@main_blueprint.route('/')
def index_view():
  quantity = Opinion.query.count()
  if not quantity:
    return render_template('opinions.html')
  offset = random.randrange(quantity)
  opinion = Opinion.query.offset(offset).first()
  return render_template('opinion.html', opinion=opinion)


@main_blueprint.route('/add', methods=['GET', 'POST'])
def add_opinion_view():
  form = OpinionForm()
  if form.validate_on_submit():
    text = form.text.data
    if Opinion.query.filter_by(text=text).first():
      flash('Такое мнение уже есть в базе данных!')
      return render_template('add_opinion.html', form=form)
    opinion = Opinion(
        title=form.title.data,
        text=text,
        source=form.source.data,
        added_by='WebUser',
    )
    db.session.add(opinion)
    db.session.commit()
    return redirect(url_for('main.opinion_view', id=opinion.id))
  return render_template('add_opinion.html', form=form)


@main_blueprint.route('/opinions/<int:id>')
def opinion_view(id):
  opinion = Opinion.query.get_or_404(id)
  return render_template('opinion.html', opinion=opinion)