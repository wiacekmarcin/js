#include "lampa.h"
#include "wyjscia.h"

Lampa::Lampa(Wejcia & we, Wyjscia & wy) : wej(we), wyj(wy)
{ 

}

void Lampa::set()
{
    bool on = wyj.getSwiatlo();

    Drzwi drzwi(wyj.getDrzwi());
    Klawisz klawisz(wyj.getKlawisz());
}

