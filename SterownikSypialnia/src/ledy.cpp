#include "ledy.hpp"
#include "utils.hpp"

LampaLed::LampaLed(uint8_t lsze, uint8_t ids[]):
    lsize(lsze), tiktokNr(t15m)
{
    t = new TLedOne[lsze];
    for (uint8_t i = 0; i < lsize; ++i) {
        t[i].a_time = 0;
        t[i].on = false;
        t[i].index = ids[i];
    }
}

LampaLed::~LampaLed()
{
    delete [] t;
}

void LampaLed::tiktok()
{
    uint8_t on_l = 0;
    --tiktokNr;
    for (uint8_t i = 0; i < lsize; ++i) {
        if (t[i].on) {
            ++(t[i].a_time);
            ++on_l;
        }
    }

    if (on_l == 0 || on_l == lsize) {
        tiktokNr = t15m;
        return;
    }

    for (uint8_t i = 0; i < lsize-1; ++i) {
        if (t[i].a_time > t[i+1].a_time) {
            auto temp = t[i+1];
            t[i+1] = t[i];
            t[i] = temp;
        }
    }

    if (tiktokNr > 0)
        return;

    tiktokNr = t15m;
    uint8_t x1 = 0, x2 = lsize - 1;
    for(uint8_t i=0; i < lsize; ++i) {
        if (! t[i].on) {
            x1 = i;
            break;
        }
    }

    for(uint8_t i=0; i < lsize; ++i) {
        if (t[lsize-1-i].on) {
            x2 = lsize-1-i;
            break;
        }
    }

    t[x1].on = true;
    mcp_digitalWrite(t[x1].index, HIGH);

    t[x2].on = false;
    mcp_digitalWrite(t[x2].index, LOW);

}

void LampaLed::on1()
{
    for (uint8_t i = 0; i < lsize; ++i) {
        if (! t[i].on) {
            t[i].on = true;
            mcp_digitalWrite(t[i].index, HIGH);
            break;
        }
    }
}

void LampaLed::off1()
{    
    for (int8_t i = lsize-1; i >= 0; --i) {
        if (t[i].on) {
            t[i].on = false;
            mcp_digitalWrite(t[i].index, LOW);
            break;
        }
    }
}

void LampaLed::off()
{
    for (uint8_t i = 0; i < lsize; ++i) {
        t[i].on = false;
        mcp_digitalWrite(t[i].index, LOW);
    }
}

bool LampaLed::isOn()
{
    for (int8_t i = lsize-1; i >= 0; --i) {
        if (t[i].on) {
            return true;
        }
    }
    return false;
}

bool LampaLed::isAll()
{
    for (uint8_t i = 0; i < lsize; ++i) {
        if (! t[i].on) {
            return false;
        }
    }
    return true;
}
