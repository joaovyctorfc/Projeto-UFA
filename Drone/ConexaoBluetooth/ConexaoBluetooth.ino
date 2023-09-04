
#include "BluetoothSerial.h"


String device_name = "ESP32-BT";

BluetoothSerial SerialBT;

void setup() {
  Serial.begin(9600);
  SerialBT.begin(device_name); //Bluetooth device name
  Serial.printf("O dispositivo: \"%s\" está pronto.\nEsperando conexão!\n", device_name.c_str());
}

void loop() {
  if (Serial.available()) {
    SerialBT.write(Serial.read());
  }
  if (SerialBT.available()) {
    Serial.write(SerialBT.read());
  }
  delay(20);
}
