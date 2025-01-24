#ifndef _DRZWI_HPP_
#define _DRZWI_HPP_

class Drzwi {
    public :
    Drzwi();

    void set(bool val);

    bool czyZamkniete() const { return val; }
    bool czyOtwarte() const { return !val; }
    bool czyZostalyZamkniete() const { return !prev && val; }
    bool czyZostalyOtwarte() const { return prev && !val; }
    
    private:
        bool prev;
        bool val;
};

#endif /* DRZWI */
