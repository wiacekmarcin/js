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


Wejscia w;
Podswietlenie swPod;
SwiatloLED swLED;
SwiatloSufit swSufit;
SwiatloJadalnia swJadalnia;

static long maskawejsc = 0x00;
static long prevmaskawejsc = 0x00;
void printW(const long & t, const Wejscia &w) 
{
	maskawejsc = 0x00;
	maskawejsc |= w.czyDrzwiOtwarte() << 1;
	maskawejsc |= w.czyklJadDown() << 2;
	maskawejsc |= w.czyklJadUp() << 3;
	maskawejsc |= w.czyklKuchADown() << 4;
	maskawejsc |= w.czyklKuchAUp() << 5;
	maskawejsc |= w.czyklKuchBDown() << 6;
	maskawejsc |= w.czyklKuchUp() << 7;
	maskawejsc |= w.czyNoc() << 8;
	maskawejsc |= w.czyRuchDrzwi(1) << 9;
	maskawejsc |= w.czyRuchKuchnia(1) << 10;
	maskawejsc |= w.czyWieczor() << 11;

	if (prevmaskawejsc != maskawejsc)
	{
		prevmaskawejsc = maskawejsc;
		Serial.println(t, DEC);
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
		Serial.println('-');
	}
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

	 swPod.zapalSzafa(true);
	 Serial.begin(38400);
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
	printW(t, w);


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

	swPod.zapal(w, swSufit.czyZapalone(), swJadalnia.czyZapalone(), swLED.czyZapalonySufit());
	
#ifdef DBG
		Serial.print("CZAS TRWANIA");
		Serial.println(millis() - t, DEC);
#endif
	}

	swSufit.rotate();
	delay(100 - (millis() - t));

}
