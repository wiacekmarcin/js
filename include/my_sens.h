#ifndef MSENS_H_
#define MSENS_H_

#define MY_GATEWAY_SERIAL
#define MY_DISABLED_SERIAL
#define MY_SERIALDEVICE Serial
#define MY_BAUD_RATE 115200
//#define ARDUINO_ARCH_MEGAAVR
//#define ARDUINO_ARCH_AVR

#include "mysensor/MySensors.h"
#define SLEEP_MODE false                        // flowvalue can only be reported when sleep mode is false.
#define MAX_FLOW 60   

#include<avr/interrupt.h>

/* code */
#endif //MSENS_H_



