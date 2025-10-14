#ifndef ZAWORGAZ
#define ZAWORGAZ

#include <Adafruit_MCP23X17.h>
class MyZaworGaz {
public:
    MyZaworGaz(Adafruit_MCP23X17 * mcp, uint8_t in, uint8_t out1, uint8_t out2, uint8_t id);
    void pushBtn();
    void init();

protected:
    void setPin(bool val);
    void set(bool on);
private:
    Adafruit_MCP23X17 * mcp;
    uint8_t btn;
    uint8_t pinF1;
    uint8_t pinF2;
    unsigned long lastAction;
    bool enable;
    uint8_t id;
};

#endif // DEBUG