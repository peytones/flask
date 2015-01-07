import os
from flask.ext.mail import Mail, Message
mail=Mail(app)
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['FLASKY_MAIL_SUBJECT_PREFIX'] = '[Peyton]'
app.config['FLASKY_MAIL_SENDER'] = 'Peyton Sarmiento <peytonsarmiento@gmail.com'

def send_email(to, subject, template, **kwargs):
        msg = Message(app.config['FLASKY_MAIL_SUBJECT_PREFIX'] + subject, sender=app.config['FLASKY_MAIL_SENDER'], recipients=[to])
        msg.body = render_template(template+ '.txt' , **kwargs)
        msg.html = render_template(template + '.html' , **kwargs)
        mail.send(msg)
