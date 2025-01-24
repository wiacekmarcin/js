#include "wyjscia.h"
Wyjscia::Wyjscia() :
    wyjscia(0x21)
{
    
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
}

void Wyjscia::tiktok() 
{
    unsigned long mls = millis();
    for (int i = 0; i < maxWyj; ++i) {
        if (on[i]) {
            if (timeout[i] < mls) {
                on[i] = false;
                wyjscia.digitalWrite(i, o(i, false));
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