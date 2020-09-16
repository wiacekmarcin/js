#include "lampa.h"
#include "wyjscia.h"
#include "wejscia.h"
#include "czruchu.h"
#include "util.h"

Lampa::Lampa(Wejscia & we, Wyjscia & wy) : wej(we), wyj(wy)
{ 

}

void Lampa::set()
{
    bool onS = wyj.getSwiatlo();
    bool onL = wyj.getLustro();

    Drzwi drzwi(wej.getDrzwi());
    Klawisz klawisz(wej.getWlacznik());
    bool wieczor = wej.getWieczor();
    bool noc = wej.getNoc();
    Czujka czujka(wej.getCzRuchu());

    if (klawisz.isChange() && klawisz.val()) {
        if (!noc) {
            wyj.setSwiatlo(!onS, 5L*60L*1000);
        } else {
            if (onS)
                wyj.setSwiatlo(false);
            if (onL)
                wyj.setLustro(false);
            if (!onS && !onL) 
                wyj.setLustro(true, 5L*60L*1000L);
            if (!onS && onL) {
                wyj.setLustro(false);
                wyj.setSwiatlo(true, 5L*60L*1000L);
            }
        }
    }
}

