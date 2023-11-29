from flask import Flask, request, render_template, redirect, flash,session
import requests
import json,re
from Cadastrar import cadastrar 
from flask_mail import Mail, Message
##import serial
from flask import jsonify
from flask_bcrypt import Bcrypt
import random

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta_aqui'
bcrypt = Bcrypt(app)
link = "https://projeto-ufa-default-rtdb.firebaseio.com/"
@app.route('/')
def retorno():
    return render_template('login.html')
    


@app.route('/login', methods=['POST'])
def login():
    try:
        if request.method == 'POST':
            email = request.form.get('email')
            senha = request.form.get('senha')

            response = requests.get(f'{link}/users.json')
            response.raise_for_status()  # Verifica se houve um erro na requisição

            data = response.json()

            if data:
                usuario = next((user for user in data.values() if user.get('email') == email), None)

                if usuario:
                    senha_criptografada = usuario.get('senha')

                    if senha_criptografada and bcrypt.check_password_hash(senha_criptografada, senha):
                        session['logged_in'] = True
                        session['user_email'] = email
                        session['user_nome'] = usuario.get('nome')

                        return render_template('usuario.html', user_email=email, user_nome=usuario.get('nome'))
                    else:
                        flash('Senha incorreta.')
                        return redirect('/')
                else:
                    flash('E-mail não encontrado.')
                    return redirect('/')
            else:
                flash('Nenhum usuário cadastrado.')
                return redirect('/')
        else:
            return redirect('/')
    except Exception as e:
        mensagem_erro = "Ocorreu um erro a tentativa de acesso."
        detalhes_erro = str(e)  # Converta o erro para uma string

        flash(mensagem_erro)
        return render_template('erro.html', mensagem=mensagem_erro, detalhes=detalhes_erro)


    
@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar_rota():
    try:
        return cadastrar()
    except Exception as e:
        mensagem_erro = "Ocorreu um erro ao processar a solicitação."
        detalhes_erro = str(e)  # Converta o erro para uma string

        flash(mensagem_erro)
        return render_template('erro.html', mensagem=mensagem_erro, detalhes=detalhes_erro)

@app.route('/Video', methods=['GET', 'POST'])
def video():
    try:
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
    except Exception as e:
        mensagem_erro = "Ocorreu um erro ao carregar os vídeos."
        detalhes_erro = str(e)  # Converta o erro para uma string

        flash(mensagem_erro)
        return render_template('erro.html', mensagem=mensagem_erro, detalhes=detalhes_erro)
 

#########
@app.route('/home', methods=['POST', 'GET'])
def home():
    try:
        if 'logged_in' in session and session['logged_in']:
            user_email = session['user_email']  
            user_nome = session['user_nome']  

            return render_template('usuario.html', user_email=user_email, user_nome=user_nome)
        else:
            return redirect('/')
    except Exception as e:
        mensagem_erro = "Ocorreu um erro ao processar a solicitação."
        detalhes_erro = str(e)  # Converta o erro para uma string

        flash(mensagem_erro)
        return render_template('erro.html', mensagem=mensagem_erro, detalhes=detalhes_erro)
    
@app.route('/Upload', methods=['GET', 'POST'])
def upload():
    try:
        if 'logged_in' in session and session['logged_in']:
            user_email = session['user_email']  
            user_nome = session['user_nome']   

            return render_template('upload.html', user_email=user_email, user_nome=user_nome)
        else:
            return redirect('/')
    except Exception as e:
        mensagem_erro = "Ocorreu um erro ao fazer upload."
        detalhes_erro = str(e)  # Converta o erro para uma string

        flash(mensagem_erro)
        return render_template('erro.html', mensagem=mensagem_erro, detalhes=detalhes_erro)
    

# Configuração do Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'reconviewads@gmail.com'
app.config['MAIL_PASSWORD'] = 'fdwr jxgw rvtx gsbr'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

# Inicialização do Flask-Mail
mail = Mail(app)

codigos_de_confirmacao = {}

# Gera um código de confirmação
def gerar_codigo():
    return str(random.randint(1000, 9999))

@app.route('/senha')
def redefinicao_senha():
    try:
        return render_template('Email.html')
    except Exception as e:
        mensagem_erro = "Ocorreu um erro ao processar a solicitação."
        detalhes_erro = str(e)  # Converta o erro para uma string

        flash(mensagem_erro)
        return render_template('erro.html', mensagem=mensagem_erro, detalhes=detalhes_erro)

@app.route('/confirmacao', methods=['POST'])
def enviar_codigo():
    try:
        lista_provedores = ["hotmail", "gmail", "outlook"]

        destinatario = request.form['destinatario']
        if not destinatario:
            flash('Por favor, insira um endereço de e-mail.', 'error')
            return render_template('Email.html')
        elif "@" not in destinatario or destinatario.split("@")[1].split(".")[0] not in lista_provedores:
            flash('Por favor, insira um endereço de e-mail válido.', 'error')
            return render_template('Email.html')
        codigo = gerar_codigo()
        codigos_de_confirmacao[destinatario] = codigo

        msg = Message('Código de Confirmação', sender='reconviewads@gmail.com', recipients=[destinatario])
        msg.body = f'Seu código de confirmação é: {codigo}'
        mail.send(msg)

        return render_template('redefinicao_senha.html', destinatario=destinatario, codigo_enviado=True)
    
    except Exception as e:
        mensagem_erro = "Ocorreu um erro ao fazer confirmação."
        detalhes_erro = str(e)  # Converta o erro para uma string

        flash(mensagem_erro)
        return render_template('erro.html', mensagem=mensagem_erro, detalhes=detalhes_erro)
   
  

def encontrar_usuario_por_email(email, link):
    response = requests.get(f'{link}/users.json')
    data = response.json()

    for key, user_data in data.items():
        if user_data.get('email') == email:
            return key  # Retorna a chave (ID) do usuário no Firebase

    return None

@app.route('/atualizar_senha', methods=['POST'])
def atualizar_senha():
    try:
        destinatario = request.form['destinatario']
        codigo = request.form['codigo']
        nova_senha = request.form['novaSenha']
        senha_confirmacao = request.form.get('senha1')  # Nova variável para a senha de confirmação

        pasta_do_destinatario = encontrar_usuario_por_email(destinatario, link)

        response = requests.get(f'{link}/users.json')
        response.raise_for_status()  # Verifica se houve um erro na requisição
        data = response.json()

        codigo_gerado = codigos_de_confirmacao.get(destinatario)

        if destinatario in [user.get('email') for user in data.values()]:
            if codigo_gerado is not None and codigo == codigo_gerado and nova_senha==senha_confirmacao:
                senha_criptografada = bcrypt.generate_password_hash(nova_senha).decode('utf-8')
                dados = {'senha': senha_criptografada}
                requests.patch(f'{link}/users/{pasta_do_destinatario}/.json', data=json.dumps(dados))
                flash( 'Senha atualizada com sucesso!')
            elif nova_senha!= senha_confirmacao:
                flash('As senhas não coincidem.')
                return render_template('redefinicao_senha.html')
            else:
                flash ('Código incorreto. Mande novamente o código.')
                return render_template('redefinicao_senha.html')

        else:
             flash ( 'Email não encontrado.')
        return render_template('redefinicao_senha.html')

    except Exception as e:
        mensagem_erro = "Ocorreu um erro ao processar a solicitação."
        detalhes_erro = str(e)  # Converta o erro para uma string

        flash(mensagem_erro)
        return render_template('erro.html', mensagem=mensagem_erro, detalhes=detalhes_erro)


#*ser = serial.Serial('/dev/ttyACM0', 9600)

##@app.route('/api', methods=['GET'])
##def obter_dados():
    # Lê uma linha da porta serial
    ##linha = ser.readline()
    
    ##linha_decodificada = linha.decode('utf-8').strip()
    
    # Retorna os dados como JSON
    ##return jsonify({'dados': linha_decodificada})
if __name__ == "__main__":
    app.run(debug=True)
