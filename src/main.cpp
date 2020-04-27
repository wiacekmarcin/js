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

void printW(const Wejscia &w) {
	Serial.println("JAD UP | JAD DOWN | KUCH A UP | KUCH A DOWN | KUCH B UP | KUCH B DOWN | WIE | NOC | RUCH_KUCH | RUCH_DRZWI | DRZWI_OTW");
	Serial.print  ("     ");
	Serial.print (w.czyklJadUp(), DEC);
	Serial.print ("|        ");
	Serial.print (w.czyklJadDown(), DEC);
	Serial.print ("|          ");
	Serial.print (w.czyklKuchAUp(), DEC);
	Serial.print ("|            ");
	Serial.print (w.czyklKuchADown(), DEC);
	Serial.print ("|          ");
	Serial.print (w.czyklKuchBUp(), DEC);
	Serial.print ("|            ");
	Serial.print (w.czyklKuchBDown(), DEC);
	Serial.print ("|    ");
	Serial.print(w.czyWieczor());
	Serial.print ("|    ");
	Serial.print(w.czyNoc());
	Serial.print ("|          ");
	Serial.print(w.czyRuchKuchnia(2000));
	Serial.print ("|           ");
	Serial.print(w.czyRuchDrzwi(2000));
	Serial.print ("|          ");
	Serial.println(w.czyDrzwiOtwarte());
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

	 Serial.begin(57600);
}

unsigned long t = 0;

unsigned long mss = 0;

bool prev = false;
void loop() {


	t = millis();
#ifdef DBG
	Serial.print("READ");
#endif
  	w.read();
#ifdef DBG
	printW(w);
#endif
	if (w.czyklJadUp() && w.czyklJadDown() && w.czyklKuchBUp() && w.czyklKuchBDown()) {
		if (millis() - mss > 2000) {
#ifdef DBG
			Serial.println("wlacz ledy");
#endif
			prev = !prev;
			swLED.zapalSufit1(prev);
			swLED.zapalSufit2(prev);
		}
		mss = millis();
	}
	else {
		swJadalnia.zapal(w);

		swSufit.zapal(w, swLED, swJadalnia.czyZapalone());
		swLED.zapal(w, swSufit.czyZapalone());
/*
	swPod.zapal(w, swSufit.czyZapalone(), swJadalnia.czyZapalone(), swLED.czyZapalonySufit());
	*/
#ifdef DBG
		Serial.print("CZAS TRWANIA");
		Serial.println(millis() - t, DEC);
#endif
	}
	delay(100 - (millis() - t));

}
