#include "wejscia.h"
#include "util.h"
#include "lcd.h"
#include "debug.h"
#if 0
Wejscia::Wejscia(Adafruit_MCP23X17 & wej) :
    wejscia(wej)
{

}

void Wejscia::init(void (*fun)(void))
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
    pinMode(INTERPIN, INPUT);
    wejscia.setupInterrupts(false, false, LOW);
    attachInterrupt(digitalPinToInterrupt(INTERPIN), fun, FALLING );


    wejscia.setupInterruptPin(8 + CZ_R_LUSTRO, FALLING); //H->L wykrycie
    wejscia.setupInterruptPin(8 + CZ_R_WC, RISING); //L->H wykrycie
    wejscia.setupInterruptPin(8 + DRZWI, CHANGE); //L->H otwarcie H->L zamkniecie
    wejscia.setupInterruptPin(8 + KLAWISZ, FALLING); //H->L naciśniecie
    //wejscia.setupInterruptPin(8 + NOC, CHANGE); //H->L = yes, L->H = no
    //wejscia.setupInterruptPin(8 + WIECZOR, CHANGE); //H->L = yes, L->H = no
    //wejscia.setupInterruptPin(8 + TARYF2, CHANGE); //H->L = yes, L->H = no
    wejscia.setupInterruptPin(8 + Z_AWAR, CHANGE); //H->L = yes, L->H = no
#endif
}

void Wejscia::get(unsigned long timeInt, unsigned int timeAfterInt) 
{
    static uint8_t inSave = 0;
    uint8_t inD = wejscia.readGPIO(1);

#ifdef DEBUG    
    print_wejscie(inSave, inD);
    bool printd = false;
#endif // DEBUG    
    
    if (inD != inSave) {
        inSave = inD;
#ifdef LCD_DEBUG        
        lcd_print(inD);
#endif        
    }

    wl.ustaw(MASK(inD, KLAWISZ), timeInt, timeAfterInt);
    czBl.ustaw(MASK(inD, CZ_R_LUSTRO), timeInt, timeAfterInt);
    czR.ustaw(MASK(inD, CZ_R_WC), timeInt, timeAfterInt);
    drz.ustaw(MASK(inD, DRZWI), timeInt, timeAfterInt);
    prd.ustaw(MASK(inD, NOC), MASK(inD, WIECZOR), MASK(inD, Z_AWAR), MASK(inD, TARYF2));

#ifdef DEBUG    
    if (printd) {
        Serial.print(" => ");
        Serial.print(prd.czyNoc() ? 'N' : '-');
        Serial.print(prd.czyWieczor() ? 'W' : '-');
        Serial.print(wl.nacisniety() ? 'K' : '-');
        Serial.print(czR.czyRuch() ? 'R' : '-');
        Serial.print(drz.czyOtwarte() ? 'D' : '-'); 
        Serial.print(czBl.czyRuch() ? (czBl.czyDlugiRuch() ? "LL" : "LS") : "-");
        Serial.print(prd.czyTaryf2() ? '2' : '-');
        Serial.println(prd.czyZasAwar() ? 'Z' : '-');
        print();
    }
#endif    
}

void Wejscia::print() 
{
    wl.print();
    czBl.print();
    czR.print();
    drz.print();
    prd.print();
}

#endif



