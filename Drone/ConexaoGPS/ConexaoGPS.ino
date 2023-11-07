#include "dht.h" //INCLUSÃO DE BIBLIOTECA
#include <Adafruit_Sensor.h> //INCLUSÃO DE BIBLIOTECA
#include <Wire.h>
#include <Adafruit_BMP280.h>
#include <SPI.h> //INCLUSÃO DE BIBLIOTECA
#include <MFRC522.h> //INCLUSÃO DE BIBLIOTECA
#include <Wire.h> //INCLUSÃO DE BIBLIOTECA
#include <Adafruit_GFX.h> //INCLUSÃO DE BIBLIOTECA
#include <Adafruit_SSD1306.h> //INCLUSÃO DE BIBLIOTECA

Adafruit_SSD1306 display = Adafruit_SSD1306(); //OBJETO DO TIPO Adafruit_SSD1306

//Leitor Pressao
Adafruit_BMP280 bmp; //I2C

//Leitor Umidade
const int pinoDHT11 = A2; //PINO ANALÓGICO UTILIZADO PELO DHT11
dht DHT; //VARIÁVEL DO TIPO DHT

//Leitor Cartao
#define SS_PIN 10 //PINO SDA
#define RST_PIN 9 //PINO DE RESET
MFRC522 rfid(SS_PIN, RST_PIN); //PASSAGEM DE PARÂMETROS REFERENTE AOS PINOS

//Leitor Luz
int pinoLDR = A0; // Define o pino LDR onde o sensor está conectado
int valorSensor;  

//Leitor Chuva
const int pinoChuva = 3; //PINO DIGITAL UTILIZADO PELO SENSOR DE CHUVA


void setup(){
  Serial.begin(9600); //INICIALIZA A SERIAL
  delay(2000); //INTERVALO DE 2 SEGUNDO ANTES DE INICIAR
  pinMode(pinoChuva, INPUT); //DEFINE O PINO COMO ENTRADA
  SPI.begin(); //INICIALIZA O BARRAMENTO SPI
  rfid.PCD_Init(); //INICIALIZA MFRC522

  //tela
  Wire.begin(); //INICIALIZA A BIBLIOTECA WIRE
  display.begin(SSD1306_SWITCHCAPVCC, 0x3C); //INICIALIZA O DISPLAY COM ENDEREÇO I2C 0x3C
  display.setTextColor(WHITE); //DEFINE A COR DO TEXTO
  display.setTextSize(1); //DEFINE O TAMANHO DA FONTE DO TEXTO
  display.clearDisplay(); //LIMPA AS INFORMAÇÕES DO DISPLAY

}

void loop(){

  //CÓDIGO DHT - UMIDADE E TEMPERATURA
  DHT.read11(pinoDHT11); //LÊ AS INFORMAÇÕES DO SENSOR
  Serial.print("Umidade: "); //IMPRIME O TEXTO NA SERIAL
  Serial.print(DHT.humidity); //IMPRIME NA SERIAL O VALOR DE UMIDADE MEDIDO
  Serial.print("%"); //ESCREVE O TEXTO EM SEGUIDA
  Serial.print(" | Temperatura: "); //IMPRIME O TEXTO NA SERIAL
  Serial.print(DHT.temperature, 0); //IMPRIME NA SERIAL O VALOR DE UMIDADE MEDIDO E REMOVE A PARTE DECIMAL
  Serial.print("C"); //IMPRIME O TEXTO NA SERIAL
  
//CÓDIGO LDR
  valorSensor = analogRead(pinoLDR); // Lê o valor do sensor
  Serial.print(" | Luminosidade: ");
  Serial.print(valorSensor); // Exibe o valor lido
  

  //CÓDIGO CHUVA

  if(digitalRead(pinoChuva) == LOW){ //SE A LEITURA DO PINO FOR IGUAL A LOW, FAZ
      Serial.print(" | Chuva = S ");
  }
  else
  { Serial.print(" | Chuva = N ");
  }



  //CÓDIGO BMP - PRESSAO

    //Imprimindo os valores de Pressão
    Serial.print(F(" Pressao = "));
    Serial.print(bmp.readPressure());
    Serial.println(" Pa");
    //Imprimindo os valores de Altitude Aproximada
    Serial.print(F(" Altitude Aprox = "));
    Serial.print(bmp.readAltitude(1013.25)); /* Ajustar a pressão de nível do mar de acordo com o local!*/
    Serial.println(" m");

    //CÓDIGO RFID

    Serial.println("-----------------------------------"); //IMPRIME UMA LINHA NO MONITOR SERIAL
      delay(2000); //INTERVALO DE 2 SEGUNDOS * NÃO DIMINUIR ESSE VALOR
}