#include "swiatlo.h"
#include "wyjscia.h"
#include "wejscia.h"
#include "util.h"

Swiatlo::Swiatlo(Wejscia & we, Wyjscia & wy) : wej(we), wyj(wy), trybNormalny(false)
{ 

}

void Swiatlo::zapalSwiatlo(unsigned int s) 
{
    Serial.print("Zapal swiatlo, s=");
    Serial.println(s, DEC);
    wyj.setSwiatlo(true, s);
    wyj.print("Zapal swiatlo");
}

void Swiatlo::zgasSwiatlo()
{
    Serial.println("zgas swiatlo");
    wyj.setSwiatlo(false, 0);
    wyj.print("zgas swiatlo");
}

void Swiatlo::zapalLustro(int mls)
{
    trybNormalny = true;
    Serial.print("Zapal lustro, s=");
    Serial.println(mls, DEC);
    wyj.setLustro(true, mls);
    wyj.print("Zapal");
}

void Swiatlo::zapalLustroJakoSwiatlo(int mls)
{
    trybNormalny = false;
    Serial.print("Zapal lustro, s=");
    Serial.println(mls, DEC);
    wyj.setLustro(true, mls);
    wyj.print("Zapal");
}

void Swiatlo::zgasLustro()
{
    trybNormalny = true;
    Serial.println("Zgas lustro");
    wyj.setLustro(false);
    wyj.print("Lutro off");
}

void Swiatlo::setSwiatlo(bool pr)
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
        zgasSwiatlo();
        return ;
    }

    //jezeli swieci swiatlo to klawiszem zawsze wylaczamy
    if (onS && klawisz.isChange() && klawisz.czyNacisniety()) {
        Serial.print(__FILE__);Serial.print(":");Serial.println(__LINE__);
        zgasSwiatlo();
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

bool Swiatlo::set(bool pr)
{
    //reakcja na dlugi czas nacisniecia klawisza -> off
    Klawisz k = wej.getWlacznik();
    if (k.czasWcisniecia() > 2000) {
        Serial.print(__FILE__);Serial.print(":");Serial.println(__LINE__);
        trybNormalny = true;
        zgasLustro();
        return trybNormalny;
    }


    if (!trybNormalny && !wyj.getLustro())
        trybNormalny = true;

    if (trybNormalny && setNormal(pr))
        return trybNormalny;

    trybNormalny = !setSpecial(pr);
    return trybNormalny;
    
}

bool Swiatlo::setNormal(bool pr)
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
        zapalLustro(drzwi.czyOtwarte() ? 30 : 3*60);
        return true;
    }

    // w przypadku gdy lustro swiecie i nastepuje otwarcie drzwi lustro gasnie
    if (onLustro && drzwi.isChange() && drzwi.czyOtwarte()) {
        Serial.print(__FILE__);Serial.print(":");Serial.println(__LINE__);
        zgasLustro();
        return true;
    }
    return false;
}

bool Swiatlo::setSpecial(bool pr)
{
    /**
     * Mamy 3 scenariusze zapalania światła głównego i podświetlenia lustra
     * Scenariusze to dzień, wieczór i noc.
     * ************ DZIEN ************************
     * 1. Włącznik zapala lampe jak jest zgaszona
     * 2. Włącznik zgasza lampę jak jest zgaszona 
     * 3. Czujnik ruchu zapala lustro na 1 min przy otwartych drzwiach
     * 4. Czujnik ruchu zapala lustro na 5 min przy zamkniętych drzwiach
     * 5. Czujnik zbliżeniowy zapala lustro na 1 min przy otwartych drzwiach 
     * 6. Czujnik zbliżeniowy zapala lustro na 3 min przy zamkniętych drzwiach 
     * 7. Otwarcie drzwi powoduje zgaszenie lustra
     * 
     * ************ WIECZOR ********************
     * 1. Włącznik zapala lampę główną jak jest zgaszona
     * 2. Włącznik gasi lampę główną jak jest zapalona
     * 3. Włącznik gasi lustro przy zamkniętych drzwiach jak jest zapalone
     * 3. Czujnik ruchu zapala lampę główną na 1 min przy otwartych drzwiach
     * 4. Czujnik ruchu zapala lampę główną na 5 min przy zamkniętych drzwiach
     * 5. Czujnik zbliżeniowy zapala lustro na 1 min przy otwartych drzwiach
     * 6. Czujnik zbliżeniowy zapala lustro na 3 min przy zamknietych drzwiach
     * 7. Otwarcie drzwi jeżeli lustro pali się to gasi lustro
     * 8. Zamknięcie drzwi jeżeli lustro pali się to gasi je po 15s 
     *      od zamknięcia - w ten sposób dam czas czujnikowi ruchu na zapalanie lampy
     * 
     * ************** NOC ***********************
     * 1. Włącznik zapala lustro jak jest zgaszone lustro i światło
     * 2. Włącznik zapala światło i gasi lustro jak świeci się już lustro i czas od poprzedniego 
     *     załąćzenia włącznika mniejsze niż 10 s. 
     * 3!. Włącznik gasi światło i/lub lustro jeżelilustro lub światło główne jeżeli odstępy między kolejnymi 
     *     załączeniami jest większy niż 10 s //do poprawki
     * 4. Czujnik ruchu zapala lustro główną na 1 min przy otwartych drzwiach
     * 5. Czujnik ruchu zapala lustro główną na 3 min przy zamkniętych drzwiach
     * 6. Czujnik zbliżeniowy zapala lustro jeżeli świeci lampa główna na 0.5 min przy otwartych drzwiach
     * 7. Czujnik zbliżeniowy zapala lustro jeżeli świeci lampa główna na 2 min przy zamknietych drzwiach
     * 8. Otwarcie drzwi jeżeli lustro pali i pali się światło główne to gasi lustro
     **/
    
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
        zapalLustroJakoSwiatlo(5*60);
        return true;
    }

    //noc klawisz wcisniety gasimy wszystko
    if (noc && onL && !onS && k.czyNacisniety() && k.czasWcisniecia() < 1000) {
        Serial.print(__FILE__);Serial.print(":");Serial.println(__LINE__);
        zgasLustro();
        zapalSwiatlo(5*60);
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
            zapalLustroJakoSwiatlo(5*60);
            return true;
        }

        //noc nacisniecie w krotkim okresie czasu drugi raz klawisz 2s
        if (noc && !onL && onS && k.isChange() && k.czyNacisniety() && k.czasPrzedWcisnieciem() < 2000) {
            Serial.print(__FILE__);Serial.print(":");Serial.println(__LINE__);
            zgasLustro();
            zapalSwiatlo(5*60);
            return false; //wracamy do normalnosci
        }

        if (noc && onL && !onS && k.isChange() && k.czyNacisniety()) {
            Serial.print(__FILE__);Serial.print(":");Serial.println(__LINE__);
            zgasLustro();
            return false; //wracamy do normalnosci
        }

        //otwarcie drzwi
        if (!onL && !onS && d.isChange() && d.czyOtwarte()) {
            Serial.print(__FILE__);Serial.print(":");Serial.println(__LINE__);
            zapalLustroJakoSwiatlo(1*60);
            return true;
        }

        //ruch przy zamknietych/otwarych drzwiach nie ma swiatla
        if (!onL && c.czyRuch() && c.isChange()) {
            Serial.print(__FILE__);Serial.print(":");Serial.println(__LINE__);
            zapalLustroJakoSwiatlo(d.czyOtwarte() ? 1* 60 : 5*60);
            return true;
        }
    }
    return !trybNormalny;
 }



