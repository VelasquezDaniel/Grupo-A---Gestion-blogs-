#import yagmail as yagmail
from flask import Flask, render_template, flash, request, redirect, url_for
import utils
from db import get_db, close_db
import os
<<<<<<< HEAD
from sqlite3 import Error 
=======
from sqlite3 import Error
>>>>>>> refs/remotes/origin/main

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

<<<<<<< HEAD
@app.route('/CrearCuenta', methods=('GET', 'POST') )
=======
@app.route('/CrearCuenta' , methods=('GET', 'POST'))
>>>>>>> refs/remotes/origin/main
def registro():
    #return render_template('createUser.html')
    try:
        if request.method == 'POST':
            name = request.form['name']
            lastname = request.form['lastname']
            username = request.form['user']
            password = request.form['password']
            confirmPass = request.form['confirmPass']
            email = request.form['email']
            active = True
            error = None
            db = get_db() #Conectarse a la base de datos

            if not utils.isUsernameValid( username ):
                error = "El usuario debe ser alfanumerico o incluir solo '.','_','-'"
                flash( error )
                return render_template( 'createUser.html' )

            if password != confirmPass:
                error = "Las contraseñas no coinciden, por favor verifiquelas"
                flash( error )
                return render_template( 'createUser.html' )    

            if not utils.isPasswordValid( password ):
                error = 'La contraseña debe contenir al menos una minúscula, una mayúscula, un número y 8 caracteres'
                flash( error )
                return render_template( 'createUser.html' )

            if not utils.isEmailValid( email ):
                error = 'Correo invalido'
                flash( error )
                return render_template( 'createUser.html' )

            #Preguntar si el correo no ha sido registrado anteriormente
            if db.execute( 'SELECT usuario_ID FROM usuarios WHERE correo = ?', (email,) ).fetchone() is not None:
                error = 'El correo ya existe'.format( email )
                flash( error )
                return render_template( 'createUser.html' )

            #Preguntar si el usuario existe
            if db.execute( 'SELECT usuario_ID FROM usuarios WHERE usuario = ?', (username,) ).fetchone() is not None:
                error = 'El usuario ya existe'.format( email )
                flash( error )
                return render_template( 'createUser.html' )    

            db.execute(
                'INSERT INTO usuarios (usuario, contraseña, correo, nombre, apellido, activo) VALUES (?,?,?,?,?,?)',
                (username, password, email, name, lastname, active)
            )
            db.commit()
            close_db()
            # yag = yagmail.SMTP('micuenta@gmail.com', 'clave') #modificar con tu informacion personal
            # yag.send(to=email, subject='Activa tu cuenta',
            #        contents='Bienvenido, usa este link para activar tu cuenta ')
            #flash( 'Revisa tu correo para activar tu cuenta' )
            return render_template( 'login.html', user_created="El usuario ha sido creado con exito" )
        return render_template( 'createUser.html' )
    except:
        return render_template( 'createUser.html' )
###################

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

@app.route('/validacion', methods=('GET', 'POST'))
def validacion():
    """if usuario == "admin" and password == "admin":
        return render_template('dashboard.html')
    else:
        flash("Usuario y/o contraseña invalido")
        return render_template('login.html')"""
    try:
        if request.method == 'POST':
            db = get_db()
            error = None
            username = request.form['username']
            password = request.form['password']

            if not username:
                error = 'Debes ingresar el usuario'
                flash( error )
                return render_template( 'login.html' )

            if not password:
                error = 'Contraseña requerida'
                flash( error )
                return render_template( 'login.html' )

            user = db.execute(
                'SELECT * FROM usuarios WHERE usuario = ? AND contraseña = ?', (username, password)
            ).fetchone()

            if user is None:
                error = 'Usuario o contraseña inválidos'
            else:
                return redirect( 'mensajes' )
            flash( error )
        return render_template( 'login.html' )
    except:
        return render_template( 'login.html' )  

if __name__ == '__main__':
    app.run()
