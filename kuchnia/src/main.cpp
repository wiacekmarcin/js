#include <Arduino.h>

#include <Wire.h>
#include <PCF8574.h>

#include "wejscia.h"
#include "wyjscia.h"

#include "lampa.h"

//PCF8574 expWejscia(0x20);
Wejscia expWejscia;

//PCF8574 expWyjscia(0x21);
Wyjscia expWyjscia;

Lampa lampa(expWyjscia);

//p0 p1 p2 p3
//p0 czujnik zblizeniowy 0 - blisko 1 - daleko
//p1 czujnik ruchu 
//p2 drzwi 0 - zamkniete 1 - otwarte
//p3 klawisz 0 - nacisniety 1 - w normalnej pozycji

//p4 noc
//p5 wieczor
//p6 czujnik poziomu wody

    expWyjscia.setSwiatlo(! expWyjscia.getSwiatlo(), 1000*60*10); //wlacz lampe z 10 min opoźnieniem do wylaczenia
}

void zapalLustro(const Value & lus, const Value &drzwi, const Value & kl) {
  if (lus.val()) {
    expWyjscia.setLustro(true, 1000*60*5); //wlacz lustro z 5 min do wylaczenia
  } else if (kl.val() && expWyjscia.getLustro())
    expWyjscia.setLustro(false); //wylacz lustro - nie ma zblizenia i drzwi sie otworzyly
  else {
    unsigned long mls = millis();
    if (mls - lus.time() < 3*60*1000 && drzwi.val() && mls - drzwi.time() < 500)
      expWyjscia.setLustro(false); //wylacz lustro - nie ma zblizenia i drzwi sie otworzyly
    
  }
}

void setup() {  
  
  expWejscia.init();

  expWyjscia.init();

  Serial.begin(9600);
  
}

uint8_t cntNum = 0;
unsigned int am = 0;
unsigned int pm = 0;
void loop() {
    expWejscia.get();

    am = expWejscia.getMask();
    if (am != pm) {
      pm = am;
      
      bool klawisz = expWejscia.getWlacznik();
      if (klawisz) { //naciśniecie klawisza
        lampa.setKlawisz(klawisz);
        lustro.setKlawisz(klawisz);
      }
      
      Value czR = expWejscia.getCzRuchu();
      lampa.setRuchWC(czR.val(), czR.time());
      lustro.setRuchWC(czR.val(), czR.time());

      Value czL = expWejscia.getLustro();
      lustro.setRuch(czL.val(), czL.time(), czL.prevtime());

      Value drzwiOtw = expWejscia.getDrzwiOtw();
      lampa.setDrzwiOtw(drzwiOtw.val(), drzwiOtw.time());
      lustro.setDrzwiOtw(drzwiOtw.val(), drzwiOtw.time());

      Value drzwiZam = expWejscia.getDrzwiOtw();
      lampa.setDrzwiZam(drzwiZam.val(), drzwiZam.time());
    }

    if (++cntNum == 10) {
      cntNum = 0;
      lampa.tiktok();
      lustro.tiktok();
    }
  delay(100);
}
