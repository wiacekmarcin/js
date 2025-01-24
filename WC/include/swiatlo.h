#ifndef __LAMPA_H__
#define __LAMPA_H__

#include "wyjscia.h"
#include "wejscia.h"

#if 0
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
    void setDzien(); 
    void setWieczor(); 
    void setNoc(); 
    bool setNormal(bool r);
    bool setSpecial(bool p);
    void setSwiatlo(bool p);


private:
    Wejscia & wej;
    Wyjscia & wyj;

    bool trybNormalny; //w jakim trybie swieci lustro
};

#endif 
#endif //! ___LAMPA_H__