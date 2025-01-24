#include "wyjscia.h"

class Lampa {
public:

    Lampa(Wejscia & we, Wyjscia & wy);
    void set();



private:
    Wyjscia & wyj;
    Wejscia & wej;
};
