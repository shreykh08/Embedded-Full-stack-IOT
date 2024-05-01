#include <Arduino.h>



/*
// Define the pin connections
const int irSensorPin = 2; // Digital pin for IR sensor output
const int ledPin = 13;     // Digital pin for the LED
const int buzzerPin = 9;   // Digital pin for the buzzer

void setup() {
  pinMode(irSensorPin, INPUT);
  pinMode(ledPin, OUTPUT);
  pinMode(buzzerPin, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  int objectDetected = digitalRead(irSensorPin);

  if (objectDetected == HIGH) {
    // Object detected, blink the LED and sound the buzzer
    digitalWrite(ledPin, HIGH);
    tone(buzzerPin, 1000, 500); // 1kHz frequency for 500ms
  } else {
    // No object detected, turn off the LED and buzzer
    digitalWrite(ledPin, LOW);
    noTone(buzzerPin);
  }
}
*/
static const int led_pin = 14;
static const int ir_pin=5;
static const int buzzer_pin = 4;
bool ir;
void setup()
{
  Serial.begin(9600);
  while(!Serial);
  pinMode(led_pin,OUTPUT);
  pinMode(ir_pin,INPUT);
  pinMode(buzzer_pin , OUTPUT);
}
void loop()
{
  ir=digitalRead(ir_pin);
  if(ir==0)
  {
    digitalWrite(led_pin,HIGH);
    Serial.println("Presence is detected");
    //digitalWrite(buzzer_pin,HIGH);
    tone(buzzer_pin,2300,500);
    delay(200);
  
  }
  else if(ir==1)
  {
    digitalWrite(led_pin,LOW);
    //digitalWrite(buzzer_pin,LOW);
    noTone(buzzer_pin);
    
  }
}

/*
pulse  width modulation :
if we make the waveform periodic and in that if we on and off it for some time either high or low ,
then we can var its average value from 1-100O(max magnitude).
Tone(pin,frequency,time duration) function is also used  to generate the pwm by the given parameters
passive ir detects the thermal radiation with the help of diffuser that increases it range.it also gives different colors on detection of different objects.it onlu detects living things

*/