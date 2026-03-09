#ifndef __WYJSCIA_H__
#define __WYJSCIA_H__

#include <Adafruit_MCP23X17.h>
#include "wejscia.h"
#include "value.h"


class Wyjscia {
public:
    Wyjscia(Adafruit_MCP23X17 * _mcp, Wejscia * _wejscia)
     :  mcp(_mcp), wejscia(_wejscia)
    {}

    void init();

    void setExternal(uint8_t o, uint8_t val);
#if 0
    bool tiktok();

    void setSwiatlo(bool on = true, unsigned int timeout = 10*60)
        { set(SWIATLO, on, timeout); }

    void setSzafka(bool on = true, unsigned int timeout = 0)
        { set(SZAFKA, on, timeout); }

    void setZawor(bool on = true, unsigned int timeout = 30 )
        { set(ZAWOR, on, timeout); }

    void setLustro(bool on = true, unsigned int timeout = 5*60)
        { set(LUSTRO, on, timeout); }

    inline static uint8_t lo(bool value) { return value ? LOW : HIGH; }
    inline static uint8_t ho(bool value) { return value ? HIGH : LOW; }

    inline static bool li(uint8_t value) { return value == LOW; }
    inline static bool hi(uint8_t value) { return value == HIGH; }

    static uint8_t o(uint8_t id, bool value);
    static bool i(uint8_t id, uint8_t value);

    void print(const char *ff) const;

protected:
    void set(uint8_t pos, bool value, unsigned int timeout);
#endif
private:

    static constexpr uint8_t ZAWOR = 8+0; //fiolet
    static constexpr uint8_t LUSTRO = 8+1;  //niebieski
    static constexpr uint8_t SWIATLO = 8+2;  //bialy
    static constexpr uint8_t SZAFKA = 8+3;   //zolty
    static constexpr uint8_t WY_SWIATLO = A7; //procek
    
    static constexpr uint8_t WY_KONTAKTRON = 8+6;
    static constexpr uint8_t WY_CZUJNIK_RUCHU = 8+7;


    Adafruit_MCP23X17 * mcp;
    Wejscia * wejscia;


};


#endif // !__WYJSCIA_H__
