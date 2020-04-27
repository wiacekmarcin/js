#ifndef _MW_JADALNIA_H
#define _MW_JADALNIA_H
#include <Arduino.h>

#include "wejscia.h"

class SwiatloJadalnia
{


public:
  	SwiatloJadalnia() : level(0)
  	{ }

  	void init();

  	void rotate();

	void up();

  	void down();

  	bool czyZapalone() const;

	void zapal(const Wejscia & w);

protected:
  	void setPrzekaz();


private:
  	uint8_t level;
  	static constexpr uint8_t maxSw = 3;
  	bool sw[maxSw] = { false, false, false };
  	static constexpr uint8_t mapPins[3] = { 1,  0,  4 };
};

#endif
