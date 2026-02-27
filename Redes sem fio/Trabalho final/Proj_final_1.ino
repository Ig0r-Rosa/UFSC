#define BLYNK_TEMPLATE_ID "TMPL2sVtvOVEw"
#define BLYNK_TEMPLATE_NAME "Quickstart Template"
#define BLYNK_AUTH_TOKEN "ndY54v76oYhKQ7SX7c0oc8d185Yk0rTN"

#include <BlynkSimpleEsp8266.h>
#include "ESP8266WiFi.h"

const char* id = "Zé Paulo";
const char* senha = "...";

int botaoTeste = 0;
int SenCasa = 0;
int flag = 0;
const int PinoLed = LED_BUILTIN;
const int IPviwer = V2;
const int StatusViwer = V3;
const int Sonoro = D8;
void update();

BLYNK_WRITE(V0)
{
  botaoTeste = param.asInt();
  Serial.println(botaoTeste);
  update();
}

BLYNK_WRITE(V1)
{
  SenCasa = param.asInt();
  Serial.println(SenCasa);
  update();
}

void update()
{
  if(SenCasa == 1)
  {
    if(flag == 1 || botaoTeste == 1 || digitalRead(D1)==0 || digitalRead(D2)==0 || digitalRead(D3)==0 || digitalRead(D4)==0 || digitalRead(D5)==0)
    {
      digitalWrite(PinoLed, 0);
      digitalWrite(Sonoro, 1);
      
      flag = 1;
      String voidString = "Sua casa pode ter sido invadida!!!";
      Blynk.virtualWrite(StatusViwer, voidString);
    }
  }
  else
  {
    digitalWrite(PinoLed, 1);    
    digitalWrite(Sonoro, 0);

    flag = 0;
    String voidString = "Sua casa aparentemente está segura.";
    Blynk.virtualWrite(StatusViwer, voidString);
  }
}

void conectarBlynk()
{
  while (!Blynk.connected()) {
    // Espera até que a conexão seja estabelecida
    delay(10);
    Serial.println("Conectado ao Blynk!");
  }
}

void VerificarRSSI()
{
  String ipString = WiFi.localIP().toString() + " = " + WiFi.RSSI() + " dBm";
  Blynk.virtualWrite(IPviwer, ipString);
}

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(D1, INPUT); //sensor de input 1
  pinMode(D2, INPUT); //sensor de input 2
  pinMode(D3, INPUT); //sensor de input 3, também é o botão do esp
  pinMode(D4, INPUT); //sensor de input 4
  pinMode(D5, INPUT); //sensor de input 5

  //pinMode(D7, OUTPUT); //algum outro aviso
  pinMode(Sonoro, OUTPUT); //Aviso sonoro D8
  pinMode(PinoLed, OUTPUT); // ascende o led


  update();

  Blynk.begin(BLYNK_AUTH_TOKEN,id,senha,"blynk.cloud",80);

  conectarBlynk();

  Serial.println(WiFi.localIP());
  VerificarRSSI();

  String voidString = " ";
  Blynk.virtualWrite(StatusViwer, voidString);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (!Blynk.connected()) {
    conectarBlynk();
    Serial.println("Conectado ao Blynk!");
  }

  Blynk.run();
  VerificarRSSI();
  update();

  delay(1);
}
