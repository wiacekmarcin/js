#include "swiatlosufit.h"
#include "main.h"

#ifndef NEW_BOARD
#include <PCF8574.h>
extern PCF8574 expOczka;
extern PCF8574 expPozostale;
#else
#include "io.h"
#endif
const uint8_t SwiatloSufit::mapPins[SwiatloSufit::maxLed] = { 5, 7, 0, 2, 8, 4, 6, 3, 1 };

void SwiatloSufit::init() {
#ifndef NEW_BOARD	
	for (uint8_t p = 0; p < 8; ++p) {
		expOczka.pinMode(p, OUTPUT, ho(false));
	}
	expOczka.begin();
	expPozostale.pinMode(3, OUTPUT, ho(false));
#endif	

	for (short i = 0; i < maxLed; i++) {
		tabela[i].on = false;
		tabela[i].time = 0L;
	}
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
	unsigned mls = millis();
	for (short i = 0; i < maxLed; i++) {
		tabela[i].time = mls + 150*i;
		tabela[i].on = false;
	}
	//setPrzekaz();
}

void  SwiatloSufit::on() {
	setLevel(4);
	//setPrzekaz();
	unsigned mls = millis();
	for (short i = 0; i < maxLed; i++) {
		tabela[i].time = mls + 150*i;
		tabela[i].on = true;
	}
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
#ifndef NEW_BOARD
  	uint8_t p = SwiatloSufit::mapPins[pin];
  	if (p < 8) {
    	expOczka.digitalWrite( p, ho(on)); //piny są odwrócone najpierw P3, na koniec P0
  	} else {
    	expPozostale.digitalWrite( 3, ho(on));
  	}
#else
	zapalKuchnia(pin, on);
#endif
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

bool SwiatloSufit::ZapalWieczor(uint8_t maska, SwiatloLED & led)
{

	switch(maska) {
		
		//klawisz up
		case KLBUP:
		case KLBUP | ZAPSUF:
		case KLAUP:
		case KLAUP | ZAPSUF:
		case KLBDN:
		case KLADN:
		 	if (level == maxLevel) {
			 	led.zapalSufit(maska & (KLBUP | ZAPSUF), maska & (KLAUP | ZAPSUF));
				off();
			} else {
				up();
			}
		 	return true;
		
		
		case KLBDN | ZAPSUF:
		case KLADN | ZAPSUF:
		 	down();
		 	return true;

		case KLADN | KLAUP:
		case KLBDN | KLBUP:
			on();
			return true;

		case KLADN | KLAUP | ZAPSUF:
		case KLBDN | KLBUP | ZAPSUF:
			off();
			return true;

		case KLAUP | ZAPLED1:
		case KLAUP | ZAPLED2:
		case KLBUP | ZAPLED1:
		case KLBUP | ZAPLED2:
			led.zapalSufit(true, true);
			return true;

		case KLBDN | ZAPLED1 | ZAPLED2:
			led.zapalSufit(false, true);
			return true;
		
		case KLADN | ZAPLED1 | ZAPLED2:
			led.zapalSufit(true, false);
			return true;

		case KLADN | KLAUP | ZAPLED1 | ZAPLED2:
		case KLBDN | KLBUP | ZAPLED1 | ZAPLED2:
			led.zapalSufit(false, false);
			return true;

		case KLBDN | ZAPLED2:
		case KLBDN | ZAPLED1:
		case KLADN | ZAPLED1:
		case KLADN | ZAPLED2:
			led.zapalSufit(false, false);
			return true;
		
		
		default:
			break;
	}
	return false;
}

bool SwiatloSufit::ZapalWieczoriNoc(uint8_t maska, SwiatloLED & led)
{

	switch(maska) {
		
		//klawisz up w nocy wieczorem zapla najpierw ledy
		case KLBUP:
		case KLBDN:
			led.zapalSufit(true, false);
			return true;

		case KLAUP:
		case KLADN:
		 	led.zapalSufit(false, true);
		 	return true;
		
		case KLBDN | KLBUP:
		case KLADN | KLAUP:
			led.zapalSufit(true, true);
			return true;

		case KLBDN | KLBUP | ZAPLED1 | ZAPLED2:
		case KLADN | KLAUP | ZAPLED1 | ZAPLED2:
			led.zapalSufit(false, false);
			return true;

		// drugie ledy mozna zalaczyc drugim klawiszem
		case KLBUP | ZAPLED2:
		case KLBDN | ZAPLED2:
		case KLADN | ZAPLED1:
		case KLAUP | ZAPLED1:
			led.zapalSufit(true, true);
			return true;

		case KLBDN | ZAPLED1:
			led.zapalSufit(false, false);
			return true;

		case KLADN | ZAPLED2:
			led.zapalSufit(false, false);
			return true;


		case KLBUP | ZAPLED1:
		case KLAUP | ZAPLED2:
		case KLBUP | ZAPLED1 | ZAPLED2:
		case KLAUP | ZAPLED2 | ZAPLED1:
			led.zapalSufit(false, false);
			up();
			return true;

		case KLBDN | ZAPLED1 | ZAPLED2:
			led.zapalSufit(false, true);
			return true;

		case KLADN | ZAPLED2 | ZAPLED1:
			led.zapalSufit(true, false);
			return true;

		case KLBDN | ZAPSUF:
		case KLADN | ZAPSUF:
		 	down();
			return true;

		case KLBUP | ZAPSUF:
		case KLAUP | ZAPSUF:
		 	up();
			return true;
			
		case KLADN | KLAUP | ZAPSUF:
		case KLBDN | KLBUP | ZAPSUF:
			off();
			return true;

			
		default:
			break;
	}
	return false;
}

bool SwiatloSufit::ZapalDzien(uint8_t maska, SwiatloLED & led)
{
	if ((maska & ZAPLED2) | (maska & ZAPLED1)) {
		led.zapalSufit(false, false); //jak juz jest dzien a swieca ledy zgas i zapal
		up(); //swiatlo
	}

	switch(maska) {
		
		//klawisz up
		case KLBUP:
		case KLBUP | ZAPSUF:
		case KLAUP:
		case KLAUP | ZAPSUF:
		 	up();
		 	return true;
		
		case KLBDN:
		case KLBDN | ZAPSUF:
		case KLADN:
		case KLADN | ZAPSUF:
		 	down();
		 	return true;

		case KLADN | KLAUP:
		case KLBDN | KLBUP:
			on();
			return true;

		case KLADN | KLAUP | ZAPSUF:
		case KLBDN | KLBUP | ZAPSUF:
			off();
			return true;

		default:
			break;
	}
	return false;
}

bool SwiatloSufit::ZapalNoc(uint8_t maska, SwiatloLED & led)
{
	return ZapalDzien(maska, led);
}


void SwiatloSufit::zapal(const Wejscia & w, SwiatloLED & led) {
	/**
	 * KUCHNIA
	 * 
	 *    X               X               X        |       X   
	 *                                             |
	 *      --- LED2 ----                           
	 *                                             L
	 *    X               X                X       E       X
	 *                                             D
	 *                                             1
	 *    * *                                        
	 *    ----------------------------------       |       X
	 * Jada  Kuchnia              Kuchnia B | *
	 * lnia  A                              |
	 *                                      | *
	 *                                      | * Właczniki salon
	 *                                        
	 * */

	bool czyNoc = w.czyNoc();
	bool czyWieczor = w.czyWieczor();

	uint8_t mask = 0x00;
	mask = (mask << 1 ) | led.czyZapalonySufit2();
	mask = (mask << 1 ) | led.czyZapalonySufit1();
	mask = (mask << 1 ) | czyZapalone();
	mask = (mask << 1 ) | w.czyklKuchBUp(); 
	mask = (mask << 1 ) | w.czyklKuchBDown();
	mask = (mask << 1 ) | w.czyklKuchAUp();
	mask = (mask << 1 ) | w.czyklKuchADown();





	if ((mask & 0x0f) == 0x00) { //nie nacisnieto zadnego klawisza 
		return ;
	}
		
	else if (millis() - timeChange < czasReakcji) { //zbyt wczesna reakcja
		return;
	}
	
	timeChange = millis();
	bool ret = true;

	if (czyNoc && czyWieczor) {
		ret = ZapalWieczoriNoc(mask, led);
	} else if (czyWieczor) {
		ret = ZapalWieczor(mask, led);
	} else if (czyNoc) {
		ret = ZapalNoc(mask, led);
	} else {
		ret = ZapalDzien(mask, led);
	}

	if (!ret) {
		Serial.println("Nie znaleziona akcja ");
		Serial.println("noc wie le2 le1 zap bup bdn aup adn");
		Serial.print(czyNoc ? "  1" : "  0");
		Serial.print(" ");
		Serial.print(czyWieczor ? "  1" : "  0");
		Serial.print(" ");
		Serial.print(mask & ZAPLED2 ? "  1" : "  0");
		Serial.print(" ");
		Serial.print(mask & ZAPLED1 ?  "  1" : "  0");
		Serial.print(" ");
		Serial.print(mask & ZAPSUF ? "  1" : "  0");
		Serial.print(" ");
		Serial.print(mask & KLBUP ? "  1" : "  0");
		Serial.print(" ");
		Serial.print(mask & KLBDN ? "  1" : "  0");
		Serial.print(" ");
		Serial.print(mask & KLAUP ? "  1" : "  0");
		Serial.print(" ");
		Serial.println(mask & KLADN ? "  1" : "  0");

	} else {
		Serial.println("OK");
	}
}

void SwiatloSufit::tiktok(unsigned long mls) 
{
	for (short i = 0; i < maxLed; i++) {
		if (tabela[i].time == 0 || tabela[i].time > mls)
			continue;
		tabela[i].time = 0; //znacznik wykonanej roboty
		zapalKuchnia(i, tabela[i].on);
	}
}
