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

    //drzwi.print();
    //klawisz.print();
    //czujka.print();
    //Serial.print("Noc=");
    //Serial.println(noc, DEC);
    //Serial.print("Wieczor=");
    //Serial.println(wieczor, DEC);

    if (klawisz.isChange() && klawisz.nacisniety()) {
        if (onS)
        {
            wyj.setSwiatlo(false);
        }
        else
        {
            wyj.setSwiatlo(true);
        }
        wyj.print("lampa");
    }

    /*
    if (klawisz.isChange() && klawisz.val()) {
        if (!noc) {
            //Serial.print(__FILE__);
            //Serial.print(":");
            //Serial.println(__LINE__, DEC);
            wyj.setSwiatlo(!onS, 5*60);
        } else {
            if (onS) {
                //Serial.print(__FILE__);
                //Serial.print(":");
                //Serial.println(__LINE__, DEC);
                wyj.setSwiatlo(false);
            }
            if (onL) {
                //Serial.print(__FILE__);
                //Serial.print(":");
                //Serial.println(__LINE__, DEC);
                wyj.setLustro(false);
            }
            if (!onS && !onL) {
                //Serial.print(__FILE__);
                //Serial.print(":");
                //Serial.println(__LINE__, DEC);
                wyj.setLustro(true, 5*60);
            }
            if (!onS && onL) {
                //Serial.print(__FILE__);
                //Serial.print(":");
                //Serial.println(__LINE__, DEC);
                wyj.setLustro(false);
                wyj.setSwiatlo(true, 5*60);
            }
        }
    }
    */
}

