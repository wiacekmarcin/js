#include "wentylator.hpp"

MyWentylator::MyWentylator(Adafruit_MCP23X17 * mcp_, uint8_t in_, uint8_t out_, unsigned int czasOnMin, bool reverse_, uint8_t id)
:    mcp(mcp_), 
    in(in_),
    out(out_),  
    lastAction(0L), 
    maxtick1s(60*czasOnMin), 
    ticks(0L),
    enable(false),
    reverse(reverse_),
    msg(id, V_STATUS)
{

}

void MyWentylator::init(void (*fun)())
{
    pinMode(in, INPUT);
    attachInterrupt(digitalPinToInterrupt(in), fun, FALLING); 
    mcp->pinMode(out, OUTPUT);    
}

void MyWentylator::presentation(const char * descr)
{
    present(msg.getSensor(), S_BINARY, descr);
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
    mcp->digitalWrite(out, v ? HIGH : LOW);
}

void MyWentylator::tick()
{
    if (enable)
        return;
    if (ticks == 0) {
        set(false);
        return;
    }
    ticks--;
}

