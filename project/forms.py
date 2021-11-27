from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Sign in')

class SignupForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators =[DataRequired()])
    submit = SubmitField('Register')

class CreateFlash(FlaskForm):
    title = Stringfield('Title', validators=[DataRequired()])
    body = Stringfield('Body', validators=[DataRequired()])
    submit = SubmitField('Create')

class ShareForm(FlaskForm):
    UserShare = StringField('User', validators=[DataRequired()])
    FlashTitles = Stringfield('FlashCard', validators=[DataRequired()])
    submit = SubmitField('Share')



