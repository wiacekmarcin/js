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
	swNum = 0;
}

void SwiatloJadalnia::rotate() {
	/*
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
	*/
}

void SwiatloJadalnia::up() {
	//for (uint8_t id = 0 ; id < maxSw; ++id) {
  	//	if (!sw[id]) {
	//		sw[id] = true;
	//		setPrzekaz();
	//return;
  	//	}
	//}
	if (swNum < 8) {
		++swNum;
		setPrzekaz2();
	}
	
}

void SwiatloJadalnia::down() {
	//for (uint8_t id = 0 ; id < maxSw; ++id) {
  	//	if (sw[id]) {
	//		sw[id] = false;
	//		setPrzekaz();
	//		//return;
  	//	}
	//}
	if (swNum > 0) {
		--swNum;
		setPrzekaz2();
	}
}

void SwiatloJadalnia::off() {
	//for (uint8_t id = 0 ; id < maxSw; ++id) {
 	//	sw[id] = false;
	//}
	//setPrzekaz();

	swNum = 0;
	setPrzekaz2();
}

void SwiatloJadalnia::on(uint8_t num) 
{
	if (num < 8) {
		swNum = num;
		setPrzekaz2();
	}
}

bool SwiatloJadalnia::czyZapalone() const {
	//for (uint8_t id = 0 ; id < maxSw; ++id)
  	//	if (sw[id])
	//		return true;
	//return false;
	return swNum > 0;
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

void SwiatloJadalnia::setPrzekaz2()
{
	zapalJadalnia(1, swNum & 0x01);
	zapalJadalnia(2, swNum & 0x02);
	zapalJadalnia(3, swNum & 0x04);
}

void SwiatloJadalnia::zapal(const Wejscia & w)
{

	bool klup = w.czyklJadUp();
	bool kldown = w.czyklJadDown();
	bool czyWieczor = w.czyWieczor();
	bool czyNoc = w.czyNoc();

	if (w.czyZmianaZasAwaryjne()) {
		off();
		return;
	}

	if (w.czyZasilanieAwaryjne()) {
		return;
	}


	if (!klup && !kldown)
		return;
	else {
		if (millis() - timeChange < czasReakcji) {
			return;
		}
	}

	timeChange = millis();
	if (!czyZapalone() && (klup || kldown)) {
		on(czyNoc ? LASER1 : (czyWieczor ? LASER4 : LASER7));
 	} else if (czyZapalone() && klup && kldown) {
		off();
	} else if (klup) {
		up();
	} else if (kldown) {
		down();
	}
}
