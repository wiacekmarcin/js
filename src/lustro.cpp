#include "lustro.h"
#include "util.h"
#include "wejscia.h"
#include "wyjscia.h"

Lustro::Lustro(Wejscia & we, Wyjscia & wy) : prevczL(false), timeFirstCzZb(0),
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
    bool czL = wej.getLustro();

    if (onLustro && drzwi.isChange() && drzwi.otwarte()) { //zmiana i drzwi otwarte
        off();
        return ;
    }
    if (! prevczL && czL) { //jezeli wykryto ruch 
        prevczL = true;
        timeFirstCzZb = mls;
    } else if (prevczL && czL) { 
        if (mls - timeFirstCzZb > 500) { //przez 0.5 s
            wyj.setLustro(true, mls + drzwi.otwarte() ? OFF_DRZWIOTWARTE : OFF_DRZWIZAMKNIETE);
        }
    }
}

