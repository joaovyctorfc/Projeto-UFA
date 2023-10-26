from flask import Flask, request, render_template, redirect, flash,session
import requests
import json
from Cadastrar import cadastrar 
import serial
from flask import jsonify
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta_aqui'
bcrypt = Bcrypt(app)
link = "https://projeto-drone-default-rtdb.firebaseio.com/"
@app.route('/')
def retorno():
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
                    session['user_email'] = email
                    session['user_nome'] = usuario['nome']  

                    return render_template('usuario.html', user_email=email, user_nome=usuario['nome'])
                else:
                    flash('Senha incorreta.')
                    return redirect('/')
            else:
                flash('E-mail não encontrado.')
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
@app.route('/Video', methods=['GET', 'POST'])
def video():
    if 'logged_in' in session and session['logged_in']:
        user_email = session['user_email']  
        user_nome = session['user_nome']
        
        # Criar um dicionário com os dados do vídeo
        video_data = {
            'title': 'Meu Vídeo',
            'imageurl': 'URL_do_video.mp4',
            'email': user_email  # Associar o vídeo ao e-mail do usuário
        }

        # Adicionar video_data ao Firebase Realtime Database ou Firestore
        # Certifique-se de usar o método apropriado aqui para adicionar dados ao Firebase.

        return render_template('Video.html', user_email=user_email, user_nome=user_nome)
    else:
        return redirect('/')
 


########


@app.route('/home', methods=['POST', 'GET'])
def home():
    if 'logged_in' in session and session['logged_in']:
        user_email = session['user_email']  
        user_nome = session['user_nome']  

        return render_template('usuario.html', user_email=user_email, user_nome=user_nome)
    else:
        return redirect('/')
    
@app.route('/Upload', methods=['GET', 'POST'])
def upload():
    if 'logged_in' in session and session['logged_in']:
        user_email = session['user_email']  
        user_nome = session['user_nome']   

        return render_template('upload.html', user_email=user_email, user_nome=user_nome)
    else:
        return redirect('/')
    

@app.route('/senha', methods=['GET', 'POST'])
def senha():
   
        return render_template('Email.html')
  
# Abre a conexão com a porta serial
#ser = serial.Serial('/dev/cu.usbmodem1201', 9600)

#@app.route('/api', methods=['GET'])
#def obter_dados():
    # Lê uma linha da porta serial
   # linha = ser.readline()
    
 #   linha_decodificada = linha.decode('utf-8').strip()
    
    # Retorna os dados como JSON
  #  return jsonify({'dados': linha_decodificada})
if __name__ == "__main__":
    app.run(debug=True)
