#include "wejscia.h"
#include "main.h"

#ifndef NEW_BOARD
#include <PCF8574.h>
extern PCF8574 expWejscia;
extern PCF8574 expLedy;
#else
#include "io.h"
#include <LiquidCrystal_I2C.h>
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



void Wejscia::read(bool printlcd, LiquidCrystal_I2C * lcd) {
#ifdef DBG
	static unsigned int num = 0;
	++num;


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
	//
	//d = d & 0xff1f;
	if (printlcd) {
		lcd->setCursor(0,1);
		lcd->print(((d >> 1 ) & 0x01) ? '1' : '0');
		lcd->print(' ');
		lcd->print(((d >> 2 ) & 0x01) ? '1' : '0');
		lcd->print(' ');
		lcd->print(((d >> 3 ) & 0x01) ? '1' : '0');
		lcd->print(' ');
		lcd->print(((d >> 4 ) & 0x01) ? '1' : '0');
	}
#ifdef DBG
	static uint16_t prev = 0x00;
	if (prev != d) {
		prev = d;
		Serial.print(num);
		Serial.print(". ");
		Serial.println(d, BIN);
		//Serial.print(((d >> KONTAKT ) & 0x01) ? "KON "  : "--- ");
		Serial.print(((d >> ZAS_AWAR ) & 0x01) ? "ZAW " : "--- ");
		Serial.print(((d >> TARYF2 ) & 0x01) ? " TAR " : "--- ");
		Serial.print(((d >> WIECZOR ) & 0x01) ? "WIE " : "--- ");
		Serial.print(((d >> NOC ) & 0x01) ? "NOC " : "--- ");
		//Serial.print(((d >> JAD2 ) & 0x01) ? "JA2 " : "--- ");
		//Serial.print(((d >> JAD1 ) & 0x01) ? "JA1 " : "--- ");
		//Serial.print(((d >> KUCHB2 ) & 0x01) ? "KB2 " : "--- ");
		//Serial.print(((d >> KUCHB1 ) & 0x01) ? "KB1 " : "--- ");
		//Serial.print(((d >> KUCHA2 ) & 0x01) ? "KA2 " : "--- ");
		//Serial.print(((d >> KUCHA1 ) & 0x01) ? "KA1 " : "--- ");
		//Serial.print(((d >> RUCH1 ) & 0x01) ? "RU1 " : "--- ");
		//Serial.println(((d >> RUCH2 ) & 0x01) ? "RU2" : "---");
		Serial.println(" ");
	}

#ifdef DBG
/*
	Serial.println("|KONTAKT,ZAS_AWA, TARYF2,WIECZOR,    NOC, JADAL2, JADAL1, KUCHB2, KUCHB1, KUCHA2, KUCHA1,  RUCH1, RUCH2");
	Serial.println("|  L    |    H  |   H   |    H  |    H  |   L   |   L   |    L  |   L   |   L   |   L   |   H   |    H ");
	  Serial.print("|      ");Serial.print((d >> KONTAKT ) & 0x01, DEC);
	  Serial.print("|      ");Serial.print((d >> ZAS_AWAR ) & 0x01, DEC);
	  Serial.print("|      ");Serial.print((d >> TARYF2 ) & 0x01, DEC);
	  Serial.print("|      ");Serial.print((d >> WIECZOR ) & 0x01, DEC);
	  Serial.print("|      ");Serial.print((d >> NOC ) & 0x01, DEC);
	  Serial.print("|      ");Serial.print((d >> JAD2 ) & 0x01, DEC);
	  Serial.print("|      ");Serial.print((d >> JAD1 ) & 0x01, DEC);
	  Serial.print("|      ");Serial.print((d >> KUCHB2 ) & 0x01, DEC);
	  Serial.print("|      ");Serial.print((d >> KUCHB1 ) & 0x01, DEC);
	  Serial.print("|      ");Serial.print((d >> KUCHA2 ) & 0x01, DEC);
	  Serial.print("|      ");Serial.print((d >> KUCHA1 ) & 0x01, DEC);
	  Serial.print("|      ");Serial.print((d >> RUCH1 ) & 0x01, DEC);
	  Serial.print("|      ");Serial.println((d >> RUCH2 ) & 0x01, DEC);
*/
#endif


#endif	
/*
	static int pos = -1;
	if (LI(d, JAD2)) {
		digitalWrite(ZASLED, LOW);
		digitalWrite(ZAWAPRZ, LOW);
		Serial.println("ZASLED LOW");
		io24.digitalWrite(LEDDRZ1, LOW);
		io24.digitalWrite(LEDDRZ2, HIGH);
		io24.digitalWrite(LEDSUFL, LOW);
		io24.digitalWrite(LEDSUFJ, HIGH);
	}

	if (LI(d, JAD1)) {
		digitalWrite(ZASLED, HIGH);
		digitalWrite(ZAWAPRZ, HIGH);
		Serial.println("ZASLED HIGH");
		io24.digitalWrite(LEDDRZ1, LOW);
		io24.digitalWrite(LEDDRZ2, HIGH);
		io24.digitalWrite(LEDSUFL, LOW);
		io24.digitalWrite(LEDSUFJ, HIGH);
	}
*/
	

	kl_jad_up = LI(d, JAD2);
	kl_jad_down = LI(d, JAD1);
	kl_kuch_b_up = LI(d, KUCHB2);
	kl_kuch_b_down = LI(d, KUCHB1);
	kl_kuch_a_up = LI(d, KUCHA2);
	kl_kuch_a_down = LI(d, KUCHA1);
	noc = LI(d, NOC);
	wieczor = LI(d, WIECZOR);
	taryfa2 = LI(d, TARYF2);
	zas_awar = LI(d, ZAS_AWAR);
	ruch_kuch = HI(d, RUCH1);
	ruch_drzwi = HI(d, RUCH2);
	drzwi_otw = HI(d, KONTAKT);
	
#endif
}


bool Wejscia::czyWieczor() const {
  return wieczor;
}

bool Wejscia::czyDrzwiOtwarte() const {
  return drzwi_otw;
}

bool Wejscia::czyZasilanieAwaryjne() const {
	return zas_awar;
}

bool Wejscia::czyZmianaZasAwaryjne() const {
	return zas_awar && zas_awar.czyZmiana();
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