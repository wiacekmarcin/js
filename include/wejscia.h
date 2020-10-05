#ifndef __WEJSCIA_H__
#define __WEJSCIA_H__

#include "value.h"
#include <PCF8574.h>
class Wejscia {
public:
    Wejscia();

    void init();

    void get();

    const Value & getWlacznik() const { return w[KLAWISZ]; }
    const Value & getLustro() const { return w[CZ_R_LUSTRO]; }
    const Value & getCzRuchu() const { return w[CZ_R_WC]; }
    const Value & getDrzwi() const { return w[DRZWI]; }
    const Value & getWieczor() const { return w[WIECZOR]; }
    const Value & getNoc() const { return w[NOC]; }
    //const Value & getPoziomWody() const { return w[CZ_POW_WODY]; }
    
    bool isChange() const;

    void print();
    
    void print(PCF8574::DigitalInput inp);

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

    Value w[lenWej];
    uint8_t in[lenWej];

//p0 czujnik zblizeniowy 0 - blisko 1 - daleko
//p1 czujnik ruchu 0 -brak ruchu 1 - ruch
//p2 drzwi 0 - zamkniete 1 - otwarte
//p3 klawisz 0 - nacisniety 1 - w normalnej pozycji

//p4 noc
//p5 wieczor
//p6 czujnik poziomu wody
};

#endif // !__WEJSCIA_H__
