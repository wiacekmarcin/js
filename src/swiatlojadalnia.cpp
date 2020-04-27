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
#if 0
  	bool tmp = sw[0];
  	sw[0] = sw[1];
  	sw[1] = sw[2];
  	sw[2] = tmp;
  	setPrzekaz();
#endif
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

bool SwiatloJadalnia::czyZapalone() const {
	for (uint8_t id = 0 ; id < maxSw; ++id)
  		if (sw[id])
			return true;
	return false;
}

void SwiatloJadalnia::setPrzekaz() {
  	for (uint8_t id = 0 ; id < maxSw; ++id) {
		expPozostale.digitalWrite(mapPins[id], sw[id]);
  	}
}

void SwiatloJadalnia::zapal(const Wejscia & w)
{

}
