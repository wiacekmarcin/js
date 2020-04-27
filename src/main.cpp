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

class PseudoTimer {
private:
  unsigned long tik;

public:
  PseudoTimer() : tik(0) { }
  void tiktok() {
    constexpr unsigned int min5 = 20*60*5;
    constexpr unsigned long min30 = 20*60*30;
    ++tik;
    if (tik % min5 == 0) {//5 min
      swSufit.rotate();
      swJadalnia.rotate();
    }

    if (tik % min30 == 0) {////30 min
      swSufit.down();
      swJadalnia.down();
      tik = 0;
    }
  }
};

PseudoTimer psT;

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

unsigned int id = 0;
void loop() {

  	Serial.println(id, DEC);
  	w.readTest();

	//

#if 0
  //ledy na otwartymi drzwiami w dzien
  swLED.drzwi1(zapalLedDrzwiDzien());

  //ledy na otwartymi drzwiami w nocy
  swLED.drzwi2(zapalLedDrzwiNoc());

  //zapal swiatlo w jadalni
  if (w.czyklJadUp()) {
    swJadalnia.up();
  }

  //zgas swiatlo w jadalni
  if (w.czyklJadDown()) {
    swJadalnia.down();
  }

  //zapal swiatlo w kuchni
  // jezeli noc to najper zapal ledy na gorze
  if (w.czyklKuchDown() || w.czyklKuchUp()) {
#ifdef DBG
    Serial.print("Klawisz kuchnia nacisniety");
#endif
    if (w.czyNoc()) {
#ifdef DBG
      Serial.print(" Noc = true|");
      Serial.print(" sufit = ");
      Serial.print(swSufit.czyZapalone() ? "tak" : "nie");
      Serial.print("| ledy ");
      Serial.print(swSufit.czyZapalone() ? "tak" : "nie");
#endif
      if (swSufit.czyZapalone() || swLED.czyZapalone()) {
#ifdef DBG
        Serial.print("| gasze ledy ");
#endif
        swLED.sufit1(false);
        swLED.sufit2(false);

        if (w.czyklKuchDown()) {
#ifdef DBG
          Serial.println("| swSufit down");
#endif
          swSufit.down();
        } else if (w.czyklKuchUp()) {
#ifdef DBG
          Serial.println("| swSufit up");
#endif
          swSufit.up();
        }

      } else {
#ifdef DBG
        Serial.print("| zalaczam ledy ");
#endif
        swLED.sufit1(true);
        swLED.sufit2(true);
      }
    } else {
#ifdef DBG
      Serial.print(" Noc = false");
#endif
      if (w.czyklKuchDown()) {
#ifdef DBG
        Serial.println(" swSufit down");
#endif
        swSufit.down();
      } else if (w.czyklKuchUp()) {
#ifdef DBG
        Serial.println(" swSufit up");
#endif
        swSufit.up();
      }
    }

  }

  //podwietlanie wlacznika jadalnia
  swPod.zapalJadalnia(zapalOswietlenieJadalnia());

  //podwietlanie wlacznika kuchnia
  swPod.zapalKuchnia(zapalOswietlenieKuchnia());

  swPod.zapalSzafa(zapalSzafa())  ;

  psT.tiktok();
#ifdef DBG
  Serial.println("---\n");
#endif

  //delay(5000);
  delay(50);
#else
Serial.println("\n\n\---\n");

delay(2000);
#endif
}
