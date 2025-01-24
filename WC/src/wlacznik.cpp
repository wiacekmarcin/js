#include "wlacznik.hpp"
#include <Arduino.h>
Wlacznik::Wlacznik() :
    prevVal(false),
    holdOn(false),
    jedenKlik(false),
    dwuKlik(false),
    trojKlik(false),
    cntKlik(0),
    timeLastEvent(0)
{
#ifdef DEBUG
    printmask = 0;
#endif // DEBUG      
}

void Wlacznik::set(bool on, unsigned long timelaps)
{
    if (prevVal == on) {
        if (!on && (holdOn || jedenKlik || dwuKlik || trojKlik)) {
            if (timelaps-timeLastEvent > 1000) {
                holdOn = false;
                jedenKlik = false;
                dwuKlik = false;
                trojKlik = false;
                cntKlik = 0;  
            }
        }
        return;
    }

    prevVal = on;
    if (on) {
        if (timelaps-timeLastEvent > 2000) {
            holdOn = false;
            jedenKlik = false;
            dwuKlik = false;
            trojKlik = false;
            cntKlik = 0;    
        }
        timeLastEvent = timelaps;
        return; //reaguje nie na wcisniecie klawisza tylko na wycisnienie klawisza 
    }

    if (timelaps-timeLastEvent > 500) {
        holdOn = true;
        jedenKlik = false;
        dwuKlik = false;
        trojKlik = false;
        cntKlik = 0;
    } else {
        ++cntKlik;
        holdOn = false;
        jedenKlik = cntKlik == 1;
        dwuKlik = cntKlik == 2;
        trojKlik = cntKlik == 3;
    }
}

void Wlacznik::print() 
{
#ifdef DEBUG
    unsigned long mask2  = 0;

    mask2 |= holdOn ? 0x1 : 0x0;
    mask2 |= jedenKlik ? 0x2 : 0x0;
    mask2 |= dwuKlik ? 0x4 : 0x0;
    mask2 |= trojKlik ? 0x8 : 0x0;

    if (mask2 != printmask) {
        printmask = mask2;
        Serial.println("------- Wlacznik ------");
        Serial.print("HoldON = ");
        Serial.println(holdOn, DEC);
        Serial.print("1Klik = ");
        Serial.println(jedenKlik, DEC);
        Serial.print("2klik = ");
        Serial.println(dwuKlik, DEC);
        Serial.print("3klik = ");
        Serial.println(trojKlik);
        Serial.println("---------------------------");
    } 
#endif // DEBUG    
}    
