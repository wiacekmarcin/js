#ifndef __WEJSCIA_H__
#define __WEJSCIA_H__

#include <PCF8574.h>

#include "in.h"

class Wejscia {
public:
    Wejscia(void (*fun)());

    void init();

    void get(unsigned long timeInt, unsigned int timeAfterInt);
    void czysc() { wl.czysc(); }
    const Wlacznik & getWlacznik() const { return wl; }
    const CzujkaZblizeniowa & getCzujkaZbl() const { return czBl; }
    const CzujkaRuchu & getCzujkaRuchu() const { return czR; }
    const Drzwi & getDrzwi() const { return drz; }
    const PoraDnia & getPoraDnia() const { return prd; }
   

    void print();

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

    class Wlacznik wl;
    class CzujkaZblizeniowa czBl;
    class CzujkaRuchu czR;
    class Drzwi drz;
    class PoraDnia prd;
};







#endif // !__WEJSCIA_H__
