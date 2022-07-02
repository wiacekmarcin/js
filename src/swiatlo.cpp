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

    static bool ponL, ponS;
    static PoraDnia ppora;
    static Wlacznik pw;
    static Drzwi pd;
    static CzujkaRuchu pc;
    static CzujkaZblizeniowa pl;
    bool wasPr = false;
    
    if (ponL != onL) { Serial.print("onl=");Serial.print(onL, DEC); wasPr = true; }
    if (ponS != onS) { Serial.print(" onS=");Serial.print(onS, DEC); wasPr = true; }
    if (ppora.czyWieczor() != pora.czyWieczor()) { pora.print();/*Serial.print(" wie=");Serial.print(pora.czyWieczor(), DEC);*/ wasPr = true; }
    if (ppora.czyNoc() != pora.czyNoc()) { pora.print();/*Serial.print(" noc=");Serial.print(pora.czyNoc(), DEC);*/ wasPr = true; }
    if (pw.nacisniety() != w.nacisniety()) { w.print();/*Serial.print(" kla1=");Serial.print(w.nacisniety(), DEC);*/ wasPr = true; }
    if (pw.nacisnietyDrugiRaz() != w.nacisnietyDrugiRaz()) { w.print();/*Serial.print(" kla2=");Serial.print(w.nacisnietyDrugiRaz(), DEC);*/ wasPr = true; }
    if (pw.nacisnietyTrzeciRaz() != w.nacisnietyTrzeciRaz()) { w.print();/*Serial.print(" kla3=");Serial.print(w.nacisnietyTrzeciRaz(), DEC);*/ wasPr = true; }
    if (pd.czyOtwarte() != d.czyOtwarte()) { d.print();/*Serial.print(" dotw=");Serial.print(d.czyOtwarte());*/ wasPr = true; }
    if (pd.zostalyOtwarte() != d.zostalyOtwarte()) { d.print();/*Serial.print(" dott=");Serial.print(d.zostalyOtwarte());*/ wasPr = true; }
    if (pc.czyRuch() != c.czyRuch()) { c.print();/*Serial.print(" ruc=");Serial.print(c.czyRuch());*/ wasPr = true; }
    if (pl.czyRuch() != l.czyRuch()) { l.print();/*Serial.print(" lus=");Serial.print(l.czyRuch());*/ wasPr = true; }
    if (pl.czyDlugiRuch() != l.czyDlugiRuch()) { l.print();/*Serial.print(" ldr=");Serial.print(l.czyDlugiRuch());*/ wasPr = true; }

    //if (wasPr) {
    //    Serial.println();
    //    pora.print();

    ponL = onL;
    ponS = onS;
    ppora = pora;
    pw = w;
    pd = d;
    pc = c;
    pl = l;

    //zapal swiatlo przyciskem
    if (!onL && !onS && w.nacisniety()) {
        if (pora.czyWieczor() && !pora.czyNoc()) { //zapalamy glowne swiatlo
            //zapalSwiatlo(czasZapaleniaSwiatlo(pora.czyNoc(), d.czyOtwarte()));
            zapalSwiatlo(L_MIN(5));
        } else {  //zapalamy lustro
            lustroJakoSwiatlo = true;
            //zapalLustro(czasZapaleniaSwiatlo(pora.czyNoc(), d.czyOtwarte()));
            zapalLustro(L_MIN(5));
        }
        return true;
    }

    //gas swiatlo przyciskiem
    if ((onL || onS) && w.nacisniety()) {
        zgasLustro();
        lustroJakoSwiatlo = false;
        if (pora.czyNoc())
            zapalSwiatlo(L_SEC(5));
        else
            zgasSwiatlo();
        return true;
    }

    //drugi raz przycisk
    if (!onS && onL && w.nacisnietyDrugiRaz() && lustroJakoSwiatlo) {
        zgasLustro();
        lustroJakoSwiatlo = false;
        //zapalSwiatlo(czasZapaleniaSwiatlo(pora.czyNoc(), d.czyOtwarte()));
        zapalSwiatlo(L_MIN(20));
        return true;
    }

    //otwarcie drzwi
    if ((onS || onL) && d.zostalyOtwarte() && mls - w.czasWcisniecia() > L_SEC(5)) {
        if (onS && onL) {
            zgasLustro();
            zapalSwiatlo(L_MIN(1));
        }
        if (onS) {
            zapalSwiatlo(L_MIN(1));
        }
        if (onL) {
            zapalLustro(L_MIN(1));
        }
        return true;
    }

    //czujniki ruchu
    if (c.czyRuch() || l.czyRuch()) {
        if (onL && lustroJakoSwiatlo) {
            przedluzLustro(czasZapaleniaLustro(pora.czyNoc(), d.czyOtwarte()));
        } else if (onS) {
            przedluzSwiatlo(czasZapaleniaSwiatlo(pora.czyNoc(), d.czyOtwarte()));
        } else if (pora.czyWieczor()) {
            zapalSwiatlo(L_MIN(2));
        } else {
            lustroJakoSwiatlo = true;
            zapalLustro(L_MIN(2));
        }
        return true;
    }

    //podswietlenie lustra
    if (!onL && l.czyDlugiRuch() && !lustroJakoSwiatlo) {
        zapalLustro(czasZapaleniaLustro(pora.czyNoc(), d.czyOtwarte()));
        return true;
    }

    if (w.nacisnietyTrzeciRaz()) {
        wyj.setWiatrak(true, L_MIN(5));
    }
    

    return true;
}
