#include "Arduino.h"
#include "value.h"
class Drzwi : public Value {
public:
    Drzwi(Value & val);

    unsigned long czasOtwarte() const  {  return val() ? time() : prevtime(); }
    unsigned long czasZamkniete() const  {  return val() ? prevtime() : time(); }

    bool otwarte() const  { return val() ; }
    bool zamkniete() const  { return ! val() ; }

};

class Klawisz : public Value {
    public:
    Klawisz(Value & val) : Value(val) { }
    
    bool nacisniety() const { return val(); }
}