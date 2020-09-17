#include <Arduino.h>

#include <Wire.h>
#include <PCF8574.h>

#include "wejscia.h"
#include "wyjscia.h"

#include "lampa.h"
#include "lustro.h"
#include "czruchu.h"

#include "OneWire.h"
#include "DallasTemperature.h"

// Data wire is plugged into port 2 on the Arduino
#define ONE_WIRE_BUS 9

// Setup a oneWire instance to communicate with any OneWire devices (not just Maxim/Dallas temperature ICs)
OneWire oneWire(ONE_WIRE_BUS);

// Pass our oneWire reference to Dallas Temperature. 
DallasTemperature sensors(&oneWire);


//PCF8574 expWejscia(0x20);
Wejscia expWejscia;

//PCF8574 expWyjscia(0x21);
Wyjscia expWyjscia;

Lampa lampa(expWejscia, expWyjscia);
Lustro lustro(expWejscia, expWyjscia);
CzRuchu czujka(expWejscia, expWyjscia);

//p0 p1 p2 p3
//p0 czujnik zblizeniowy 0 - blisko 1 - daleko
//p1 czujnik ruchu 
//p2 drzwi 0 - zamkniete 1 - otwarte
//p3 klawisz 0 - nacisniety 1 - w normalnej pozycji

//p4 noc
//p5 wieczor
//p6 czujnik poziomu wody

DeviceAddress insideThermometer;
void setup() {  
  
  expWejscia.init();

  expWyjscia.init();

  Serial.begin(115200);

  expWejscia.get();
  expWejscia.print();
  
    // Start up the library
  sensors.begin();

  if (!sensors.getAddress(insideThermometer, 0)) //Serial.println("Unable to find address for Device 0"); 
  
  // set the resolution to 9 bit (Each Dallas/Maxim device is capable of several different resolutions)
  sensors.setResolution(insideThermometer, 9);
 
}

// function to print the temperature for a device
void printTemperature(DeviceAddress deviceAddress)
{
  // method 1 - slower
  ////Serial.print("Temp C: ");
  ////Serial.print(sensors.getTempC(deviceAddress));
  ////Serial.print(" Temp F: ");
  ////Serial.print(sensors.getTempF(deviceAddress)); // Makes a second call to getTempC and then converts to Fahrenheit

  // method 2 - faster
  float tempC = sensors.getTempC(deviceAddress);
  if(tempC == DEVICE_DISCONNECTED_C) 
  {
    //Serial.println("Error: Could not read temperature data");
    return;
  }
  //Serial.print("Temp C: ");
  //Serial.print(tempC);
}

unsigned long tik = 0;

// function to print a device address
void printAddress(DeviceAddress deviceAddress)
{
  for (uint8_t i = 0; i < 8; i++)
  {
    if (deviceAddress[i] < 16) //Serial.print("0");
    //Serial.print(deviceAddress[i], HEX);
    ;
  }
}

void loop() {

  
    unsigned long mls = millis();
    /*
    if (++tik % 100 == 0) {
      ////Serial.print("Requesting temperatures...");
      sensors.requestTemperatures(); // Send the command to get temperatures
      ////Serial.println("DONE");
  
      // It responds almost immediately. Let's print out the data
      printTemperature(insideThermometer); // Use a simple function to print out the data
     
     expWejscia.print();
     expWyjscia.print("loop");
    }

    */
    expWejscia.get();
    if (expWejscia.isChange()) {
        expWejscia.print();
        lampa.set();
        lustro.set();
    }
    
    
    


    /*   
    czujka.set();
    
    Value drzwi = expWejscia.getDrzwi();
    if (drzwi.isChange() && !drzwi.val()) {
        if (expWyjscia.getSwiatlo()) {
            //Serial.print(__FILE__);
            //Serial.print(":");
            //Serial.println(__LINE__, DEC);
            expWyjscia.setSwiatlo(true, 30);
            if (expWyjscia.getLustro()) {
                  //Serial.print(__FILE__);
                  //Serial.print(":");
                  //Serial.println(__LINE__, DEC);
                  expWyjscia.setLustro(false);
            }
        }
        if (expWyjscia.getLustro()) {
            //Serial.print(__FILE__);
            //Serial.print(":");
            //Serial.println(__LINE__, DEC);
            expWyjscia.setLustro(true, 30);
        }
    }
    */
    //expWyjscia.tiktok();

    delay(100 - (millis() - mls));
}
