#ifndef     _IN_H_
#define     _IN_H_

#include <PCF8574.h>
#include "util.h"

//#define DEBUG
/**
 * Podstawowa klasa dla wlacznika, czujnika ruchu i czujnia zblizeniowego
 * funkcje ustaw - ustawia wartosc odczytana z pcf8572 i tutaj trzeba zrobic
 * rozpoznanie czy LOW jest true czy HIGH jest true
 * funkcja get pobiera wartocsc true/false
 * funkcje czysc - czysci dodatkowe parametry
 * funkcja print - drukuje do Serial zawartosc klasy
 * m_val - biezaca wartosc
 * m_prev - poprzednia wartosc m_val/m_prev sluza do jednoznacznego
 * ustalenia zmiany zmiennej
 */
class ValueBase {
public:
    ValueBase() : m_val(false), m_prev(false) 
    {}
    void ustaw(uint8_t val, unsigned long timeInt, unsigned int timeAfterInt) {}
   
    void czysc() {}
#ifdef DEBUG    
    void print() const;
#endif

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
 * 
 */
class Wlacznik : public ValueBase {
public:
    Wlacznik();
    void ustaw(uint8_t val, unsigned long timeInt, unsigned int timeAfterInt);

    bool nacisniety() const { return m_val && m_val != m_prev && m_cntPush == 1; }
    bool wcisniety() const  { return m_val && m_val == m_prev; }
    unsigned int czasWcisniecia() const { return m_timeHold; }
    bool nacisnietyDrugiRaz() const { return m_val && m_val != m_prev && m_cntPush == 2; }
    bool nacisnietyTrzeciRaz() const { return m_val && m_val != m_prev && m_cntPush == 3; }

#ifdef DEBUG
    void print() const;
#endif

    void czysc() { clearState(); }
protected:
    void clearState();
private:
    unsigned int m_cntPush;
    unsigned long m_timeInt;
    unsigned long m_timePush;
    unsigned int m_timeHold;
    static constexpr unsigned long maxTimeMultiClick = SEC(10); //maksymalny czas podczas ktorego mozna 1,2,3 razy nacisnac klawisz
};

/**
 * Klasa czujnika zbliżeniowego
 * Jeżeli czujnik wykryje bliską obecność przez około 0.5s to 
 * podaje raz sygnał o zmianie
 * funkcja czyRuch - zwraca ruch przez jeden cykl jezeli przez wykryto ruch dlizej niz czasZblizenia
 * funkcja czyDlugiRuch - zwraca ruch przez jeden cykl jezeli przez wykryto ruch dlizej niz czasDlugiegoZblizenia
 * 
 */
class CzujkaZblizeniowa : public ValueBase {
public:
    CzujkaZblizeniowa();
    void ustaw(uint8_t val, unsigned long timeInt, unsigned int timeAfterInt);
    bool czyRuch() const { return m_wykrytoRuch; }
    bool czyDlugiRuch() const { return m_wykrytoDlugiRuch; }

#ifdef DEBUG
    void print() const;
#endif

    void czysc() ;

private:
    unsigned long m_timeSig;
    unsigned int m_timeHold;
    bool m_ruch;
    bool m_wykrytoRuch;
    bool m_wykrytoDlugiRuch;
    static constexpr unsigned long czasZblizenia = 500; //ms
    static constexpr unsigned long czasDlugiegoZblizenia = 5000; //ms
};

/**
 * Klasa czujnika ruchu
 * Klasa odpowiedzialna jest za wykrycie ruchu
 * Podaje sygnał tylko raz jak zmieni się z sygnał z LOW na HIGH
 * m_timeLastMove - znacznik czasowy kiedy wystąpił ruch - informacja jak dawno nie było ruchu
 * m_prevtimelastMove - zapasowa informacja o wystąpieniu ruchu - (poprzedni parametr jest ustawiany
 * na nowo podczas ruchu, przydatne aby okreslic jak dawno wystapil poprzedni ruch)
 **/
class CzujkaRuchu : public ValueBase {
public:
    CzujkaRuchu();

    void ustaw(uint8_t val, unsigned long timeInt, unsigned int timeAfterInt);
    bool czyRuch() const { return m_ruch; }
    unsigned long czasBezRuchu() const { return millis() - m_timelastMove; }
    unsigned long poprzCzasBezRuchu() const { return millis() - m_prevtimelastMove; }

#ifdef DEBUG
    void print() const;
#endif

    void czysc() ;
private:
    unsigned long m_timelastMove;
    unsigned long m_prevtimelastMove;
    bool m_ruch;
};

class Drzwi : public ValueBase {
public:
    Drzwi();

    void ustaw(uint8_t val, unsigned long timeInt, unsigned int timeAfterInt);
    bool zostalyOtwarte() const { return m_otworzone; };
    bool czyOtwarte() const { return m_otwarte; }
    bool czyZamkniete() const { return !m_otwarte; }
    unsigned long czasOtwarcia() const { return m_otwarte ? millis() - m_timeOpen : 0; }
    unsigned long czasZamkniecia() const { return m_otwarte ? 0 : millis() - m_timeClose; }

#ifdef DEBUG
    void print() const;
#endif

    void czysc() ;

private:
    bool m_otwarte;
    unsigned long m_timeOpen;
    unsigned long m_timeClose;
    bool m_otworzone;
};

class PoraDnia  {
public:
    typedef enum epora {
        DZIEN,
        WIECZOR,
        NOC
    } Pora;

    PoraDnia();
    void ustaw(uint8_t valN, uint8_t valW);
    bool czyWieczor() const { return m_wieczor && m_prevwieczor; }
    bool czyNoc() const { return m_noc & m_prevwieczor; }
    bool czyDzien() const { return !((m_wieczor && m_prevwieczor) || (m_noc & m_prevwieczor)); }

    Pora getPoraDnia() const;
    
#ifdef DEBUG
    void print() const;
#endif

    void czysc() { }
private:
    bool m_noc;
    bool m_wieczor;
    bool m_prevnoc;
    bool m_prevwieczor;
};

#endif  //_IN_H_

