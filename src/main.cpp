#include <Arduino.h>
#include <PCF8574.h>

#include "main.h"
#include "wejscia.h"
#include "podswietlenie.h"
#include "swiatloled.h"
#include "swiatlojadalnia.h"
#include "swiatlosufit.h"

PCF8574 expWejscia(0x20);
PCF8574 expLedy(0x25);
PCF8574 expOczka(0x26);
PCF8574 expPozostale(0x27);



#define DBG 1



Wejscia w;
Podswietlenie swPod;
SwiatloLED swLED;
SwiatloSufit swSufit;
SwiatloJadalnia swJadalnia;


bool zapalOswietlenieJadalnia() {
#ifdef DBG
  Serial.print("zapalOswietlenieJadalnia wieczor=");
  Serial.print(w.czyWieczor() ? "tak" : "nie");
  Serial.print(" sufit czyZapalone=");
  Serial.print(swSufit.czyZapalone() ? "tak" : "nie");
  Serial.print(" led czyZapalone=");
  Serial.print(swLED.czyZapalone() ? "tak" : "nie");
  Serial.print(" wynik=");
  Serial.println((w.czyWieczor() && !swJadalnia.czyZapalone() && !swSufit.czyZapalone() && !swLED.czyZapalone()) ? "tak" : "nie");
#endif
    if (!w.czyWieczor())
      return false;
    if (swJadalnia.czyZapalone() || swSufit.czyZapalone() || swLED.czyZapalone())
      return false;
    return true;
}

bool zapalOswietlenieKuchnia() {
#ifdef DBG
  Serial.print("zapalOswietlenieKuchnia wieczor=");
  Serial.print(w.czyWieczor() ? "tak" : "nie");
  Serial.print(" sufit czyZapalone=");
  Serial.print(swSufit.czyZapalone() ? "tak" : "nie");
  Serial.print(" led czyZapalone=");
  Serial.print(swLED.czyZapalone() ? "tak" : "nie");
  Serial.print(" wynik=");
  Serial.println((w.czyWieczor() && !swSufit.czyZapalone() && !swLED.czyZapalone()) ? "tak" : "nie");
#endif

  if (!w.czyWieczor())
    return false;
  if (swSufit.czyZapalone() || swLED.czyZapalone())
    return false;
  return true;
}

bool zapalLedDrzwiDzien() {
#ifdef DBG
  Serial.print("zapalLedDrzwiDzien noc=");
  Serial.print(w.czyNoc() ? "tak" : "nie");
  Serial.print(" czyDrzwiOtwarte=");
  Serial.print(w.czyDrzwiOtwarte() ? "tak" : "nie");
  Serial.print(" czyRuch=");
  Serial.print(w.czyRuchDrzwi(5*60) ? "tak" : "nie");
  Serial.print(" wynik=");
  Serial.println(!w.czyNoc() && w.czyRuchDrzwi(5*60) && w.czyDrzwiOtwarte() ? "tak" : "nie");
#endif

  if (!w.czyDrzwiOtwarte())
      return false;

  if (w.czyNoc())
      return false;

  if (w.czyRuchDrzwi(5*60))
      return true;

  return false;

}

bool zapalLedDrzwiNoc() {
#ifdef DBG
  Serial.print("zapalLedDrzwiNoc noc=");
  Serial.print(w.czyNoc() ? "tak" : "nie");
  Serial.print(" czyDrzwiOtwarte=");
  Serial.print(w.czyDrzwiOtwarte() ? "tak" : "nie");
  Serial.print(" czyRuch=");
  Serial.print(w.czyRuchDrzwi(5*60) ? "tak" : "nie");
  Serial.print(" wynik=");
  Serial.println(w.czyNoc() && w.czyRuchDrzwi(5*60) && w.czyDrzwiOtwarte() ? "tak" : "nie");

#endif
  if (!w.czyDrzwiOtwarte())
      return false;

  if (!w.czyNoc())
      return false;

  if (w.czyRuchDrzwi(5*60))
      return true;
  return false;
}

bool zapalSzafa() {
#ifdef DBG
  Serial.print("ZapalSzafa noc=");
  Serial.print(w.czyNoc() ? "tak" : "nie");
  Serial.print(" czyRuch=");
  Serial.print(w.czyRuchKuchnia(10*60) ? "tak" : "nie");
  Serial.print(" wynik=");
  Serial.println(w.czyNoc() && w.czyRuchKuchnia(10*60) ? "tak" : "nie");

#endif
  if (w.czyNoc() && w.czyRuchKuchnia(10*60))
    return false;
  return true;
}

void setup() {
	 swSufit.init();
	 //expOczka.begin(); -- w srodku jest funkcja begin

	 swJadalnia.init();
     swPod.init();
	 expPozostale.begin();

	 swLED.init();
	 w.init();
	 expLedy.begin();


  //swPod.zapalKuchnia(true);
  //swPod.zapalJadalnia(true);
}

unsigned long t = 0;
void loop() {


	t = millis();
  	w.readTest();
	swJadalnia.zapal(w);
	swSufit.zapal(w, swLED, swJadalnia.czyZapalone());
	swLED.zapal(w, swSufit.czyZapalone());
	swPod.zapal(w, swSufit.czyZapalone(), swJadalnia.czyZapalone(), swLED.czyZapalonySufit());
delay(500);

}
