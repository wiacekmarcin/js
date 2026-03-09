#include "wejscia.h"
#include "version.h"

void print_input_bin16(Stream * serial, uint16_t val)
{
    uint16_t mask = 0;
    for (int8_t m = 15; m >= 0; --m) {
        if (m >= 7 && m != Wejscia::p_noc )  {
            serial->print('X');
        } else {
            mask = 0x1 << m;

            if ((val & mask) == mask)   
                serial->print('1');
            else
                serial->print('0');
        }
    }
}

void print_input_bin_8corr(Stream * serial, uint8_t val)
{
    uint16_t mask = 0;
    for (int8_t m = 7; m >= 0; --m) {
        mask = 0x1 << m;

        if ((val & mask) == mask)   
            serial->print('1');
        else
            serial->print('0');
    }
}

void Wejscia::init()
{
    mcp->pinMode(p_ruch, INPUT);
    mcp->pinMode(p_zblizeniowy, INPUT);
    mcp->pinMode(p_drzwi, INPUT);
    mcp->pinMode(p_klawisz, INPUT);
    mcp->pinMode(p_zasAwar, INPUT);
    mcp->pinMode(p_2taryfa, INPUT);
    mcp->pinMode(p_wieczor, INPUT);
    mcp->pinMode(p_noc, INPUT);

    
    mcp->setupInterruptPin(p_klawisz, CHANGE);
    mcp->setupInterruptPin(p_ruch, CHANGE);
    mcp->setupInterruptPin(p_zblizeniowy, CHANGE);
    mcp->setupInterruptPin(p_drzwi, CHANGE);
    mcp->setupInterruptPin(p_zasAwar, CHANGE);

    mcp->setupInterrupts(true, true, LOW) ;
}

 

bool Wejscia::read()
{
    unsigned long now = millis();
    uint16_t input = mcp->readGPIOAB();
#ifdef DEBUG
    Serial1.print("INPUT:");
    print_input_bin16(&Serial1, input);
    Serial1.println();
#endif
    mcp->clearInterrupts();
    unsigned long diff;
    if (now > prev_read)
        diff = now - prev_read;
    else 
        diff = (UINT32_MAX - prev_read) + now;
    
    if (diff < 50)
        return false;

    uint8_t val = input & 0x7f;
    if ((input & p_noc_mask) == p_noc_mask)
        val |= 0x80;
    
    
    if (val == act_val)
        return false;

    return set_input(val);
}

bool Wejscia::set_input(uint8_t val)
{
    act_val = val;

    Serial1.print("I;");
    Serial1.print(DEVICE);
    Serial1.print(";");
    print_input_bin_8corr(&Serial1, val);
    Serial1.println("");

#ifdef DEBUG
    Serial.print("INPUT_CORR:");
    print_input_bin_8corr(&Serial, val);
    Serial.println();
#endif
    uint8_t cntChange = 0;

    if (bp_zasilanie_awaryjne != b_zasilanie_awaryjne)
        ++cntChange;

    bp_zasilanie_awaryjne = b_zasilanie_awaryjne;
    b_zasilanie_awaryjne = act_val & ( 0x1 << p_zasAwar);

    b_wieczor = act_val & ( 0x1 << p_wieczor);
    b_noc = act_val & 0x80; //0x80 zamiast 12 bitu 7 bit

    klawisz.set(act_val & ( 0x1 << p_klawisz));
    cntChange += klawisz.isChange() ? 1 : 0;
    
    czLustro.set(act_val & ( 0x1 << p_zblizeniowy ));
    cntChange += czLustro.isChange() ? 1 : 0;

    czRuch.set(act_val & ( 0x1 << p_ruch));
    cntChange += czRuch.isChange() ? 1 : 0;

#ifdef DEBUG
    Serial.print("Zmieniono wejscia:");
    Serial.println(cntChange);
#endif

    return cntChange > 0;
}





#if 0





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
        ////Serial.print("IN=");
        ////Serial.println(inD, BIN);
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

    
    
    //Serial.print(" ");
    //Serial.println(buff);
    //Serial.println(" --- Wejscia --- ");
    //Serial.print("- isChange : ");
    
    const char et[] = { "| wlacznik  " 
                        "|   lustro  "
                        "| cz. ruchu " 
                        "|    drzwi  "
                        "|  wieczor  " 
                        "|      noc  |"};
    int klucze[] = { KLAWISZ, CZ_R_LUSTRO, CZ_R_WC, DRZWI, WIECZOR, NOC };

    //Serial.println(et);
    for (int n = 0; n < lenWej; n++) {
        //Serial.print("|     ");
        //Serial.print(in[klucze[n]] == LOW ? "L" : "H");
        //Serial.print("     ");
    }
    //Serial.println("|");
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

    //Serial.print("Hex:");
    //Serial.print(in.p7);
    //Serial.print(in.p6);
    //Serial.print(in.p5);
    //Serial.print(in.p4);
    //Serial.print(in.p3);
    //Serial.print(in.p2);
    //Serial.print(in.p1);
    //Serial.println(in.p0);
}


Wlacznik::Wlacznik() : ValueBase(), m_prev(false), m_cntPush(0)
{
    m_timeInt = 0;
    m_timeAfterInt = 0;
}
    
void Wlacznik::clearState() 
{
    m_cntPush = 0;
    m_timePush = 0;
    m_timeHold = 0;
}    
void Wlacznik::set(uint8_t value, unsigned long timeInt, unsigned int timeAfterInt)
{
    m_timeInt = timeInt;
    m_timeAfterInt = timeAfterInt;
    m_prev = m_val;
    m_val = (value == LOW); //klawisz nacisniety

    ////Serial.print("milis()=");
    ////Serial.println(millis(), DEC);
    ////Serial.print("value = ");
    ////Serial.println(value, DEC);
    ////Serial.print("val = ");
    ////Serial.println(m_val, DEC);
    ////Serial.print("prev = ");
    ////Serial.println(m_prev, DEC);
    ////Serial.print("timeInt=");
    ////Serial.println(timeInt, DEC);
    ////Serial.print("timeAfterInt=");
    ////Serial.println(timeAfterInt, DEC);
    
    if (m_timeInt != timeInt || timeAfterInt > SEC(10)) {
        m_timeInt = timeInt;
        //Serial.println("clear");
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
        //Serial.println("------- Wlacznik ------");
        //Serial.print("val = ");
        //Serial.println(m_val, DEC);
        //Serial.print("prev = ");
        //Serial.println(m_prev, DEC);
        //Serial.print("cntPush = ");
        //Serial.println(m_cntPush, DEC);
        //Serial.print("timePush = ");
        //Serial.println(m_timePush, DEC);
        //Serial.print("timeHold = ");
        //Serial.println(m_timeHold, DEC);
        //Serial.println("****");
        //Serial.print("nacisniety = ");
        //Serial.println(nacisniety(), DEC);
        //Serial.print("wcisniety = ");
        //Serial.println(wcisniety(), DEC);
        //Serial.print("czasWcisniecia = ");
        //Serial.println(czasWcisniecia(), DEC);
        //Serial.print("nacisnietyDrugiRaz = ");
        //Serial.println(nacisnietyDrugiRaz(), DEC);
        //Serial.print("nacisnietyTrzeciRaz = ");
        //Serial.println(nacisnietyTrzeciRaz(), DEC);
        //Serial.println("---------------------------");
    } 
}
#endif
    
    



