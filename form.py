from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FieldList, RadioField, IntegerField, EmailField, validators

class UseForm(Form):
    nombre = StringField("Nombre", [
        validators.DataRequired(message="Campo requerido"),
        validators.Length(min=3, max=10, message="Ingrese un nombre")
    ])
    APaterno = StringField("Apellido Paterno", [
        validators.DataRequired(message="Campo requerido"),
        validators.Length(min=3, max=10, message="Ingrese un apellido paterno")
    ])
    AMaterno = StringField("Apellido Materno", [
        validators.DataRequired(message="Campo requerido"),
        validators.Length(min=3, max=10, message="Ingrese un apellido materno")
    ])
    dia = IntegerField("Día", [
        validators.DataRequired(message="Campo requerido"),
        validators.NumberRange(min=1, max=31, message="Ingrese un día válido")
    ])
    mes = IntegerField("Mes", [
        validators.DataRequired(message="Campo requerido"),
        validators.NumberRange(min=1, max=12, message="Ingrese un mes válido")
    ])
    ano = IntegerField("Año", [
        validators.DataRequired(message="Campo requerido"),
        validators.NumberRange(min=1900, max=2100, message="Ingrese un año válido")
    ])
    sexo = RadioField("Sexo", choices=[('masculino', 'Masculino'), ('femenino', 'Femenino')], validators=[
        validators.DataRequired(message="Campo requerido")
    ])
