from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FieldList, RadioField, IntegerField, EmailField, validators


class UseForm(Form):
    matricula = StringField("Matricula",[
        validators.DataRequired(message="Campo requerido"),
        validators.Length(min=3, max=10, message="La matricula debe tener entre 3 y 10 caracteres")
    ])
    nombre = StringField("Nombre")
    apellido = StringField("Apellido")
    email= EmailField("Correo",[
        validators.Email(message="Correo invalido")
    ])