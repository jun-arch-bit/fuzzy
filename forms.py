from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, FileField
from wtforms.validators import DataRequired, Length, Email


class RegisterForm(FlaskForm):
username = StringField('Username', validators=[DataRequired(), Length(min=3, max=50)])
email = StringField('Email', validators=[DataRequired(), Email()])
password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
submit = SubmitField('Register')


class LoginForm(FlaskForm):
username = StringField('Username', validators=[DataRequired()])
password = PasswordField('Password', validators=[DataRequired()])
submit = SubmitField('Login')


class NoteForm(FlaskForm):
title = StringField('Title', validators=[Length(max=200)])
content = TextAreaField('Content')
submit = SubmitField('Save')


class UploadForm(FlaskForm):
file = FileField('File', validators=[DataRequired()])
submit = SubmitField('Upload')
