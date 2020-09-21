#ifndef __LUSTRO_H__
#define __LUSTRO_H__

#include "Arduino.h"
#include "wyjscia.h"
#include "wejscia.h"
#include "value.h"

class Lustro {
public:
    
    Lustro(Wejscia & we, Wyjscia & wy);

    bool set(bool p);

    void zapal(int mls = 5*60);
    void zapalJakoGlowne(int mls = 2*60);
    void off();
protected:
    bool setNormal(bool r);
    bool setSpecial(bool p);
private:

    static constexpr unsigned long OFF_DRZWIOTWARTE = 60;
    static constexpr unsigned long OFF_DRZWIZAMKNIETE = 5*60;
    Wejscia & wej;
    Wyjscia & wyj;
    bool trybNormalny;  
    
};
#endif // !__LUSTRO_H__
