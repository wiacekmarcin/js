#include <Arduino.h>
#include <Wire.h>

#include <DallasTemperature.h>
#include <PCF8574.h>


class Temp {
public:

private:
  const uint8_t pin = 4;
  const uint8_t precision = 0;



  OneWire onewire;
};



#define DBG
// Data wire is plugged into port 2 on the Arduino
#define ONE_WIRE_BUS 4
#define TEMPERATURE_PRECISION 9 // Lower resolution

// Setup a oneWire instance to communicate with any OneWire devices (not just Maxim/Dallas temperature ICs)
OneWire oneWire(ONE_WIRE_BUS);


PCF8574 expWejscia(0x20);
PCF8574 expLedy(0x25);
PCF8574 expOczka(0x26);
PCF8574 expPozostale(0x27);



inline uint8_t lo(bool val) { return val ? LOW : HIGH; }
inline uint8_t ho(bool val) { return val ? HIGH : LOW; }

inline bool li(uint8_t val) { return val == LOW; }
inline bool hi(uint8_t val) { return val == HIGH; }

//#define READBAL(nameB, expW, pin, mask) bal_##nameB = (bal_##nameB << 1) | (expW.digitalRead(pin) == HIGH ? 1 : 0); \
//                                  nameB = checkValue(nameB, bal_##nameB, mask);

class WejscieValue {
private:
  bool value, prevvalue;
  uint8_t mask;
  unsigned long timeChange;

public:
    WejscieValue() : value(false), prevvalue(false), mask(0), timeChange(0)
    { }

    //adresobiektu, nr pinu do odczytania, czy stan high to jedynka logiczna
    void read(PCF8574 * addr, uint8_t pin, uint8_t checkmask, bool h ) {
        prevvalue = value;
        uint8_t pmask = mask;
        mask = mask << 1;
        bool p = 0;
        uint8_t rv = addr->digitalRead(pin);
        if (h)
          p = hi(rv);
        else
          p = li(rv);

        mask |= p ? 1 : 0;
#ifdef DBG

           bool pr = false;
           if (addr == &expWejscia) {
             if (pin > 5) {
               char * text[] = { "jad_up", "jad_down", "kuch_b_up", "kuch_b_down", "kuch_a_up", "kuch_a_down", "wieczor", "noc" };
               Serial.print(pin);
               Serial.print(" [");
               Serial.print(text[pin]);
               pr = true;
             }
           } else if (addr == &expLedy){
             if (pin > 4) {
               char * text[] = { "-", "-", "-", "-", "-", "drzwi_otwarte", "ruch_kuch", "ruch_drzwi" };
               Serial.print(pin);
               Serial.print(" [");
               Serial.print(text[pin]);
               pr = true;
             }
           }
           if (pr) {


             Serial.print("] rv= ");
             Serial.print(rv);
             Serial.print(" p=");
             Serial.print(p ? "yes" : "no");
             //Serial.print(" pmask=");
             //Serial.print(pmask, HEX);
             //Serial.print(" mask=");
             //Serial.print(mask, HEX);
             Serial.print(" val=");
           }
#endif
        if ((mask & checkmask) == checkmask) {
          value = true;
          mask = 0x00;
        } else if ((mask & checkmask) == 0x00) {
          value = false;
        }
        if (value && !prevvalue) //zalacznie na 1
          timeChange = millis();
#ifdef DBG
        if (pr)
          Serial.println(value?"true":"false");
#endif
    }

    inline bool czyZmiana() const {
      return value != prevvalue;
    }

    inline unsigned int czasOdZmiany() const {
      return (millis() - timeChange) / 1000; //w sekundach
    }

    inline bool getVal() const {
      return value;
    }
};


class Wejscia
{
private:
  WejscieValue wieczor, drzwi_otw, noc, ruch_kuch, ruch_drzwi;
  WejscieValue kl_kuch_a_up, kl_kuch_a_down, kl_kuch_b_up, kl_kuch_b_down, kl_jad_up, kl_jad_down;


public:
  Wejscia()
  {}

    inline bool czyWieczor() const {
      return wieczor.getVal();
    }

    inline bool czyDrzwiOtwarte() const {
      return drzwi_otw.getVal();
    }

    inline bool czyNoc() const {
      return noc.getVal();
    }

    inline bool czyRuchKuchnia(unsigned long timeins) const {
      return ruch_kuch.czasOdZmiany() < timeins;
    }

    inline bool czyRuchDrzwi(unsigned long timeins) const {
      return ruch_drzwi.czasOdZmiany() < timeins;
    }

    inline bool czyklKuchUp() const {
      return kl_kuch_a_up.getVal() || kl_kuch_b_up.getVal();
    }

    inline bool czyklKuchDown() const {
      return kl_kuch_a_down.getVal() || kl_kuch_b_down.getVal();
    }

    inline bool czyklJadUp() const {
      return kl_jad_up.getVal();
    }

    inline bool czyklJadDown() const {
      return kl_jad_down.getVal();
    }


    void read() {

      wieczor.read(   &expWejscia,  6, 0x0f, false);
      noc.read(       &expWejscia,  7, 0x0f, false);
      drzwi_otw.read( &expLedy,     5, 0xff, true);
      ruch_kuch.read( &expLedy,     6, 0x0f, false);
      ruch_drzwi.read(&expLedy,     7, 0x0f, false);

      kl_kuch_a_up.read(  &expWejscia, 4, 0x0f, false);
      kl_kuch_a_down.read(&expWejscia, 5, 0x0f, false);
      kl_kuch_b_up.read(  &expWejscia, 2, 0x0f, false);
      kl_kuch_b_down.read(&expWejscia, 3, 0x0f, false);
      kl_jad_up.read(     &expWejscia, 0, 0x0f, false);
      kl_jad_down.read(   &expWejscia, 1, 0x0f, false);
    }



};

Wejscia w;

class Podswietlenie {
private:
  bool kuchnia, jadalnia, szafa;

public:
  Podswietlenie() : kuchnia(false), jadalnia(false), szafa(true)
  { }

  void zapalKuchnia(bool on) {
    if (on == kuchnia)
      return;
    kuchnia = on;
    setPrzekaz();
  }

  void zapalJadalnia(bool on) {
    if (on == jadalnia)
      return;
    jadalnia = on;
    setPrzekaz();
  }

  void zapalSzafa(bool on) {
    if (on == szafa)
      return;
    szafa = on;
    setPrzekaz();
  }

  void init() {
    setPrzekaz();
  }

protected:
    void setPrzekaz() {
      expPozostale.digitalWrite(2, ho(szafa));
      expPozostale.digitalWrite(6, ho(jadalnia));
      expPozostale.digitalWrite(5, ho(kuchnia));
    }
};

Podswietlenie swPod;


class SwiatloLED
{
private:
    bool m_sufit1, m_sufit2, m_drzwi1, m_drzwi2;

public:
    SwiatloLED(): m_sufit1(false), m_sufit2(false), m_drzwi1(false), m_drzwi2(false)
    { }

   void sufit1(bool on) {
        if (m_sufit1 != on) {
          m_sufit1 = on;
          ustaw_przekaz();
        }
     }

     void sufit2(bool on) {
        if (m_sufit2 != on) {
          m_sufit2 = on;
          ustaw_przekaz();
        }
     }

     void drzwi1(bool on) {
        if (m_drzwi1 != on) {
          m_drzwi1 = on;
          ustaw_przekaz();
        }
     }

     void drzwi2(bool on) {
        if (m_drzwi2 != on) {
          m_drzwi2 = on;
          ustaw_przekaz();
        }
     }

     bool czyZapalone() {
       return  m_sufit1 || m_sufit2 || m_drzwi1 || m_drzwi2;
     }

     void init() {
       ustaw_przekaz();
     }

protected:


    void ustaw_przekaz() {
        expLedy.digitalWrite(1, lo(m_sufit1)); //ustawiane sygnałem LOW
        expLedy.digitalWrite(2, lo(m_sufit2));
        expLedy.digitalWrite(3, lo(m_drzwi1));
        expLedy.digitalWrite(4, lo(m_drzwi2));
        expLedy.digitalWrite(0, lo(m_sufit1 || m_sufit2 || m_drzwi1 || m_drzwi2));
    }
};

SwiatloLED swLED;

class SwiatloSufit
{
private:
    static constexpr uint8_t maxLed = 9; //0  1  2  3  4  5  6  7  8

    //na listwie               2 7 1 6 8 4 9 3 | 5 10 11 12 | 13
    //wejscia na przekaznikach 8 7 6 5 4 3 2 1 | 4  3  2  1 |  1
    //wejscia na expanderach   7 6 5 4 3 2 1 0 | 3  2  1  0 |  4
    static const uint8_t mapPins[maxLed]; /* = { 5, 7, 0, 2, 8, 4, 6, 3, 1 };*/

    uint8_t level;
    static constexpr uint8_t maxLevel = 4;
    bool led[maxLed] = { false, false, false, false, false, false, false, false, false};

public :
    SwiatloSufit() : level(0)
    {}

    void init() {
      setPrzekaz();
    }

    void up() {
      if (level >= maxLevel)
        return;
      level += 1;
      setLevel();
      setPrzekaz();
    }

    void down() {
      if (level == 0)
        return;
      level -= 1;
      setLevel();
      setPrzekaz();
    }

    bool czyZapalone() {
      for (uint8_t id = 0 ; id < maxLed; ++id)
        if (led[id])
          return true;
      return false;
    }

    void rotate() {
      if (level == 0 || level == 4)
        return;
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
      setPrzekaz();
    }

protected:
    void set(uint8_t pin, bool on) {
      if (pin >= 9)
        return;

      uint8_t p = mapPins[pin];
#ifdef DBG
      Serial.print("Lampa ");
      Serial.print(p);
      Serial.print(" setting on");
      Serial.println(on ? "true": "false");
#endif
      if (p < 8) {
        expOczka.digitalWrite( p, ho(on)); //piny są odwrócone najpierw P3, na koniec P0
      } else {
        expPozostale.digitalWrite( 3, ho(on));
      }
    }

    void setPrzekaz() {
      for (uint8_t id = 0; id < maxLed; ++id) {
          set(id, led[id]);
      }
    }

    void setLevel() {
#ifdef DBG
      Serial.print("SetLevel ");
      Serial.println(level);
#endif
      switch(level) {
        case 0 :
        default:
          for (uint8_t id = 0; id < maxLed; ++id) {
            led[id] = false;
          }
          break;

          case 1:
            for (uint8_t id = 0; id < maxLed; ++id) {
              led[id] = id == 0 || id == 4 ? true : false;
            }
            break;

          case 2:
          for (uint8_t id = 0; id < maxLed; ++id) {
            led[id] = id == 0 || id == 3 || id == 4 || id == 7 ? true : false;
          }
          break;

          case 3:
            for (uint8_t id = 0; id < maxLed; ++id) {
              led[id] = id == 1 || id == 5 || id == 9 ? false : true;
            }
            break;

          case 4:
            for (uint8_t id = 0; id < maxLed; ++id) {
              led[id] = true;
            }
            break;
      }
    }


};

//na listwie               2 7 1 6 8 4 9 3 | 5 10 11 12 | 13
//wejscia na przekaznikach 8 7 6 5 4 3 2 1 | 4  3  2  1 |  1
//wejscia na expanderach   7 6 5 4 3 2 1 0 | 3  2  1  0 |  4

const uint8_t SwiatloSufit::mapPins[SwiatloSufit::maxLed] = { 5, 7, 0, 2, 8, 4, 6, 3, 1 };
                                                          //  1  2  3  4  5  6  7  8  9


SwiatloSufit swSufit;

class SwiatloJadalnia
{
private:
  uint8_t level;
  static constexpr uint8_t maxSw = 3;
  bool sw[maxSw] = { false, false, false };
  static constexpr uint8_t mapPins[3] = { 1,  0,  4 };

public:
  SwiatloJadalnia() : level(0)
  { }

  void rotate() {
    bool tmp = sw[0];
    sw[0] = sw[1];
    sw[1] = sw[2];
    sw[2] = tmp;
    setPrzekaz();
  }

  void init() {
    setPrzekaz();
  }

  void up() {
    for (uint8_t id = 0 ; id < maxSw; ++id) {
      if (!sw[id]) {
        sw[id] = true;
        setPrzekaz();
        return;
      }
    }
  }

  void down() {
    for (uint8_t id = 0 ; id < maxSw; ++id) {
      if (sw[id]) {
        sw[id] = false;
        setPrzekaz();
        return;
      }
    }
  }

  bool czyZapalone() {
    for (uint8_t id = 0 ; id < maxSw; ++id)
      if (sw[id])
        return true;
    return false;
  }

protected:
  void setPrzekaz() {
    for (uint8_t id = 0 ; id < maxSw; ++id) {
      expPozostale.digitalWrite(mapPins[id], sw[id]);
    }
  }
};
SwiatloJadalnia swJadalnia;

class PseudoTimer {
private:
  unsigned long tik;

public:
  PseudoTimer() : tik(0) { }
  void tiktok() {
    constexpr unsigned int min5 = 20*60*5;
    constexpr unsigned long min30 = 20*60*30;
    ++tik;
    if (tik % min5 == 0) {//5 min
      swSufit.rotate();
      swJadalnia.rotate();
    }

    if (tik % min30 == 0) {////30 min
      swSufit.down();
      swJadalnia.down();
      tik = 0;
    }
  }
};

PseudoTimer psT;

bool zapalOswietlenieJadalnia() {
#ifdef DBG
  Serial.print("zapalOswietlenieJadalnia wieczor=");
  Serial.print(w.czyWieczor() ? "tak" : "nie");
  Serial.print(" sufit czyZapalone=");
  Serial.print(swSufit.czyZapalone() ? "tak" : "nie");
  Serial.print(" led czyZapalone=");
  Serial.print(swLED.czyZapalone() ? "tak" : "nie");
  Serial.print(" wynik=");
  Serial.println((w.czyWieczor() && !swJadalnia.czyZapalone() && !swSufit.czyZapalone() && !swLED.czyZapalone()) ? "tak" : "nie");
#endif
    if (!w.czyWieczor())
      return false;
    if (swJadalnia.czyZapalone() || swSufit.czyZapalone() || swLED.czyZapalone())
      return false;
    return true;
}

bool zapalOswietlenieKuchnia() {
#ifdef DBG
  Serial.print("zapalOswietlenieKuchnia wieczor=");
  Serial.print(w.czyWieczor() ? "tak" : "nie");
  Serial.print(" sufit czyZapalone=");
  Serial.print(swSufit.czyZapalone() ? "tak" : "nie");
  Serial.print(" led czyZapalone=");
  Serial.print(swLED.czyZapalone() ? "tak" : "nie");
  Serial.print(" wynik=");
  Serial.println((w.czyWieczor() && !swSufit.czyZapalone() && !swLED.czyZapalone()) ? "tak" : "nie");
#endif

  if (!w.czyWieczor())
    return false;
  if (swSufit.czyZapalone() || swLED.czyZapalone())
    return false;
  return true;
}

bool zapalLedDrzwiDzien() {
#ifdef DBG
  Serial.print("zapalLedDrzwiDzien noc=");
  Serial.print(w.czyNoc() ? "tak" : "nie");
  Serial.print(" czyDrzwiOtwarte=");
  Serial.print(w.czyDrzwiOtwarte() ? "tak" : "nie");
  Serial.print(" czyRuch=");
  Serial.print(w.czyRuchDrzwi(5*60) ? "tak" : "nie");
  Serial.print(" wynik=");
  Serial.println(!w.czyNoc() && w.czyRuchDrzwi(5*60) && w.czyDrzwiOtwarte() ? "tak" : "nie");
#endif

  if (!w.czyDrzwiOtwarte())
      return false;

  if (w.czyNoc())
      return false;

  if (w.czyRuchDrzwi(5*60))
      return true;

  return false;

}

bool zapalLedDrzwiNoc() {
#ifdef DBG
  Serial.print("zapalLedDrzwiNoc noc=");
  Serial.print(w.czyNoc() ? "tak" : "nie");
  Serial.print(" czyDrzwiOtwarte=");
  Serial.print(w.czyDrzwiOtwarte() ? "tak" : "nie");
  Serial.print(" czyRuch=");
  Serial.print(w.czyRuchDrzwi(5*60) ? "tak" : "nie");
  Serial.print(" wynik=");
  Serial.println(w.czyNoc() && w.czyRuchDrzwi(5*60) && w.czyDrzwiOtwarte() ? "tak" : "nie");

#endif
  if (!w.czyDrzwiOtwarte())
      return false;

  if (!w.czyNoc())
      return false;

  if (w.czyRuchDrzwi(5*60))
      return true;
  return false;
}

bool zapalSzafa() {
#ifdef DBG
  Serial.print("ZapalSzafa noc=");
  Serial.print(w.czyNoc() ? "tak" : "nie");
  Serial.print(" czyRuch=");
  Serial.print(w.czyRuchKuchnia(10*60) ? "tak" : "nie");
  Serial.print(" wynik=");
  Serial.println(w.czyNoc() && w.czyRuchKuchnia(10*60) ? "tak" : "nie");

#endif
  if (w.czyNoc() && w.czyRuchKuchnia(10*60))
    return false;
  return true;
}

void setup() {
  // put your setup code here, to run once:
  for (int i = 0; i < 8; ++i) {
    expOczka.pinMode(i, OUTPUT, LOW);
    expPozostale.pinMode(i, OUTPUT, LOW);
  }
  expOczka.begin();
  expPozostale.begin();

  for (int i = 0; i < 8; ++i) {
    if (i < 5) {
      expLedy.pinMode(i, OUTPUT, i ? HIGH : LOW);
    } else if ( i == 5){
      expLedy.pinMode(i, INPUT); //kontaktron
    } else {
      expLedy.pinMode(i, INPUT);
    }
  }
  expLedy.begin();


  for (int i = 0; i < 8; ++i)
    //expWejscia.pinMode(i, i < 6 ? INPUT : INPUT_PULLUP);
    expWejscia.pinMode(i, INPUT);
  expWejscia.begin();
  swLED.init();
  swSufit.init();
  swJadalnia.init();
  swPod.init();


  //swPod.zapalKuchnia(true);
  //swPod.zapalJadalnia(true);
}

unsigned int id = 0;
void loop() {
  // put your main code here, to run repeatedly:
  id++;
  Serial.println(id, DEC);
  w.read();
#if 0
  //ledy na otwartymi drzwiami w dzien
  swLED.drzwi1(zapalLedDrzwiDzien());

  //ledy na otwartymi drzwiami w nocy
  swLED.drzwi2(zapalLedDrzwiNoc());

  //zapal swiatlo w jadalni
  if (w.czyklJadUp()) {
    swJadalnia.up();
  }

  //zgas swiatlo w jadalni
  if (w.czyklJadDown()) {
    swJadalnia.down();
  }

  //zapal swiatlo w kuchni
  // jezeli noc to najper zapal ledy na gorze
  if (w.czyklKuchDown() || w.czyklKuchUp()) {
#ifdef DBG
    Serial.print("Klawisz kuchnia nacisniety");
#endif
    if (w.czyNoc()) {
#ifdef DBG
      Serial.print(" Noc = true|");
      Serial.print(" sufit = ");
      Serial.print(swSufit.czyZapalone() ? "tak" : "nie");
      Serial.print("| ledy ");
      Serial.print(swSufit.czyZapalone() ? "tak" : "nie");
#endif
      if (swSufit.czyZapalone() || swLED.czyZapalone()) {
#ifdef DBG
        Serial.print("| gasze ledy ");
#endif
        swLED.sufit1(false);
        swLED.sufit2(false);

        if (w.czyklKuchDown()) {
#ifdef DBG
          Serial.println("| swSufit down");
#endif
          swSufit.down();
        } else if (w.czyklKuchUp()) {
#ifdef DBG
          Serial.println("| swSufit up");
#endif
          swSufit.up();
        }

      } else {
#ifdef DBG
        Serial.print("| zalaczam ledy ");
#endif
        swLED.sufit1(true);
        swLED.sufit2(true);
      }
    } else {
#ifdef DBG
      Serial.print(" Noc = false");
#endif
      if (w.czyklKuchDown()) {
#ifdef DBG
        Serial.println(" swSufit down");
#endif
        swSufit.down();
      } else if (w.czyklKuchUp()) {
#ifdef DBG
        Serial.println(" swSufit up");
#endif
        swSufit.up();
      }
    }

  }

  //podwietlanie wlacznika jadalnia
  swPod.zapalJadalnia(zapalOswietlenieJadalnia());

  //podwietlanie wlacznika kuchnia
  swPod.zapalKuchnia(zapalOswietlenieKuchnia());

  swPod.zapalSzafa(zapalSzafa())  ;

  psT.tiktok();
#ifdef DBG
  Serial.println("---\n");
#endif

  //delay(5000);
  delay(50);
#else
Serial.println("\n\n\---\n");

delay(2000);
#endif
}
