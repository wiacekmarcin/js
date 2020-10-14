#ifndef __UTIL_H__
#define __UTIL_H__

#include <string.h>

#include "Arduino.h"
#include "value.h"

void printtime(unsigned long mls, char * buf);

#define SEC(X) ((unsigned long)(1000L*(X)))
#define MIN(X) ((unsigned long)(6000L*(X)))


class Drzwi : public Value {
public:
    Drzwi(const Value & val) : Value(val) {} ;

    bool czyOtwarte() const { return !val(); }

    unsigned long czasOtwarcia() const  {  return czyOtwarte() ? millis() - time() : time() - prevtime(); }
    unsigned long czasZamkniecia() const  {  return czyOtwarte() ? time() - prevtime() : millis() - time(); }

    void print() {
        Serial.print("DRZWI val=");
        Serial.print(val(),DEC);
        Serial.print("bin=");
        Serial.print(bin(),DEC);
        Serial.print(" czasOtwarcia=");
        char buf[12];
        printtime(czasOtwarcia(), buf);
        Serial.print(buf);
        Serial.print(" czasZamkniecia=");
        printtime(czasZamkniecia(), buf);
        Serial.println(buf);
    }
};

class Czujka : public Value {
public :
    Czujka(const Value & val) : Value(val) { }

    bool czyRuch() const { return val(); }
    unsigned long czasBezRuchu() const { return val() ? 0 : millis() - time(); }
    unsigned long czasRuchu() const { return val() ? millis() - time() : 0; }

    void print() {
        Serial.print("CZUJKA val=");
        Serial.print(bin(),DEC);
        Serial.print(" ruch=");
        Serial.print(czyRuch(),DEC);
        Serial.print(" bezruch=");
        char buf[12];
        printtime(czasBezRuchu(), buf);
        Serial.println(buf);
    }

};




#endif // !__UTIL_H__