#ifndef WENTYLATOR
#define WENTYLATOR

#include <Adafruit_MCP23X17.h>
#include "my_sens.h"
class MyWentylator {
public:
    MyWentylator(Adafruit_MCP23X17 * mcp, uint8_t p, unsigned int czasOnMin, bool reverse, uint8_t id);
    void pushBtn();
    void init();

protected:
    void setPin(bool val);
    void set(bool on);
private:
    Adafruit_MCP23X17 * mcp;
    uint8_t pin;
    unsigned long lastAction;
    unsigned int maxtick1s;
    unsigned int ticks;
    bool enable;
    bool reverse;
    MyMessage msg;
};

#endif /* WENTYLATOR */
