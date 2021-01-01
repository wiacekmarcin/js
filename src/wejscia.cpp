#include "wejscia.h"
#include "util.h"
#include <PCF8574.h>

// For arduino uno only pin 1 and 2 are interrupted
#define ARDUINO_UNO_INTERRUPTED_PIN 7


#define MASK(X, M) (((0x01 << (M)) & (X)) >> M)
Wejscia::Wejscia(void (*fun)()) :
    wejscia(0x20, ARDUINO_UNO_INTERRUPTED_PIN, fun) 
{

    
}

void Wejscia::init()
{
    wejscia.begin(); 

    wejscia.pinMode(CZ_R_LUSTRO, INPUT);
    wejscia.pinMode(CZ_R_WC, INPUT);
    wejscia.pinMode(DRZWI, INPUT);
    wejscia.pinMode(KLAWISZ, INPUT);
    wejscia.pinMode(NOC, INPUT);
    wejscia.pinMode(WIECZOR, INPUT);
    //wejscia.pinMode(6, INPUT);
    //wejscia.pinMode(7, INPUT);
    //wejscia.pinMode(CZ_POZ_WODY, INPUT);

}


void Wejscia::get(unsigned long timeInt, unsigned int timeAfterInt) 
{
    static uint8_t inSave = 0;
    
    uint8_t inD = wejscia.digitalReadAll();
    if (inD != inSave) {
        inSave = inD;
        Serial.print("mls=");
        Serial.println(millis(),DEC);
        Serial.print("IN=");
        Serial.println(inD, BIN);
    }

    wl.ustaw(MASK(inD, KLAWISZ), timeInt, timeAfterInt);
    czBl.ustaw(MASK(inD, CZ_R_LUSTRO), timeInt, timeAfterInt);
    czR.ustaw(MASK(inD, CZ_R_WC), timeInt, timeAfterInt);
    drz.ustaw(MASK(inD, DRZWI), timeInt, timeAfterInt);
    prd.ustaw(MASK(inD, NOC), MASK(inD, WIECZOR));

}

void Wejscia::print() 
{
#ifdef DEBUG   
    wl.print();
    czBl.print();
    czR.print();
    drz.print();
    prd.print();
#endif

}





