#include "in.h"
#include "debug.h"

#if 0
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

void Wlacznik::ustaw(uint8_t value, unsigned long timeInt, unsigned long timeAfterInt)
{
    m_prev = m_val;
    m_val = (value == LOW); //klawisz nacisniety
#ifdef MYINTERUPTS 
    if (m_timeInt != timeInt || (timeAfterInt - m_timePush) > SEC(1)) { //inne przerwanie lub czas powyzej 1s
        m_timeInt = timeInt;
        clearState();
    }
#else
    if (timeInt - m_timeInt > SEC(1)) { // czas powyzej 1s
        m_timeInt = timeInt;
        clearState();
    }    
#endif    
    if (m_val && !m_prev) {
        ++m_cntPush;
        m_timePush = timeAfterInt;
        m_timeHold = 0;
    }

    if (m_val && m_prev ) { //nacisniety klawisz i przytrzymany przez 
        m_timeHold = timeAfterInt - m_timePush;
    }
    print();
}

void Wlacznik::print() const
{
#ifdef DEBUG
    print_wlacznik(this);
#endif // DEBUG    
}    

CzujkaZblizeniowa::CzujkaZblizeniowa() : m_timeSig(0), m_timeHold(0), m_ruch(false), m_wykrytoRuch(false)
{
    m_prev = 1;
    m_val = 1;
}

void CzujkaZblizeniowa::ustaw(uint8_t value, unsigned long timeInt, unsigned long timeAfterInt)
{
#ifdef DEBUG    
    //Serial.print("value=");
    //Serial.print(value,DEC);
    //Serial.print(" prev=");
    //Serial.print(m_prev,DEC);
    //Serial.print(" val=");
    //Serial.println(m_val,DEC);
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

void CzujkaZblizeniowa::print() const
{
#ifdef DEBUG
    print_czujkazblizeniowa(this);
#endif    
}    

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

void CzujkaRuchu::ustaw(uint8_t val, unsigned long timeInt, unsigned long timeAfterInt)
{
    m_prev = m_val;
    m_val = (val == HIGH); 

    if (!m_ruch && m_val && !m_prev) {
        m_ruch = true;
        return;
        
    } else if (m_prev) { /// m_val || (!m_val && m_prev)
        m_prevtimelastMove = m_timelastMove;
        m_timelastMove = timeInt;// + timeAfterInt;
    }
    
    if (m_ruch) {
        m_ruch = false;
    }
    //print();
}
void CzujkaRuchu::print() const 
{
#ifdef DEBUG    
    print_czujkaruchu(this);
#endif
}


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
        m_timeOpen = timeInt ; /* + timeAfterInt;  */
    } else if (!m_val && m_prev) {
        m_otwarte = false;
        m_timeClose = timeInt; /* + timeAfterInt; */
    } else if (m_val && m_prev && m_otworzone) {
        m_otworzone = false;
    }

}

void Drzwi::czysc() 
{
    //nie wiem czy jest cos do czyszczeni
}


void Drzwi::print() const 
{
#ifdef DEBUG
    print_drzwi(this);
#endif // DEBUG    
}

PoraDnia::PoraDnia() : m_noc(false), m_wieczor(false), m_prevnoc(false),  m_prevwieczor(false),
       m_taryf2(false), m_prevtaryf2(false), m_zas_awar(false), m_prevzas_awar(false)
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

void PoraDnia::ustaw(uint8_t valN, uint8_t valW, uint8_t valZ, uint8_t valT)
{
    m_prevnoc = m_noc;
    m_noc = valN == LOW;

    m_prevwieczor = m_wieczor;
    m_wieczor = valW == LOW;

    m_prevzas_awar = m_zas_awar;
    m_zas_awar = valZ == LOW;

    m_prevtaryf2 = m_taryf2;
    m_taryf2 = valT == LOW;
}


void PoraDnia::print() const
{
#ifdef DEBUG
    print_poradnia(this);
#endif
}

#endif