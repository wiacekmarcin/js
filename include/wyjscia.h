#ifndef __WYJSCIA_H__
#define __WYJSCIA_H__

#include <PCF8574.h>

#include "value.h"
class Wyjscia {
public:
    Wyjscia();

    void init();

    void tiktok();

    void setSwiatlo(bool on = true, unsigned long timeout = 10L*60L*1000L)
        { set(SWIATLO, on, timeout); }

    void setSzafka(bool on = true, unsigned long timeout = 0L)
        { set(SZAFKA, on, timeout); }

    void setZawor(bool on = true, unsigned long timeout = 30L*1000L )
        { set(ZAWOR, on, timeout); }

    void setLustro(bool on = true, unsigned long timeout = 5L*60L*1000L)
        { set(LUSTRO, on, timeout); }

    void setWiatrak(bool on = true, unsigned long timeout = 1000L)
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

protected:
    void set(uint8_t pos, bool value, unsigned long timeout);
    void print();

private:

    PCF8574 wyjscia;

    static constexpr uint8_t SWIATLO = 0;
    static constexpr uint8_t SZAFKA = 1;
    static constexpr uint8_t LUSTRO = 2;
    static constexpr uint8_t ZAWOR = 3;
    static constexpr uint8_t WIATRAK = 4;

    static constexpr uint8_t maxWyj = 5;

    bool on[maxWyj] = { false, false, false, false, false };
    unsigned long timeout[maxWyj] = { 0, 0, 0, 0, 0};

    bool change;
    unsigned long mask = 0;

};

#endif // !__WYJSCIA_H__
