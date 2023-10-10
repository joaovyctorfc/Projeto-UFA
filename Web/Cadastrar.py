
from flask import Flask, request, render_template, redirect, flash
import requests
import json

link = "https://projeto-drone-default-rtdb.firebaseio.com/"

app = Flask(__name__)

# Defina a chave secreta aqui
app.secret_key = 'sua_chave_secreta_aqui'
@app.route('/')
def home():
    return render_template('login.html')
def cadastrar():
    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        senha = request.form.get('senha')

        if not nome or not email or not senha:
            flash('Preencha todos  os campos.')
        else:
            dados = {'nome': nome, 'email': email, 'senha': senha}
            criar = requests.post(f'{link}/users.json', data=json.dumps(dados))

            if criar.status_code == 200:
                flash('Usuário cadastrado com sucesso.')
            else:
                print(f'Falha ao cadastrar usuário .Status Code: {criar.status_code}')
                flash('Falha ao cadastrar usuário ')

    return render_template('cadastrar.html')

if __name__ == "__main__":
    app.run(debug=True)


