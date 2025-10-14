#include "zaworgaz.hpp"
#include "msg.h"

extern FlowMessage flowMsg;

MyZaworGaz::MyZaworGaz(Adafruit_MCP23X17 * mcp_, uint8_t in, uint8_t out1, uint8_t out2, uint8_t id_)
: mcp(mcp_), btn(in), pinF1(out1), pinF2(out2), lastAction(0L), enable(false), id(id_)
{

}

void MyZaworGaz::pushBtn()
{
    if (millis() - lastAction < 1000)
        return;
    set(!enable);    
}
    
void MyZaworGaz::init()
{
    pinMode(btn, INPUT);
    mcp->pinMode(pinF1, OUTPUT);
    mcp->pinMode(pinF2, OUTPUT);
    mcp->digitalWrite(pinF1, LOW);
    mcp->digitalWrite(pinF2, LOW);
}

void MyZaworGaz::set(bool on)
{
    enable = on;
    setPin(on);
    flowMsg.sendZaworGaz(id, on);
}

void MyZaworGaz::setPin(bool val)
{
    bool v = !val;
    mcp->digitalWrite(pinF1, v);
    mcp->digitalWrite(pinF2, v);
}