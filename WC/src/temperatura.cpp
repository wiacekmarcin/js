#include "temperatura.h"

// Inicjalizacja protokoli
OneWire oneWire(ONE_WIRE_BUS);
// Inicjalizacja sterownika
DallasTemperature sensors(&oneWire, ONE_WIRE_BUS);
DeviceAddress insideThermometer;
bool noSensors = false;
void temp_init() {
    // Inicjalizacja biblioteki
    sensors.begin();

    if (!sensors.getAddress(insideThermometer, 0)) 
      noSensors = true;
    
    // ustaw rozdzielczosc na 9 bit
    sensors.setResolution(insideThermometer, 9);

}

// function to print the temperature for a device
void printTemperature(DeviceAddress deviceAddress)
{
  
  // method 2 - faster
  float tempC = sensors.getTempC(deviceAddress);
  if(tempC == DEVICE_DISCONNECTED_C) 
  {
    tempC == -100.0;
    return;
  }
  Serial.print("Temp C: ");
  Serial.println(tempC);
}

void print_temp() {
    sensors.requestTemperatures(); // Send the command to get temperatures
    printTemperature(insideThermometer);
}