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

void SwiatloSufit::updown(bool up) {
	uint8_t lid = 0;
  	for (uint8_t id = 0; id < nrPodzial; ++id) {
	  	lid = (id + rotationId) % nrPodzial;
		if (led[lid] != up) {
			led[lid] = up;
			break;
		}
	}

	for (uint8_t id = 0; id < maxLed - nrPodzial; ++id) {
		lid = (id + rotationId) % (maxLed - nrPodzial) + nrPodzial;
		if (led[lid] != up) {
			led[lid] = up;
			break;
		}
	}
}

void SwiatloSufit::up() {
  	updown(true);
	level = level < maxLevel ? level + 1 : level;
	if (level == maxLevel)
		setLevel(level);
  	setPrzekaz();
}

void SwiatloSufit::down() {
  	updown(false);
	level = level > 0 ? level - 1 : 0;
	if (level == 0)
		setLevel(level);
	setPrzekaz();
}

void  SwiatloSufit::off() {
	setLevel(0);
	setPrzekaz();
}

void  SwiatloSufit::on() {
	setLevel(4);
	setPrzekaz();
}

bool SwiatloSufit::czyZapalone() const {
  	for (uint8_t id = 0 ; id < maxLed; ++id)
		if (led[id])
	  		return true;
  	return false;
}

bool SwiatloSufit::czyWszystkie() const {
	for (uint8_t id = 0 ; id < maxLed; ++id)
		if (!led[id])
		  	return false;
  	return false;
}

void SwiatloSufit::rotate() {
	rotationId = (rotationId + 1) % 4;
	if (level == 0 || level == maxLevel)
		return;

	if (!rotationinProgress && (millis() - timeRotate > czasRotacji)) {
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
		setPrzekaz(true, false);
		rotationinProgress = true;
	} else if (rotationinProgress && (millis() - timeRotate > czasOffsetu)) {
		rotationinProgress = false;
		setPrzekaz(false, true);
	}

}

void SwiatloSufit::set(uint8_t pin, bool on) {
  	if (pin >= 9)
    	return;

  	uint8_t p = SwiatloSufit::mapPins[pin];
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
	    	led[id] = false;
	    }
		updown(true);
	    break;

	case 2:
		for (uint8_t id = 0; id < maxLed; ++id) {
	    	led[id] = false;
	    }
		updown(true);
		updown(true);
	    break;

	case 3:
		for (uint8_t id = 0; id < maxLed; ++id) {
	    	led[id] = false;
	    }
		updown(true);
		updown(true);
		updown(true);
		break;

	case 4:
		for (uint8_t id = 0; id < maxLed; ++id) {
			led[id] = true;
		}
		break;
  	}
}

void SwiatloSufit::zapal(const Wejscia & w, SwiatloLED & led, bool jadalnia) {
	uint8_t mask = 0x00;
	mask = (mask << 1 ) | w.czyNoc();
	mask = (mask << 1 ) | (led.czyZapalonySufit() || jadalnia);
	mask = (mask << 1 ) | czyZapalone();
	mask = (mask << 1 ) | w.czyklKuchBUp(); 
	mask = (mask << 1 ) | w.czyklKuchBDown();
	mask = (mask << 1 ) | w.czyklKuchAUp();
	mask = (mask << 1 ) | w.czyklKuchADown();

	constexpr uint8_t NOC 		= 0x40;
	constexpr uint8_t ZAPLED 	= 0x20;
	constexpr uint8_t ZAPSUF 	= 0x10;

	constexpr uint8_t KLBUP 	= 0x08;
	constexpr uint8_t KLBDN 	= 0x04;
	constexpr uint8_t KLAUP 	= 0x02;
	constexpr uint8_t KLADN 	= 0x01;

	if ((mask & 0x0f) == 0x00) { //nie nacisnieto zadnego klawisza 
		return ;
	}
		
	else if (millis() - timeChange < czasReakcji) { //zbyt wczesna reakcja
		return;
	}
	
	timeChange = millis();

	switch(mask) {
		default:
			break;
		//noc
		case NOC | KLBUP:
		case NOC | KLBDN:
		case NOC | KLAUP:
		case NOC | KLADN:
			led.zapalSufit(true);
			break;
		
		// noc i zapalone ledy
		case NOC | ZAPLED | KLBUP:
		case NOC | ZAPLED | KLAUP:
			led.zapalSufit(false);
			up();
			break;
		
		case NOC | ZAPLED | KLBDN:
		case NOC | ZAPLED | KLADN:
			led.zapalSufit(false);
			break;

		
		//dwa nacisniete klawisze swiatlo wylaczone
		case NOC | KLBUP | KLBDN:
		case NOC | KLAUP | KLADN:
		case KLBUP | KLBDN:
		case KLAUP | KLADN:
			on();
			break;

		//dwa nacisniete klawisze swiatlo wlaczone
		case NOC | ZAPSUF | KLBUP | KLBDN :
		case NOC | ZAPSUF | KLAUP | KLADN:
		case ZAPSUF | KLBUP | KLBDN:
		case ZAPSUF | KLAUP | KLADN:
			off();
			break;

		//nie zapalone swiatlo
		case KLBUP:
		case KLBDN:
		case KLAUP:
		case KLADN:
		case ZAPSUF | KLBUP:
		case ZAPSUF | KLAUP:
			up();
			break;

		case ZAPSUF | KLBDN:
		case ZAPSUF | KLADN:
			down();
			break;

	}
}

