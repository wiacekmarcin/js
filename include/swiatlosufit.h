#ifndef _MW_SWIATLO_SUFIT_H
#define _MW_SWIATLO_SUFIT_H
#include <Arduino.h>
#include "wejscia.h"
#include "swiatloled.h"

class SwiatloSufit
{
public:
	SwiatloSufit() : level(0), timeChange(0), rotationinProgress(0)
    {}

	void init();

	void up();

	void down();

	void off();

	bool czyZapalone() const;

	void rotate();

	void zapal(const Wejscia & w, SwiatloLED & led, bool jadalnia);

protected:
	void set(uint8_t pin, bool on);

	void setPrzekaz(bool on = true, bool off = true);

	void setLevel(int8_t level);

private:
    static constexpr uint8_t maxLed = 9; //0  1  2  3  4  5  6  7  8

    //na listwie               2 7 1 6 8 4 9 3 | 5 10 11 12 | 13
    //wejscia na przekaznikach 8 7 6 5 4 3 2 1 | 4  3  2  1 |  1
    //wejscia na expanderach   7 6 5 4 3 2 1 0 | 3  2  1  0 |  4
    static const uint8_t mapPins[maxLed];

    uint8_t level;
    static constexpr uint8_t maxLevel = 4;
    bool led[maxLed] = { false, false, false, false, false, false, false, false, false};

	static constexpr unsigned int czasReakcji = 1000;
	unsigned long timeChange;
	static constexpr unsigned long czasRotacji = 900000;
	static constexpr unsigned int czasOffsetu = 250;
	unsigned long timeRotate;
	bool rotationinProgress;

public :








};
#endif
