#include "lampa.h"
#include "wyjscia.h"
#include "wejscia.h"
#include "util.h"

Lampa::Lampa(Wejscia & we, Wyjscia & wy) : wej(we), wyj(wy)
{ 

}

void Lampa::set()
{
    bool onS = wyj.getSwiatlo();
    bool onL = wyj.getLustro();
    bool noc = wej.getNoc();
    Klawisz klawisz(wej.getWlacznik());


    if (!noc && klawisz.nacisniety()) {
        wyj.setSwiatlo(!onS, 30L*60L*1000L);
        return ;
    }

    if (noc && klawisz.nacisniety()) {
        if (!onS && !onL)
            wyj.setLustro(true);
        else if (onL && (millis() - klawisz.time() > 1000)) {
            wyj.setLustro(false);
            wyj.setSwiatlo(true);
        } else if (onS) {
            wyj.setSwiatlo(false);
        } 
    }

    Drzwi drzwi(wej.getDrzwi());
    
}

