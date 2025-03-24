#ifndef _LEDY_HPP_
#define _LEDY_HPP_
#include <Arduino.h>
#include "decl_io.hpp"

typedef struct _ledOne {
    uint32_t a_time;
    bool on;
    uint8_t index;
} TLedOne;

class LampaLed 
{
    public:
    LampaLed(uint8_t lsze, uint8_t index[]); 
    ~LampaLed();

    void tiktok();
    void on1();
    void off1();
    void off();
    bool isOn();
    bool isAll();
    void on();

    void set(uint8_t index, bool val);

    private:
    const uint8_t lsize;
    TLedOne * t;
    uint16_t tiktokNr;
};

#define t15m 15*60


#endif