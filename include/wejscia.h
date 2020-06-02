#ifndef MW_WEJSCIA
#define MW_WEJSCIA

#include <Arduino.h>

class WejscieValue {
public:
  WejscieValue() : value(false), prevvalue(false), timeChange(0)
  { }

	const WejscieValue & operator=(const bool value) {
    if (value != this->value)
      timeChange = millis();
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

  inline void setRuch() {
    timeChange = millis();
    value = false;
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

  bool czyklKuch() const;

  bool czyklJadalnia() const;
  
  bool czyklKuchAUp() const;

  bool czyklKuchBUp() const;

  bool czyklKuchADown() const;

  bool czyklKuchBDown() const;

  bool czyklKuchDouble() const;

  void setRuch();

private:
  WejscieValue wieczor, drzwi_otw, noc, ruch_kuch, ruch_drzwi;
  WejscieValue kl_kuch_a_up, kl_kuch_a_down, kl_kuch_b_up, kl_kuch_b_down, kl_jad_up, kl_jad_down;


};



#endif
