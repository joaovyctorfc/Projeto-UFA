/ Este exemplo demonstra o uso do método BluetoothSerial para recuperar o endereço MAC do dispositivo BT local em vários formatos.
// Por Tomas Pilny - 2023

#include "BluetoothSerial.h"

String nome_dispositivo = "ESP32-exemplo";

#if !defined(CONFIG_BT_ENABLED) || !defined(CONFIG_BLUEDROID_ENABLED)
#error O Bluetooth não está habilitado! Por favor, execute make menuconfig e habilite-o
#endif

#if !defined(CONFIG_BT_SPP_ENABLED)
#error Bluetooth Serial não está disponível ou não está habilitado. Está disponível apenas para o chip ESP32.
#endif

BluetoothSerial SerialBT;

void setup() {
Serial.begin(9600);
SerialBT.begin(nome_dispositivo); // Nome do dispositivo Bluetooth

uint8_t mac_arr[6]; // Array de bytes para armazenar o endereço MAC obtido a partir de getBtAddress()
BTAddress mac_obj; // Objeto que mantém uma instância de BTAddress com o endereço MAC (para mais detalhes, consulte libraries/BluetoothSerial/src/BTAddress.h)
String mac_str; // String que mantém a versão de texto do endereço MAC no formato AA:BB:CC:DD:EE:FF

SerialBT.getBtAddress(mac_arr); // Preencha o array
mac_obj = SerialBT.getBtAddressObject(); // Instancie o objeto
mac_str = SerialBT.getBtAddressString(); // Copie a string

Serial.print("Este dispositivo foi instanciado com o nome "); Serial.println(nome_dispositivo);

Serial.print("O endereço MAC usando um array de bytes: ");
for(int i = 0; i < ESP_BD_ADDR_LEN-1; i++){
Serial.print(mac_arr[i], HEX); Serial.print(":");
}
Serial.println(mac_arr[ESP_BD_ADDR_LEN-1], HEX);

Serial.print("O endereço MAC usando o objeto BTAddress com o método padrão toString(): "); Serial.println(mac_obj.toString().c_str());
Serial.print("O endereço MAC usando o objeto BTAddress com o método toString(true)\n\tque imprime o MAC com letras maiúsculas: "); Serial.println(mac_obj.toString(true).c_str()); // Isso é o que é usado na função getBtAddressString()

Serial.print("O endereço MAC usando uma string: "); Serial.println(mac_str.c_str());
}

void loop(){

}