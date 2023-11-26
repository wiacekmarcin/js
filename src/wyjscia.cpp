#include "wyjscia.h"
#include "util.h"
#include "debug.h"
#if 0

Wyjscia::Wyjscia(Adafruit_MCP23X17 &wyj) :
    wyjscia(wyj)
{
    for (int i = 0; i < maxWyj; ++i) {
        on[i] = false;
        timeout[i] = 0;
    }
    
}

void Wyjscia::init()
{
    wyjscia.pinMode(SWIATLO, OUTPUT);
    wyjscia.digitalWrite(SWIATLO, HIGH);

    wyjscia.pinMode(SZAFKA, OUTPUT);
    wyjscia.digitalWrite(SZAFKA, HIGH);

    wyjscia.pinMode(LUSTRO, OUTPUT);
    wyjscia.digitalWrite(LUSTRO, HIGH);

    wyjscia.pinMode(ZAWOR, OUTPUT);
    wyjscia.digitalWrite(ZAWOR, HIGH);

    wyjscia.pinMode(WY_SWIATLO, OUTPUT);
    wyjscia.digitalWrite(WY_SWIATLO, HIGH);

    wyjscia.pinMode(WIATRAK, OUTPUT);
    wyjscia.digitalWrite(WIATRAK, HIGH);

    for (int i = WY_FIRST; i <= WY_LAST; ++i) {
        set(i, false, 0);
    }
}

void Wyjscia::off() {
     for (int i = WY_FIRST; i <= WY_LAST; ++i) {
        set(i, false, 0);
    }
}

void Wyjscia::set(uint8_t pos, bool value, unsigned long tmt)
{
    unsigned long mls = millis();
    wyjscia.digitalWrite(pos, o(pos, value));
    on[pos] = value;
    timeout[pos] = 1000L*tmt + mls;
#ifdef DEBUG
    Serial.print("set pos=");
    Serial.print((int)pos, DEC);
    Serial.print(" value=");
    Serial.print((int)value, DEC);
    Serial.print(" tmt=");
    Serial.print(tmt, DEC);
    Serial.print(" timeout=");
    Serial.println(timeout[pos], DEC);
#endif // DEBUG        
}

void Wyjscia::add(uint8_t pos, unsigned long tmt)
{
    timeout[pos] += 1000L*tmt;
#ifdef DEBUG
    Serial.print(" tmt=");
    Serial.print(tmt, DEC);
    Serial.print(" timeout=");
    Serial.println(timeout[pos], DEC);
#endif // DEBUG        
}


bool Wyjscia::tiktok() 
{
    bool ret = false;
    unsigned long mls = millis();

    for (int i = WY_FIRST; i <= WY_LAST; ++i) {
        if (on[i]) {
            ret = true;
            if (timeout[i] < mls && timeout[i]) {
                on[i] = false;
                wyjscia.digitalWrite(i, o(i, false));
                timeout[i] = 0;
#ifdef DEBUG                
                Serial.print("tittok OFF = ");
                Serial.println(i, DEC);
#endif                
                print("tiktok OFF");
            }
        }
    }
#ifdef DEBUG      
    //Serial.print("tiktok call : ");
    //Serial.println(ret ? "One_On" : "All_off");
#endif    
    return ret;
}

uint8_t Wyjscia::o(uint8_t id, bool value)
{
    return (id == WIATRAK || id == WY_SWIATLO) ? ho(value) : lo(value);
}

void Wyjscia::print(const char * funn) const
{
#ifdef DEBUG
    unsigned long mls = millis();
    unsigned long mms = mls % 1000;
    Serial.print(mls, DEC);
    Serial.print(" (");
    Serial.print(mls/1000, DEC);
    Serial.print(".");
    if (mms < 10) 
        Serial.print("0");
    if (mms < 100) 
        Serial.print("0");
    Serial.print(mms, DEC);
    Serial.print(") ");
    Serial.println(funn);
    const char et[][9] = {  "swiatlo ", 
                            "lustro  ",
                            "szafka  ", 
                            "zawor   ",
                            "wy_swiat",
                            "wiatrak ",
                            "?       ", 
                            "?       ",
                        };

    int klucze[] = { SWIATLO, LUSTRO, SZAFKA, ZAWOR, WY_SWIATLO, WIATRAK };
    char buff[12];
    for (int i = 0; i < sizeof(klucze)/sizeof(klucze[0]); ++i) {
        Serial.print(et[i]);
        Serial.print(on[klucze[i]-SZAFKA] ? "1 " : "0 ");
        Serial.print(o(klucze[i], on[klucze[i]-SZAFKA]) ? "(H)" : "(L)");
        Serial.print(" ");
        printtime(timeout[on[klucze[i]-SZAFKA]], buff);
        Serial.println(buff);
    }
    
#endif // DEBUG    
}

#endif