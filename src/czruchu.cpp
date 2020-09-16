#include "czruchu.h"
#include "util.h"

CzRuchu::CzRuchu(Wejscia & wej_ , Wyjscia & wyj_) : wej(wej_), wyj(wyj_)
{
    
}

void CzRuchu::set() 
{
    Czujka c(wej.getCzRuchu());
    //Drzwi d(wej.getDrzwi());

    bool wieczor = wej.getWieczor();
    bool noc = wej.getNoc();

    if (c.isChange() && c.ruch()) {
        if (wyj.getLustro() || wyj.getSwiatlo())
            return;
        if (!wieczor || noc) {
            wyj.setLustro(true, 2L*60L*1000L);
        } else {
            wyj.setSwiatlo(true, 2L*60L*1000);
        }
    }
}
