#include "wejscia.h"
#include "util.h"


#define MASK(X, M) (((0x01 << (M)) & (X)) >> M)
Wejscia::Wejscia(Adafruit_MCP23017 & wej) :
    wejscia(wej)
{

    
}

void Wejscia::init()
{
    wejscia.pinMode(8 + CZ_R_LUSTRO, INPUT);
    wejscia.pinMode(8 + CZ_R_WC, INPUT);
    wejscia.pinMode(8 + DRZWI, INPUT);
    wejscia.pinMode(8 + KLAWISZ, INPUT);
    wejscia.pinMode(8 + NOC, INPUT);
    wejscia.pinMode(8 + WIECZOR, INPUT);
    wejscia.pinMode(8 + TARYF2, INPUT);
    wejscia.pinMode(8 + Z_AWAR, INPUT);
#ifdef MYINTERUPTS
    wejscia.setupInterruptPin(8 + CZ_R_LUSTRO, CHANGE);
    wejscia.setupInterruptPin(8 + CZ_R_WC, CHANGE);
    wejscia.setupInterruptPin(8 + DRZWI, CHANGE);
    wejscia.setupInterruptPin(8 + KLAWISZ, CHANGE);
    wejscia.setupInterruptPin(8 + NOC, CHANGE);
    wejscia.setupInterruptPin(8 + WIECZOR, CHANGE);
    wejscia.setupInterruptPin(8 + TARYF2, CHANGE);
    wejscia.setupInterruptPin(8 + Z_AWAR, CHANGE);
#endif
}

void Wejscia::get()
{
    uint8_t inD = wejscia.readGPIO(1);
    Serial.print("T ");
    Serial.print(millis(),DEC);
    Serial.print(" --");
    Serial.print(MASK(inD, NOC) ? 'N' : '-');
    Serial.print(MASK(inD, WIECZOR) ? 'W' : '-');
    Serial.print(MASK(inD, KLAWISZ) ? 'K' : '-');
    Serial.print(MASK(inD, DRZWI) ? 'D' : '-');
    Serial.print(MASK(inD, CZ_R_LUSTRO) ? 'L' : '-');
    Serial.print(MASK(inD, TARYF2) ? 'T' : '-');
    Serial.println(MASK(inD, Z_AWAR) ? 'Z' : '-');
}

void Wejscia::get(unsigned long timeInt, unsigned int timeAfterInt) 
{
    static uint8_t inSave = 0;
    //bool printd = false;
    
    uint8_t inD = wejscia.readGPIO(1);
    if (inD != inSave) {
        inSave = inD;
        Serial.println(inD, HEX);
        //printd = true;
#ifdef DEBUG        
        Serial.print("mls=");
        Serial.println(millis(),DEC);
        Serial.print("IN=");
        Serial.println(inD, BIN);
      
        Serial.print("I ");
        Serial.print(millis(),DEC);
        Serial.print(" --");
        Serial.print(MASK(inD, NOC) ? 'N' : '-');
        Serial.print(MASK(inD, WIECZOR) ? 'W' : '-');
        Serial.print(MASK(inD, KLAWISZ) ? 'K' : '-');
        Serial.print(MASK(inD, DRZWI) ? 'D' : '-');
        Serial.print(MASK(inD, CZ_R_LUSTRO) ? 'L' : '-');
        Serial.print(MASK(inD, CZ_R_WC) ? 'R' : '-');
        Serial.print(MASK(inD, TARYF2) ? 'T' : '-');
        Serial.println(MASK(inD, Z_AWAR) ? 'Z' : '-');
#endif          
    }

    wl.ustaw(MASK(inD, KLAWISZ), timeInt, timeAfterInt);
    czBl.ustaw(MASK(inD, CZ_R_LUSTRO), timeInt, timeAfterInt);
    czR.ustaw(MASK(inD, CZ_R_WC), timeInt, timeAfterInt);
    drz.ustaw(MASK(inD, DRZWI), timeInt, timeAfterInt);
    prd.ustaw(MASK(inD, NOC), MASK(inD, WIECZOR), MASK(inD, Z_AWAR), MASK(inD, TARYF2));
    //if (printd) {
    //Serial.print(" => ");
    //Serial.print(prd.czyNoc() ? 'N' : '-');
    //Serial.print(prd.czyWieczor() ? 'W' : '-');
    //Serial.print(wl.nacisniety() ? 'K' : '-');
    //Serial.print(drz.czyOtwarte() ? 'D' : '-'); 
    //Serial.print(czBl.czyRuch() ? (czBl.czyDlugiRuch() ? "LL" : "LS") : "-");
    //Serial.print(prd.czyTaryf2() ? '2' : '-');
    //Serial.print(prd.czyZasAwar() ? 'Z' : '-');
    //Serial.println(czR.czyRuch() ? 'R' : '-');

    //}
}

void Wejscia::print() 
{
#ifdef DEBUG   
    //wl.print();
    //czBl.print();
    //czR.print();
    //drz.print();
    //prd.print();
#endif

}





