#include "wyjscia.h"
#include "util.h"
#include "version.h"
void Wyjscia::init()
{
    mcp->pinMode(ZAWOR, OUTPUT);
    mcp->pinMode(LUSTRO, OUTPUT);
    mcp->pinMode(SWIATLO, OUTPUT);
    mcp->pinMode(SZAFKA, OUTPUT);
    mcp->pinMode(WY_KONTAKTRON, OUTPUT);
    mcp->pinMode(WY_CZUJNIK_RUCHU, OUTPUT);
    pinMode(WY_SWIATLO, OUTPUT);
   
}

void Wyjscia::setExternal(uint8_t o, uint8_t val)
{
    switch(o) {
        case 1:
            mcp->digitalWrite(ZAWOR, val);
            break;
        case 2:
            mcp->digitalWrite(LUSTRO, val);
            break;
        case 3:
            mcp->digitalWrite(SWIATLO, val);
            break;
        case 4:
            mcp->digitalWrite(SZAFKA, val);
            break;
        default:
            return;
    }

    Serial1.print("S;");
    Serial1.print(DEVICE);
    Serial1.print(";");
    Serial1.print(o, DEC);
    Serial1.print(";");
    Serial1.println(val, DEC);
}


#if 0
void Wyjscia::set(uint8_t pos, bool value, unsigned int tmt)
{
    unsigned long mls = millis();
    wyjscia.digitalWrite(pos, o(pos, value));
    on[pos] = value;
    timeout[pos] = 1000L*tmt + mls;
    Serial.print("set pos=");
    Serial.print((int)pos, DEC);
    Serial.print(" value=");
    Serial.print((int)value, DEC);
    Serial.print(" tmt=");
    Serial.print(tmt, DEC);
    Serial.print(" timeout=");
    Serial.println(timeout[pos], DEC);
}

bool Wyjscia::tiktok() 
{
    bool ret = false;
    unsigned long mls = millis();

    for (int i = 0; i < maxWyj; ++i) {
        if (on[i]) {
            ret = true;
            if (timeout[i] < mls && timeout[i]) {
                on[i] = false;
                wyjscia.digitalWrite(i, o(i, false));
                timeout[i] = 0;
                Serial.print("tittok OFF = ");
                Serial.println(i, DEC);
                print("tiktok OFF");
            }
        }
    }
    Serial.print("tiktok call : ");
    Serial.print(ret ? "One_ON" : "All_off");
    return ret;
}

uint8_t Wyjscia::o(uint8_t id, bool value)
{
    return (id == WIATRAK) ? ho(value) : lo(value);
}

bool Wyjscia::i(uint8_t id, uint8_t value)
{
    return (id == WIATRAK) ? hi(value) : li(value);
}

void Wyjscia::print(const char * funn) const
{
    unsigned mls = millis();
    unsigned mms = mls % 1000;
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
    const char et[] = { "|  swiatlo  " 
                        "|   lustro  "
                        "|   szafka  " 
                        "|    zawor  "
                        "| wy_swiat  "
                        "|  wiatrak  |" 
                        };

    int klucze[] = { SWIATLO, LUSTRO, SZAFKA, ZAWOR, WY_SWIATLO, WIATRAK };
    Serial.println(et);
    for (int i = 0; i < maxWyj; ++i) {
        Serial.print("|     ");
        Serial.print(on[klucze[i]] ? "T" : "N");
        Serial.print("     ");
    }
    Serial.println("|");
    for (int i = 0; i < maxWyj; ++i) {
        Serial.print("|     ");
        Serial.print(o(klucze[i], on[klucze[i]]) ? "H" : "L");
        Serial.print("     ");
    }
    Serial.println("|");

    char buff[12];
    for (int i = 0; i < maxWyj; ++i) {
        Serial.print("|");
        //printtime(timeout[klucze[i]], buff);
        Serial.print(buff);
    }
    Serial.println("|");

}
#endif
