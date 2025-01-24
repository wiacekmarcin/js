#include "debug.h"
#include <Arduino.h>
#include "myMcp.hpp"


using  WC_IO = MyMcp2317WC;

void debug_print_wejscie(uint8_t prev, uint8_t inD)
{
    if (prev == inD)
        return;
    Serial.print(millis(), DEC);
    Serial.print(" ");
    Serial.println(inD, BIN);
        
    Serial.print("PREV = ");
    for (int i=7; i >= 0; i--) 
        Serial.print(MASK(prev, i)?'1':'0');
    Serial.print("\nACTV = ");
    for (int i=7; i >= 0; i--) 
        Serial.print(MASK(inD, i)?'1':'0');
    
    Serial.print("\nCHAN = ");
    for (int i=7; i >= 0; i--) 
        Serial.print(MASK(prev^inD, i)?'1':'0');
    Serial.println("");

    
    Serial.print(MASK(inD, WC_IO::KLAWISZ) ? 'K' : 'k');
    Serial.print(MASK(inD, WC_IO::DRZWI) ? 'D' : 'd');
    Serial.print(MASK(inD, WC_IO::CZ_R_LUSTRO) ? 'L' : 'l');
    Serial.print(MASK(inD, WC_IO::CZ_R_WC) ? 'R' : 'r');
    Serial.print(MASK(inD, WC_IO::NOC) ? 'N' : 'n');
    Serial.print(MASK(inD, WC_IO::WIECZOR) ? 'W' : 'w');
    Serial.print(MASK(inD, WC_IO::TARYF2) ? 'T' : 't');
    Serial.println(MASK(inD, WC_IO::Z_AWAR) ? 'Z' : 'z');

    Serial.print(CHAN(inD, prev,  WC_IO::KLAWISZ) ? 'K' : ' ');
    Serial.print(CHAN(inD, prev,  WC_IO::DRZWI) ? 'D' : ' ');
    Serial.print(CHAN(inD, prev,  WC_IO::CZ_R_LUSTRO) ? 'L' : ' ');
    Serial.print(CHAN(inD, prev,  WC_IO::CZ_R_WC) ? 'R' : ' ');
    Serial.print(CHAN(inD, prev,  WC_IO::NOC) ? 'N' : ' ');
    Serial.print(CHAN(inD, prev,  WC_IO::WIECZOR) ? 'W' : ' ');
    Serial.print(CHAN(inD, prev,  WC_IO::TARYF2) ? 'T' : ' ');
    Serial.println(CHAN(inD, prev,  WC_IO::Z_AWAR) ? 'Z' : ' ');
}

