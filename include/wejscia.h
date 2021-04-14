#ifndef MW_WEJSCIA
#define MW_WEJSCIA

#include <Arduino.h>





// 0x24
/*
#define KONTAKT   0 //A0 IN
#define ZAS_AWAR  1 //A1 IN 
#define TARYF2    2 //A2 IN 
#define WIECZOR   3 //A3 IN 
#define NOC       4 //A4 IN
#define JAD2      8  //B0 IN 
#define JAD1      9  //B1 IN
#define KUCHB2    10 //B2 IN
#define KUCHB1    11 //B3 IN
#define KUCHA2    12 //B4 IN
#define KUCHA1    13 //B5 IN
#define RUCH1     14 //B6 IN
#define RUCH2     15 //B7 IN
*/

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
