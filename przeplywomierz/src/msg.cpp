#include "msg.h"


FlowMessage::FlowMessage()
{

}


void FlowMessage::sendWentylator(uint8_t id, bool on)
{
    Serial.print("W;");
    Serial.print(id, DEC);
    Serial.print(";");
    Serial.print(on, DEC);
    Serial.println(";");
}

void FlowMessage::sendZaworGaz(uint8_t id, bool on)
{
    Serial.print("G;");
    Serial.print(id, DEC);
    Serial.print(";");
    Serial.print(on, DEC);
    Serial.println(";");
}

void FlowMessage::sendFlow(uint8_t id, uint16_t val, uint32_t all)
{
    Serial.print("F;");
    Serial.print(id, DEC);
    Serial.print(";");
    Serial.print(val, DEC);
    Serial.print(";");
    Serial.print(all, DEC);
    Serial.println(";");
}