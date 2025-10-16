#ifndef WENTYLATOR
#define WENTYLATOR

#include <Adafruit_MCP23X17.h>
class MyWentylator {
public:
    MyWentylator(Adafruit_MCP23X17 * mcp, uint8_t in, uint8_t out, unsigned int czasOnMin, bool reverse, uint8_t id);
    void pushBtn();
    void init(void (*fun)(void));
    void tick();
    void set(bool on);
protected:
    void setPin(bool val);
    
private:
    Adafruit_MCP23X17 * mcp;
    uint8_t in;
    uint8_t out;
    unsigned long lastAction;
    unsigned int maxtick1s;
    unsigned int ticks;
    bool enable;
    bool reverse;
    uint8_t id;
};

#endif /* WENTYLATOR */
