#include <Arduino.h>

#include <Wire.h>
#include <PCF8574.h>

#include "wejscia.h"
#include "wyjscia.h"

#include "lampa.h"
#include "lustro.h"

//PCF8574 expWejscia(0x20);
Wejscia expWejscia;

//PCF8574 expWyjscia(0x21);
Wyjscia expWyjscia;

Lampa lampa(expWejscia, expWyjscia);
Lustro lustro(expWejscia, expWyjscia);

//p0 p1 p2 p3
//p0 czujnik zblizeniowy 0 - blisko 1 - daleko
//p1 czujnik ruchu 
//p2 drzwi 0 - zamkniete 1 - otwarte
//p3 klawisz 0 - nacisniety 1 - w normalnej pozycji

//p4 noc
//p5 wieczor
//p6 czujnik poziomu wody


void setup() {  
  
  expWejscia.init();

  expWyjscia.init();

  Serial.begin(9600);
  
}

void loop() {
    
    expWejscia.get();
    expWejscia.print();
    unsigned long mls = millis();
    
    expWejscia.print();
    lampa.set();
    lustro.set();
    
    delay(100 - (millis() - mls));
}
