from flask import Flask, render_template, flash, request, redirect, url_for
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/perfil')
def userInf():
    return render_template('userInformation.html')

@app.route('/CrearCuenta')
def registro():
    return render_template('createUser.html')

@app.route('/recuperarCuenta')
def forgetPassword():
    return render_template('forgetPassword.html')
    
@app.route('/cambiarClave')
def changePassword():
    return render_template('changePassword.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/create')
def createBlog():
    return render_template('createBlog.html')

@app.route('/edit', methods=['POST'])
def editBlog():
    return render_template('editBlog.html')

@app.route('/resultados', methods=['GET'])
def search():
    return render_template('search.html')

@app.route('/validacion', methods=['POST'])
def validacion():
    print(request.method)
    usuario = request.form['usuario']
    password = request.form['password']
    if usuario == "admin" and password == "admin":
        return render_template('dashboard.html')
    else:
        flash("Usuario y/o contraseña invalido")
        return render_template('login.html')
    
if __name__ == '__main__':
    app.run()
