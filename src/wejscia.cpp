#include "wejscia.h"

#include <PCF8574.h>

extern PCF8574 expWejscia;
extern PCF8574 expLedy;


void Wejscia::init() {

	expWejscia.pinMode(0, INPUT_PULLUP); //jadalnia up
	expWejscia.pinMode(1, INPUT_PULLUP); //jadalnia down
	expWejscia.pinMode(2, INPUT_PULLUP); //kuchnia B up
	expWejscia.pinMode(3, INPUT_PULLUP); //kuchnia B down
	expWejscia.pinMode(4, INPUT_PULLUP); //kuchnia A up
	expWejscia.pinMode(5, INPUT_PULLUP); //kuchnia A down
	expWejscia.pinMode(6, INPUT); //noc?
	expWejscia.pinMode(7, INPUT); //wieczor
	expWejscia.begin();

	expLedy.pinMode(5, INPUT_PULLUP); //kontaktron
	expLedy.pinMode(6, INPUT); //ruch kuchnia
	expLedy.pinMode(7, INPUT); //ruch drzwi

};

void Wejscia::readTest() {
	static unsigned int num = 0;
	++num;
	Serial.print(num);
	Serial.print(". ");
	auto d1 = expWejscia.digitalReadAll();
	auto d2 = expLedy.digitalReadAll();
	Serial.print(d1.p7, 2);
	Serial.print(d1.p6, 2);
	Serial.print(d1.p5, 2);
	Serial.print(d1.p4, 2);
	Serial.print(d1.p3, 2);
	Serial.print(d1.p2, 2);
	Serial.print(d1.p1, 2);
	Serial.print(d1.p0, 2);
	Serial.print("|");
	Serial.print(d2.p7, 2);
	Serial.print(d2.p6, 2);
	Serial.println(d2.p5, 2);

	kl_jad_up = d1.p0;
	kl_jad_down = d1.p1;
	kl_kuch_b_up = d1.p2;
	kl_kuch_b_down = d1.p3;
	kl_kuch_a_up = d1.p4;
	kl_kuch_a_down = d1.p5;
	noc = d1.p6;
	wieczor = d1.p7;
	drzwi_otw = d2.p5;
	ruch_kuch = d2.p6;
	ruch_drzwi = d2.p7;
}


bool Wejscia::czyWieczor() const {
  return wieczor;
}

bool Wejscia::czyDrzwiOtwarte() const {
  return drzwi_otw;
}

bool Wejscia::czyNoc() const {
  return noc;
}

bool Wejscia::czyRuchKuchnia(unsigned long timeins) const {
  return ruch_kuch.czasOdZmiany() < timeins;
}

bool Wejscia::czyRuchDrzwi(unsigned long timeins) const {
  return ruch_drzwi.czasOdZmiany() < timeins;
}

bool Wejscia::czyklKuchUp() const {
  return kl_kuch_a_up.getVal() || kl_kuch_b_up.getVal();
}

bool Wejscia::czyklKuchDown() const {
  return kl_kuch_a_down.getVal() || kl_kuch_b_down.getVal();
}

bool Wejscia::czyklJadUp() const {
  return kl_jad_up;
}

bool Wejscia::czyklJadDown() const {
  return kl_jad_down;
}
