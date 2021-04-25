#include "wejscia.h"
#include "util.h"
#include "LiquidCrystal_I2C.h"

#define MASK(X, M) (((0x01 << (M)) & (X)) >> M)

#define CHAN(X, Y, M) (((X)^(Y)) & (0x01 << (M)))
#define MYINTERUPTS 1

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
    wejscia.setupInterruptPin(8 + CZ_R_LUSTRO, CHANGE); //H->L wykrycie
    wejscia.setupInterruptPin(8 + CZ_R_WC, CHANGE); //L->H wykrycie
    wejscia.setupInterruptPin(8 + DRZWI, CHANGE); //L->H otwarcie H->L zamkniecie
    wejscia.setupInterruptPin(8 + KLAWISZ, FALLING); //H->L naciśniecie
    wejscia.setupInterruptPin(8 + NOC, CHANGE); //H->L = yes, L->H = no
    wejscia.setupInterruptPin(8 + WIECZOR, CHANGE); //H->L = yes, L->H = no
    wejscia.setupInterruptPin(8 + TARYF2, CHANGE); //H->L = yes, L->H = no
    wejscia.setupInterruptPin(8 + Z_AWAR, CHANGE); //H->L = yes, L->H = no
#endif
}

void Wejscia::get(bool awakeByInt, unsigned long timeInt, unsigned int timeAfterInt, bool printLCD, LiquidCrystal_I2C * lcd) 
{
    static uint8_t inSave = 0;
    uint8_t prev = inSave;
    if (awakeByInt) {
        Serial.println("i");

        //Serial.print(wejscia.getLastInterruptPin(), DEC);
        //Serial.print(" (");
        //Serial.print(wejscia.getLastInterruptPinValue(), DEC);
        //Serial.println(")");
    }
    uint8_t inD = wejscia.readGPIO(1);
#ifdef DEBUG
    bool printd = false;
#endif // DEBUG    
    
    if (inD != inSave) {
        prev = inSave;
        inSave = inD;
        Serial.println(millis(), DEC);
        
        Serial.print("PREV = ");
        for (int i=7; i >= 0; i--) 
            Serial.print(MASK(prev, i)?'1':'0');
        Serial.print("\nACT  = ");
        for (int i=7; i >= 0; i--) 
            Serial.print(MASK(inD, i)?'1':'0');
        Serial.print("\nCHAN = ");
        for (int i=7; i >= 0; i--) 
            Serial.print(MASK(prev^inD, i)?'1':'0');
        Serial.println("");
#ifdef DEBUG
        printd = true;
#endif // DEBUG        
        

        if (printLCD) {
            lcd->setCursor(0,1);
            lcd->print(MASK(inD, 0)?'1':'0');
            lcd->print(' ');
            lcd->print(MASK(inD, 1)?'1':'0');
            lcd->print(' ');
            lcd->print(MASK(inD, 2)?'1':'0');
            lcd->print(' ');
            lcd->print(MASK(inD, 3)?'1':'0');
            lcd->print(' ');
            lcd->print(MASK(inD, 4)?'1':'0');
            lcd->print(' ');
            lcd->print(MASK(inD, 5)?'1':'0');
            lcd->print(' ');
            lcd->print(MASK(inD, 6)?'1':'0');
            lcd->print(' ');
            lcd->print(MASK(inD, 7)?'1':'0');
            lcd->cursor_off();
        }
//#ifdef DEBUG        
        //Serial.print("mls=");
        //Serial.println(millis(),DEC);
        //Serial.print("IN=");
        //Serial.println(inD, BIN);
      
        //Serial.print("I ");
        //Serial.print(millis(),DEC);
        //Serial.print(" --");
        Serial.print(MASK(inD, NOC) ? 'N' : '-');
        Serial.print(MASK(inD, WIECZOR) ? 'W' : '-');
        Serial.print(MASK(inD, KLAWISZ) ? 'K' : '-');
        Serial.print(MASK(inD, DRZWI) ? 'D' : '-');
        Serial.print(MASK(inD, CZ_R_LUSTRO) ? 'L' : '-');
        Serial.print(MASK(inD, CZ_R_WC) ? 'R' : '-');
        Serial.print(MASK(inD, TARYF2) ? 'T' : '-');
        Serial.println(MASK(inD, Z_AWAR) ? 'Z' : '-');

        Serial.print(CHAN(inD, prev,  NOC) ? 'N' : ' ');
        Serial.print(CHAN(inD, prev,  WIECZOR) ? 'W' : ' ');
        Serial.print(CHAN(inD, prev,  KLAWISZ) ? 'K' : ' ');
        Serial.print(CHAN(inD, prev,  DRZWI) ? 'D' : ' ');
        Serial.print(CHAN(inD, prev,  CZ_R_LUSTRO) ? 'L' : ' ');
        Serial.print(CHAN(inD, prev,  CZ_R_WC) ? 'R' : ' ');
        Serial.print(CHAN(inD, prev,  TARYF2) ? 'T' : ' ');
        Serial.println(CHAN(inD, prev,  Z_AWAR) ? 'Z' : ' ');


//#endif          
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
#ifdef DEBUG   
    wl.print();
    czBl.print();
    czR.print();
    drz.print();
    prd.print();
#endif

}





