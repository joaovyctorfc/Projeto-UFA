import serial

# Abra a conexão com a porta serial
ser = serial.Serial('/dev/cu.usbmodem1201', 9600)  # Substitua 'COMx' com a porta COM onde o Arduino está conectado

try:
    while True:
        # Leia uma linha da porta serial
        linha = ser.readline()
        
        # Decodifique a linha para texto (opcional)
        linha_decodificada = linha.decode('utf-8').strip()
        
        # Imprima a linha
        print(linha_decodificada)

# Interrompa a execução do código quando pressionar Ctrl+C
except KeyboardInterrupt:
    ser.close()  # Feche a conexão com a porta serial quando o programa for encerrado
