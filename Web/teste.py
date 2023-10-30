from flask import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__)

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
    return render_template('Email.html')

@app.route('/enviar-email', methods=['POST'])
def enviar_email():
    destinatario = request.form['destinatario']
    assunto = request.form['assunto']
    corpo = request.form['corpo']

    msg = Message(assunto, sender='seu_email@gmail.com', recipients=[destinatario])
    msg.body = corpo

    mail.send(msg)

    return 'E-mail enviado com sucesso!'

if __name__ == '__main__':
    app.run(debug=True)
