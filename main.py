from flask import Flask, render_template, request
import forms
import form
from datetime import datetime
app = Flask(__name__)

@app.route('/')
def index():
    titulo="Chi"
    lista=["Pedor","Juan","Pepe"]
    return render_template("index.html", titulo=titulo, lista=lista)

@app.route('/user/<string:user>')
def user(user):
    return f"Hola, {user}"

@app.route('/user/<int:n>/<string:user>')
def username(id,username):
    return f"El usuario es : {username}, con el id: {id}"

@app.route('/suma/<float:n1>/<float:n2>')
def suma(n1,n2):
    return f'La suma es: {n1} + {n2}'

@app.route("/default/")
@app.route("/default/<string:tem>")
def func1(tem='Juan'):
    return f"Hola, {tem}"

@app.route("/form1")
def form1():
    return '''
            <form>
            <label>nombre</label>
            </form>
            '''

@app.route("/ejemplo1")
def ejemplo1():
    return render_template("ejemplo1.html")

@app.route("/ejemplo2")
def ejemplo2():
    return render_template("ejemplo2.html")

@app.route('/OperasBas', methods=['GET', 'POST'])
def operas():
    if request.method == 'POST':
        num1 = request.form.get('n1')
        num2 = request.form.get('n2')
        operacion = request.form.get('operacion')
        if num1 and num2 and operacion:
            num1 = float(num1)
            num2 = float(num2)
            if operacion == 'suma':
                resultado = num1 + num2
            elif operacion == 'resta':
                resultado = num1 - num2
            elif operacion == 'multiplicacion':
                resultado = num1 * num2
            elif operacion == 'division':
                resultado = num1 / num2 if num2 != 0 else 'Error: División por cero'
            else:
                resultado = 'Operación no válida'
            return render_template('OperasBas.html', resultado=resultado, num1=num1, num2=num2, operacion=operacion)
    return render_template('OperasBas.html')

@app.route('/cinepolis', methods=['GET', 'POST'])
def cine():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        numPersonas = int(request.form.get('cantidadC'))
        numBoletos = int(request.form.get('cantidadB'))
        metodo_pago = request.form.get('tarjetaC')

        boletos_maximos = numPersonas * 7
        if numBoletos > boletos_maximos or numBoletos <= 0:
            error = f"El límite es de {boletos_maximos} boletos para {numPersonas} persona(s)."
            return render_template('Cinepolis.html', error=error)

        total = numBoletos * 12
        if numBoletos > 5:
            descuento = total * 0.15
            total -= descuento
        elif numBoletos >= 3:
            descuento = total * 0.10
            total -= descuento

        if metodo_pago == 'si':
            descuento2 = total * 0.10
            total -= descuento2

        return render_template('Cinepolis.html', total=total, nombre=nombre)

    return render_template('Cinepolis.html')

@app.route("/alumnos", methods=["GET","POST"])
def alumnos():
    matr=''
    nom = ''
    ape=''
    email=''
    alumno_clase = forms.UseForm(request.form)
    if request.method == "POST" and alumno_clase.validate():
        matr = alumno_clase.matricula.data
        nom = alumno_clase.nombre.data
        ape = alumno_clase.apellido.data
        email = alumno_clase.email.data
        print('Nombre: {}'.format(nom))
    return render_template("alumnos.html", form= alumno_clase, mat = matr, nom = nom, ape = ape, email = email)

@app.route("/zodiaco", methods=["GET", "POST"])
def zodiaco():
    nombre = ''
    APaterno = ''
    AMaterno = ''
    dia = 0
    mes = 0
    ano = 0
    edad = 0
    signo_chino = ''
    signo_imagen = ''
    zodiaco_clase = form.UseForm(request.form)
    
    if request.method == "POST" and zodiaco_clase.validate():
        nombre = zodiaco_clase.nombre.data
        APaterno = zodiaco_clase.APaterno.data
        AMaterno = zodiaco_clase.AMaterno.data
        dia = zodiaco_clase.dia.data
        mes = zodiaco_clase.mes.data
        ano = zodiaco_clase.ano.data

        today = datetime.today()
        birthdate = datetime(ano, mes, dia)
        edad = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))

        zodiacs = ['Mono', 'Gallo', 'Perro', 'Cerdo', 'Rata', 'Buey', 'Tigre', 'Conejo', 'Dragon', 'Serpiente', 'Caballo', 'Cabra']
        signo_chino = zodiacs[ano % 12]

        signo_imagen = f"static/img/{signo_chino.lower()}.png"

        print(f'Nombre: {nombre} {APaterno} {AMaterno}, Fecha de nacimiento: {dia}/{mes}/{ano}, Edad: {edad}, Signo Chino: {signo_chino}, Imagen: {signo_imagen}')
    
    return render_template("zodiaco.html", form=zodiaco_clase, nombre=nombre, APaterno=APaterno, AMaterno=AMaterno, dia=dia, mes=mes, ano=ano, edad=edad, signo_chino=signo_chino, signo_imagen=signo_imagen)

if __name__ == '__main__':
    app.run(debug=True, port=3000)