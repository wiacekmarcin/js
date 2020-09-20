#include "lustro.h"
#include "util.h"
#include "wejscia.h"
#include "wyjscia.h"

Lustro::Lustro(Wejscia & we, Wyjscia & wy) : 
                    wej(we), wyj(wy), trybNormalny(true)
{

} 

void Lustro::zapal(int mls)
{
    trybNormalny = true;
    Serial.print("Zapal lustro, s=");
    Serial.println(mls, DEC);
    wyj.setLustro(true, mls);
    wyj.print("Zapal");
}

void Lustro::zapalJakoGlowne(int mls)
{
    trybNormalny = false;
    Serial.print("Zapal lustro, s=");
    Serial.println(mls, DEC);
    wyj.setLustro(true, mls);
    wyj.print("Zapal");
}

void Lustro::off()
{
    trybNormalny = true;
    Serial.println("Zgas lustro");
    wyj.setLustro(false);
    wyj.print("Lutro off");
}

void Lustro::set()
{
    if (!trybNormalny && !wyj.getLustro())
        trybNormalny = true;

    if (trybNormalny && setNormal())
        return;

    trybNormalny = !setSpecial();
    
}

bool Lustro::setNormal()
{
    bool onLustro = wyj.getLustro();
    Drzwi drzwi(wej.getDrzwi());
    Czujka czL = Czujka(wej.getLustro());

    //jezeli czujnik zblizeniowy wykryje ruch przez 0.5 s 
    //zalacze swiatlo na 30 s przy otwartych drzwiach i na 3 min przy zamknietych
    if (czL.czyRuch() && czL.czasRuchu() > 500) {
        Serial.print(__FILE__);Serial.print(":");Serial.println(__LINE__);
        zapal(drzwi.czyOtwarte() ? 30 : 3*60);
        return true;
    }

    // w przypadku gdy lustro swiecie i nastepuje otwarcie drzwi lustro gasnie
    if (onLustro && drzwi.isChange() && drzwi.czyOtwarte()) {
        Serial.print(__FILE__);Serial.print(":");Serial.println(__LINE__);
        off();
        return true;
    }
    return false;
}

bool Lustro::setSpecial()
{
        //tryb zastepczy swiatla glownego
    //1. w nocy po nacisnieciu klawisza
    //2.  dzien gdy drzwi sa otwarte i nie ma swiatla glownego a jest ruch

    bool noc = wej.getNoc();
    bool onL = wyj.getLustro();
    bool onS = wyj.getSwiatlo();
    bool wieczor = wej.getWieczor();
    Klawisz k = wej.getWlacznik();
    Drzwi d = wej.getDrzwi();
    Czujka c = wej.getCzRuchu();

    //noc zapalamy lustro
    if (noc && !onL && !onS && k.isChange() && k.czyNacisniety()) {
        Serial.print(__FILE__);Serial.print(":");Serial.println(__LINE__);
        zapalJakoGlowne(5*60);
        return true;
    }

    //noc klawisz wcisniety zapalamy glowne
    if (noc && onL && !onS && k.czyNacisniety() && k.czasWcisniecia() > 1000) {
        Serial.print(__FILE__);Serial.print(":");Serial.println(__LINE__);
        off();
        wyj.setSwiatlo(true, 5*60);
        return false; //wychodzi ze special trybu
    }

    //jak pali sie swiatlo glowne to nie ma specjalnych funkcji
    if (onS)
        return false;

    if (noc || wieczor) {
        //otwarcie drzwi
        if (d.isChange() && d.czyOtwarte()) {
            Serial.print(__FILE__);Serial.print(":");Serial.println(__LINE__);
            zapalJakoGlowne(1*60);
            return true;
        }

        //ruch przy zamknietych drzwiach
        if (! d.czyOtwarte() && c.czyRuch()) {
            Serial.print(__FILE__);Serial.print(":");Serial.println(__LINE__);
            zapalJakoGlowne(5*60);
            return true;
        }

        //ruch przy otwartych drzwiach
        if (d.czyOtwarte() && c.czyRuch()) {
            Serial.print(__FILE__);Serial.print(":");Serial.println(__LINE__);
            zapalJakoGlowne(1*60);
            return true;
        }

    }
    return !trybNormalny;
 }

