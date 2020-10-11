#include "wejscia.h"
#include "util.h"
#include <PCF8574.h>

// For arduino uno only pin 1 and 2 are interrupted
#define ARDUINO_UNO_INTERRUPTED_PIN 7

Wejscia::Wejscia(void (*fun)()) :
    wejscia(0x20, ARDUINO_UNO_INTERRUPTED_PIN, fun) 
{

    w[CZ_R_LUSTRO].setLowAsTrue(); //poziom niski
    w[DRZWI].setLowAsTrue(); //zamkniete drzwi to true
    w[KLAWISZ].setLowAsTrue(); //poziom niski
    
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
    uint8_t inD = wejscia.digitalReadAll();
    Serial.print("IN=");
    Serial.println(inD, BIN);

    for (uint8_t i = 0; i < lenWej; ++i) {
        in[i] = ((0x01 << i) & inD) >> i;
        w[i] = in[i];
    }
    printBin(inD);
    print();
    //for (uint8_t i = 0; i < lenWej; ++i) {
        //Serial.print("time=");
        //Serial.print(w[i].time());
        //Serial.print("  prevtime=");
        //Serial.println(w[i].prevtime());
    //}
}

bool Wejscia::isChange() const
{
    for (uint8_t i = 0; i < lenWej; ++i) {
        if (w[i].isChange())
            return true;
    }
    return false;
}

void Wejscia::print() {
    
    char buff[12];
    printtime(millis(), buff);

    
    
    Serial.print(" ");
    Serial.print(buff);
    Serial.println(" --- Wejscia --- ");
    Serial.print("- isChange : ");
    Serial.println(isChange(), DEC);

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
    for (int n = 0; n < lenWej; n++) {
        Serial.print("|     ");
        Serial.print(w[klucze[n]] == true ? "T" : "N");
        Serial.print("     ");
    }
    Serial.println("|");
    for (int n = 0; n < lenWej; n++) {
        Serial.print("|    ");
        Serial.print(w[klucze[n]].isChange() == true ? "CHG" : "EQU");
        Serial.print("    ");
    }
    Serial.println("|");

    
    for (int n = 0; n < lenWej; n++) {
        Serial.print("|");
        printtime(w[klucze[n]].time(), buff);
        Serial.print(buff);
        Serial.print("");
    }
    Serial.println("|");

    for (int n = 0; n < lenWej; n++) {
        Serial.print("|");
        printtime(w[klucze[n]].prevtime(), buff);
        Serial.print(buff);
        Serial.print("");
    }
    Serial.println("|");
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


Wlacznik::Wlacznik() : m_val(false), m_prev(false), m_cntPush(0)
{
    unsigned long m_timeInt;
    unsigned int m_timeAfterInt;
}
    
void Wlacznik::set(uint8_t val, unsigned long timeInt, unsigned int timeAfterInt)
{
    if (m_val != val) {
        m_prev = m_val;
        m_val = val;
        if (m_val == LOW) { //klawisz nacisniety
            ++m_cntPush;
        }
    } else {
        m_prev = val;
    }

    if (val == LOW) //nacisniety klawisz {
        if (m_val != val) { //zmiana stanu

        }


    }
}


    
    



