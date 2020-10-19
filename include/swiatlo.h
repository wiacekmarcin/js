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

    unsigned long czasZapaleniaSwiatlo(bool noc, bool otwarte_drzwi) {
        return noc ? (otwarte_drzwi ? L_SEC(30) : L_MIN(2)) : (otwarte_drzwi ? L_MIN(1) : L_MIN(5));
    }

    unsigned long czasZapaleniaLustro(bool noc, bool otwarte_drzwi) {
        return noc ? (otwarte_drzwi ? L_SEC(20) : L_MIN(1)) : (otwarte_drzwi ? L_MIN(1) : L_MIN(3));
    }
    
private:
    Wejscia & wej;
    Wyjscia & wyj;

    bool lustroJakoSwiatlo; //w jakim trybie swieci lustro
};

#endif //! ___LAMPA_H__