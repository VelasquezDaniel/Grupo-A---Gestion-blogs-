import pdfkit #para pdf
#path_wkhtmltopdf = 'venv\\include\\wkhtmltopdf\\bin\\wkhtmltopdf.exe'
#config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
resultado = {}
import functools
import datetime

from flask import Flask, render_template, flash, request, redirect, url_for, jsonify, session, send_file, current_app, g, make_response
import utils
from db import get_db, close_db
import os
from sqlite3 import Error
import yagmail as yagmail


app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=('POST','GET'))
def login():
    return render_template('login.html')

@app.route('/validacion', methods=('GET', 'POST'))
def validacion():
    try:
        if g.user:
            return redirect( url_for( 'dashboard' ) )
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

            user = db.execute('SELECT * FROM usuarios WHERE usuario = ? AND contraseña = ?',(username, password)).fetchone()

            if user is None:
                error = 'Usuario o contraseña inválidos'
            else:
                session.clear()
                session['usuario_ID'] = user[0]
                session['username'] = user[1]
                session['correo'] = user[3]
                session['nombre'] = user[4]
                session['apellido'] = user[5]
                return redirect(url_for('dashboard'))
            flash( error )
        return render_template( 'login.html' )    
    except:
        return render_template( 'login.html' )  


def login_required(view):
    @functools.wraps( view )
    def wrapped_view():
        if g.user is None:
            return redirect( url_for( 'login' ) )
        return view( )
    return wrapped_view 
    
@app.route('/perfil')
@login_required
def userInf():
    return render_template('userInformation.html')


@app.route('/CrearCuenta' , methods=('GET', 'POST'))
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
                error = 'El usuario ya existe'.format( username )
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

@app.route('/recuperarCuenta')
def forgetPassword():
    return render_template('forgetPassword')



@app.route('/sendEmail', methods=('GET', 'POST'))
def sendEmail():
    email = request.form['email']
    db = get_db() #Conectarse a la base de datos

    if not utils.isEmailValid( email ):
                error = 'Correo invalido'
                flash( error )
                return render_template( 'register.html' )


    #Preguntar si el correo no ha sido registrado anteriormente
    if db.execute( 'SELECT id FROM usuarios WHERE correo = ?', (email,) ).fetchone() is not None:
        yag = yagmail.SMTP('micuenta@gmail.com', 'clave') #modificar con tu informacion personal
        yag.send(to=email, subject='Recupera tu cuenta',
        contents='Bienvenido, usa este link para entrar a tu cuenta ')
    return render_template('forgetPassword')




@app.route('/cambiarClave')
@login_required
def changePassword():
    return render_template('changePassword.html')

    
@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

@app.route('/create')
@login_required
def createBlog():
    return render_template( 'createBlog.html' )

@app.route('/createBlog')
@login_required
def crearBlog():
    try:
        if request.method == 'POST':
            titulo = request.form['titulo']
            cuerpo = request.form['cuerpo']
            imagen = "No hay" #DEBEMOS MODIFICAR ESTO
            etiquetas = "Modificar etiquetas"
            usuarioCreador = session['usuario_ID']
            likes = 0
            fechaCreacion = datetime.now()
            error = None
            db = get_db() #Conectarse a la base de datos

            if request.form['privacidad'] == True:
                privado = True
            else:
                privado = False 
            
            if cuerpo is None:
                error = "debe ingresar el titulo del blog"
                flash( error )
                return render_template( 'create.html' )

            if cuerpo is None:
                error = "debe ingresar el cuerpo del blog"
                flash( error )
                return render_template( 'create.html' )

            if privado is None:
                error = "debe seleccionar la privacidad del blog"
                flash( error )
                return render_template( 'create.html' )

            db.execute(
                'INSERT INTO blogs (titulo, imagen, cuerpo, privado, etiquetas, usuarioCreador, likes, fechaCreacion) VALUES (?,?,?,?,?,?,?,?)',
                (titulo, imagen, cuerpo, privado, etiquetas, usuarioCreador, likes, fechaCreacion)
            )
            db.commit()
            close_db()
            # yag = yagmail.SMTP('micuenta@gmail.com', 'clave') #modificar con tu informacion personal
            # yag.send(to=email, subject='Activa tu cuenta',
            #        contents='Bienvenido, usa este link para activar tu cuenta ')
            #flash( 'Revisa tu correo para activar tu cuenta' )
            return render_template( 'dashboard.html', blog_created="El blog ha sido creado con exito" )
        return render_template( 'createBlog.html' )
    except:
        return render_template( 'createBlog.html' )       
def search():
    return render_template('search.html')

@app.before_request
def load_logged_in_user():
    user_id = session.get( 'usuario_ID' )

