#include <Arduino.h>

#include <Wire.h>
#include <Adafruit_MCP23X17.h>
#include "myMcp.hpp"
#include "debug.h"
#include "wlacznik.hpp"
#include "wiatrak.hpp"
#include "swiatlo.h"

MyMcp2317WC mcp;


void setup() {
    delay(5000);  
    Serial.begin(115200);

    if (!mcp.begin_I2C()) {
        Serial.println("Error.");
        while (1);
    }
    Serial.println("Mcp16 OK");

    if (!mcp.init_wc_io()) {
        Serial.println("Error while settings IO.");
        while (1);
    }
    
    Serial.println("My Mcp16 OK");
}

#define DELAYTIME 50
unsigned long actT = 0L;
Wlacznik wlacznik;
Wiatrak wiatrak(mcp);
Swiatlo swiatlo(mcp, wiatrak, DELAYTIME);
void loop()
{
    actT = millis();
    if (mcp.isChange()) {
        //mcp.print_wejscie();
        wlacznik.set(mcp.czyWlacznik(), actT);
        //wlacznik.print();
        if (wlacznik.get()) {
            swiatlo.setWlacznik(wlacznik);
        }
    } else {
        swiatlo.tiktok();
        wiatrak.tiktok();
    }
    delay(DELAYTIME);
    //Serial.println(mcp.getValue(), HEX);
}


