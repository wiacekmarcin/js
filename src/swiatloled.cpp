#include "swiatloled.h"
#include "main.h"

#ifndef NEW_BOARD
#include <PCF8574.h>
extern PCF8574 expLedy;
#else
#include "io.h"
#endif

void SwiatloLED::init()
{
	m_sufit1 = false;
	m_sufit2 = false;
	m_drzwi1 = false;
	m_drzwi2 = false;
#ifndef NEW_BOARD
	expLedy.pinMode(ALL, OUTPUT, lo(false));
	expLedy.pinMode(SUFIT1, OUTPUT, lo(false));
	expLedy.pinMode(SUFIT2, OUTPUT, lo(false));
	expLedy.pinMode(DRZWI1, OUTPUT, lo(false));
	expLedy.pinMode(DRZWI2, OUTPUT, lo(false));
#endif // !NEW_BOARD	
	
}

void SwiatloLED::ustaw_przekaz() {
#ifndef NEW_BOARD	
	expLedy.digitalWrite(SUFIT1, lo(m_sufit1)); //ustawiane sygnałem LOW
	expLedy.digitalWrite(SUFIT2, lo(m_sufit2));
	expLedy.digitalWrite(DRZWI1, lo(m_drzwi1));
	expLedy.digitalWrite(DRZWI2, lo(m_drzwi2));
	expLedy.digitalWrite(ALL, lo(m_sufit1 || m_sufit2 || m_drzwi1 || m_drzwi2));
#else
	zapalLedSufitLod(m_sufit1);
	zapalLedSufitJad(m_sufit2);
	zapalLedDrzwi1(m_drzwi1);
	zapalLedDrzwi2(m_drzwi2);
	zapalLEDZasilacz(m_sufit1 || m_sufit2 || m_drzwi1 || m_drzwi2);
#endif

}

void SwiatloLED::zapalSufit1(bool on) {
	 if (m_sufit1 != on) {
	   m_sufit1 = on;
	   ustaw_przekaz();
	 }
  }

void SwiatloLED::zapalSufit2(bool on) {
 	if (m_sufit2 != on) {
   		m_sufit2 = on;
   		ustaw_przekaz();
 	}
}

void SwiatloLED::zapalDrzwi1(bool on) {
	if (m_drzwi1 != on) {
   		m_drzwi1 = on;
   		ustaw_przekaz();
 	}
}

void SwiatloLED::zapalDrzwi2(bool on) {
	if (m_drzwi2 != on) {
   		m_drzwi2 = on;
   		ustaw_przekaz();
 	}
}

bool SwiatloLED::czyZapalone() const {
	return  m_sufit1 || m_sufit2 || m_drzwi1 || m_drzwi2;
}

bool SwiatloLED::czyZapalonySufit() const {
	return  m_sufit1 || m_sufit2;
}

bool SwiatloLED::czyZapalonySufit1() const {
	return  m_sufit1;
}

bool SwiatloLED::czyZapalonySufit2() const {
	return  m_sufit2;
}


void SwiatloLED::zapal(const Wejscia & w, bool s)
{
	//rzeczy zwiazane z ledami od sufitu przeniesione do swiatlosufit

	if (s) {
		zapalDrzwi1(false);
		zapalDrzwi2(false);
		return;
	}

	if (! w.czyDrzwiOtwarte()) {
		zapalDrzwi1(false);
		zapalDrzwi2(false);
		return;
	}

	if (w.czyRuchDrzwi(czasSwiecenieLED)) {
		uint8_t ch = (w.czyNoc() << 1) | w.czyWieczor();
		switch(ch) {
			default:
			case 0:
				zapalDrzwi1(true);
				zapalDrzwi2(true);
				break;
			case 1:
				zapalDrzwi1(true);
				zapalDrzwi2(false);
				break;
			case 2:
			case 3:
				zapalDrzwi1(false);
				zapalDrzwi2(true);
				break;
		}
	} else {
		zapalDrzwi1(false);
		zapalDrzwi2(false);
	}

}
