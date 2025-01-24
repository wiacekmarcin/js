#ifndef _TEMP_H_
#define _TEMO_H_

#include "OneWire.h"
#include <DallasTemperature.h>

// na 9 pinie jest temperatury
#define ONE_WIRE_BUS 9

void printTemperature(DeviceAddress deviceAddress);
void printAddress(DeviceAddress deviceAddress);
void SensorInitalize();
void temp_init();
void print_temp();

#endif // !_TEMP_H_




