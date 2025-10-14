#include "temp.h"
#if 0
void Temp::loadTemp() {
	sensors.requestTemperatures(); // Send the command to get temperatures
	float tempC = sensors.getTempCByIndex(0);
	// Check if reading was successful
	if(tempC != DEVICE_DISCONNECTED_C)
		temp = tempC;
}
#endif