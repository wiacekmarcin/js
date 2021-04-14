#include "wejscia.h"
#include "main.h"

#ifndef NEW_BOARD
#include <PCF8574.h>
extern PCF8574 expWejscia;
extern PCF8574 expLedy;
#else
#include "io.h"
#endif

void Wejscia::init() {
#ifndef NEW_BOARD
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
#endif
};

#define LI(d, p) (((~(d))&(1<<(p)))>>(p))
#define HI(d, p) (((d)&(1<<(p)))>>(p))
void Wejscia::read() {
#ifdef DBG
	static unsigned int num = 0;
	++num;

	Serial.print(num);
	Serial.print(". ");
#endif
#ifndef NEW_BOARD
	auto d1 = expWejscia.digitalReadAll();
	auto d2 = expLedy.digitalReadAll();

#ifdef DBG
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
#endif

	kl_jad_up = li(d1.p0);
	kl_jad_down = li(d1.p1);
	kl_kuch_b_up = li(d1.p2);
	kl_kuch_b_down = li(d1.p3);
	kl_kuch_a_up = li(d1.p4);
	kl_kuch_a_down = li(d1.p5);
	noc = hi(d1.p6);
	wieczor = hi(d1.p7);
	drzwi_otw = hi(d2.p5);
	ruch_kuch = hi(d2.p6);
	ruch_drzwi = hi(d2.p7);

#else
	auto d = readWejscia();
#ifdef DBG
	Serial.println(d, BIN);
#endif	
	kl_jad_up = LI(d, JAD2);
	kl_jad_down = LI(d, JAD1);
	kl_kuch_b_up = LI(d, KUCHB2);
	kl_kuch_b_down = LI(d, KUCHB1);
	kl_kuch_a_up = LI(d, KUCHA2);
	kl_kuch_a_down = LI(d, KUCHA1);
	noc = HI(d, NOC);
	wieczor = HI(d, WIECZOR);
	//taryfa2 = HI(d, TARYF2);
	//zas_awar = HI(d, ZAS_AWAR);
	ruch_kuch = HI(d, RUCH1);
	ruch_drzwi = HI(d, RUCH2);

#endif
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

bool Wejscia::czyRuchKuchnia(unsigned long timeinms) const {
  return ruch_kuch.getVal() || ruch_kuch.czasOdZmiany()  < timeinms;
}

bool Wejscia::czyRuchDrzwi(unsigned long timeinms) const {
  return ruch_drzwi.getVal() || ruch_drzwi.czasOdZmiany() < timeinms;
}

bool Wejscia::czyklKuchUp() const {
  return kl_kuch_a_up.getVal() || kl_kuch_b_up.getVal();
}

bool Wejscia::czyklKuchDown() const {
  return kl_kuch_a_down.getVal() || kl_kuch_b_down.getVal();
}

bool Wejscia::czyklJadUp() const {
  return kl_jad_up.getVal();
}

bool Wejscia::czyklJadDown() const {
  return kl_jad_down.getVal();
}

bool Wejscia::czyklKuch() const {
	return kl_kuch_a_up.getVal() || kl_kuch_b_up.getVal() || kl_kuch_a_down.getVal() || kl_kuch_b_down.getVal();
}

bool Wejscia::czyklJadalnia() const {
	return kl_jad_up.getVal() || kl_jad_down.getVal();
}


bool Wejscia::czyklKuchAUp() const { 
	return kl_kuch_a_up.getVal(); 
}

bool Wejscia::czyklKuchBUp() const { 
	return kl_kuch_b_up.getVal(); 
}

bool Wejscia::czyklKuchADown() const { 
	return kl_kuch_a_down.getVal(); 
}

bool Wejscia::czyklKuchBDown() const { 
	return kl_kuch_b_down.getVal(); 
}

bool Wejscia::czyklKuchDouble() const {
	return (kl_kuch_a_down.getVal() && kl_kuch_a_up.getVal()) || (kl_kuch_b_down.getVal() && kl_kuch_b_up.getVal());
}

void Wejscia::setRuch()
{

}