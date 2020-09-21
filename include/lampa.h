#ifndef __LAMPA_H__
#define __LAMPA_H__

#include "wyjscia.h"
#include "wejscia.h"
class Lampa {
public:

    Lampa(Wejscia & we, Wyjscia & wy);
    void set(bool p);
    void zapalSwiatlo(unsigned int s);
    void off();


private:
    Wejscia & wej;
    Wyjscia & wyj;
};

#endif //! ___LAMPA_H__
