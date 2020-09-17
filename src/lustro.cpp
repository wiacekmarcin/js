#include "lustro.h"
#include "util.h"
#include "wejscia.h"
#include "wyjscia.h"

Lustro::Lustro(Wejscia & we, Wyjscia & wy) : prevczL(false), prevDrzwiOtw(false), timeFirstCzZb(0),
                    wej(we), wyj(wy)
{

} 

void Lustro::zapal(unsigned long mls)
{
    wyj.setLustro(true, mls);
}

void Lustro::off()
{
    wyj.setLustro(false);
}

void Lustro::set()
{
    auto mls = millis();
    bool onLustro = wyj.getLustro();
    Drzwi drzwi(wej.getDrzwi());
    Value czL = wej.getLustro();

    if (czL.isChange() && czL.val()) {
        wyj.setLustro(true, 60);
        wyj.print("lustro");
    } else if (czL.isChange() && !czL.val()) {
        wyj.setLustro(false, 60);
        wyj.print("lustro");
    }

    /*
    if (onLustro && drzwi.isChange() && drzwi.otwarte()) { //zmiana i drzwi otwarte
        ////Serial.print(__FILE__);
        ////Serial.print(":");
        ////Serial.println(__LINE__, DEC);
        off();
        return ;
    }
    if (! prevczL && czL) { //jezeli wykryto ruch 
        ////Serial.print(__FILE__);
        ////Serial.print(":");
        ////Serial.println(__LINE__, DEC);
        prevczL = true;
        timeFirstCzZb = mls;
    } else if (prevczL && czL) { 
        ////Serial.print(__FILE__);
        ////Serial.print(":");
        ////Serial.println(__LINE__, DEC);
        if (mls - timeFirstCzZb > 500) { //przez 0.5 s
            ////Serial.print(__FILE__);
            ////Serial.print(":");
            ////Serial.println(__LINE__, DEC);
            wyj.setLustro(true, (drzwi.otwarte() ? OFF_DRZWIOTWARTE : OFF_DRZWIZAMKNIETE));
        }
    }
    */
}

