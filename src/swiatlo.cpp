#include "swiatlo.h"
#include "wyjscia.h"
#include "wejscia.h"
#include "util.h"
#include "in.h"


Swiatlo::Swiatlo(Wejscia & we, Wyjscia & wy) : wej(we), wyj(wy), lustroJakoSwiatlo(false)
{ 

}

void Swiatlo::zapalSwiatlo(unsigned int s) 
{
#ifdef DEBUG    
    Serial.print("Zapal swiatlo, s=");
    Serial.println(s, DEC);
#endif    
    wyj.setSwiatlo(true, s);
    wyj.print("Zapal swiatlo");
}

void Swiatlo::przedluzSwiatlo(unsigned int s) 
{
#ifdef DEBUG    
    Serial.print("Przedluz swiatlo, s=");
    Serial.println(s, DEC);
#endif    
    wyj.addSwiatlo(s);
    wyj.print("Zapal swiatlo");
}


void Swiatlo::zgasSwiatlo()
{
#ifdef DEBUG
    Serial.println("zgas swiatlo");
#endif    
    wyj.setSwiatlo(false, 0);
    wyj.print("zgas swiatlo");
}

void Swiatlo::zapalLustro(int mls)
{
#ifdef DEBUG
    Serial.print("Zapal lustro, s=");
    Serial.println(mls, DEC);
#endif
    wyj.setLustro(true, mls);
    wyj.print("Zapal");
}

void Swiatlo::przedluzLustro(int mls)
{
#ifdef DEBUG
    Serial.print("Przedluz lustro, s=");
    Serial.println(mls, DEC);
#endif
    wyj.addLustro(mls);
    wyj.print("Zapal");
}

void Swiatlo::zgasLustro()
{
#ifdef DEBUG
    Serial.println("Zgas lustro");
#endif // DEBUG    
    wyj.setLustro(false);
    wyj.print("Lutro off");
    
}

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

bool Swiatlo::set(unsigned long mls)
{
    bool onL = wyj.getLustro();
    bool onS = wyj.getSwiatlo();
    
    const PoraDnia & pora = wej.getPoraDnia();
    const Wlacznik & w = wej.getWlacznik();
    const Drzwi & d = wej.getDrzwi();
    const CzujkaRuchu & c = wej.getCzujkaRuchu();
    const CzujkaZblizeniowa & l = wej.getCzujkaZbl();

    if (!onL && !onS && w.nacisniety()) {
        if (pora.czyWieczor() && !pora.czyNoc()) { //zapalamy glowne swiatlo
            zapalSwiatlo(czasZapaleniaSwiatlo(pora.czyNoc(), d.czyOtwarte()));
        } else {  //zapalamy lustro
            lustroJakoSwiatlo = true;
            zapalLustro(czasZapaleniaSwiatlo(pora.czyNoc(), d.czyOtwarte()));
        }
        return;
    }

    if (!onS && onL && w.nacisnietyDrugiRaz() && lustroJakoSwiatlo) {
        zgasLustro();
        lustroJakoSwiatlo = false;
        zapalSwiatlo(czasZapaleniaSwiatlo(pora.czyNoc(), d.czyOtwarte()));
    }

    if (onS && w.nacisniety()) {
        if (pora.czyNoc() && pora.czyWieczor()) {
            zapalSwiatlo(L_SEC(15));
        } else {
            zgasSwiatlo();
        }
    }

    if (onL && w.nacisniety() && lustroJakoSwiatlo) {
        if (pora.czyNoc() && pora.czyWieczor()) {
            zapalLustro(L_SEC(15));
        } else {
            zgasLustro();
        }
        lustroJakoSwiatlo = false;
        return;
    } 

    if (!lustroJakoSwiatlo && !onL && l.czyRuch()) {
        zapalLustro(czasZapaleniaLustro(pora.czyNoc(), d.czyOtwarte()));
        return;
    }

    if (!onL && !onS && c.czyRuch()) {
        if (pora.czyNoc() && pora.czyWieczor()) {
            zapalLustro(L_MIN(1));
            lustroJakoSwiatlo = true;
        } else {
            zapalSwiatlo(L_MIN(3));
        }
        return;    
    }
    
    if (onS && c.czyRuch()) {
        if (pora.czyNoc() && pora.czyWieczor()) {
            przedluzSwiatlo(L_MIN(1));
        } else {
            przedluzSwiatlo(L_MIN(3));
        }
        return;    
    }
    
    if (onL && c.czyRuch() && lustroJakoSwiatlo) {
        if (pora.czyNoc() && pora.czyWieczor()) {
            przedluzLustro(L_MIN(1));
        } else {
            przedluzLustro(L_MIN(3));
        }
        return;    
    }

    return true;
}


void Swiatlo::setDzien() 
{
    // * 1. Włącznik zapala lustro jak jest zgaszona
    // * 2. Podwojny włącznik zapala swiatlo jak jest zgaszona i gasi lustro
    // * 3. Włącznik zgasza lampę i lustro jak jest zapalone
    // * 4. Czujnik ruchu zapala lustro na 1 min przy otwartych drzwiach
    // * 5. Czujnik ruchu zapala lustro na 5 min przy zamkniętych drzwiach
    // * 6. Czujnik zbliżeniowy zapala lustro na 1 min przy otwartych drzwiach 
    // * 7. Czujnik zbliżeniowy zapala lustro na 3 min przy zamkniętych drzwiach 
    // * 8. Otwarcie drzwi powoduje zgaszenie lustra przy zapalonym swietle glownym
    // * 9. jak jest zapalone swiatlo glowne i lusro przy otwarciu drzwi zgas swiatlo

    bool onL = wyj.getLustro();
    bool onS = wyj.getSwiatlo();

    const Wlacznik & w = wej.getWlacznik();
    const Drzwi & d = wej.getDrzwi();
    const CzujkaRuchu & c = wej.getCzujkaRuchu();
    const CzujkaZblizeniowa & l = wej.getCzujkaZbl();

    //1.
    if (!onL && !onS && w.nacisniety()) {
        zapalLustro(L_MIN(5));
        //return;
    }

    //2
    if (onL && !onS && w.nacisnietyDrugiRaz()) {
        zgasLustro();
        zapalSwiatlo(L_MIN(10));
        //return;
    }

    //3
    if ((onL || onS) && w.nacisniety()) {
        zgasLustro();
        zgasSwiatlo();
        //return;
    }

    //4 i 5 ruch wydluza zapalone swiatlo lustra
    if (c.czyRuch() && onL && !onS) {
        przedluzLustro(d.czyOtwarte() ? L_MIN(1) : L_MIN(5));
        //return; 
    }

    //4 i 5 ruch wydluza zapalone swiatlo glowne
    if (c.czyRuch() && onS) {
        przedluzSwiatlo(d.czyOtwarte() ? L_MIN(1) : L_MIN(5));
        //return; 
    }
    
    //4 i 5 zapala lustro 
    if (c.czyRuch() && !onS && !onL) {
        zapalLustro(d.czyOtwarte() ? L_MIN(1) : L_MIN(5));
        //return;
    }

    // 6 i 7
    if (!onL && l.czyRuch()) {
        zapalLustro(d.czyOtwarte() ? L_MIN(1) : L_MIN(5));
    }

    //9
    if (onL && onS && d.zostalyOtwarte()) {
        zgasLustro();
    }

   
}

void Swiatlo::setWieczor() {
    // * 1. Włącznik zapala lampę główną jak jest zgaszona
    // * 2. Włącznik gasi lampę główną jak jest zapalona
    // * 3. Włącznik gasi lustro przy zamkniętych drzwiach jak jest zapalone
    // * 4. Czujnik ruchu przedluza swiecenie lampy głównej na 1 min przy otwartych drzwiach
    // * 5. Czujnik ruchu przedluza swiecenie lampę główną na 5 min przy zamkniętych drzwiach
    // * 6. Czujnik ruchu zapala lampę główną na 1 min przy otwartych drzwiach
    // * 7. Czujnik ruchu zapala lampę główną na 5 min przy zamkniętych drzwiach
    // * 8. Czujnik zbliżeniowy zapala lustro na 1 min przy otwartych drzwiach
    // * 9. Czujnik zbliżeniowy zapala lustro na 3 min przy zamknietych drzwiach
    // *10. Otwarcie drzwi jeżeli lustro pali się to gasi lustro


    bool onL = wyj.getLustro();
    bool onS = wyj.getSwiatlo();

    const Wlacznik & w = wej.getWlacznik();
    const Drzwi & d = wej.getDrzwi();
    const CzujkaRuchu & c = wej.getCzujkaRuchu();
    const CzujkaZblizeniowa l = wej.getCzujkaZbl();

    //1 
    if (w.nacisniety() && !onS) {
        zapalSwiatlo(L_MIN(5));
        return;
    }

    //2
    if (w.nacisniety() && onS) {
        zgasSwiatlo();
        return;
    }

    //3
    if (w.nacisniety() && onL && d.czyZamkniete()) {
        zgasLustro();
        return;
    }

    //4 i 5
    if (c.czyRuch() && onS) {
        przedluzSwiatlo(d.czyOtwarte() ? L_MIN(1) : L_MIN(5));
        return; 
    }
    
    //6 i 7
    if (c.czyRuch() && !onS) {
        zapalSwiatlo(d.czyOtwarte() ? L_MIN(1) : L_MIN(5));
        return; 
    }

    //8 i 9
    if (l.czyRuch() && !onL) {
        zapalLustro(d.czyOtwarte() ? L_MIN(1) : L_MIN(3));
        return;
    }

    //8 i 9
    if (l.czyRuch() && onL) {
        przedluzLustro(d.czyOtwarte() ? L_MIN(1) : L_MIN(3));
        return;
    }

    //10
    if (onL && onS && d.zostalyOtwarte()) {
        zgasLustro();
        return;
    }

}

void Swiatlo::setNoc()
{
    // * 1. Włącznik zapala lustro jak jest zgaszone lustro i światło
    // * 2. Włącznik zapala światło i gasi lustro jak świeci się już lustro i czas od poprzedniego 
    // *     załąćzenia włącznika mniejsze niż 10 s. 
    // * 3!. Włącznik gasi światło i/lub lustro jeżelilustro lub światło główne jeżeli odstępy między kolejnymi 
    // *     załączeniami jest większy niż 10 s //do poprawki
    // * 4. Czujnik ruchu zapala lustro główną na 1 min przy otwartych drzwiach
    // * 5. Czujnik ruchu zapala lustro główną na 3 min przy zamkniętych drzwiach
    // * 6. Czujnik zbliżeniowy zapala lustro jeżeli świeci lampa główna na 0.5 min przy otwartych drzwiach
    // * 7. Czujnik zbliżeniowy zapala lustro jeżeli świeci lampa główna na 2 min przy zamknietych drzwiach
    // * 8. Otwarcie drzwi jeżeli lustro pali i pali się światło główne to gasi lustro
     

    bool onL = wyj.getLustro();
    bool onS = wyj.getSwiatlo();
    const Wlacznik & w = wej.getWlacznik();
    const Drzwi & d = wej.getDrzwi();
    const CzujkaRuchu & c = wej.getCzujkaRuchu();
    const CzujkaZblizeniowa & l = wej.getCzujkaZbl();

    //1
    if (w.nacisniety() && !onL && !onS) {
        zapalLustro(L_MIN(5));
        return;
    }

    //2
    if (w.nacisnietyDrugiRaz() && onL) {
        zgasLustro();
        zapalSwiatlo(L_MIN(5));
        return;
    }

    //3
    if (w.nacisniety() && onL) {
        zapalLustro(L_SEC(15)); //nie gas od razu tylko po 15 s
        return;
    }

    //3
    if (w.nacisniety() && onS) {
        zgasLustro();
        zapalLustro(L_SEC(15)); //nie gas od razu tylko po 15 s
        return;
    }

    //6 i 7
    if (onS && !onL && l.czyRuch()) {
        zapalLustro(d.czyOtwarte() ? L_SEC(30) : L_MIN(2));
        return;
    }

    //4 i 5
    if (onS && c.czyRuch()) {
        przedluzSwiatlo(d.czyOtwarte() ? L_SEC(30) : L_MIN(2));
        return;
    }

    //4 i 5
    if (!onS && onL && c.czyRuch()) {
        przedluzLustro(d.czyOtwarte() ? L_SEC(30) : L_MIN(2));
        return;
    }

    if (onL && onS && d.zostalyOtwarte()) {
        zgasLustro();
        zapalSwiatlo(L_SEC(15)); // gas po 15s
        return;
    }
}