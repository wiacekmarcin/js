#ifndef __LAMPA_H__
#define __LAMPA_H__

#include "myMcp.hpp"

#include "wlacznik.hpp"
#include "wiatrak.hpp"

class Swiatlo 
{
    public:
    explicit Swiatlo(MyMcp2317WC & mcp, Wiatrak & wiatrak, unsigned short timeDelay);

    void setWlacznik(Wlacznik & wl);
    void tiktok();
    
    unsigned int getTikCnt(unsigned short min, unsigned short sec);
    private:

    MyMcp2317WC & io;
    unsigned int swiatloGorneOff;
    unsigned int swiatloBoczneOff;
    unsigned int swiatloLustroOff;

    bool stateHoldOn;
    Wiatrak & wiatrak;
    unsigned short div;
};








#if 0
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

        /* Lsustro */
    void zapalRegal(int mls = 5*60);
    void przedluzRegal(int mls = 5*60);
    void zgasRegal();
protected:

    unsigned long czasZapaleniaSwiatlo(bool noc, bool otwarte_drzwi) {
        return noc ? (otwarte_drzwi ? L_SEC(30) : L_MIN(2)) : (otwarte_drzwi ? L_MIN(1) : L_MIN(5));
    }

    unsigned long czasZapaleniaLustro(bool noc, bool otwarte_drzwi) {
        return noc ? (otwarte_drzwi ? L_SEC(20) : L_MIN(1)) : (otwarte_drzwi ? L_MIN(1) : L_MIN(3));
    }
    
private:
    Wejscia & wej;
    Wyjscia & wyj;

    bool regaljakoSwiatlo; //w jakim trybie swieci lustro
};
;
#endif
#endif //! ___LAMPA_H__