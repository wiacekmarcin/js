#ifndef __LAMPA_H__
#define __LAMPA_H__

#include "wyjscia.h"
#include "wejscia.h"

#define DEBUG
class Swiatlo {
public:

    Swiatlo(Wejscia & we, Wyjscia & wy);
    
    bool set(unsigned long mls);
    
    /* Lampa */
    void zapalSwiatlo(unsigned int s);
    void przedluzSwiatlo(unsigned int s);
    void zgasSwiatlo();

    /* Lsustro */
    void zapalLustro(int mls = 5*60);
    void przedluzLustro(int mls = 5*60);
    void zgasLustro();
protected:
    void setDzien(); 
    void setWieczor(); 
    void setNoc(); 



private:
    Wejscia & wej;
    Wyjscia & wyj;

    bool trybNormalny; //w jakim trybie swieci lustro
};

#endif //! ___LAMPA_H__