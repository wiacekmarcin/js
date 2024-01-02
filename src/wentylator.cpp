#include "wentylator.hpp"

MyWentylator::MyWentylator(Adafruit_MCP23X17 * mcp_, uint8_t p, unsigned int czasOnMin, bool reverse_, uint8_t id)
:    mcp(mcp_), 
    uint8_t pin(p), 
    lastAction(0L), 
    maxtick1s(60*czasOnMin), 
    ticks(0L),
    enable(false),
    reverse(reverse_),
    msg(id, V_STATUS)
{

}

void MyWentylator::init()
{
    mcp->pinMode(pin, OUTPUT);    
}

void MyWentylator::pushBtn()
{
    if (millis() - lastAction < 1000)
        return;
    set(!enable);    
}

void MyWentylator::set(bool on)
{
    enable = on;
    ticks = on ? maxtick1s : 0L;
    setPin(on);
    send(msg.set(on));
}

void MyWentylator::setPin(bool val)
{
    bool v = reverse ? !val : val;
    mcp->digitalWrite(pin, v ? HIGH : LOW);
}

void MyWentylator::tick()
{
    if (enable)
        return;
    if (tick1s == 0) {
        set(false);
        return;
    }
    tick1s--;
}

