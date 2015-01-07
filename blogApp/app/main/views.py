from datetime import datetime
from flask import render_template, session, redirect ,url_for
from . import main
from ..auth.forms import LoginForm
from .. import db
from ..models import User

@main.route('/', methods=['GET', 'POST'])
def index():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect(url_for('.index'))
    return render_template('base.html', form=form, name=session.get('name'), known=session.get('known', False), current_time=datetime.utcnow())
