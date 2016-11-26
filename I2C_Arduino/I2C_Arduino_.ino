/*
 * I2C yaitu media untuk komunikasi antara arduino pada pin A4 dan A5, dengan raspberry pi pada GPIO 02(pin 03) dan GPIO 03(pin 05)
 */

#include <Wire.h>
#include <LiquidCrystal.h>
 
#define SLAVE_ADDRESS 0x2a

LiquidCrystal lcd(12,11,10,9,8,7);

int dataDiterima = 0;
int dataTerkirim = 0;
int LED = 12;
 
double temp;
int sens;
int s[4] = {2,3,4,5};
int aktifMultiplex=6;
 
void setup() {
 Serial.begin(9600);
 lcd.begin(16, 2);
 pinMode(LED, OUTPUT);
 for(int k=0;k<4;k++){
    pinMode(s[k], OUTPUT);
 }
 pinMode(aktifMultiplex, OUTPUT);
 digitalWrite(aktifMultiplex,LOW);
 
 Wire.begin(SLAVE_ADDRESS);
 Wire.onReceive(receiveData);
 Wire.onRequest(sendData);
}
 
void loop(){
  if(dataDiterima == 1){
    sens = GetSensor1(); // baca data sensor LDR
    Serial.print("Sensor 1 = ");Serial.println(sens);
    if(sens < 900){
      digitalWrite(13,HIGH);
    }else{
      digitalWrite(13,LOW);
    }
  }else if(dataDiterima == 2){
    sens = GetSensor2(); // baca data resistivitas yang sedang diukur
    Serial.print("Sensor 2 = ");Serial.println(sens);
  }else if(dataDiterima == 3){
    sens = GetSensor3(); // null
    Serial.print("Sensor 3 = ");Serial.println(sens);
  }
  
  aksi(dataDiterima);
  lcd.setCursor(0, 0);
  lcd.print("Data diterima=");
  lcd.print(dataDiterima);
  lcd.setCursor(0, 1);
  lcd.print("Nilai=");
  lcd.print(sens);
  delay(1000);
}

/*======================= Komunikasi I2C ============================================*/
// menerima data dari raspberry pi
void receiveData(int byteCount){
 while(Wire.available()) {
  dataDiterima = Wire.read();
  Serial.print("Data yang diterima dari raspi = ");Serial.print(dataDiterima);
  multiplex(dataDiterima);
  if (dataDiterima == 1){
    dataTerkirim = GetSensor1();
  }
  else if(dataDiterima == 2) {
    dataTerkirim = GetSensor2();
  }
  else if(dataDiterima == 3){
    dataTerkirim = dataDiterima*1000;
  }
  Serial.print("\t Data yang dikirim ke raspi = ");Serial.println(dataTerkirim);
 }
}
// mengirim data ke raspberry pi
// karena data dari arduino berukuran 10 bit, dan data yg diterima raspberry via I2C berukuran 8 bit
// dilakukan pembagian data yg dikirim menjadi 4 blok masing2 berukuran 8 bit (255)
int index = 0;
int dataArr[4] = {0,0,0,0};
void sendData(){
  if(dataTerkirim<256){
    dataArr[0] = dataTerkirim;
  }
  else if(dataTerkirim<512){
    dataArr[0] = 255;
    dataArr[1] = dataTerkirim%256;
  }
  else if(dataTerkirim<768){
    dataArr[0] = 255;
    dataArr[1] = 255;
    dataArr[2] = dataTerkirim%256;
  }
  else if(dataTerkirim<1024){
    dataArr[0] = 255;
    dataArr[1] = 255;
    dataArr[2] = 255;
    dataArr[3] = dataTerkirim%256;
  }
  Wire.write(dataArr[index]);
  Serial.print("DATAAAAA\t");Serial.println(dataArr[index]);
  ++index;
  if (index >= 4) {
    index = 0;
    // reset data
    for(int in=0;in<4;in++){
      dataArr[in] = 0;
    }
  }
}
/*================================= End ============================================*/

int GetSensor1(){
  int sensor1 = analogRead(A0); // pin A0 terhubung pada sensor LDR
  return (sensor1);
}
int GetSensor2(){
  int sensor2 = analogRead(A1); // pin A1 terhubung ke modul pembaca resistivitas
  return (sensor2);
}
int GetSensor3(){
  int sensor3 = analogRead(A1);
  return (sensor3);
}
void aksi(int data){
  for(int i=0;i<data;i++){
    digitalWrite(LED,HIGH);
    delay(200);
    digitalWrite(LED,LOW);
    delay(200);
  }
}

// mengontrol sinyal yang lewat pada multiplexer
void multiplex(int chanel){
  int bits;
  for(int i=0;i<4;i++){
    bits = chanel%2;
    chanel =(int) chanel/2;
    digitalWrite(s[i],bits);
  }
}

/*
 * Agung Dwi Prasetyo
 * G64130073
 * cs.ipb.ac.id
 */

