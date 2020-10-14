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
    uint8_t inD = wejscia.digitalReadAll();
    if (inD != inSave) {
        inSave = inD;
        Serial.print("IN=");
        Serial.println(inD, BIN);
    }
    

    wl.set(MASK(inD, KLAWISZ), timeInt, timeAfterInt);


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
    wl.print();
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


Wlacznik::Wlacznik() : ValueBase(), m_prev(false), m_cntPush(0)
{
    unsigned long m_timeInt;
    unsigned int m_timeAfterInt;
}
    
void Wlacznik::clearState() 
{
    m_cntPush = 0;
    m_timePush = 0;
    m_timeHold = 0;
}    
void Wlacznik::set(uint8_t value, unsigned long timeInt, unsigned int timeAfterInt)
{
    
    m_prev = m_val;
    m_val = (value == LOW); //klawisz nacisniety

    Serial.print("milis()=");
    Serial.println(millis(), DEC);
    Serial.print("value = ");
    Serial.println(value, DEC);
    Serial.print("val = ");
    Serial.println(m_val, DEC);
    Serial.print("prev = ");
    Serial.println(m_prev, DEC);
    Serial.print("timeInt=");
    Serial.println(timeInt, DEC);
    Serial.print("timeAfterInt=");
    Serial.println(timeAfterInt, DEC);
    
    if (m_timeInt != timeInt || timeAfterInt > SEC(10)) {
        m_timeInt = timeInt;
        Serial.println("clear");
        clearState();
    }

    
    if (m_val && !m_prev) {
        if (m_val) { 
            ++m_cntPush;
            m_timePush = timeAfterInt;
            m_timeHold = 0;
        }
    }

    if (m_val && m_prev ) { //nacisniety klawisz i przytrzymany przez {
        m_timeHold = timeAfterInt - m_timePush;
    }
}

void Wlacznik::print() const
{
    static unsigned long mask  = 0;
    unsigned long mask2  = 0;

    mask2 |= 0x01 & m_val;
    mask2 |= (0x01 & m_prev) << 1;
    mask2 |= (0x0F & m_cntPush) << 2;
    mask2 |= (0xFF & m_timePush) << 6;
    mask2 |= (0xFF & m_timeHold) << 14;

    if (mask2 != mask) {
        mask = mask2;
        Serial.println("------- Wlacznik ------");
        Serial.print("val = ");
        Serial.println(m_val, DEC);
        Serial.print("prev = ");
        Serial.println(m_prev, DEC);
        Serial.print("cntPush = ");
        Serial.println(m_cntPush, DEC);
        Serial.print("timePush = ");
        Serial.println(m_timePush, DEC);
        Serial.print("timeHold = ");
        Serial.println(m_timeHold, DEC);
        Serial.println("****");
        Serial.print("nacisniety = ");
        Serial.println(nacisniety(), DEC);
        Serial.print("wcisniety = ");
        Serial.println(wcisniety(), DEC);
        Serial.print("czasWcisniecia = ");
        Serial.println(czasWcisniecia(), DEC);
        Serial.print("nacisnietyDrugiRaz = ");
        Serial.println(nacisnietyDrugiRaz(), DEC);
        Serial.print("nacisnietyTrzeciRaz = ");
        Serial.println(nacisnietyTrzeciRaz(), DEC);
        Serial.println("---------------------------");
    } 
}

    
    



