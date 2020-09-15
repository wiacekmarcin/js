#ifndef __LUSTRO_H__
#define __LUSTRO_H__

#include "Arduino.h"
#include "wyjscia.h"
#include "wejscia.h"
#include "value.h"

class Lustro {
public:
    
    Lustro(Wejscia & we, Wyjscia & wy);

    void set();

    void zapal(unsigned long mls = 5L*60L*1000L);
    void off();

private:
    bool prevczL;
    bool prevDrzwiOtw;
    unsigned long timeFirstCzZb; 
    static constexpr unsigned long OFF_DRZWIOTWARTE = 1L*60L*1000L;
    static constexpr unsigned long OFF_DRZWIZAMKNIETE = 5L*60L*1000L;
    Wejscia & wej;
    Wyjscia & wyj;
    
};
#endif // !__LUSTRO_H__