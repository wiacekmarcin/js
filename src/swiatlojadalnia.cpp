#include "swiatlojadalnia.h"

#include <PCF8574.h>
#include "main.h"
extern PCF8574 expPozostale;

void SwiatloJadalnia::init() {
	expPozostale.pinMode(0, OUTPUT, ho(false));
	expPozostale.pinMode(1, OUTPUT, ho(false));
	expPozostale.pinMode(4, OUTPUT, ho(false));
}

void SwiatloJadalnia::rotate() {
	if (!rotationinProgress && (millis() - timeRotate < czasRotacji))
		return;

	if (rotationinProgress && (millis() - timeRotate < 500)) {
		setPrzekaz(false, true);
		rotationinProgress = false;
		return;
	}

  	bool tmp = sw[0];
  	sw[0] = sw[1];
  	sw[1] = sw[2];
  	sw[2] = tmp;
  	setPrzekaz(true, false);
	rotationinProgress = true;
}

void SwiatloJadalnia::up() {
	for (uint8_t id = 0 ; id < maxSw; ++id) {
  		if (!sw[id]) {
			sw[id] = true;
			setPrzekaz();
			return;
  		}
	}
}

void SwiatloJadalnia::down() {
	for (uint8_t id = 0 ; id < maxSw; ++id) {
  		if (sw[id]) {
			sw[id] = false;
			setPrzekaz();
			return;
  		}
	}
}

void SwiatloJadalnia::off() {
	for (uint8_t id = 0 ; id < maxSw; ++id) {
 		sw[id] = false;
	}
	setPrzekaz();
}

bool SwiatloJadalnia::czyZapalone() const {
	for (uint8_t id = 0 ; id < maxSw; ++id)
  		if (sw[id])
			return true;
	return false;
}

void SwiatloJadalnia::setPrzekaz(bool on = true, bool off = true) {
  	for (uint8_t id = 0 ; id < maxSw; ++id) {
		if (on && sw[id])
			expPozostale.digitalWrite(id, ho(true));
		else if (off && !sw[id])
			expPozostale.digitalWrite(id, ho(false));
  	}
}

void SwiatloJadalnia::zapal(const Wejscia & w)
{
#ifdef DBG
	Serial.print(millis(), DEC);
	Serial.println(" Zapal 1");
#endif
	bool klup = w.czyklJadUp();
	bool kldown = w.czyklJadDown();
	if (!klup && !kldown)
		return;
	else {
#ifdef DBG
		Serial.print("Klawisz od jadalni wcisniety");
		Serial.print("ile ms temu ");
		Serial.println(millis() - timeChange);
#endif
		if (millis() - timeChange < czasReakcji)
			return;
	}
	timeChange = millis();
	if (!czyZapalone() && (klup || kldown)) {
#ifdef DBG
		Serial.print("up");
#endif
		up();
 	} else if (klup && kldown) {
#ifdef DBG
		Serial.print("off");
#endif
		off();
	}
	else if (klup) {
#ifdef DBG
		Serial.print("up");
#endif
		up();
	}
	else {
#ifdef DBG
		Serial.print("down");
#endif
		down();
	}
}
