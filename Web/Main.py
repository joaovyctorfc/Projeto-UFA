from flask import Flask, request, render_template, redirect, flash
import requests
import json
from Cadastrar import cadastrar  # Importe a função cadastrar

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta_aqui'

link = "https://projeto-drone-default-rtdb.firebaseio.com/"
@app.route('/')
def home():
    return render_template('login.html')
    


@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    senha = request.form.get('senha')

    if email and senha:
        response = requests.get(f'{link}/users.json')
        usuarios = response.json()
        
        if usuarios:
            for usuario_id, dados in usuarios.items():
                if dados.get('email') == email and dados.get('senha') == senha:
                    print(f"Usuário logado: {email}")
                    return render_template('usuario.html')

        flash('Credenciais de login incorretas')
        return redirect('/')
    else:
        flash('Preencha todos os campos')
        return redirect('/')
    #Chamar função Cadastro do banco de Dados
@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar_rota():
    return cadastrar()  
#############################


if __name__ == "__main__":
    app.run(debug=True)
