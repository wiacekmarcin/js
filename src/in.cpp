#include "in.h"

Wlacznik::Wlacznik() : ValueBase(), m_cntPush(0), m_timeInt(0), m_timePush(0), m_timeHold(0) 
{
    m_prev = 1;
    m_val = 1;
}
    
void Wlacznik::clearState() 
{
    m_cntPush = 0;
    m_timePush = 0;
    m_timeHold = 0;
}    

void Wlacznik::ustaw(uint8_t value, unsigned long timeInt, unsigned int timeAfterInt)
{
    m_prev = m_val;
    m_val = (value == LOW); //klawisz nacisniety
 
    if (m_timeInt != timeInt || (timeAfterInt - m_timePush) > SEC(1)) { //inne przerwanie lub czas powyzej 1s
        m_timeInt = timeInt;
        clearState();
    }
    
    if (m_val && !m_prev) {
        ++m_cntPush;
        m_timePush = timeAfterInt;
        m_timeHold = 0;
    }

    if (m_val && m_prev ) { //nacisniety klawisz i przytrzymany przez {
        m_timeHold = timeAfterInt - m_timePush;
    }
}

#ifdef DEBUG
void Wlacznik::print() const
{
    static unsigned long mask  = 0;
    unsigned long mask2  = 0;

    mask2 |= 0x01 & m_val;
    mask2 |= (0x01 & m_prev) << 1;
    mask2 |= (0x0F & m_cntPush) << 2;
    mask2 |= (0xFF & m_timePush) << 6;
    mask2 |= (0xFF & m_timeHold) << 14;

    if (mask2 != mask) {
        mask = mask2;
        Serial.println("------- Wlacznik ------");
        Serial.print("val = ");
        Serial.println(m_val, DEC);
        Serial.print("prev = ");
        Serial.println(m_prev, DEC);
        Serial.print("cntPush = ");
        Serial.println(m_cntPush, DEC);
        Serial.print("timePush = ");
        Serial.println(m_timePush, DEC);
        Serial.print("timeHold = ");
        Serial.println(m_timeHold, DEC);
        Serial.println("****");
        Serial.print("nacisniety = ");
        Serial.println(nacisniety(), DEC);
        Serial.print("wcisniety = ");
        Serial.println(wcisniety(), DEC);
        Serial.print("czasWcisniecia = ");
        Serial.println(czasWcisniecia(), DEC);
        Serial.print("nacisnietyDrugiRaz = ");
        Serial.println(nacisnietyDrugiRaz(), DEC);
        Serial.print("nacisnietyTrzeciRaz = ");
        Serial.println(nacisnietyTrzeciRaz(), DEC);
        Serial.println("---------------------------");
    } 
}
#endif
CzujkaZblizeniowa::CzujkaZblizeniowa() : m_timeSig(0), m_timeHold(0), m_ruch(false), m_wykrytoRuch(false)
{
    m_prev = 1;
    m_val = 1;
}

void CzujkaZblizeniowa::ustaw(uint8_t value, unsigned long timeInt, unsigned int timeAfterInt)
{
#ifdef DEBUG    
    Serial.print("value=");
    Serial.print(value,DEC);
    Serial.print(" prev=");
    Serial.print(m_prev,DEC);
    Serial.print(" val=");
    Serial.println(m_val,DEC);
#endif    
    m_prev = m_val;
    m_val = (value == LOW); 

    if (m_val && !m_prev) {
        m_timeSig = timeAfterInt;
        m_timeHold = 0;
        m_ruch = false;
        m_wykrytoRuch = false;
    }
    else if (m_val && m_prev) {
        m_timeHold = timeAfterInt - m_timeSig;
        m_ruch = true;
    }
    else if (!m_val && m_prev) {
        m_timeHold = 0;
        m_timeSig = 0;
        m_ruch = false;
        m_wykrytoRuch = false;
    }

    if (m_ruch && m_timeHold > czasZblizenia && !m_wykrytoRuch) {
        m_wykrytoRuch = true;
    } else if (m_timeHold > czasZblizenia && m_wykrytoRuch) {
        m_wykrytoRuch = false;
    }

    if (m_ruch && m_timeHold > czasDlugiegoZblizenia && !m_wykrytoDlugiRuch) {
        m_wykrytoRuch = true;
    } else if (m_timeHold > czasDlugiegoZblizenia && m_wykrytoDlugiRuch) {
        m_wykrytoDlugiRuch = false;
    }

    //print();
}
#ifdef DEBUG
void CzujkaZblizeniowa::print() const
{
    static unsigned long mask  = 0;
    unsigned long mask2  = 0;

    mask2 |= 0x01 & m_val;
    mask2 |= (0x01 & m_prev) << 1;
    mask2 |= (0xFF & m_timeSig) << 2;
    mask2 |= (0xFF & m_timeHold) << 10;

    if (mask2 != mask) {
        mask = mask2;
        Serial.println("------- Czujka zblizeniowa ------");
        Serial.print("val = ");
        Serial.println(m_val, DEC);
        Serial.print("prev = ");
        Serial.println(m_prev, DEC);
        Serial.print("ruch = ");
        Serial.println(m_ruch, DEC);
        Serial.print("wykrytoRuch = ");
        Serial.println(m_wykrytoRuch);
        Serial.print("timeSig = ");
        Serial.println(m_timeSig, DEC);
        Serial.print("timeHold = ");
        Serial.println(m_timeHold, DEC);
        Serial.println("****");
        Serial.print("czyRuch = ");
        Serial.println(czyRuch(), DEC);
        Serial.println("---------------------------");
    } 
}
#endif

void CzujkaZblizeniowa::czysc() 
{
    m_timeSig = 0;
    m_timeHold = 0;
    m_ruch = false;
    m_wykrytoRuch = false;
    m_wykrytoDlugiRuch = false;
}    




CzujkaRuchu::CzujkaRuchu() : m_timelastMove(0), m_prevtimelastMove(0), m_ruch(false)
{
    m_prev = 0;
    m_val = 0;
}

void CzujkaRuchu::ustaw(uint8_t val, unsigned long timeInt, unsigned int timeAfterInt)
{
    m_prev = m_val;
    m_val = (val == HIGH); 

    if (!m_ruch && m_val && !m_prev) {
        m_prevtimelastMove = m_timelastMove;
        m_timelastMove = timeAfterInt + timeAfterInt;
        m_ruch = true;
    } else if (m_ruch) {
        m_ruch = false;
    }
    //print();
}
#ifdef DEBUG
void CzujkaRuchu::print() const 
{
    static unsigned long mask  = 0;
    unsigned long mask2  = 0;

    mask2 |= 0x01 & m_val;
    mask2 |= (0x01 & m_prev) << 1;
    mask2 |= (0x01 & m_ruch) << 2;

    if (mask2 != mask) {
        mask = mask2;
        Serial.println("------- Czujka ruchu ------");
        Serial.print("val = ");
        Serial.println(m_val, DEC);
        Serial.print("prev = ");
        Serial.println(m_prev, DEC);
        Serial.print("ruch = " );
        Serial.println(m_ruch, DEC);
        Serial.print("timelastMove = ");
        Serial.println(m_timelastMove, DEC);
        Serial.println("****");
        Serial.print("czyRuch = ");
        Serial.println(czyRuch(), DEC);
        Serial.print("czasBezRuchu = ");
        Serial.println(czasBezRuchu(), DEC);
        Serial.println("---------------------------");
    } 
}
#endif

void CzujkaRuchu::czysc() 
{
    //m_timelastMove = 0;   //nie wiem czy chce to czyscic po przerwaniu
    //m_prevtimelastMove = 0; // jak wyzej
    m_ruch = 0;
}

Drzwi::Drzwi() : ValueBase(), m_otwarte(false), m_timeOpen(0), m_timeClose(0), m_otworzone(false)
{
    m_prev = 1;
    m_val = 1;
}


void Drzwi::ustaw(uint8_t val, unsigned long timeInt, unsigned int timeAfterInt)
{
    m_prev = m_val;
    m_val = (val == HIGH); //otwarte

    if (m_val && !m_prev) {
        m_otwarte = true;
        m_otworzone = true;
        m_timeOpen = timeInt + timeAfterInt;       
    } else if (!m_val && m_prev) {
        m_otwarte = false;
        m_timeClose = timeInt + timeAfterInt;
    } else if (m_val && m_prev && m_otworzone) {
        m_otworzone = false;
    }

}

void Drzwi::czysc() 
{
    //nie wiem czy jest cos do czyszczeni
}

#ifdef DEBUG
void Drzwi::print() const 
{
    static unsigned long mask  = 0;
    unsigned long mask2  = 0;

    mask2 |= 0x01 & m_val;
    mask2 |= (0x01 & m_prev) << 1;
    mask2 |= (0x01 & m_otwarte) << 2;

    if (mask2 != mask) {
        mask = mask2;
        Serial.println("---------- Drzwi ---------");
        Serial.print("val = ");
        Serial.println(m_val, DEC);
        Serial.print("prev = ");
        Serial.println(m_prev, DEC);
        Serial.print("otwarte = " );
        Serial.println(m_otwarte, DEC);
        Serial.print("timeOpen = ");
        Serial.println(m_timeOpen, DEC);
        Serial.print("timeClose = ");
        Serial.println(m_timeClose, DEC);
        Serial.println("****");
        Serial.print("czyOtwarte = ");
        Serial.println(czyOtwarte(), DEC);
        Serial.print("czyZamkniete = ");
        Serial.println(czyZamkniete(), DEC);
        Serial.print("czasOtwarcia = ");
        Serial.println(czasOtwarcia(), DEC);
        Serial.print("czasZamkniecia = ");
        Serial.println(czasZamkniecia(), DEC);
        Serial.println("---------------------------");
    } 
}
#endif

PoraDnia::PoraDnia() : m_noc(false), m_wieczor(false), m_prevnoc(false),  m_prevwieczor(false)
{

}

PoraDnia::Pora PoraDnia::getPoraDnia() const
{
    if (m_noc && m_prevnoc)
        return NOC;
    else if (m_wieczor && m_prevwieczor)
        return WIECZOR;
    else
        return DZIEN;
}

void PoraDnia::ustaw(uint8_t valN, uint8_t valW)
{
    m_prevnoc = m_noc;
    m_noc = valN == HIGH;

    m_prevwieczor = m_wieczor;
    m_wieczor = valW == HIGH;
}

#ifdef DEBUG
void PoraDnia::print() const
{
    static unsigned long mask  = 0;
    unsigned long mask2  = 0;

    mask2 |= 0x01 & m_noc;
    mask2 |= (0x01 & m_prevnoc) << 1;
    mask2 |= (0x01 & m_wieczor) << 2;
    mask2 |= (0x01 & m_prevwieczor) << 3;
    if (mask2 != mask) {
        mask = mask2;
        Serial.println("---------- Pora dnia ---------");
        Serial.print("noc = ");
        Serial.println(m_noc, DEC);
        Serial.print("prevnoc = ");
        Serial.println(m_prevnoc, DEC);
        Serial.print("wieczor = ");
        Serial.println(m_wieczor, DEC);
        Serial.print("prevwieczor = ");
        Serial.println(m_prevwieczor, DEC);
        Serial.println("-------");

        Serial.print("czyWieczor() = ");
        Serial.println(czyWieczor());
        Serial.print("czyNoc() = ");
        Serial.println(czyNoc());
        Serial.print("czyDzien() = ");
        Serial.println(czyDzien());
    }
}
#endif