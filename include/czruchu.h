#ifndef __CZRUCHU_H__
#define __CZRUCHU_H__

#include "wejscia.h"
#include "wyjscia.h"


class CzRuchu {
public:

    CzRuchu(Wejscia & wej , Wyjscia & wyj);

    void set();
    
private:
    Wejscia & wej;
    Wyjscia & wyj;
};


#endif // __CZRUCHU_H__