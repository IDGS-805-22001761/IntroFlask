from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FieldList, RadioField, integerField

class UserForm(Form):
    matricula = StringField('Matricula')
    nombre = integerField('Nombre')
    apellido = SubmitField('Apellido')
    email = StringField('Email')
    

