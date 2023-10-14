
from flask import Flask, request, render_template, redirect, flash
import requests
import json
from flask_bcrypt import Bcrypt

link = "https://projeto-drone-default-rtdb.firebaseio.com/"

app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = 'sua_chave_secreta_aqui'
@app.route('/')
def home():
    return render_template('login.html')
@app.route('/Video', methods=['GET', 'POST'])
def video():
    
    return render_template('Video.html')