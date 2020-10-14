#include "in.h"

Wlacznik::Wlacznik() : ValueBase(), m_prev(false), m_cntPush(0)
{
    unsigned long m_timeInt;
    unsigned int m_timeAfterInt;
}
    
void Wlacznik::clearState() 
{
    m_cntPush = 0;
    m_timePush = 0;
    m_timeHold = 0;
}    
void Wlacznik::set(uint8_t value, unsigned long timeInt, unsigned int timeAfterInt)
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

CzujkaZblizeniowa::CzujkaZblizeniowa() : m_timePush(0), m_timeHold(0), m_ruch(false)
{

}

void CzujkaZblizeniowa::set(uint8_t value, unsigned long timeInt, unsigned int timeAfterInt)
{
    m_prev = m_val;
    m_val = (value == HIGH); 

    if (m_val && !m_prev) {
        m_timePush = timeAfterInt;
        m_timeHold = 0;
        m_ruch = false;
    }
    else if (m_val && !m_prev) {
        m_timeHold = timeAfterInt - m_timeHold;
    }
    else if (!m_val && m_prev) {
        m_timeHold = 0;
        m_timePush = 0;
        m_ruch = false;
    }

    if (m_timeHold > 500 && !m_ruch) {
        //czy wykryto ruch
    }
}