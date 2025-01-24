#ifndef __WYJSCIA_H__
#define __WYJSCIA_H__

#include <PCF8574.h>

#include "value.h"
class Wyjscia {
public:
    Wyjscia();

    void init();

    bool tiktok();

    void setSwiatlo(bool on = true, unsigned int timeout = 10*60)
        { set(SWIATLO, on, timeout); }

    void setSzafka(bool on = true, unsigned int timeout = 0)
        { set(SZAFKA, on, timeout); }

    void setZawor(bool on = true, unsigned int timeout = 30 )
        { set(ZAWOR, on, timeout); }

    void setLustro(bool on = true, unsigned int timeout = 5*60)
        { set(LUSTRO, on, timeout); }

    void setWiatrak(bool on = true, unsigned int timeout = 1)
        { set(WIATRAK, on, timeout); }

    
    bool getSwiatlo()
        { return on[SWIATLO]; }

    bool getSzafka()
        { return on[SZAFKA]; }

    bool getZawor()
        { return on[ZAWOR]; }

    bool getLustro()
        { return on[LUSTRO]; }

    bool getWiatrak()
        { return on[WIATRAK]; }

    inline static uint8_t lo(bool value) { return value ? LOW : HIGH; }
    inline static uint8_t ho(bool value) { return value ? HIGH : LOW; }

    inline static bool li(uint8_t value) { return value == LOW; }
    inline static bool hi(uint8_t value) { return value == HIGH; }

    static uint8_t o(uint8_t id, bool value);
    static bool i(uint8_t id, uint8_t value);

    void print(const char *ff) const;

protected:
    void set(uint8_t pos, bool value, unsigned int timeout);

private:

    PCF8574 wyjscia;

    static constexpr uint8_t ZAWOR = 0; //fiolet
    static constexpr uint8_t LUSTRO = 1;  //niebieski
    static constexpr uint8_t SWIATLO = 2;  //bialy
    static constexpr uint8_t SZAFKA = 3;   //zolty
    static constexpr uint8_t WY_SWIATLO = 4;
    static constexpr uint8_t WIATRAK = 5;

    static constexpr uint8_t maxWyj = 6;

    bool on[maxWyj] = { false, false, false, false, false, false };
    unsigned long timeout[maxWyj] = { 0, 0, 0, 0, 0, 0};

};

#endif // !__WYJSCIA_H__