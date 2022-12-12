from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, RadioField
from flask_login import current_user

class LoginForm(FlaskForm):
    username = StringField('Username')
    password = PasswordField('Password')
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign in')

class RegisterForm(FlaskForm):
    username = StringField('Username')
    password = PasswordField('Password')
    submit = SubmitField('Register')
    
class DeleteAccountForm(FlaskForm):
    password = PasswordField('Confirm Password for ')
    submit = SubmitField('Delete Account')

class MessageForm(FlaskForm):
    message = StringField('Message')
    submit = SubmitField('Send')


class SearchForm(FlaskForm):
    query = StringField('Search Query')
    mode = RadioField('Search for: ', choices=[('Users', 'Search for users'), ('Messages', 'Search for messages')])
    submit = SubmitField('Search')
