
from flask import Flask, request, render_template, redirect, flash
import requests
import json
from flask_bcrypt import Bcrypt

link = "https://projeto-drone-default-rtdb.firebaseio.com/"

app = Flask(__name__)
bcrypt = Bcrypt(app)

app.config['MAIL_SERVER'] = 'smtp.office365.com'  # Servidor SMTP do SendGrid
app.config['MAIL_PORT'] = 587  # Porta de envio de e-mails
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'connect.fatec@hotmail.com'
app.config['MAIL_PASSWORD'] = 'connect2023'


# Defina a chave secreta aqui
app.secret_key = 'sua_chave_secreta_aqui'
@app.route('/')
def retorno():
    return render_template('login.html')
@app.route('/codigo', methods=['GET', 'POST'])
def codigo():
   
    if request.method == 'POST':
        email = request.form.get('email')
       
        response = requests.get(f'{link}/users.json')
        data = response.json()

        if data:
            usuario = next((user for user in data.values() if user['email'] == email), None)
            if usuario:
             flash('.')
            else:
                flash('Nenhum usuário cadastrado.')


    return render_template('Email.html')
@app.route('/senha', methods=['GET', 'POST'])
def senha():
 flash('Nenhum usuário cadastrado.')

   

 return render_template('Email.html')




  


