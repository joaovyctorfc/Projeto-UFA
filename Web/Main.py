from flask import Flask, request, render_template, redirect, flash,session
import requests
import json
from Cadastrar import cadastrar  # Importe a função cadastrar
from flask_bcrypt import Bcrypt
app = Flask(__name__)
app.secret_key = 'sua_chave_secreta_aqui'
bcrypt = Bcrypt(app)
link = "https://projeto-drone-default-rtdb.firebaseio.com/"
@app.route('/')
def home():
    return render_template('login.html')
    


@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        senha = request.form.get('senha')

        # Recupere a senha criptografada do Firebase com base no e-mail
        response = requests.get(f'{link}/users.json')
        data = response.json()

        if data:
            usuario = next((user for user in data.values() if user['email'] == email), None)
            if usuario:
                senha_criptografada = usuario['senha']

                # Verifique se a senha fornecida corresponde à senha criptografada
                if bcrypt.check_password_hash(senha_criptografada, senha):
                    # Login bem-sucedido, inicie a sessão
                    session['logged_in'] = True
                    return render_template('usuario.html')
                else:
                    flash('Senha incorreta. Tente novamente.')
            else:
                flash('E-mail não encontrado. Verifique seu e-mail.')
        else:
            flash('Nenhum usuário cadastrado.')
    #Chamar função Cadastro do banco de Dados
@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar_rota():
    return cadastrar()
#############################


if __name__ == "__main__":
    app.run(debug=True)
