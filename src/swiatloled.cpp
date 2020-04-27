#include "swiatloled.h"

#include <PCF8574.h>
#include "main.h"
extern PCF8574 expLedy;

void SwiatloLED::init()
{
	expLedy.pinMode(0, OUTPUT, lo(false));
	expLedy.pinMode(1, OUTPUT, lo(false));
	expLedy.pinMode(2, OUTPUT, lo(false));
	expLedy.pinMode(3, OUTPUT, lo(false));
	expLedy.pinMode(4, OUTPUT, lo(false));
}

void SwiatloLED::ustaw_przekaz() {
	expLedy.digitalWrite(1, lo(m_sufit1)); //ustawiane sygnałem LOW
	expLedy.digitalWrite(2, lo(m_sufit2));
	expLedy.digitalWrite(3, lo(m_drzwi1));
	expLedy.digitalWrite(4, lo(m_drzwi2));
	expLedy.digitalWrite(0, lo(m_sufit1 || m_sufit2 || m_drzwi1 || m_drzwi2));
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
