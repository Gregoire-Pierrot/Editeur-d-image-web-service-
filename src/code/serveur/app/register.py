from flask_wtf import FlaskForm
from app import app
from wtforms import StringField, PasswordField, validators
from wtforms.validators import DataRequired, Email

class RegisterForm(FlaskForm):
    email = StringField(label='email', validators=[DataRequired(message='* le champ "email" est obligatoire *'), Email(message="* l'email n'est pas valide *")])
    username = StringField(label='username', validators=[DataRequired(message='* le champ "username" est obligatoire *')])
    password = PasswordField(label='password', validators=[DataRequired(message='* le champ "password" est obligatoire *')])
    confirm = PasswordField(label='confirm password', validators=[validators.EqualTo('password', message=('* le champ "confirm" ne correspond pas au "password" *'))])

app.config['SECRET_KEY'] = 'uneChaineQuelconque'