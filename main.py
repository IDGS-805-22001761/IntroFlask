from flask import Flask, render_template

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

if __name__ == '__main__':
    app.run(debug=True, port=3000)