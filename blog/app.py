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

@app.route('/CrearCuenta')
def registro():
    return render_template('createUser.html')

@app.route('/recuperarCuenta')
def forgetPassword():
    return render_template('forgetPassword.html')
    
@app.route('/create')
def createBlog():
    return render_template('createBlog.html')

@app.route('/resultados', methods=['GET'])
def search():
    return render_template('search.html')

if __name__ == '__main__':
    app.run()
