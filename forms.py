

from flask_wtf import FlaskForm

# Import fields depending on the types of variables being used
from wtforms import StringField, PasswordField, BooleanField, SubmitField

# Use to valdate the users inputs
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):

    # Define the fields of the form
    # validators=[DataRequired()] ensures field is not empty
    username = StringField('Username', validators=[DataRequired()]) 
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit =SubmitField('Sign in')