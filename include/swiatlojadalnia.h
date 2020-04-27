#ifndef _MW_JADALNIA_H
#define _MW_JADALNIA_H
#include <Arduino.h>

#include "wejscia.h"

class SwiatloJadalnia
{


public:
  	SwiatloJadalnia() :timeChange(0), timeRotate(0), rotationinProgress(false)
  	{ }

  	void init();

  	void rotate();

	void up();

  	void down();

	void off();

  	bool czyZapalone() const;

	void zapal(const Wejscia & w);


protected:
  	void setPrzekaz(bool on = true, bool off = true);


private:
  	static constexpr uint8_t maxSw = 3;
  	bool sw[maxSw] = { false, false, false };
  	static constexpr uint8_t mapPins[3] = { 1,  0,  4 };
	static constexpr unsigned int czasReakcji = 500;
	unsigned long timeChange;
	static constexpr unsigned int czasRotacji = 15000;
	unsigned long timeRotate;
	bool rotationinProgress;
};

#endif
