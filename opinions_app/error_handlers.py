from flask import render_template
from opinions_app import db


# Можно подключить позже через app.errorhandler
def page_not_found(e):
  return render_template('404.html'), 404


def internal_server_error(e):
  db.session.rollback()
  return render_template('500.html'), 500