#ifndef _MY_MSG_H_
#define _MY_MSG_H_
#include <Arduino.h>

class FlowMessage {
public:


    FlowMessage();
    void sendWentylator(uint8_t id, bool on);
    void sendZaworGaz(uint8_t id, bool on);
    void sendFlow(uint8_t id, uint16_t val, uint32_t all);
private:


};










#endif