from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.secret_key = 'Sigma'

class NameForm(FlaskForm):
    name = StringField('Enter your name:', validators=[DataRequired()])
    email = StringField('Enter your email:', validators=[DataRequired()])
    feedback = StringField('Enter feedback:', validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        feedback = form.feedback.data
        return f'Hello, {name}! Thank you for your feedback: "{feedback}". Our response will be sent to your email: {email}.'

    return render_template('home.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
