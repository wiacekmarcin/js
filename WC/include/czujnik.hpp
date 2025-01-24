#ifndef _CZUJNIK_HPP_
#define _CZUJNIK_HPP_

class Czujnik {

public:
    Czujnik();
    
    bool set(bool val, unsigned long timeStamp);

    bool wykrytoRuch();
    
private:
    bool val;
    bool prev;
    unsigned long timeStamp;
};


#endif /* CZUJNIK */
