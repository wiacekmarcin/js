#include "debug.h"
#include "in.h"
#include "util.h"
#include "wejscia.h"
#include <Arduino.h>
#include "myMcp.hpp"
#if 0
#ifdef DEBUG
void print_wlacznik(const Wlacznik * w)
{
    static unsigned long mask  = 0;
    unsigned long mask2  = 0;

    mask2 |= 0x01 & w->m_val;
    mask2 |= (0x01 & w->m_prev) << 1;
    mask2 |= (0x0F & w->m_cntPush) << 2;
    mask2 |= (0xFF & w->m_timePush) << 6;
    mask2 |= (0xFF & w->m_timeHold) << 14;

    if (mask2 != mask) {
        mask = mask2;
        Serial.println("------- Wlacznik ------");
        Serial.print("val = ");
        Serial.println(w->m_val, DEC);
        Serial.print("prev = ");
        Serial.println(w->m_prev, DEC);
        Serial.print("cntPush = ");
        Serial.println(w->m_cntPush, DEC);
        Serial.print("timePush = ");
        Serial.println(w->m_timePush, DEC);
        Serial.print("timeHold = ");
        Serial.println(w->m_timeHold, DEC);
        Serial.println("****");
        Serial.print("nacisniety = ");
        Serial.println(w->nacisniety(), DEC);
        Serial.print("wcisniety = ");
        Serial.println(w->wcisniety(), DEC);
        Serial.print("czasWcisniecia = ");
        Serial.println(w->czasWcisniecia(), DEC);
        Serial.print("nacisnietyDrugiRaz = ");
        Serial.println(w->nacisnietyDrugiRaz(), DEC);
        Serial.print("nacisnietyTrzeciRaz = ");
        Serial.println(w->nacisnietyTrzeciRaz(), DEC);
        Serial.println("---------------------------");
    } 
}

void print_czujkazblizeniowa(const CzujkaZblizeniowa * cz)
{
    static unsigned long mask  = 0;
    unsigned long mask2  = 0;

    mask2 |= 0x01 & cz->m_val;
    mask2 |= (0x01 & cz->m_prev) << 1;
    mask2 |= (0xFF & cz->m_timeSig) << 2;
    mask2 |= (0xFF & cz->m_timeHold) << 10;

    if (mask2 != mask) {
        mask = mask2;
        Serial.println("------- Czujka zblizeniowa ------");
        Serial.print("val = ");
        Serial.println(cz->m_val, DEC);
        Serial.print("prev = ");
        Serial.println(cz->m_prev, DEC);
        Serial.print("ruch = ");
        Serial.println(cz->m_ruch, DEC);
        Serial.print("wykrytoRuch = ");
        Serial.println(cz->m_wykrytoRuch);
        Serial.print("timeSig = ");
        Serial.println(cz->m_timeSig, DEC);
        Serial.print("timeHold = ");
        Serial.println(cz->m_timeHold, DEC);
        Serial.println("****");
        Serial.print("czyRuch = ");
        Serial.println(cz->czyRuch(), DEC);
        Serial.println("---------------------------");
    } 
}

void print_czujkaruchu(const CzujkaRuchu *cr)
{
        static unsigned long mask  = 0;
    unsigned long mask2  = 0;

    mask2 |= 0x01 & cr->m_val;
    mask2 |= (0x01 & cr->m_prev) << 1;
    mask2 |= (0x01 & cr->m_ruch) << 2;

    if (mask2 != mask) {
        mask = mask2;
        Serial.println("------- Czujka ruchu ------");
        Serial.print("val = ");
        Serial.println(cr->m_val, DEC);
        Serial.print("prev = ");
        Serial.println(cr->m_prev, DEC);
        Serial.print("ruch = " );
        Serial.println(cr->m_ruch, DEC);
        Serial.print("timelastMove = ");
        Serial.println(cr->m_timelastMove, DEC);
        Serial.println("****");
        Serial.print("czyRuch = ");
        Serial.println(cr->czyRuch(), DEC);
        Serial.print("czasBezRuchu = ");
        Serial.println(cr->czasBezRuchu(), DEC);
        Serial.println("---------------------------");
    } 
}

void print_drzwi(const Drzwi *d)
{
    static unsigned long mask  = 0;
    unsigned long mask2  = 0;

    mask2 |= 0x01 & d->m_val;
    mask2 |= (0x01 & d->m_prev) << 1;
    mask2 |= (0x01 & d->m_otwarte) << 2;

    if (mask2 != mask) {
        mask = mask2;
        Serial.println("---------- Drzwi ---------");
        Serial.print("val = ");
        Serial.println(d->m_val, DEC);
        Serial.print("prev = ");
        Serial.println(d->m_prev, DEC);
        Serial.print("otwarte = " );
        Serial.println(d->m_otwarte, DEC);
        Serial.print("timeOpen = ");
        Serial.println(d->m_timeOpen, DEC);
        Serial.print("timeClose = ");
        Serial.println(d->m_timeClose, DEC);
        Serial.println("****");
        Serial.print("czyOtwarte = ");
        Serial.println(d->czyOtwarte(), DEC);
        Serial.print("czyZamkniete = ");
        Serial.println(d->czyZamkniete(), DEC);
        Serial.print("czasOtwarcia = ");
        Serial.println(d->czasOtwarcia(), DEC);
        Serial.print("czasZamkniecia = ");
        Serial.println(d->czasZamkniecia(), DEC);
        Serial.println("---------------------------");
    } 
}

void print_poradnia(const PoraDnia * p)
{    
    static unsigned long mask  = 0;
    unsigned long mask2  = 0;

    mask2 |= 0x01 & p->m_noc;
    mask2 |= (0x01 & p->m_prevnoc) << 1;
    mask2 |= (0x01 & p->m_wieczor) << 2;
    mask2 |= (0x01 & p->m_prevwieczor) << 3;
    mask2 |= (0x01 & p->m_taryf2) << 4;
    mask2 |= (0x01 & p->m_prevtaryf2) << 5;
    mask2 |= (0x01 & p->m_zas_awar) << 6;
    mask2 |= (0x01 & p->m_prevzas_awar) << 7;
    if (mask2 != mask) {
        mask = mask2;
        Serial.println("---------- Pora dnia ---------");
        Serial.print("noc = ");
        Serial.println(p->m_noc, DEC);
        Serial.print("prevnoc = ");
        Serial.println(p->m_prevnoc, DEC);
        Serial.print("wieczor = ");
        Serial.println(p->m_wieczor, DEC);
        Serial.print("prevwieczor = ");
        Serial.println(p->m_prevwieczor, DEC);
        Serial.print("taryf2 = ");
        Serial.println(p->m_taryf2, DEC);
        Serial.print("prevtaryf2 = ");
        Serial.println(p->m_prevtaryf2, DEC);
        Serial.print("zas.awar = ");
        Serial.println(p->m_zas_awar, DEC);
        Serial.print("prev.zas.awar = ");
        Serial.println(p->m_prevzas_awar, DEC);
        Serial.println("-------");

        Serial.print("czyWieczor() = ");
        Serial.println(p->czyWieczor());
        Serial.print("czyNoc() = ");
        Serial.println(p->czyNoc());
        Serial.print("czyDzien() = ");
        Serial.println(p->czyDzien());
        Serial.print("CzyZasAwar()=");
        Serial.println(p->czyZasAwar());
        Serial.print("CzyTaryf2()=");
        Serial.println(p->czyTaryf2());
    }
}

#endif
#endif

using  WC_IO = MyMcp2317WC;

void debug_print_wejscie(uint8_t prev, uint8_t inD)
{
    if (prev == inD)
        return;
    Serial.print(millis(), DEC);
    Serial.print(" ");
    Serial.println(inD, BIN);
        
    Serial.print("PREV = ");
    for (int i=7; i >= 0; i--) 
        Serial.print(MASK(prev, i)?'1':'0');
    Serial.print("\nACTV = ");
    for (int i=7; i >= 0; i--) 
        Serial.print(MASK(inD, i)?'1':'0');
    
    Serial.print("\nCHAN = ");
    for (int i=7; i >= 0; i--) 
        Serial.print(MASK(prev^inD, i)?'1':'0');
    Serial.println("");

    
    Serial.print(MASK(inD, WC_IO::KLAWISZ) ? 'K' : 'k');
    Serial.print(MASK(inD, WC_IO::DRZWI) ? 'D' : 'd');
    Serial.print(MASK(inD, WC_IO::CZ_R_LUSTRO) ? 'L' : 'l');
    Serial.print(MASK(inD, WC_IO::CZ_R_WC) ? 'R' : 'r');
    Serial.print(MASK(inD, WC_IO::NOC) ? 'N' : 'n');
    Serial.print(MASK(inD, WC_IO::WIECZOR) ? 'W' : 'w');
    Serial.print(MASK(inD, WC_IO::TARYF2) ? 'T' : 't');
    Serial.println(MASK(inD, WC_IO::Z_AWAR) ? 'Z' : 'z');

    Serial.print(CHAN(inD, prev,  WC_IO::KLAWISZ) ? 'K' : ' ');
    Serial.print(CHAN(inD, prev,  WC_IO::DRZWI) ? 'D' : ' ');
    Serial.print(CHAN(inD, prev,  WC_IO::CZ_R_LUSTRO) ? 'L' : ' ');
    Serial.print(CHAN(inD, prev,  WC_IO::CZ_R_WC) ? 'R' : ' ');
    Serial.print(CHAN(inD, prev,  WC_IO::NOC) ? 'N' : ' ');
    Serial.print(CHAN(inD, prev,  WC_IO::WIECZOR) ? 'W' : ' ');
    Serial.print(CHAN(inD, prev,  WC_IO::TARYF2) ? 'T' : ' ');
    Serial.println(CHAN(inD, prev,  WC_IO::Z_AWAR) ? 'Z' : ' ');
}

