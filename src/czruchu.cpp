#include "czruchu.h"
#include "util.h"

CzRuchu::CzRuchu(Wejscia & wej_ , Wyjscia & wyj_) : wej(wej_), wyj(wyj_)
{
    
}

void CzRuchu::set() 
{
    /*
    Czujka c(wej.getCzRuchu());
    //Drzwi d(wej.getDrzwi());

    bool wieczor = wej.getWieczor();
    bool noc = wej.getNoc();

    if (c.isChange() && c.ruch()) {
        if (wyj.getLustro() || wyj.getSwiatlo())
            return;
        if (!wieczor || noc) {
            //Serial.print(__FILE__);
            //Serial.print(":");
            //Serial.println(__LINE__, DEC);
            wyj.setLustro(true, 2*60);
        } else {
            //Serial.print(__FILE__);
            //Serial.print(":");
            //Serial.println(__LINE__, DEC);
            wyj.setSwiatlo(true, 2*60);
        }
    }
    */
}
