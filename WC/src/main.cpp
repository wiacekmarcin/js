#include <Arduino.h>

#include <Wire.h>
#include <Adafruit_MCP23X17.h>
#include "myMcp.hpp"
#include "debug.h"
#include "wlacznik.hpp"
#include "wiatrak.hpp"
#include "swiatlo.hpp"
#include "drzwi.hpp"
#include "czujnik.hpp"
MyMcp2317WC mcp;


void setup() {
    pinMode(13, OUTPUT);
    digitalWrite(13, HIGH);
    delay(2000);  
    //Serial.begin(115200);

    if (!mcp.begin_I2C()) {
        //Serial.println("Error.");
        while (1) {
            digitalWrite(13, LOW);
            delay(200);
            digitalWrite(13, HIGH);
            delay(200);
        }
    }
    //Serial.println("Mcp16 OK");

    if (!mcp.init_wc_io()) {
        //Serial.println("Error while settings IO.");
        while (1) {
            digitalWrite(13, LOW);
            delay(500);
            digitalWrite(13, HIGH);
            delay(500);
        }
    }
    digitalWrite(13, LOW);
    //Serial.println("My Mcp16 OK");
}

#define DELAYTIME 50
unsigned long actT = 0L;
Wlacznik wlacznik;
Wiatrak wiatrak(mcp);
Swiatlo swiatlo(mcp, wiatrak, DELAYTIME);
Drzwi drzwi;
Czujnik czujkaRuchu;
Czujnik czujnikZbliz;
void loop()
{
    actT = millis();
    if (mcp.isChange()) {
        mcp.print_wejscie();
        wlacznik.set(mcp.czyWlacznik(), actT);
        //wlacznik.print();
        if (wlacznik.get()) {
            swiatlo.setWlacznik(wlacznik);
        }
        drzwi.set(mcp.czyZamknieteDrzwi());
        swiatlo.setDrzwi(drzwi);
        
        if (czujkaRuchu.set(mcp.czyCzujnikRuchu(), actT)) 
            swiatlo.setCzujnikRuchu(czujkaRuchu.wykrytoRuch(), drzwi.czyOtwarte());

        if (czujnikZbliz.set(mcp.czyCzujnikLustra(), actT)) 
            swiatlo.setCzujkaLustro(czujnikZbliz.wykrytoRuch(), drzwi.czyOtwarte());
        
    } else {
        swiatlo.tiktok();
        wiatrak.tiktok();
    }
    delay(DELAYTIME);
    //Serial.println(mcp.getValue(), HEX);
}


