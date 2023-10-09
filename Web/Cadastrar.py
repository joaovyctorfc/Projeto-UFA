from flask import Flask, request, render_template, redirect, flash
import requests
import json
app = Flask(__name__)

link = "https://projeto-drone-default-rtdb.firebaseio.com"
@app.route('/cadastrar')
def cadastrar():
    return render_template('cadastrar.html')