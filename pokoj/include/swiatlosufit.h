#ifndef MW_SWIATLO_SUFIT_H
#define MW_SWIATLO_SUFIT_H
#include <Arduino.h>
#include "wejscia.h"
#include "swiatloled.h"

class SwiatloSufit
{
public:
	SwiatloSufit() : level(0), timeChange(0), timeRotate(0), rotationinProgress(0), rotationId(0)
    {}

	void init();

	void up();

	void down();

	void off();

	void on();

	bool czyZapalone() const;

	bool czyWszystkie() const;

	void rotate();

	void zapal(const Wejscia & w, SwiatloLED & led);

	void tiktok(unsigned long mls);

protected:
	void updown(bool up);

	void set(uint8_t pin, bool on);

	void setPrzekaz(bool on = true, bool off = true);

	void setLevel(int8_t level);

	bool ZapalDzien(uint8_t maska, SwiatloLED & led);
	bool ZapalNoc(uint8_t maska, SwiatloLED & led);
	bool ZapalWieczor(uint8_t maska, SwiatloLED & led);
	bool ZapalWieczoriNoc(uint8_t maska, SwiatloLED & led);
	bool ZapalAwaryjnie(const Wejscia & w, SwiatloLED & led);
private:
    static constexpr uint8_t maxLed = 9; //0  1  2  3  4  5  6  7  8

    //na listwie               2 7 1 6 8 4 9 3 | 5 10 11 12 | 13
    //wejscia na przekaznikach 8 7 6 5 4 3 2 1 | 4  3  2  1 |  1
    //wejscia na expanderach   7 6 5 4 3 2 1 0 | 3  2  1  0 |  4
    static const uint8_t mapPins[maxLed];

    uint8_t level;
    static constexpr uint8_t maxLevel = 4;
    bool led[maxLed] = { false, false, false, false, false, false, false, false, false};

	static constexpr unsigned int czasReakcji = 500;
	unsigned long timeChange;
	static constexpr unsigned long czasRotacji = 900000;
	static constexpr unsigned int czasOffsetu = 400;
	unsigned long timeRotate;
	bool rotationinProgress;

	uint8_t rotationId;
	static constexpr uint8_t nrPodzial = 4;


	static constexpr uint8_t ZAPLED2 	= 0x40;
	static constexpr uint8_t ZAPLED1 	= 0x20;
	static constexpr uint8_t ZAPSUF 	= 0x10;

	static constexpr uint8_t KLBUP 	= 0x08;
	static constexpr uint8_t KLBDN 	= 0x04;
	static constexpr uint8_t KLAUP 	= 0x02;
	static constexpr uint8_t KLADN 	= 0x01;

	struct czas {
		unsigned long time;
		bool on;
	};

	struct czas tabela[9];
	unsigned long tik;

public :








};
#endif
