from flask import Flask, request, render_template, redirect, flash,session
import requests
import json
from Cadastrar import cadastrar 
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

        response = requests.get(f'{link}/users.json')
        data = response.json()

        if data:
            usuario = next((user for user in data.values() if user['email'] == email), None)
            if usuario:
                senha_criptografada = usuario['senha']

                if bcrypt.check_password_hash(senha_criptografada, senha):
                    session['logged_in'] = True
                    return render_template('/usuario.html')
                else:
                    flash('Senha incorreta.')
                    return redirect('/')  
            else:
                flash('E-mail não encontrado. ')
                return redirect('/') 
        else:
            flash('Nenhum usuário cadastrado.')
            return redirect('/') 
    return redirect('/')
    #Chamar função Cadastro do banco de Dados
@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar_rota():
    return cadastrar()
#############################


if __name__ == "__main__":
    app.run(debug=True)
