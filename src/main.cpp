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

bool change(unsigned int timeinsKuchnia, unsigned int timeimsDrzwi) {
	static unsigned long prevmaskawejsc = 0x00;
	unsigned long maskawejsc = 0x00;

	maskawejsc |= w.czyklJadDown() << 1;
	maskawejsc |= w.czyklJadUp() << 2;
	maskawejsc |= w.czyklKuchADown() << 3;
	maskawejsc |= w.czyklKuchAUp() << 4;
	maskawejsc |= w.czyklKuchBDown() << 5;
	maskawejsc |= w.czyklKuchUp() << 6;
	maskawejsc |= w.czyDrzwiOtwarte() << 7;
	maskawejsc |= w.czyNoc() << 8;
	maskawejsc |= w.czyWieczor() << 9;
	maskawejsc |= w.czyRuchDrzwi(1000*timeinsDrzwi) << 10;
	maskawejsc |= w.czyRuchKuchnia(1000*timeinsKuchnia) << 11;
	

	if (prevmaskawejsc == maskawejsc)
		return false;

	if (maskawejsc & 0x3f) { // jaki kolwiek klawsz to znaczy jest ruch w kuchni 
		w.setRuch();
	}
	prevmaskawejsc = maskawejsc;
	return true;
}

void printW(const long & t, const Wejscia &w, bool force = false) 
{
	

	if (force || prevmaskawejsc != maskawejsc)
	{
		Serial.println(t, DEC);
		Serial.print(prevmaskawejsc, BIN);
		Serial.print(" => ");
		Serial.println(maskawejsc, BIN);
		prevmaskawejsc = maskawejsc;
		Serial.println("JAD UP | JAD DOWN | KUCH A UP | KUCH A DOWN | KUCH B UP | KUCH B DOWN | DRZWI_OTW | WIE | NOC | | RUCH_DRZWI | RUCH_KUCH ");
		Serial.print  ("      ");
		Serial.print (w.czyklJadUp(), DEC);
		Serial.print ("|         ");
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
		Serial.println(w.czyDrzwiOtwarte());
		Serial.print ("|    ");
		Serial.print(w.czyWieczor());
		Serial.print ("|    ");
		Serial.print(w.czyNoc());
		Serial.print ("|          ");
		Serial.print(w.czyRuchDrzwi(2000));
		Serial.print ("|         ");
		Serial.print(w.czyRuchKuchnia(2000));
		Serial.print ("|           ");
		
		
		Serial.println('-');
	}
}

unsigned long t = 0;


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

	t = millis();

	w.read();
	printW(t, w, true);
}



unsigned long mss = 0;

bool prev = false;
void loop() {


	t = millis();

	w.read();
	printW(t, w);

	if (Serial.available() > 0) {
		uint8_t inc = Serial.read();
		if (inc == 'a') {
			Serial.print(inc, DEC);
			Serial.print(" ");
			printW(t, w, true);	
		}
	}
	if (!change(30*60, 5*60)) {
		delay(100);
		return;
	}
	
	if (Serial.available() > 0) {
		 else if (inc == '0') {
			swSufit.up();
		} else if (inc == '1')
		{
			expLedy.digitalWrite(1, lo(true));
			//expLedy.digitalWrite(2, lo(true));
			//expLedy.digitalWrite(3, lo(true));
			expLedy.digitalWrite(4, lo(true));
			expLedy.digitalWrite(0, lo(true));
		} else if (inc == '2')
		{
			expLedy.digitalWrite(1, ho(true));
			expLedy.digitalWrite(2, ho(true));
			expLedy.digitalWrite(3, ho(true));
			expLedy.digitalWrite(4, ho(true));
			expLedy.digitalWrite(0, ho(true));
		}
  	}
  	
	return;

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
