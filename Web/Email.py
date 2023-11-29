
from flask import Flask, request, render_template, redirect, flash
from flask_mail import Mail, Message
import requests
import json
import random
import string
from flask_bcrypt import Bcrypt

link = "https://projeto-ufa-default-rtdb.firebaseio.com/"
app = Flask(__name__)
bcrypt = Bcrypt(app)

# Configuração do Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'reconviewads@gmail.com'
app.config['MAIL_PASSWORD'] = 'fdwr jxgw rvtx gsbr'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

# Inicialização do Flask-Mail
mail = Mail(app)

@app.route('/')
def index():
    try:
        return render_template('Email.html')
    except Exception as e:
        mensagem_erro = "Ocorreu um erro ao processar a solicitação."
        detalhes_erro = str(e)  # Converta o erro para uma string

        flash(mensagem_erro)
        return render_template('erro.html', mensagem=mensagem_erro, detalhes=detalhes_erro)

@app.route('/enviar-email', methods=['POST'])
def enviar_email():
    try:
        destinatario = request.form['destinatario']
        assunto = request.form['assunto']
        corpo = request.form['corpo']

        msg = Message(assunto, sender='seu_email@gmail.com', recipients=[destinatario])
        msg.body = corpo

        mail.send(msg)

        flash( 'E-mail enviado com sucesso!')
    except Exception as e:
        mensagem_erro = "Ocorreu um erro ao enviar o Email."
        detalhes_erro = str(e)  # Converta o erro para uma string

        flash(mensagem_erro)
        return render_template('erro.html', mensagem=mensagem_erro, detalhes=detalhes_erro)

if __name__ == '__main__':
    app.run(debug=True)


  


