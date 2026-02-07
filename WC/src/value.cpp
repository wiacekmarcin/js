#include "value.h"

#include <Arduino.h>

Value::Value(bool c) :
    m_conv(c), m_val(false), m_prev(false), m_timeChange{0L, 0L}
{
    
}

Value::Value(const Value & cval)
{
    m_val = cval.m_val;
    m_conv = cval.m_conv;
    m_prev = cval.m_prev;
    m_timeChange[0] = cval.m_timeChange[0];
    m_timeChange[1] = cval.m_timeChange[1];
}

Value & Value::operator=(const Value & oval) 
{
    m_val = oval.m_val;
    m_conv = oval.m_conv;
    m_prev = oval.m_prev;
    m_timeChange[0] = oval.m_timeChange[0];
    m_timeChange[1] = oval.m_timeChange[1];
    return *this;
}

Value& Value::operator=(uint8_t ival)
{
    //Serial.print("Value::operator= ival=");
    //Serial.print(ival, DEC);
    //Serial.print(" val = ");
    //Serial.print(m_conv ? hi(ival) : li(ival), DEC);
    //Serial.print(" mval = ");
    //Serial.println(m_val, DEC);
    bool bval = m_conv ? hi(ival) : li(ival);
    if (bval != m_val) {
        m_prev = m_val;
        m_val = bval;
        m_timeChange[m_val ? 1 : 0] = millis();
        //Serial.print("val=");
        //Serial.print(m_val, DEC);
        //Serial.print("  timeChanged[0]=");
        //Serial.print(m_timeChange[0], DEC);
        //Serial.print("  timeChanged[1]=");
        //Serial.println(m_timeChange[1], DEC);
    } else {
        m_prev = m_val; // przy pierwszym przypisaniu mmay m_val != m_prev, a przy kolejnym m_val == m_prev -
                        // mozemy dokladnie wykryc zmiane
    }
    return *this;
}