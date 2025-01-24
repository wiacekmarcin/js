#include "Arduino.h"
#include "wyjscia.h"
#include "wejscia.h"
#include "value.h"

class Lustro {
public:
    
    Lustro(Wejscia & we, Wyjscia & wy);

    void set();

    void zapal(unsigned long mls = 5*60*1000);
    void off();

private:
    bool prevczL;
    bool prevDrzwiOtw;
    unsigned long timeFirstCzZb; 
    static constexpr unsigned long OFF_DRZWIOTWARTE = 1*60*1000;
    static constexpr unsigned long OFF_DRZWIZAMKNIETE = 5*60*1000;
    Wyjscia & wyj;
    Wejscia & wej;
};
