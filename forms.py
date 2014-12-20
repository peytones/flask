from flask.ext.bootstrap import Bootstrap
from flask import Flask, render_template, session, redirect, url_for
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required
 
app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
class NameForm(Form):
	name= StringField('What is your name?', validators=[Required()])
	submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
	form = NameForm()
	if form.validate_on_submit():
		session['name']=form.name.data
		return redirect(url_for('index'))
	return render_template('form.html',form=form,name=session.get('name'))
bootstrap=Bootstrap(app)
if __name__ == "__main__":
	app.run(debug=True)
