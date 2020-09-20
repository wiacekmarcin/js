#ifndef __UTIL_H__
#define __UTIL_H__

#include <string.h>

#include "Arduino.h"
#include "value.h"
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

class Klawisz : public Value {
    public:
    Klawisz(const Value & val) : Value(val) { }
    
    bool czyNacisniety() const { return val(); }

    unsigned long czasWcisniecia() const { return val() ? millis() - time() : 0; }
    unsigned long czasPrzedWciśnięciem() const { return !val() ? time() - prevtime() : 0; }


    void print() {
        Serial.print("KLAWISZ val=");
        Serial.print(bin(),DEC);
        Serial.print(" nacisniety=");
        Serial.println(czyNacisniety(),DEC);
        Serial.print(" czas przed wcisnieciem=");
        Serial.print(czasPrzedWciśnięciem(),DEC);
        Serial.print(" czas wcisniecia=");
        char buf[12];
        printtime(czasWcisniecia(), buf);
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

void printtime(unsigned long mls, char * buf);


#endif // !__UTIL_H__