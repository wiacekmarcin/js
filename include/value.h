#ifndef __VALUE_H__
#define __VALUE_H__

#include <Arduino.h>

class Value {
public:
    Value(bool high = true);
    Value(const Value & val);

    void setLowAsTrue() { m_conv = false; }

    bool val() const { return m_val; }

    uint8_t bin() const { return m_conv ? lo(m_val) : ho(m_val) ; }
    
    void set(bool newVal);

    bool isChange()const { return m_prev != m_val; }

    Value& operator=(const Value & rval);
    Value& operator=(uint8_t ival);

    unsigned long time() const { return m_timeChange[m_val ? 1 : 0]; }
    unsigned long prevtime() const { return m_timeChange[m_val ? 0 : 1]; }

    bool operator() () const { return m_val; }
    operator bool () const { return m_val; }

    inline static uint8_t lo(bool value) { return value ? LOW : HIGH; }
    inline static uint8_t ho(bool value) { return value ? HIGH : LOW; }

    inline static bool li(uint8_t value) { return value == LOW; }
    inline static bool hi(uint8_t value) { return value == HIGH; }
private:
    bool m_conv;
    bool m_val;
    bool m_prev;
    unsigned long m_timeChange[2];    
};

#endif
