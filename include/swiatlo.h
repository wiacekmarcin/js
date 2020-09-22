#ifndef __LAMPA_H__
#define __LAMPA_H__

#include "wyjscia.h"
#include "wejscia.h"

class Swiatlo {
public:

    Swiatlo(Wejscia & we, Wyjscia & wy);
    
    bool set(bool p);
    
    /* Lampa */
    void zapalSwiatlo(unsigned int s);
    void zgasSwiatlo();

    /* Lsustro */
    void zapalLustro(int mls = 5*60);
    void zapalLustroJakoSwiatlo(int mls = 2*60);
    void zgasLustro();
protected:
    
    bool setNormal(bool r);
    bool setSpecial(bool p);
    void setSwiatlo(bool p);


private:
    Wejscia & wej;
    Wyjscia & wyj;

    bool trybNormalny; //w jakim trybie swieci lustro
};

#endif //! ___LAMPA_H__