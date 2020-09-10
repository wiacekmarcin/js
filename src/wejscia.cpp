#include "wejscia.h"
Wejscia::Wejscia() :
    wejscia(0x20)
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
    //wejscia.pinMode(CZ_POZ_WODY, INPUT);
}


void Wejscia::get() 
{
    for (uint8_t i = 0; i < lenWej; ++i) {
        w[i] = wejscia.digitalRead(i);
    }
}

bool Wejscia::isChange() const
{
    for (uint8_t i = 0; i < lenWej; ++i) {
        if (w[i].isChange())
            return true;
    }
    return false;
}
