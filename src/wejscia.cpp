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
    wejscia.pinMode(TARYF2, INPUT);
    wejscia.pinMode(Z_AWAR, INPUT);
    

}

void Wejscia::get()
{
    uint8_t inD = wejscia.digitalReadAll();
    //Serial.print("T ");
    //Serial.print(millis(),DEC);
    //Serial.print(" --");
    //Serial.print(MASK(inD, NOC) ? 'N' : '-');
    //Serial.print(MASK(inD, WIECZOR) ? 'W' : '-');
    //Serial.print(MASK(inD, KLAWISZ) ? 'K' : '-');
    //Serial.print(MASK(inD, DRZWI) ? 'D' : '-');
    //Serial.print(MASK(inD, CZ_R_LUSTRO) ? 'L' : '-');
    //Serial.println(MASK(inD, CZ_R_WC) ? 'R' : '-');
}

void Wejscia::get(unsigned long timeInt, unsigned int timeAfterInt) 
{
    static uint8_t inSave = 0;
    //bool printd = false;
    
    uint8_t inD = wejscia.digitalReadAll();
    if (inD != inSave) {
        inSave = inD;
        Serial.println(inD, HEX);
        //printd = true;
#ifdef DEBUG        
        Serial.print("mls=");
        Serial.println(millis(),DEC);
        Serial.print("IN=");
        Serial.println(inD, BIN);
#endif        
        //Serial.print("I ");
        //Serial.print(millis(),DEC);
        //Serial.print(" --");
        //Serial.print(MASK(inD, NOC) ? 'N' : '-');
        //Serial.print(MASK(inD, WIECZOR) ? 'W' : '-');
        //Serial.print(MASK(inD, KLAWISZ) ? 'K' : '-');
        //Serial.print(MASK(inD, DRZWI) ? 'D' : '-');
        //Serial.print(MASK(inD, CZ_R_LUSTRO) ? 'L' : '-');
        //Serial.print(MASK(inD, CZ_R_WC) ? 'R' : '-');
    }

    wl.ustaw(MASK(inD, KLAWISZ), timeInt, timeAfterInt);
    czBl.ustaw(MASK(inD, CZ_R_LUSTRO), timeInt, timeAfterInt);
    czR.ustaw(MASK(inD, CZ_R_WC), timeInt, timeAfterInt);
    drz.ustaw(MASK(inD, DRZWI), timeInt, timeAfterInt);
    prd.ustaw(MASK(inD, NOC), MASK(inD, WIECZOR), MASK(inD, Z_AWAR), MASK(inD, TARYF2));
    //if (printd) {
    Serial.print(" => ");
    Serial.print(prd.czyNoc() ? 'N' : '-');
    Serial.print(prd.czyWieczor() ? 'W' : '-');
    Serial.print(wl.nacisniety() ? 'K' : '-');
    Serial.print(drz.czyOtwarte() ? 'D' : '-'); 
    Serial.print(czBl.czyRuch() ? (czBl.czyDlugiRuch() ? "LL" : "LS") : "-");
    Serial.print(prd.czyTaryf2() ? '2' : '-');
    Serial.print(prd.czyZasAwar() ? 'Z' : '-');
    Serial.println(czR.czyRuch() ? 'R' : '-');

    //}
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





