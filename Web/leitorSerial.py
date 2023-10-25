import serial
from flask import Flask, jsonify

app = Flask(__name__)

# Abre a conexão com a porta serial
ser = serial.Serial('/dev/cu.usbmodem1201', 9600)

@app.route('/api', methods=['GET'])
def obter_dados():
    # Lê uma linha da porta serial
    linha = ser.readline()
    
    linha_decodificada = linha.decode('utf-8').strip()
    
    # Retorna os dados como JSON
    return jsonify({'dados': linha_decodificada})

if __name__ == '__main__':
    app.run(debug=True)