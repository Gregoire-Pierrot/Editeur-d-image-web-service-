from flask_wtf import FlaskForm
from app import app
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email

class AccountForm(FlaskForm):
    email = StringField(label='email', validators=[Email(message="* l'email n'est pas valide *")])
    username = StringField(label='username')

app.config['SECRET_KEY'] = 'uneChaineQuelconque'