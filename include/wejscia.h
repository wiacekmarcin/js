#ifndef __WEJSCIA_H__
#define __WEJSCIA_H__

#include "value.h"
#include <PCF8574.h>

#include "in.h"

class Wejscia {
public:
    Wejscia(void (*fun)());

    void init();

    void get(unsigned long timeInt, unsigned int timeAfterInt);
    void czysc() { wl.czysc(); }
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
    class CzujkaZblizeniowa czb;
};







#endif // !__WEJSCIA_H__
