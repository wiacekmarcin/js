#ifndef _MW_WEJSCIA
#define _MW_WEJSCIA

#include <Arduino.h>

class WejscieValue {
public:
    WejscieValue() : value(false), prevvalue(false), timeChange(0)
    { }

	const WejscieValue & operator=(const bool value) {
		this->value = value;
		return (*this);
	}

    inline bool czyZmiana() const {
      return value != prevvalue;
    }

    inline unsigned int czasOdZmiany() const {
      return (millis() - timeChange); //w sekundach
    }

    inline bool getVal() const {
      return value;
    }

	operator bool() const { return value; }

private:
  	bool value, prevvalue;
  	unsigned long timeChange;
};

class Wejscia
{
public:
	Wejscia() { }

	void init();

	void read();

    bool czyWieczor() const;

    bool czyDrzwiOtwarte() const;

    bool czyNoc() const;

    bool czyRuchKuchnia(unsigned long timeins) const;

    bool czyRuchDrzwi(unsigned long timeins) const;

    bool czyklKuchUp() const;

    bool czyklKuchDown() const;

    bool czyklJadUp() const;

    bool czyklJadDown() const;

	bool czyklKuchAUp() const { return kl_kuch_a_up; }

	bool czyklKuchBUp() const { return kl_kuch_b_up; }

	bool czyklKuchADown() const { return kl_kuch_a_down; }

	bool czyklKuchBDown() const { return kl_kuch_b_down; }

private:
  WejscieValue wieczor, drzwi_otw, noc, ruch_kuch, ruch_drzwi;
  WejscieValue kl_kuch_a_up, kl_kuch_a_down, kl_kuch_b_up, kl_kuch_b_down, kl_jad_up, kl_jad_down;


};



#endif
