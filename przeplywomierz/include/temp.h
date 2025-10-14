#ifndef MW_TEMP_H
#define MW_TEMP_H
#if 0
#include <OneWire.h>
#include <DallasTemperature.h>

class Temp {
public:
	Temp() : onewire(this->pin), sensors(&(this->onewire)), temp(0.0)
	{ }

	void init() {
		sensors.begin();
	};

	float getTemp() const {
		return temp;
	}

	void loadTemp();


private:
  static constexpr uint8_t pin = 4;
  static constexpr uint8_t precision = 9;
  OneWire onewire;
  DallasTemperature sensors;

  float temp;
};

#endif
#endif