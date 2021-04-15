#include <Arduino.h>
#include "main.h"

#ifndef NEW_BOARD
#include <PCF8574.h>
#else
#include <Adafruit_MCP23017.h>
#include "io.h"
#endif


#include "wejscia.h"
#include "podswietlenie.h"
#include "swiatloled.h"
#include "swiatlojadalnia.h"
#include "swiatlosufit.h"

#ifdef NEW_BOARD
Adafruit_MCP23017 o20;
Adafruit_MCP23017 io24;
#else
PCF8574 expWejscia(0x20);
PCF8574 expLedy(0x25);
PCF8574 expOczka(0x26);
PCF8574 expPozostale(0x27);
#endif



Wejscia w;
Podswietlenie swPod;
SwiatloLED swLED;
SwiatloSufit swSufit;
SwiatloJadalnia swJadalnia;

bool change(unsigned long timeinsKuchnia, unsigned long timeimsDrzwi) {
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
	maskawejsc |= w.czyRuchDrzwi(SwiatloLED::czasSwiecenieLED) << 10;
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
	Serial.println(t);
	Serial.println("JAD UP | JAD DOWN | KUCH A UP | KUCH A DOWN | KUCH B UP | KUCH B DOWN | DRZWI_OTW | WIE | NOC | RUCH_DRZWI | RUCH_KUCH ");
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
	Serial.print ("|          ");
	Serial.print (w.czyDrzwiOtwarte());
	Serial.print ("|    ");
	Serial.print (w.czyWieczor());
	Serial.print ("|    ");
	Serial.print (w.czyNoc());
	Serial.print ("|          ");
	Serial.print (w.czyRuchDrzwi(2000));
	Serial.print ("|         ");
	Serial.println (w.czyRuchKuchnia(2000));
	Serial.println('-');
}

unsigned long t = 0;


void setup() {

#ifdef NEW_BOARD
	zapalPrzekazniki(false);
	zapalZasAwar(false);
	zapalLEDZasilacz(false);
	io_init();
	delay(500);
	w.read();
	//if (w.czyZasilanieAwaryjne) { zapalZasAwar(true); delay(50); }
	zapalPrzekazniki(true);
	delay(100);
	zapalSzafki(true);
	if (w.czyWieczor()) {
		zapalLedSufitLod(true);
		zapalLEDZasilacz(true);
	}

#endif
	 swSufit.init();
	 //expOczka.begin(); -- w srodku jest funkcja begin

	 swJadalnia.init();
     swPod.init();
#ifndef NEW_BOARD
	expPozostale.begin();
#endif 
	 

	 swLED.init();
	 w.init();
#ifndef NEW_BOARD	 
	 expLedy.begin();
#endif
	swPod.zapalSzafa(true);
	Serial.begin(38400);

	t = millis();

	w.read();
	//printW(t, w, true);



}



unsigned long mss = 0;

bool prev = false;
int passcnt = -1;
void loop() {
#if 0
	//5, 6,  8
	digitalWrite(5, HIGH);
	o20.writeGPIOAB(0xffff);
	delay(5000);
	o20.writeGPIOAB(0x0000);
	Serial.println("5 - LOW");
	for (int i=0; i< 16;i++) {
		delay(400);
		o20.digitalWrite(i, LOW);
	}
	io24.digitalWrite(LEDDRZ1, LOW);
	io24.digitalWrite(LEDSUFL, LOW);
	io24.digitalWrite(LEDSUFJ, LOW);	
	

	delay(5000);
	Serial.println("5 - HIGH");
	for (int i=0; i< 16;i++) {
		delay(400);
		o20.digitalWrite(i, HIGH);
	}
	io24.digitalWrite(LEDDRZ1, HIGH);
	io24.digitalWrite(LEDSUFL, HIGH);
	io24.digitalWrite(LEDSUFJ, HIGH);

	digitalWrite(5, LOW);
	
	return;

	if (Serial.available() > 0) {
		uint8_t inc = Serial.read();
		if (inc == 'a') {
			Serial.print(inc, DEC);
			Serial.print(" ");
			printW(t, w, true);	
		}

		if (inc == 'u') {
			++passcnt;
			test(passcnt);
		} else if (inc == 'd') {
			--passcnt;
			test(passcnt);
		}


	}
	#endif
	w.read();
	t = millis();
	swSufit.rotate();
	if (!change(30*60, 5*60)) {
		delay(100);
		return;
	}
#ifdef DBG
	printW(t, w);
#endif	
	swJadalnia.zapal(w);
	swSufit.zapal(w, swLED);
	swLED.zapal(w, swSufit.czyZapalone());
	swPod.zapal(w.czyWieczor(), swSufit.czyZapalone(), swJadalnia.czyZapalone(), swLED.czyZapalonySufit());
	
	delay(100 - (millis() - t));


}
