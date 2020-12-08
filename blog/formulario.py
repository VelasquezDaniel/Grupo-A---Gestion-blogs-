from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Length, Email

class Registro(FlaskForm):
    usuario = StringField('Usuario', 
        validators=[DataRequired(message='No dejar vacío, completar'),
                    Length(min=8,max=30)])
    email = EmailField('Correo', 
        validators=[DataRequired(message='No dejar vacío, completar'),Email()])
    password = PasswordField('Contraseña', 
        validators=[DataRequired(message='No dejar vacío, completar')])
    enviar = SubmitField('Registrarse')