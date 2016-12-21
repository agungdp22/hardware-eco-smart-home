/*
 * I2C yaitu media untuk komunikasi antara arduino pada pin A4 dan A5, dengan raspberry pi pada GPIO 02(pin 03) dan GPIO 03(pin 05)
 */

#include <Wire.h>
#include <LiquidCrystal.h>
 
#define SLAVE_ADDRESS 0x68

int dataDiterima = 0;
int dataTerkirim = 0;
int LED = 12;
int desimalDiterima=0;
int PIR;
 
double temp;
int sens;
int lampu[8] = {2,3,4,5,6,7,8,9};
int perangkat[100];
int portBegin = 22;
 
void setup() {
 Serial.begin(9600);
 for(portBegin;portBegin<40;portBegin++){
    perangkat[portBegin] = portBegin;
    pinMode(perangkat[portBegin], OUTPUT);
  }
 
 Wire.begin(SLAVE_ADDRESS);
 Wire.onReceive(receiveData);
 Wire.onRequest(sendData);
}

void loop(){
//  PIR = GetSensor1();
//  Serial.println(PIR);
//  if(PIR>10){
//    digitalWrite(perangkat[22],1);
//  }
//  else{
//    digitalWrite(perangkat[22],0);
//  }
  delay(50);
}

/*======================= Komunikasi I2C ============================================*/
// menerima data dari raspberry pi
int dataDesimal=0;
volatile byte buf [32];
void receiveData(int howMany){
    for (int i = 0; i < howMany; i++){
      buf [i] = Wire.read ();
      dataDesimal+=buf[i];
    }
  dataTerkirim=dataDesimal;
  Serial.print(buf[1]);Serial.print(" ");Serial.println(buf[2]);
  kendaliPerangkat(buf[1],buf[2]);
  Serial.print("Data biner yang diterima dari raspi = ");Serial.println(dataDesimal);Serial.print("indeks = ");Serial.println(howMany);
  dataDesimal=0;
}
// mengirim data ke raspberry pi
// karena data dari arduino berukuran 10 bit, dan data yg diterima raspberry via I2C berukuran 8 bit
// dilakukan pembagian data yg dikirim menjadi 4 blok masing2 berukuran 8 bit (255)
int index = 0;
int dataArr[4] = {0,0,0,0};
void sendData(){
  dataTerkirim = GetSensor1();
  if(dataTerkirim<255){
    dataArr[0] = dataTerkirim;
  }
  else if(dataTerkirim<510){
    dataArr[0] = 255;
    dataArr[1] = dataTerkirim%255;
  }
  else if(dataTerkirim<765){
    dataArr[0] = 255;
    dataArr[1] = 255;
    dataArr[2] = dataTerkirim%255;
  }
  else if(dataTerkirim<1020){
    dataArr[0] = 255;
    dataArr[1] = 255;
    dataArr[2] = 255;
    dataArr[3] = dataTerkirim%255;
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
/*================================= End =============================================*/

int GetSensor1(){
  int sensor1 = analogRead(A0); // pin A0 terhubung pada sensor LDR
  return (sensor1);
}
int GetSensor2(){
  int sensor2 = analogRead(A1); // pin A1 terhubung ke modul pembaca resistivitas
  return (sensor2);
}
int GetSensor3(){
  int sensor3 = analogRead(A2);
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

void kendaliPerangkat(int port, int stat){
  digitalWrite(perangkat[port],stat);
}

/*
 * Agung Dwi Prasetyo
 * G64130073
 * cs.ipb.ac.id
 */

