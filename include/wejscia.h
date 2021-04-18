#ifndef __WEJSCIA_H__
#define __WEJSCIA_H__


#include <Adafruit_MCP23017.h>
#include "in.h"
#define DEBUG
class Wejscia {
public:
    Wejscia(Adafruit_MCP23017 & wyjscia);

    void init();

    void get(unsigned long timeInt, unsigned int timeAfterInt);
    void czysc() { wl.czysc(); }
    const Wlacznik & getWlacznik() const { return wl; }
    const CzujkaZblizeniowa & getCzujkaZbl() const { return czBl; }
    const CzujkaRuchu & getCzujkaRuchu() const { return czR; }
    const Drzwi & getDrzwi() const { return drz; }
    const PoraDnia & getPoraDnia() const { return prd; }
   

    void print();

    void get();
private:
    
    Adafruit_MCP23017 & wejscia;

    static constexpr uint8_t CZ_R_WC = 0;//jasnozielony
    static constexpr uint8_t CZ_R_LUSTRO = 1;//jansobrazowy
    static constexpr uint8_t DRZWI = 2; //szary
    static constexpr uint8_t KLAWISZ = 3; //pomaranczowy
    static constexpr uint8_t Z_AWAR = 4; //fioletowy
    static constexpr uint8_t TARYF2 = 5; //brazowy
    static constexpr uint8_t WIECZOR = 6; //zolty
    static constexpr uint8_t NOC = 7; //bialy
        
    static constexpr uint8_t lenWej = 8;

    class Wlacznik wl;
    class CzujkaZblizeniowa czBl;
    class CzujkaRuchu czR;
    class Drzwi drz;
    class PoraDnia prd;
};







#endif // !__WEJSCIA_H__
