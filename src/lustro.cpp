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

bool Lustro::set(bool pr)
{
    //reakcja na dlugi czas nacisniecia klawisza -> off
    Klawisz k = wej.getWlacznik();
    if (k.czasWcisniecia() > 2000) {
        Serial.print(__FILE__);Serial.print(":");Serial.println(__LINE__);
        trybNormalny = true;
        off();
        return trybNormalny;
    }


    if (!trybNormalny && !wyj.getLustro())
        trybNormalny = true;

    if (trybNormalny && setNormal(pr))
        return trybNormalny;

    trybNormalny = !setSpecial(pr);
    return trybNormalny;
    
}

bool Lustro::setNormal(bool pr)
{
    bool onLustro = wyj.getLustro();
    Drzwi drzwi(wej.getDrzwi());
    Czujka czL = Czujka(wej.getLustro());

    if (pr) {
        Serial.println("LUSTRO SET NORMAL");
        Serial.print(" onL= ");
        Serial.print(onLustro, DEC);
        Serial.print(" d.isChange= ");
        Serial.print(drzwi.isChange(), DEC);
        Serial.print(" d.czyOtwarte= ");
        Serial.print(drzwi.czyOtwarte(), DEC);
        Serial.print(" cL.isChange= ");
        Serial.print(czL.isChange(), DEC);
        Serial.print(" cL.czasRuchu= ");
        Serial.println(czL.czasRuchu(), DEC);
    }

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

bool Lustro::setSpecial(bool pr)
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

    if (pr) {
        //noc zapalamy lustro1
        Serial.println("LUSTRO SET SPECIAL");
        Serial.print(" noc= ");
        Serial.print(noc, DEC);
        Serial.print(" wieczor= ");
        Serial.print(wieczor, DEC);
        Serial.print(" onL= ");
        Serial.print(onL, DEC);
        Serial.print(" onS= ");
        Serial.print(onS, DEC);
        Serial.print(" k.isChange= ");
        Serial.print(k.isChange(), DEC);
        Serial.print(" k.czyNacisniety= ");
        Serial.print(k.czyNacisniety(), DEC);
        Serial.print(" k.czasWcisniecia= ");
        Serial.print(k.czasWcisniecia(), DEC);
        Serial.print(" k.czasPrzedWcisnieciem= ");
        Serial.print(k.czasPrzedWcisnieciem(), DEC);
        Serial.print(" d.isChange= ");
        Serial.print(d.isChange(), DEC);
        Serial.print(" d.czyOtwarte= ");
        Serial.print(d.czyOtwarte(), DEC);
        Serial.print(" cR.isChange= ");
        Serial.print(c.isChange(), DEC);
        Serial.print(" cR.czyRuch= ");
        Serial.println(c.czyRuch(), DEC);
    }

    if (noc && !onL && !onS && k.isChange() && k.czyNacisniety()) {
        Serial.print(__FILE__);Serial.print(":");Serial.println(__LINE__);
        zapalJakoGlowne(5*60);
        return true;
    }

    //noc klawisz wcisniety gasimy wszystko
    if (noc && onL && !onS && k.czyNacisniety() && k.czasWcisniecia() < 1000) {
        Serial.print(__FILE__);Serial.print(":");Serial.println(__LINE__);
        off();
        wyj.setSwiatlo(true, 5*60);
        return false; //wychodzi ze special trybu
    }

    //jak pali sie swiatlo glowne to nie ma specjalnych funkcji
    if (onS) {
        return false;
    }

    if (noc || wieczor) {

        // noc brak swiatla nacisniecie raz klawisza
        if (noc && !onL && !onS && k.isChange() && k.czyNacisniety()) {
            Serial.print(__FILE__);Serial.print(":");Serial.println(__LINE__);
            zapalJakoGlowne(5*60);
            return true;
        }

        //noc nacisniecie w krotkim okresie czasu drugi raz klawisz 2s
        if (noc && !onL && onS && k.isChange() && k.czyNacisniety() && k.czasPrzedWcisnieciem() < 2000) {
            Serial.print(__FILE__);Serial.print(":");Serial.println(__LINE__);
            off();
            wyj.setSwiatlo(true, 5*60);
            return false; //wracamy do normalnosci
        }

        if (noc && onL && !onS && k.isChange() && k.czyNacisniety()) {
            Serial.print(__FILE__);Serial.print(":");Serial.println(__LINE__);
            off();
            return false; //wracamy do normalnosci
        }

        //otwarcie drzwi
        if (!onL && !onS && d.isChange() && d.czyOtwarte()) {
            Serial.print(__FILE__);Serial.print(":");Serial.println(__LINE__);
            zapalJakoGlowne(1*60);
            return true;
        }

        //ruch przy zamknietych/otwarych drzwiach nie ma swiatla
        if (!onL && c.czyRuch() && c.isChange()) {
            Serial.print(__FILE__);Serial.print(":");Serial.println(__LINE__);
            zapalJakoGlowne(d.czyOtwarte() ? 1* 60 : 5*60);
            return true;
        }
    }
    return !trybNormalny;
 }

