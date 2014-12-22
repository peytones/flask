import os
{% import 'database.py' %}
from flask.ext.bootstrap import Bootstrap
from flask import Flask, render_template, session, redirect, url_for, flash
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required
from flask.ext.sqlalchemy import SQLAlchemy 
basedir= os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
app.config['SQLALCHEMY_DATABASE_URI'] =\
	'sqlite://' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db=SQLAlchemy(app)
class NameForm(Form):
	name= StringField('What is your name?', validators=[Required()])
	submit = SubmitField('Submit')
class Role(db.Model):
	__tablename__ = 'roles'
	id= db.Column(db.Integer, primary_key=True)
	name= db.Column(db.String(64), unique=True)

	def __repr__(self):
		return '<Role r>' % self,name
class User(db.Model):
	__tablename__='users'
	id=db.Column(db.Integer,primary_key=True)
	username=db.Column(db.String(64), unique=True, index=True)

	def _repr_(self):
		return ',User %r>' % self.username 
@app.route('/', methods=['GET', 'POST'])
def index():
	form = NameForm()
	if form.validate_on_submit():
		user=User.query.filter_by(username=form.name.data).first()
		if user is None:
			user= User(username=form.name.data)
			db.session.add(user)	
			session['known']=False
		else:
			session['known']=True
		session['name']=form.name.data
		form.name.data=''
		return redirect(url_for('index'))
	return render_template('form.html',form=form,name=session.get('name'),known=session.get('known',False))
bootstrap=Bootstrap(app)
if __name__ == "__main__":
	app.run(debug=True)
