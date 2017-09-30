// Moisture sensor with Temp measurement
// DS18b20  to Digital Pin 2
// Moisture probe out to Analog 0

//Libraries for the DS18b20
#include "Arduino.h"
//#include <OneWire.h>
//#include <DallasTemperature.h>
#include <Wire.h>

//#define A_TEMP 20     //Define Ds18b20 pin as a variable A_TEMP
//OneWire oneWire1(A_TEMP);// Set A_TEMP variable to use as a One wire
//DallasTemperature sensors1(&oneWire1);

int sensorPin = A0;    //pin for moisture probe
int sensorValue = 0;   //initial value
int percent = 0;       //initial value

void setup() {
  Serial.begin(9600);  //Start serial port
}

void loop() {
//  sensors1.requestTemperatures(); //Request temperature from the Ds18b20


  sensorValue = analogRead(sensorPin);       //Analog read from A0
  percent = convertToPercent(sensorValue);   //Percent conversion of the A0 value
  printValuesToSerial();                     //Go to the display data loop called  printValuesToSerial();
  delay(100);                               // Add 1 second delay between measures
}

int convertToPercent(int value)                    //Convert value from A0 to Percent numbers using map
{
  int percentValue = 0;
  percentValue = map(value, 1023, 465, 0, 100);
  return percentValue;
}

void printValuesToSerial()                          //Loop that displays the info via serial.
{
//  Serial.print("temp");
//  Serial.print(sensors1.getTempCByIndex(0));       //Temp
  Serial.print("Analog Value: ");
  Serial.print(sensorValue);                       //Raw A0 value
  Serial.print("\tPercent: ");
  Serial.print(percent);                           //Moisture Percent
  Serial.println("%");
}


