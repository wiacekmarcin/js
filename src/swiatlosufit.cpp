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
	//Serial.println("rotate");
	//Serial.println(millis() - timeRotate, DEC);
	rotationId = (rotationId + 1) % 4;
	if (level == 0 || level == maxLevel)
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
		setPrzekaz(true, false);
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
	//if (!czyRuchKuchnia)


	bool klup = w.czyklKuchUp();
	bool kldown = w.czyklKuchDown();
	bool czynoc = w.czyNoc();
	bool kl = w.czyklKuch();
	//bool czywiecz = w.czyWieczor();
	bool swLed = led.czyZapalonySufit();
	bool swSuf = czyZapalone();
    bool dlkl = w.czyklKuchDouble();
	
	//nie nacisnieto zadnego klawisza
	if (!klup && !kldown)
		return;
	else if (millis() - timeChange < czasReakcji) //zbyt wczesna reakcja
		return;
	
	timeChange = millis();


	//podwojne nacisniecie swiatlo wylaczone
	if (dlkl && !swSuf) {
		on();
	} 
	
	//podwojne nacisniecie i wszystkie swiatlo zapalone
	else if (dlkl && czyWszystkie()) {
		off();
		led.zapalSufit(false);
	}

	//dowolne nacisniecie swiatlo wylaczone i jest noc
	else if (kl && !swLed && !swSuf && czynoc) {
		led.zapalSufit(true);
	}

	//dowolne nacisniecie swiatlo wylaczone i jest dzien
	else if (kl && !swLed && !swSuf && !czynoc) {
		up();
	}

	//nacisiniecie klawisza up jak jest noc i swieca ledy
	else if (klup && !swSuf && !swLed) {
		led.zapalSufit(false);
		up();
	}

	//nacisiniecie klawisza up 
	else if (klup) {
		up();
	}

	//nacisniecie klawisza down
	else if (kldown) {
		down();
	}
}
