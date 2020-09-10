#include "lampa.h"
#include "wyjscia.h"
#include "wejscia.h"
#include "util.h"

Lampa::Lampa(Wejscia & we, Wyjscia & wy) : wej(we), wyj(wy)
{ 

}

void Lampa::set()
{
    bool on = wyj.getSwiatlo();

    Drzwi drzwi(wej.getDrzwi());
    Klawisz klawisz(wej.getWlacznik());
}

