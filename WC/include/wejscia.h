#ifndef __WEJSCIA_H__
#define __WEJSCIA_H__


#include <Adafruit_MCP23X17.h>

class ValueBase {
public:
    ValueBase(bool revert) : m_revert(revert), m_val(false) 
    {}
    void set(uint8_t val) {
        m_change = val != m_val;
        if (m_change) {
            m_timeChange = millis(); 
        }
        m_val = (m_revert) ? !val : val; 
    }

    bool get() const { return m_val; }
    bool isChange() const { return m_change; }

    unsigned long lastChanged() const { return m_timeChange; }

protected:
    bool m_revert;
    bool m_val;
    bool m_change;
    unsigned long m_timeChange;
};

class Drzwi : public ValueBase {
    public:    
    
    Drzwi() : ValueBase(true) { }
    bool czyOtwarte() { return !get(); }
    bool czyZamkniete() { return get(); } 

};


class CzujnikRuchu : public ValueBase {
    public:    
    
    CzujnikRuchu() : ValueBase(false), m_timeMoveTrig(0)
    { }

    bool czyWykrytoRuch() const { return isChange() && get(); }

    void set(uint8_t val) {
        ValueBase::set(val);
        if (isChange() && val)
            m_timeMoveTrig = millis();
    }

    unsigned long lastMoveTime() const { return m_timeMoveTrig; }

protected:
    unsigned long m_timeMoveTrig;
};

class CzujnikZblizeniowy : public ValueBase {
    public:    
    
    CzujnikZblizeniowy() : ValueBase(false), m_timeNear(0)
    { }

    bool czyWykrytoRuch() const { return isChange() && get(); }

    void set(uint8_t val) {
        ValueBase::set(val);
        if (isChange() && val)
            m_timeNear = millis();
        else if (isChange() && !val)
            m_timeNear = 0;
    }

    unsigned long czasZblizenia() const { return m_timeNear; }

protected:
    unsigned long m_timeNear;
};


class Wlacznik : public ValueBase {

public:
    Wlacznik() : ValueBase(true), m_prev(0), m_cntPush(0), m_timeHold(0)
    {}

    void set(uint8_t val) { 
        m_prev = m_val;
        unsigned long prevChange = lastChanged();
        ValueBase::set(val);
        if (!isChange())
            return;
        unsigned long now = millis();
        unsigned long diff;
        
        if (now > prevChange) {
            diff = now - prevChange;
        } else {
            diff = 1500;
        }

        if (m_val) {
            if (diff < 1500) {
                ++m_cntPush;
            } else {
                m_cntPush = 0;
            }
            m_timeHold = 0;
        } else {
            m_timeHold = prevChange;
        }

    
    }

    bool nacisniety() const { return m_val && m_val != m_prev && m_cntPush == 1; }
    bool wcisniety() const  { return m_val && m_val == m_prev; }
    unsigned int czasWcisniecia() const { return m_timeHold; }
    bool nacisnietyDrugiRaz() const { return m_val && m_val != m_prev && m_cntPush == 2; }
    bool nacisnietyTrzeciRaz() const { return m_val && m_val != m_prev && m_cntPush == 3; }

    void clear() { clearState(); }
protected:
    void clearState();
private:
    bool m_prev;
    unsigned int m_cntPush;
    unsigned int m_timeHold;
};


class Wejscia 

{
public:
    Wejscia(Adafruit_MCP23X17 * _mcp) : 
        mcp(_mcp), 
        act_val(0), 
        prev_read(0L),
        b_noc(false),
        b_wieczor(false),
        b_zasilanie_awaryjne(false),
        bp_zasilanie_awaryjne(false)
    { }
    void init();

    bool read();

    bool set_input(uint8_t val);

/*
A7 - oswietlenie ?
b0 - zawor
b1 - lustro
b2 - swiatlo sufit
b3 - regal
b4 - noc
b5 - czujnik ruchu
b6 - opto czujnik ruchu
b7 - opto kontaktron
*/

    constexpr static uint8_t p_noc = 8+4;   
    constexpr static uint8_t p_wieczor = 6;
    constexpr static uint8_t p_2taryfa = 5;
    constexpr static uint8_t p_zasAwar = 4;
    constexpr static uint8_t p_klawisz = 3;
    constexpr static uint8_t p_drzwi = 2;

    constexpr static uint8_t p_ruch = 0;
    //constexpr  static uint8_t p_ruch2 = 8+5;
    constexpr static uint8_t p_zblizeniowy = 1;
    
    constexpr static uint16_t p_noc_mask =  1 << (8+4);  

    bool isNoc() { return b_noc; }
    bool isWieczor() { return b_wieczor; }
    bool isZasilanieAwaryjne() { return b_zasilanie_awaryjne; }
    bool changeZasilanieAwaryjne() { return b_zasilanie_awaryjne != bp_zasilanie_awaryjne; } 

private:
    Adafruit_MCP23X17 * mcp;
    uint8_t act_val;
    unsigned long prev_read;
    bool b_noc;
    bool b_wieczor;
    bool b_zasilanie_awaryjne;
    bool bp_zasilanie_awaryjne;

    Wlacznik klawisz;
    CzujnikZblizeniowy czLustro;
    CzujnikRuchu czRuch;
};






#if 0

#include "value.h"


class ValueBase {
public:
    ValueBase() : m_val(false) 
    {}
    void set(uint8_t val, unsigned long timeInt, unsigned int timeAfterInt) {}
    bool get() const { return m_val; }
    void clear() {}
    void print() const;
protected:
    bool m_val;
    unsigned long m_timeInt;
    unsigned int m_timeAfterInt;    
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
    bool m_prev;
    unsigned int m_cntPush;
    unsigned long m_timePush;
    unsigned int m_timeHold;
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

    Wlacznik wl;
};





#endif

#endif // !__WEJSCIA_H__
