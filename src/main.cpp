#include <Arduino.h>

#include <Wire.h>
#include <PCF8574.h>

#include "wejscia.h"
#include "wyjscia.h"

#include "swiatlo.h"
#include "util.h"

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

Swiatlo lampa(expWejscia, expWyjscia);

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

  
    // Start up the library
  sensors.begin();

  if (!sensors.getAddress(insideThermometer, 0)) //Serial.println("Unable to find address for Device 0"); 
  
  // set the resolution to 9 bit (Each Dallas/Maxim device is capable of several different resolutions)
  sensors.setResolution(insideThermometer, 9);

  
  delay(10000); //czekaj 10s az czujniki sie ustabilizuja
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

uint8_t loopCnt = 0;
unsigned long prevs = 0;
void loop() {

  
    unsigned long mls = millis();
    unsigned long s = mls / (1000L * 60);

    if (prevs != s) {
      Serial.print("Min : ");
      Serial.println(s, DEC);
      prevs = s;
    }

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
    bool isChange = expWejscia.isChange();

    Klawisz klawisz(expWejscia.getWlacznik());
    bool onS = expWyjscia.getSwiatlo();
    bool onL = expWejscia.getLustro();
    Czujka c(expWejscia.getCzRuchu());
    Drzwi d(expWejscia.getDrzwi());
    Czujka czL(expWejscia.getLustro());

    if (klawisz.isChange() && klawisz.czyNacisniety()) {
        expWyjscia.setSwiatlo(!onS, 30*60); //30 min
        expWyjscia.setLustro(false);
    }

    if (!onS && c.isChange() && c.czyRuch()) {
        expWyjscia.setLustro(true, 2*60);
    }

    if (!onL && czL.czyRuch() && czL.czasRuchu() > 500) {
        expWyjscia.setLustro(true, 4*60);
    }

    if (!onL && !onS && d.isChange() && d.czyOtwarte()) {
        expWyjscia.setLustro(true, 2*60);
    }

    if (onL && d.isChange() && !d.czyOtwarte()) {
        expWyjscia.setLustro(false, 0);
    }
    

    /*
    if (isChange) {
      
          Serial.println("------------------------------------------------\nWykroto zmiany: Wyjscie przed:");
          expWyjscia.print("MAIN BEFORE");
          Serial.println("");
          loopCnt = 10;
          expWejscia.print();
    }
    if (lustro.set(isChange)) //tryb normalny
        lampa.set(isChange);
    

    if (isChange) { 
        Serial.println("\nWyjscie po:");
        expWyjscia.print("MAIN AFTER");
        Serial.println("------------------------------------------------\n\n");
    }
*/
    expWyjscia.tiktok();
    

    delay(100 - (millis() - mls));
}
