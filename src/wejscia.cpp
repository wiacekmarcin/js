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
    wejscia.pinMode(6, INPUT);
    wejscia.pinMode(7, INPUT);
    //wejscia.pinMode(CZ_POZ_WODY, INPUT);

}


void Wejscia::get(unsigned long timeInt, unsigned int timeAfterInt) 
{
    static uint8_t inSave = 0;
    Serial.println(millis(),DEC);
    uint8_t inD = wejscia.digitalReadAll();
    if (inD != inSave) {
        inSave = inD;
        Serial.print("IN=");
        Serial.println(inD, BIN);
    }
    

    wl.ustaw(MASK(inD, KLAWISZ), timeInt, timeAfterInt);
    czb.ustaw(MASK(inD, CZ_R_LUSTRO), timeInt, timeAfterInt);




    for (uint8_t i = 0; i < lenWej; ++i) {
        in[i] = MASK(inD,i);
    }
    //printBin(inD);
    //print();
}

void Wejscia::print() {
    /*
    char buff[12];
    printtime(millis(), buff);

    
    
    Serial.print(" ");
    Serial.println(buff);
    Serial.println(" --- Wejscia --- ");
    Serial.print("- isChange : ");
    
    const char et[] = { "| wlacznik  " 
                        "|   lustro  "
                        "| cz. ruchu " 
                        "|    drzwi  "
                        "|  wieczor  " 
                        "|      noc  |"};
    int klucze[] = { KLAWISZ, CZ_R_LUSTRO, CZ_R_WC, DRZWI, WIECZOR, NOC };

    Serial.println(et);
    for (int n = 0; n < lenWej; n++) {
        Serial.print("|     ");
        Serial.print(in[klucze[n]] == LOW ? "L" : "H");
        Serial.print("     ");
    }
    Serial.println("|");
    */
#ifdef DEBUG   
    wl.print();
    czb.print();
#endif

}

void Wejscia::printBin(uint8_t  inp)
{

    struct DigitalInput {
			uint8_t p0;
			uint8_t p1;
			uint8_t p2;
			uint8_t p3;
			uint8_t p4;
			uint8_t p5;
			uint8_t p6;
			uint8_t p7;
	};
    union D {
        struct DigitalInput a;
        byte b;
    } d;
    d.b = inp;
    struct DigitalInput in = d.a;

    Serial.print("Hex:");
    Serial.print(in.p7);
    Serial.print(in.p6);
    Serial.print(in.p5);
    Serial.print(in.p4);
    Serial.print(in.p3);
    Serial.print(in.p2);
    Serial.print(in.p1);
    Serial.println(in.p0);
}





