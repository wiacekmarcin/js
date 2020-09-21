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

void Lampa::set(bool pr)
{
    bool onS = wyj.getSwiatlo();
    Klawisz klawisz(wej.getWlacznik());
    bool noc = wej.getNoc();
    bool wieczor = wej.getWieczor();
    Czujka c(wej.getCzRuchu());
    Drzwi d(wej.getDrzwi());

    //noc zapalamy lustro1
    if (pr) {
        Serial.println("LAMPA");
        Serial.print(" noc= ");
        Serial.print(noc, DEC);
        Serial.print(" wieczor= ");
        Serial.print(wieczor, DEC);
        Serial.print(" onS= ");
        Serial.print(onS, DEC);
        Serial.print(" k.isChange= ");
        Serial.print(klawisz.isChange(), DEC);
        Serial.print(" k.czyNacisniety= ");
        Serial.print(klawisz.czyNacisniety(), DEC);
        Serial.print(" k.czasWcisniecia= ");
        Serial.print(klawisz.czasWcisniecia(), DEC);
        Serial.print(" d.isChange= ");
        Serial.print(d.isChange(), DEC);
        Serial.print(" d.czyOtwarte= ");
        Serial.print(d.czyOtwarte(), DEC);
        Serial.print(" cR.isChange= ");
        Serial.print(c.isChange(), DEC);
        Serial.print(" cR.czyRuch= ");
        Serial.println(c.czyRuch(), DEC);
    }


    if (klawisz.czasWcisniecia() > 2000) {
        Serial.print(__FILE__);Serial.print(":");Serial.println(__LINE__);
        off();
        return ;
    }

    //jezeli swieci swiatlo to klawiszem zawsze wylaczamy
    if (onS && klawisz.isChange() && klawisz.czyNacisniety()) {
        Serial.print(__FILE__);Serial.print(":");Serial.println(__LINE__);
        off();
        return;
    }

    //jezeli dzien to wlaczenie klawisza zapali swiatlo
    //dla nocy zapalanie swiatla jest w lustro
    if (!onS && !noc && klawisz.isChange() && klawisz.czyNacisniety()) {
        Serial.print(__FILE__);Serial.print(":");Serial.println(__LINE__);
        zapalSwiatlo(10*60);
        return;
    }
    
    if (wieczor || noc) {
        //Serial.print(__FILE__);Serial.print(":");Serial.println(__LINE__);
        return; //funkcjonalnosc w lustro
    }

    //ruch przy zamknietych//otwartycg drzwiach drzwiach
    if (c.czyRuch() && c.isChange()) {
        Serial.print(__FILE__);Serial.print(":");Serial.println(__LINE__);
        zapalSwiatlo(d.czyOtwarte() ? 1*60 : 5*60);
        return;
    }

    
}

