#include "lampa.h"
#include "wyjscia.h"
#include "wejscia.h"
#include "util.h"

Lampa::Lampa(Wejscia & we, Wyjscia & wy) : wej(we), wyj(wy)
{ 

}

void Lampa::zapalSwiatlo(unsigned int s) 
{
    Serial.print("Zapal swiatlo, s=");
    Serial.println(s, DEC);
    wyj.setSwiatlo(true, s);
    wyj.print("Zapal swiatlo");
}

void Lampa::off()
{
    Serial.println("zgas swiatlo");
    wyj.setSwiatlo(false, 0);
    wyj.print("zgas swiatlo");
}

void Lampa::set()
{
    bool onS = wyj.getSwiatlo();
    Klawisz klawisz(wej.getWlacznik());
    bool noc = wej.getNoc();
    bool wieczor = wej.getWieczor();
    Czujka c(wej.getCzRuchu());
     Drzwi d(wej.getDrzwi());

    //jezeli swieci swiatlo to klawiszem zawsze wylaczamy
    if (onS && klawisz.isChange() && klawisz.czyNacisniety()) {
        Serial.print(__FILE__);Serial.print(":");Serial.println(__LINE__);
        off();
        return;
    }

    //jezeli dzien to wlaczenie klawisza zapali swiatlo
    //dla nocy zapalanie swiatla jest w lustro
    if (!onS && noc && klawisz.isChange() && klawisz.czyNacisniety()) {
        Serial.print(__FILE__);Serial.print(":");Serial.println(__LINE__);
        zapalSwiatlo(10*60);
        return;
    }
    
    if (wieczor || noc || onS)
        Serial.print(__FILE__);Serial.print(":");Serial.println(__LINE__);
        return; //funkcjonalnosc w lustro

    //ruch przy zamknietych drzwiach
    if (! d.czyOtwarte() && c.czyRuch()) {
        Serial.print(__FILE__);Serial.print(":");Serial.println(__LINE__);
        zapalSwiatlo(5*60);
        return;
    }

    //ruch przy otwartych drzwiach
    if (d.czyOtwarte() && c.czyRuch()) {
        Serial.print(__FILE__);Serial.print(":");Serial.println(__LINE__);
        zapalSwiatlo(1*60);
        return;
    }
}

