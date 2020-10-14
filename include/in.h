#ifndef     _IN_H_
#define     _IN_H_

#include "value.h"
#include <PCF8574.h>
#include "util.h"

/**
 * Podstawowa klasa dla wlacznika, czujnika ruchu i czujnia zblizeniowego
 * funkcje set - ustawia wartosc odczytana z pcf8572 i tutaj trzeba zrobic
 * rozpoznanie czy LOW jest true czy HIGH jest true
 * funkcja get pobiera wartocsc true/false
 * funkcje clear - czysci dodatkowe parametry
 * funkcja print - drukuje do Serial zawartosc klasy
 * m_val - biezaca wartosc
 * m_prev - poprzednia wartosc m_val/m_prev sluza do jednoznacznego
 * ustalenia zmiany zmiennej
 */
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
    bool m_prev;   
};

/**
 * Klasa wlacznik
 * funkcja nacisniety zwraca true jezeli klawisz zostal wlasnie wcisniety - trwa to dokladnie 1 cykl
 * funkcja wcisniety zwraca true jezeli klawisz jest przytrzymany conajmniej przez 1 cykl
 * funkcja czasWcisniecia zwraca czas wcisniecia (maks okolo 1 minuty - zanim zestartuje sie cykl)
 * funkcja nacisnietyDrugiRaz zwraca true jezeli klawisz zostal dwukrotnie wcisniety w ciagu 10s 
 * funkcja nacisnietyTrzeciRaz zwraca true jezeli klawisz zostal trzykrotnie wcisniety w ciagu 10s 
 */
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
    unsigned long m_timeInt;
    unsigned long m_timePush;
    unsigned int m_timeHold;
    static constexpr unsigned long maxTimeMultiClick = SEC(10); //maksymalny czas podczas ktorego mozna 1,2,3 razy nacisnac klawisz
};

class CzujkaZblizeniowa : public ValueBase {
public:
    CzujkaZblizeniowa();
    void set(uint8_t val, unsigned long timeInt, unsigned int timeAfterInt);
    bool czyRuch() const { return m_ruch; }
private:
    unsigned long m_timePush;
    unsigned int m_timeHold;
    bool m_ruch;
    bool m_wykrytoRuch;
};


#endif  //_IN_H_

