#include "swiatlosufit.h"

#include <PCF8574.h>
#include "main.h"
extern PCF8574 expOczka;
extern PCF8574 expPozostale;

const uint8_t SwiatloSufit::mapPins[SwiatloSufit::maxLed] = { 5, 7, 0, 2, 8, 4, 6, 3, 1 };

void SwiatloSufit::init() {
	for (uint8_t p = 0; p < 8; ++p) {
		expOczka.pinMode(p, OUTPUT, ho(false));
	}
	expOczka.begin();
	expPozostale.pinMode(3, OUTPUT, ho(false));
}

void SwiatloSufit::up() {
  setLevel(level + 1);
  setPrzekaz();
}

void SwiatloSufit::down() {
  setLevel(level - 1);
  setPrzekaz();
}

void  SwiatloSufit::off() {
	setLevel(0);
}

bool SwiatloSufit::czyZapalone() const {
  for (uint8_t id = 0 ; id < maxLed; ++id)
	if (led[id])
	  return true;
  return false;
}

void SwiatloSufit::rotate() {
	//Serial.println("rotate");
	//Serial.println(millis() - timeRotate, DEC);
	rotationId = (rotationId + 1) % 4;
	if (level == 0 || level == 4)
		return;

	if (!rotationinProgress && (millis() - timeRotate > czasRotacji)) {
		//Serial.print("rotate 2 progress=");
		//Serial.print(" timeRotate =");
		//Serial.println(millis() - timeRotate);
		timeRotate = millis();

		bool tmp;
		tmp = led[0];
		led[0] = led[1];
		led[1] = led[2];
		led[2] = led[3];
		led[3] = tmp;

		tmp = led[4];
		led[4] = led[5];
		led[5] = led[6];
		led[6] = led[7];
		led[7] = led[8];
		led[8] = tmp;
		setPrzekaz(true, false  );
		rotationinProgress = true;
	} else if (rotationinProgress && (millis() - timeRotate > czasOffsetu)) {
		//Serial.print("rotate 3 progress=");
		//Serial.print(rotationinProgress);
		//Serial.print(" timeRotate =");
		//Serial.println(millis() - timeRotate);

		rotationinProgress = false;
		setPrzekaz(false, true);
	}

}

void SwiatloSufit::set(uint8_t pin, bool on) {
  	if (pin >= 9)
    	return;

  	uint8_t p = SwiatloSufit::mapPins[pin];
#ifdef DBG
  	Serial.print("Lampa ");
  	Serial.print(p);
  	Serial.print(" setting on");
  	Serial.println(on ? "true": "false");
#endif
  	if (p < 8) {
    	expOczka.digitalWrite( p, ho(on)); //piny są odwrócone najpierw P3, na koniec P0
  	} else {
    	expPozostale.digitalWrite( 3, ho(on));
  	}
}

void SwiatloSufit::setPrzekaz(bool on, bool off) {
  	for (uint8_t id = 0; id < maxLed; ++id) {
		if (on && led[id])
			set(id, led[id]);
		else if (off && !led[id])
			set(id, led[id]);
	}
}

void SwiatloSufit::setLevel(int8_t lev) {
	uint8_t cid = 0;
#ifdef DBG
  Serial.print("SetLevel ");
  Serial.println(level);
#endif
	if (lev > maxLevel)
		level = maxLevel;
	else if (lev < 0)
		level = 0;
	else
		level = lev;
	switch(level) {
	case 0 :
	default:
		for (uint8_t id = 0; id < maxLed; ++id) {
	    	led[id] = false;
	    }
	    break;

	case 1:
		for (uint8_t id = 0; id < maxLed; ++id) {
			cid = id + rotationId;
			cid = (cid < 4) ? (cid % 4) : (((cid -4 ) % 5) + 4);
			led[id] = cid == 0 || cid == 4 ? true : false;
		}
		break;

	case 2:
		for (uint8_t id = 0; id < maxLed; ++id) {
			cid = id + rotationId;
			cid = (cid < 4) ? (cid % 4) : (((cid -4 ) % 5) + 4);
			led[id] = cid == 0 || cid == 3 || cid == 4 || cid == 7 ? true : false;
		}
		break;

	case 3:
		for (uint8_t id = 0; id < maxLed; ++id) {
			cid = id + rotationId;
			cid = (cid < 4) ? (cid % 4) : (((cid -4 ) % 5) + 4);
			led[id] = cid == 1 || cid == 5 || cid == 9 ? false : true;
		}
		break;

	case 4:
		for (uint8_t id = 0; id < maxLed; ++id) {
			led[id] = true;
		}
		break;
  	}
}

void SwiatloSufit::zapal(const Wejscia & w, SwiatloLED & led, bool jadalnia) {
	//if (!czyRuchKuchnia)


	bool klup = w.czyklKuchUp();
	bool kldown = w.czyklKuchDown();
	bool czynoc = w.czyNoc();
#ifdef DBG
	Serial.print("millis()");
	Serial.print(" Zapal");
#endif
	if (!klup && !kldown)
		return;
	else {
		if (millis() - timeChange < czasReakcji)
			return;
	}
	timeChange = millis();

	if (!czyZapalone() && !led.czyZapalonySufit() && !jadalnia && (klup || kldown) && czynoc)
	{
#ifdef DBG
	Serial.println("Zapal ledy");
#endif
		led.zapalSufit1(true);
		led.zapalSufit2(true);
		return; //zapal ledy
	}

	if (!czyZapalone() && led.czyZapalonySufit() && (klup || kldown)) {
		if ((klup && kldown) || kldown) {
#ifdef DBG
			Serial.println("Zgas ledy");
#endif
			led.zapalSufit1(false);
			led.zapalSufit2(false);
			return; //wylacz ledy
		}

		if (klup) {
#ifdef DBG
			Serial.println("Zgas ledy i up");
#endif
			led.zapalSufit1(false);
			led.zapalSufit2(false);
			up();
			return;
		}
	}

	if (klup && kldown) {
#ifdef DBG
		Serial.println("off");
#endif
		off();
	}
	else if (klup) {
#ifdef DBG
		Serial.println("up");
#endif
		up();
	} else {
#ifdef DBG
		Serial.println("down");
#endif
		down();
	}
}
