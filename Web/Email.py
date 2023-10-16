
from flask import Flask, request, render_template, redirect, flash
import requests
import json
from flask_bcrypt import Bcrypt

link = "https://projeto-drone-default-rtdb.firebaseio.com/"

app = Flask(__name__)
bcrypt = Bcrypt(app)
# Defina a chave secreta aqui
app.secret_key = 'sua_chave_secreta_aqui'
@app.route('/')
def retorno():
    return render_template('login.html')
@app.route('/email', methods=['GET', 'POST'])
def email():
   
    return render_template('Email.html')




  


