from flask import Flask, render_template, request

app=Flask(__name__)

@app.route('/')
def index():
    titulo="IDGS805"
    lista=["pedro","juan","luis"]
    return render_template('index.html',titulo=titulo,lista=lista)

@app.route('/Hola')
def hola():
    return '<h1>Hola, niñ@!</h1>'

@app.route('/user/<string:username>')
def user(username):
    return f'Hola, {username}!'

@app.route('/suma/<int:num1>')
def numero(num1):
    return f'El número es: {num1}'

@app.route('/user/<int:id>/<string:username>')
def user_id(id, username):
    return f'El ID: {id}, con el nombre: {username}!'

@app.route('/suma/<float:n1>/<float:n2>')
def suma(n1, n2):
    return f'La suma es: {n1 + n2}'

@app.route('/default/')
@app.route('/default/<string:tem>')
def default(tem='Pedro'):
    return f'Hola, {tem}!'

@app.route('/form1')
def form1():
    return '''
        <form>
        <label for="nombre">Nombre:</label>
        <input type="text" id="nombre" name="nombre"><br><br>
        <label for="apellido">Apellido:</label>
        <input type="text" id="apellido" name="apellido"><br><br>

'''
@app.route('/ejemplo1')
def ejemplo1():
    return render_template('ejemplo1.html')

@app.route('/ejemplo2')
def ejemplo2():
    return render_template('ejemplo2.html')

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

if __name__ == '__main__':
    app.run(debug=True, port=3000)