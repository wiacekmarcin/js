#include <Arduino.h>

#include <Wire.h>
#include <PCF8574.h>

#include "wejscia.h"
#include "wyjscia.h"

#include "swiatlo.h"
#include "util.h"

#define SENSORS


constexpr unsigned short DELAY = 200; //50;
constexpr unsigned long TIMEBEFORESLEEP = SEC(5);
constexpr unsigned int CNTMAXLOOP = TIMEBEFORESLEEP / DELAY;

#ifdef SENSORS
#include "OneWire.h"
#include "DallasTemperature.h"

// na 9 pinie jest temperatury
#define ONE_WIRE_BUS 9

// Inicjalizacja protokoli
OneWire oneWire(ONE_WIRE_BUS);

// Inicjalizacja sterownika
DallasTemperature sensors(&oneWire, ONE_WIRE_BUS);

DeviceAddress insideThermometer;
#endif

//PCF8574 expWejscia(0x20);
void keyPressedOnPCF8574();
Wejscia expWejscia(keyPressedOnPCF8574);

//PCF8574 expWyjscia(0x21);
Wyjscia expWyjscia;

Swiatlo lampa(expWejscia, expWyjscia);


void printTemperature(DeviceAddress deviceAddress);
void printAddress(DeviceAddress deviceAddress);
void SensorInitalize();


bool noSensors = false;
volatile uint8_t cntLoop = 0;
void setup() {  
  
  expWejscia.init();

  expWyjscia.init();
  
  Serial.begin(115200);


  #ifdef SENSORS
    // Inicjalizacja biblioteki
    sensors.begin();

    if (!sensors.getAddress(insideThermometer, 0)) 
      noSensors = true;
    
    // ustaw rozdzielczosc na 9 bit
    sensors.setResolution(insideThermometer, 9);

  #endif
  

    cntLoop = 0;
    expWejscia.get(0, 0);
}


// function to print the temperature for a device
void printTemperature(DeviceAddress deviceAddress)
{
  

  // method 2 - faster
  float tempC = sensors.getTempC(deviceAddress);
  if(tempC == DEVICE_DISCONNECTED_C) 
  {
    Serial.println("Error: Could not read temperature data");
    return;
  }
  Serial.print("Temp C: ");
  Serial.println(tempC);
}


unsigned long tik = 0;

unsigned long timeInt = 0L;
void keyPressedOnPCF8574()
{
    cli();
    if (!cntLoop)
        timeInt = millis();  
    cntLoop = CNTMAXLOOP;
    sei();
}

void mydelay(unsigned long ms)
{
	uint32_t start = micros();

	while (ms > 0 && !cntLoop) {
		yield();
		while ( ms > 0 && (micros() - start) >= 1000) {
			ms--;
			start += 1000;
		}
	}
}

bool wasTemp = false;
unsigned long mls = 0L;

void setWiatrak() 
{
    const Wlacznik & w = expWejscia.getWlacznik();
    if (w.nacisnietyTrzeciRaz()) {
        expWyjscia.setSwiatlo(false);
        expWyjscia.setWiatrak(true, L_MIN(5));
    }
}


void loop() {

    if (cntLoop > 0) {
        //Serial.print("cntLoop=");
        //Serial.println(cntLoop, DEC);
        --cntLoop;
        mls = millis();
        expWejscia.get(timeInt, mls - timeInt);
#ifdef DEBUG        
        expWejscia.print();
#endif        
        lampa.set(mls);
        setWiatrak();
        delay(50);
        if (cntLoop == 0) {
            expWejscia.czysc();
        }

    } else if (expWyjscia.tiktok()) {
        mydelay(1000); //co 1s
    } else {
        mydelay(60L*1000); //co 1min
        sensors.requestTemperatures(); // Send the command to get temperatures
        printTemperature(insideThermometer);
    }
}
