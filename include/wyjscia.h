#ifndef __WYJSCIA_H__
#define __WYJSCIA_H__
#include <Arduino.h>
#include <Adafruit_MCP23017.h>
//#define DEBUG
class Wyjscia {
public:
    Wyjscia(Adafruit_MCP23017 & wyjscia);

    void init();

    bool tiktok();

    void off();

    void setSwiatlo(bool on = true, unsigned long timeout = 10*60)
        { set(SWIATLO, on, timeout); }

    void setSzafka(bool on = true, unsigned long timeout = 0)
        { set(SZAFKA, on, timeout); }

    void setZawor(bool on = true, unsigned long timeout = 30 )
        { set(ZAWOR, on, timeout); }

    void setLustro(bool on = true, unsigned long timeout = 5*60)
        { set(LUSTRO, on, timeout); }

    void setWiatrak(bool on = true, unsigned long timeout = 1)
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

    void addSwiatlo(unsigned int timeout = 10*60)
        { add(SWIATLO, timeout); }

    void addLustro(unsigned int timeout = 10*60)
        { add(LUSTRO, timeout); }

    inline static uint8_t lo(bool value) { return value ? LOW : HIGH; }
    inline static uint8_t ho(bool value) { return value ? HIGH : LOW; }

    inline static bool li(uint8_t value) { return value == LOW; }
    inline static bool hi(uint8_t value) { return value == HIGH; }

    static uint8_t o(uint8_t id, bool value);

    void print(const char *ff) const;

protected:
    void set(uint8_t pos, bool value, unsigned long timeout);
    void add(uint8_t pos, unsigned long timeout);

private:

    Adafruit_MCP23017 & wyjscia;

    static constexpr uint8_t ZAWOR = 5; //fiolet
    static constexpr uint8_t LUSTRO = 4;  //niebieski
    static constexpr uint8_t SWIATLO = 3;  //bialy
    static constexpr uint8_t SZAFKA = 2;   //zolty
    static constexpr uint8_t WY_SWIATLO = 6; //brazowy
    static constexpr uint8_t WIATRAK = 7; //zielony

    static constexpr uint8_t WY_FIRST = SZAFKA;
    static constexpr uint8_t WY_LAST = WIATRAK; 

    static constexpr uint8_t maxWyj = 8;

    bool on[maxWyj] = { false, false, false, false, false, false, false, false };
    unsigned long timeout[maxWyj] = { 0, 0, 0, 0, 0, 0, 0, 0};

};

#endif // !__WYJSCIA_H__