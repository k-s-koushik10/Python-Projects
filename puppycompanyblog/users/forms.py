from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError
from flask_wtf.file import FileField,FileAllowed
from flask_login import current_user
from puppycompanyblog.models import User

class LoginForm(FlaskForm):

    email = StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    submit = SubmitField('Login')

class Registeration(FlaskForm):

    email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('UserName', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(),EqualTo('pass_confirm',message='Passwords must match')])
    pass_confirm = PasswordField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField('Register')

    def validate_email(self,email):
        if User.query.filter_by(email=self.email.data).first():
            raise ValidationError('Email is already registered!')

    def validate_username(self,username):
        if User.query.filter_by(username=self.username.data).first():
            raise ValidationError('Username is already registered!')

class UpdateUserForm(FlaskForm):

    email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('UserName', validators=[DataRequired()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg','png'])])
    submit = SubmitField('Update')

    def validate_email(self,email):
        if User.query.filter_by(email=self.email.data).first():
            raise ValidationError('Email is already registered!')

    def validate_username(self,username):
        if User.query.filter_by(username=self.username.data).first():
            raise ValidationError('Username is already registered!')
