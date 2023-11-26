#ifndef __WEJSCIA_H__
#define __WEJSCIA_H__

#if 0
#include <Adafruit_MCP23X17.h>
#include "in.h"
//#define DEBUG

#define INTERPIN 7


class LiquidCrystal_I2C;
class Wejscia {
public:
    Wejscia(Adafruit_MCP23X17 & wyjscia);

    void init(void(*fun)());

    void get(unsigned long timeInt, unsigned int timeAfterInt);
    void czysc() { wl.czysc(); }
    const Wlacznik & getWlacznik() const { return wl; }
    const CzujkaZblizeniowa & getCzujkaZbl() const { return czBl; }
    const CzujkaRuchu & getCzujkaRuchu() const { return czR; }
    const Drzwi & getDrzwi() const { return drz; }
    const PoraDnia & getPoraDnia() const { return prd; }
    const bool czyZasilAwar() const { return prd.czyZasAwar(); }
   
    void print();



private:
    
    Adafruit_MCP23X17 & wejscia;


        
    static constexpr uint8_t lenWej = 8;

    class Wlacznik wl;
    class CzujkaZblizeniowa czBl;
    class CzujkaRuchu czR;
    class Drzwi drz;
    class PoraDnia prd;

};


#endif




#endif // !__WEJSCIA_H__
