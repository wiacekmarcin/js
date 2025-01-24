#include <PCF8574.h>

#include "value.h"
class Wejscia {
public:
    Wejscia();

    void init();

    void get();

    const Value & getWlacznik() const { return w[KLAWISZ]; }
    const Value & getLustro() const { return w[CZ_R_LUSTRO]; }
    const Value & getCzRuchu() const { return w[CZ_R_WC]; }
    const Value & getDrzwi() const { return w[DRZWI]; }
    const Value & getWieczor() const { return w[WIECZOR]; }
    const Value & getNoc() const { return w[NOC]; }
    //const Value & getPoziomWody() const { return w[CZ_POW_WODY]; }
    
    bool isChange() const;

    

private:
    
    PCF8574 wejscia;

    static constexpr uint8_t CZ_R_LUSTRO = 0;
    static constexpr uint8_t CZ_R_WC = 1;
    static constexpr uint8_t DRZWI = 2;
    static constexpr uint8_t KLAWISZ = 3;
    static constexpr uint8_t NOC = 4;
    static constexpr uint8_t WIECZOR = 5;
    //static constexpr uint8_t CZ_POZ_WODY = 6;
    static constexpr uint8_t lenWej = 6; //7

    Value w[lenWej];

//p0 czujnik zblizeniowy 0 - blisko 1 - daleko
//p1 czujnik ruchu 0 -brak ruchu 1 - ruch
//p2 drzwi 0 - zamkniete 1 - otwarte
//p3 klawisz 0 - nacisniety 1 - w normalnej pozycji

//p4 noc
//p5 wieczor
//p6 czujnik poziomu wody
};
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
class LiquidCrystal_I2C;
class Wejscia
{
public:
	Wejscia() { }

	void init();

	void read(bool printlcd, LiquidCrystal_I2C * lcd);

  bool czyWieczor() const;

  bool czyDrzwiOtwarte() const;

  bool czyNoc() const;

  bool czyZasilanieAwaryjne() const;

  bool czyZmianaZasAwaryjne() const;

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
  WejscieValue wieczor, drzwi_otw, noc, ruch_kuch, ruch_drzwi, zas_awar, taryfa2;
  WejscieValue kl_kuch_a_up, kl_kuch_a_down, kl_kuch_b_up, kl_kuch_b_down, kl_jad_up, kl_jad_down;


};



#endif
