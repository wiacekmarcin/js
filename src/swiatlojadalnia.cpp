#include "swiatlojadalnia.h"


#include "main.h"

#ifndef NEW_BOARD	
#include <PCF8574.h>
extern PCF8574 expPozostale;
#else
#include "io.h"
#endif

void SwiatloJadalnia::init() {
#ifndef NEW_BOARD	
	expPozostale.pinMode(0, OUTPUT, ho(false));
	expPozostale.pinMode(1, OUTPUT, ho(false));
	expPozostale.pinMode(4, OUTPUT, ho(false));
#endif	
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

void SwiatloJadalnia::setPrzekaz(bool on, bool off) {
#ifndef NEW_BOARD		
  	for (uint8_t id = 0 ; id < maxSw; ++id) {
		if (on && sw[id])
			expPozostale.digitalWrite(mapPins[id], ho(true));
		else if (off && !sw[id])
			expPozostale.digitalWrite(mapPins[id], ho(false));
  	}
#else	  
	for (uint8_t id = 0 ; id < maxSw; ++id) {
		if (on && sw[id])
			zapalJadalnia(id + 1, true);
		else if (off && !sw[id])
			zapalJadalnia(id + 1, false);
  	}
#endif
}

void SwiatloJadalnia::zapal(const Wejscia & w)
{

	bool klup = w.czyklJadUp();
	bool kldown = w.czyklJadDown();

	if (!klup && !kldown)
		return;
	else {
		if (millis() - timeChange < czasReakcji) {
			return;
		}
	}

	timeChange = millis();
	if (!czyZapalone() && (klup || kldown)) {
		up();
 	} else if (czyZapalone() && klup && kldown) {
		off();
	} else if (klup) {
		up();
	} else if (kldown) {
		down();
	}
}
