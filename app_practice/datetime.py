from datetime import datetime
from flask import Flask,render_template
from flask.ext.moment import Moment
app= Flask (__name__)
moment= Moment(app)
@app.route('/')
def index():
	return render_template('base.html',current_time=datetime.utcnow())
if __name__ == "__main__":
	app.run(debug=True)

