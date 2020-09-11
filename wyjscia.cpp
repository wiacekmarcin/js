#include "wyjscia.h"
Wyjscia::Wyjscia() :
    wyjscia(0x21)
{
    change = true;
    unsigned long mask = 0;
}

void Wyjscia::init()
{
    wyjscia.begin();      
    wyjscia.pinMode(SWIATLO, OUTPUT, HIGH);
    wyjscia.pinMode(SZAFKA, OUTPUT, HIGH);
    wyjscia.pinMode(LUSTRO, OUTPUT, HIGH);
    wyjscia.pinMode(ZAWOR, OUTPUT, HIGH);
    wyjscia.pinMode(WIATRAK, OUTPUT, LOW);
}

void Wyjscia::set(uint8_t pos, bool value, unsigned long tmt)
{
    wyjscia.digitalWrite(pos, o(pos, value));
    on[pos] = value;
    timeout[pos] = tmt + millis();
    mask |= 1 << pos;
}

void Wyjscia::tiktok() 
{
    unsigned long mls = millis();
    for (int i = 0; i < maxWyj; ++i) {
        if (on[i]) {
            if (timeout[i] < mls) {
                on[i] = false;
                change = true;
                wyjscia.digitalWrite(i, o(i, false));
                mask |= 1 << i;
            }
        }
    }
}

uint8_t Wyjscia::o(uint8_t id, bool value)
{
    return (id == WIATRAK) ? ho(value) : lo(value);
}

bool Wyjscia::i(uint8_t id, uint8_t value)
{
    return (id == WIATRAK) ? hi(value) : li(value);
}

void Wyjscia::print() 
{
    if (!change) 
        return;
    change = false;
    const char et[] = { "| swiatlo " 
                        "|  szafka "
                        "|  lustro " 
                        "|   zawor "
                        "| wiatrak |" };


    int klucze[] = { SWIATLO, SZAFKA, LUSTRO, ZAWOR, WIATRAK }; 
    Serial.println(et);
    for (int n = 0; n < maxWyj; n++) {
        Serial.print("|     ");
        Serial.print(on[klucze[n]] ? "T" : "N");
        Serial.print("    ");
    }
    Serial.println("|");


    for (unsigned int n = 0, m = 0; n < maxWyj; n++, m = m << 1) {
        Serial.print("|    ");
        Serial.print(mask & m == m ? "CHG" : "EQU");
        Serial.print("   ");
    }
    Serial.println("|");
    mask = 0;                       
}
