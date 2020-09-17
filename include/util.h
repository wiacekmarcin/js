#ifndef __UTIL_H__
#define __UTIL_H__

#include <string.h>

#include "Arduino.h"
#include "value.h"
class Drzwi : public Value {
public:
    Drzwi(const Value & val) : Value(val) {} ;

    unsigned long czasOtwarte() const  {  return val() ? time() : prevtime(); }
    unsigned long czasZamkniete() const  {  return val() ? prevtime() : time(); }

    bool otwarte() const  { return val() ; }
    bool zamkniete() const  { return ! val() ; }
    void print() {
        //Serial.print("DRZWI val=");
        //Serial.print(val(),DEC);
        //Serial.print(" czasOtwarte=");
        //Serial.print(czasOtwarte(),DEC);
        //Serial.print(" czasZamkniete=");
        //Serial.print(czasZamkniete(),DEC);
        //Serial.print(" otwarte=");
        //Serial.print(otwarte(),DEC);
        //Serial.print(" zamkniete=");
        //Serial.println(zamkniete(),DEC);
    }
};

class Klawisz : public Value {
    public:
    Klawisz(const Value & val) : Value(val) { }
    
    bool nacisniety() const { return val(); }

    void print() {
        //Serial.print("KLAWISZ val=");
        //Serial.print(val(),DEC);
        //Serial.print(" nacisniety=");
        //Serial.println(nacisniety(),DEC);
    }
};

class Czujka : public Value {
public :
    Czujka(const Value & val) : Value(val) { }

    bool ruch() const { return val(); }
    unsigned long bezruch() const { return val() ? 0 : time(); }

    void print() {
        //Serial.print("CZUJKA val=");
        //Serial.print(val(),DEC);
        //Serial.print(" ruch=");
        //Serial.print(ruch(),DEC);
        //Serial.print(" bezruch=");
        //Serial.println(bezruch(),DEC);
    }

};

void printtime(unsigned long mls, char * buf);


#endif // !__UTIL_H__