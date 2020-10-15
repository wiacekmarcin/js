#include "in.h"

Wlacznik::Wlacznik() : ValueBase(), m_cntPush(0), m_timeInt(0), m_timePush(0), m_timeHold(0)
{
    
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
    m_val = (value == HIGH); 

    if (m_val && !m_prev) {
        m_timeSig = timeAfterInt;
        m_timeHold = 0;
        m_ruch = false;
        m_wykrytoRuch = false;
    }
    else if (m_val && m_prev) {
        m_timeHold = timeAfterInt - m_timeSig;
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




CzujkaRuchu::CzujkaRuchu() : m_timelastMove(0), m_ruch(false)
{
    
}

void CzujkaRuchu::ustaw(uint8_t val, unsigned long timeInt, unsigned int timeAfterInt)
{
    m_prev = m_val;
    m_val = (val == HIGH); 

    if (!m_ruch && m_val && !m_prev) {
        m_timelastMove = timeAfterInt + timeAfterInt;
        m_ruch = true;
    } else if (m_ruch) {
        m_ruch = false;
    }
}

Drzwi::Drzwi() : m_otwarte(false)
{

}


void Drzwi::ustaw(uint8_t val, unsigned long timeInt, unsigned int timeAfterInt)
{
    m_prev = m_val;
    m_val = (val == LOW); 

    if (m_val && !m_prev) {
        
    }
}