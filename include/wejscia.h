#ifndef __WEJSCIA_H__
#define __WEJSCIA_H__

#include "value.h"
#include <PCF8574.h>

class ValueBase {
public:
    ValueBase() : m_val(false), m_prev(false)
    {}
    void set(uint8_t val, unsigned long timeInt, unsigned int timeAfterInt) {}
    bool get() const { return m_val; }
    void clear() {}
    void print() const;
protected:
    bool m_val;    
    bool m_prev;
};

class Wlacznik : public ValueBase {

public:
    Wlacznik();
    void set(uint8_t val, unsigned long timeInt, unsigned int timeAfterInt);

    bool nacisniety() const { return m_val && m_val != m_prev && m_cntPush == 1; }
    bool wcisniety() const  { return m_val && m_val == m_prev; }
    unsigned int czasWcisniecia() const { return m_timeHold; }
    bool nacisnietyDrugiRaz() const { return m_val && m_val != m_prev && m_cntPush == 2; }
    bool nacisnietyTrzeciRaz() const { return m_val && m_val != m_prev && m_cntPush == 3; }

    void print() const;

    void clear() { clearState(); }
protected:
    void clearState();
private:
    
    unsigned int m_cntPush;
    unsigned long m_timeInt;
    unsigned long m_timePush;
    unsigned int m_timeHold;
};

class CzujnikLustro : public ValueBase {
public:    
    CzujnikLustro();
    bool isRuch() const { return m_zblizenie; }
    void set(uint8_t val, unsigned long timeInt, unsigned int timeAfterInt);
private:
    bool m_zblizenie;
};

class Wejscia {
public:
    Wejscia(void (*fun)());

    void init();

    void get(unsigned long timeInt, unsigned int timeAfterInt);
    void clear() { wl.clear(); }
    const Wlacznik & getWlacznik() const { return wl; }


   

    void print();

    void printBin(uint8_t inp);

private:
    
    PCF8574 wejscia;

    static constexpr uint8_t CZ_R_LUSTRO = 0;
    static constexpr uint8_t CZ_R_WC = 1;
    static constexpr uint8_t DRZWI = 2;
    static constexpr uint8_t KLAWISZ = 3;
    static constexpr uint8_t WIECZOR =4;
    static constexpr uint8_t NOC = 5;
    
    //static constexpr uint8_t CZ_POZ_WODY = 6;
    static constexpr uint8_t lenWej = 6; //7

    //Value w[lenWej];
    //ValueBase w[lenWej];
    uint8_t in[lenWej];

    class Wlacznik wl;
};







#endif // !__WEJSCIA_H__
