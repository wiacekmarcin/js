#include "swiatlosufit.h"

#include <PCF8574.h>
#include "main.h"
extern PCF8574 expOczka;
extern PCF8574 expPozostale;

void SwiatloSufit::init() {
	for (uint8_t p = 0; p < 8; ++p) {
		expOczka.pinMode(p, OUTPUT, ho(false));
	}
	expOczka.begin();
	expPozostale.pinMode(3, OUTPUT, ho(false));
}

void SwiatloSufit::up() {
  if (level >= maxLevel)
	return;
  level += 1;
  setLevel();
  setPrzekaz();
}

void SwiatloSufit::down() {
  if (level == 0)
	return;
  level -= 1;
  setLevel();
  setPrzekaz();
}

bool SwiatloSufit::czyZapalone() const {
  for (uint8_t id = 0 ; id < maxLed; ++id)
	if (led[id])
	  return true;
  return false;
}

void SwiatloSufit::rotate() {
  if (level == 0 || level == 4)
	return;
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
  setPrzekaz();
}

void SwiatloSufit::set(uint8_t pin, bool on) {
  	if (pin >= 9)
    	return;

  	uint8_t p = mapPins[pin];
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

void SwiatloSufit::setPrzekaz() {
  	for (uint8_t id = 0; id < maxLed; ++id) {
		set(id, led[id]);
	}
}

void SwiatloSufit::setLevel() {
#ifdef DBG
  Serial.print("SetLevel ");
  Serial.println(level);
#endif
	switch(level) {
	case 0 :
	default:
		for (uint8_t id = 0; id < maxLed; ++id) {
	    	led[id] = false;
	    }
	    break;

	case 1:
		for (uint8_t id = 0; id < maxLed; ++id) {
			led[id] = id == 0 || id == 4 ? true : false;
		}
		break;

	case 2:
		for (uint8_t id = 0; id < maxLed; ++id) {
			led[id] = id == 0 || id == 3 || id == 4 || id == 7 ? true : false;
		}
		break;

	case 3:
		for (uint8_t id = 0; id < maxLed; ++id) {
			led[id] = id == 1 || id == 5 || id == 9 ? false : true;
		}
		break;

	case 4:
		for (uint8_t id = 0; id < maxLed; ++id) {
			led[id] = true;
		}
		break;
  	}
}

void SwiatloSufit::zapal(const Wejscia & w) {

}
