#include <Arduino.h>
#include <Wire.h>
#include <Adafruit_MCP23017.h>

#define ZAS_AW 6
#define TARYF2 7
#define WIECZOR 8
#define NOC 9
// put function declarations here:

unsigned long impulse[2][15];
unsigned short index = 0;

static void WCUmywalkaZ()
{
  impulse[index][0] += 1;
}

static void WCUmywalkaC()
{
  impulse[index][1] += 1;
}

struct PinInterr {
  short pin;
  void (*fun)();
};

PinInterr mapsPin[2] = {
  { 17, WCUmywalkaZ},
  { 16, WCUmywalkaC}
};



#define INPUT1
#define OUTPUT1
#define OUTPUT2

#ifdef OUTPUT1
Adafruit_MCP23017 o1;
#endif

#ifdef OUTPUT2
Adafruit_MCP23017 o2;
#endif

#ifdef INPUT1
Adafruit_MCP23017 i1;
#endif

void zapalRaspberry(bool on);
void setup() {
  pinMode(ZAS_AW, INPUT);
  pinMode(TARYF2, INPUT);
  pinMode(WIECZOR, INPUT);
  pinMode(NOC, INPUT);

  Wire.begin();
  Serial.begin(9600);

  // put your setup code here, to run once:

#ifdef OUTPUT1
  o1.begin((uint8_t)0);
#endif

#ifdef OUTPUT2
  o2.begin((uint8_t)2);
#endif

#ifdef INPUT1  
  i1.begin((uint8_t)1);
#endif

  for (int i = 0; i < 16; i++) {
    delay(5);
#ifdef OUTPUT1    
    if (i != 0 && i != 3) {
      o1.pinMode(i, OUTPUT);
      o1.digitalWrite(i, HIGH);
    }
#endif
#ifdef OUTPUT2
    delay(5);    
    o2.pinMode(i, OUTPUT);
    o2.digitalWrite(i, i< 8 ? LOW : HIGH);
#endif
#ifdef INPUT1
    delay(5);    
    i1.pinMode(i, INPUT);
#endif    
  }

  zapalRaspberry(true);
  delay(1000);
  for (int i = 0; i < 2; ++i) {
    for (int j = 0; j < 15; ++j) {
      impulse[i][j] = 0;
    }
  }
  for (int i = 0; i < 2; ++i)
    attachInterrupt(digitalPinToInterrupt(mapsPin[i].pin), mapsPin[i].fun, RISING); 
  Serial.begin(115200);
}
#define LAZIENKA_PRAWE      1
#define LAZIENKA_LEWE       2

#define PRYSZNIC_LEWY_TYLNY  4
#define PRYSZNIC_PRAWY_TYLNY 5
#define PRYSZNIC_LEWY_PRZOD  6
#define PRYSZNIC_PRAWY_PRZOD 7

#define LUSTRO_PRAWE  8
#define LUSTRO_LEWE   9
#define RASPBERRY     10
#define RADIO         11
#define MONITOR       12
#define LAZIENKA      13
#define WANNA_LEWE    14
#define WANNA_PRAWE   15  

#define ZASILACZ12VMALY   15 // pewne
#define ZASILACZ12VDUZY   14
#define OSW_PRZED         13
#define LUSTERKO          12 //pewne
#define POKOJ1            11
#define POKOJ2            10 //pewne
#define PRACOWNIA1        9
#define PRACOWNIA2        8 // pewne


#define GNIAZDO_KAL       7
#define SUSZARKA          6
#define GRZEJNIK_ELEKT    5 //q
#define POGRZ_LUSTRA      4 //r
#define GNIAZDO_PRAWE     3 //s
#define GNIAZDO_LEWE      2 //t
#define SYG_GNI_PRAWE     1 // pewne
#define SYG_GNI_LEWE      0 // pewne

void zapalRaspberry(bool on) {
#ifdef OUTPUT1  
  o1.digitalWrite(RASPBERRY, on ? LOW : HIGH);
#endif  
}

void zapalMonitor(bool on) {
#ifdef OUTPUT1
  o1.digitalWrite(MONITOR, on ? LOW : HIGH);
#endif  
}

void zapalRadio(bool on) {
#ifdef OUTPUT1  
  o1.digitalWrite(RADIO, on ? LOW : HIGH);
#endif  
}

void zapalWanna(bool on) {
#ifdef OUTPUT1  
  o1.digitalWrite(WANNA_LEWE, on ? LOW : HIGH);
  o1.digitalWrite(WANNA_PRAWE, on ? LOW : HIGH);
#endif  
}

void zapalLustro(bool on) {
#ifdef OUTPUT1  
  o1.digitalWrite(LUSTRO_LEWE, on ? LOW : HIGH);
  o1.digitalWrite(LUSTRO_PRAWE, on ? LOW : HIGH);
#endif  
}

void zapalLusterko(bool on)
{
#ifdef OUTPUT2  
  o2.digitalWrite(LUSTERKO, on ? LOW : HIGH);
#endif  
}

void zapalLusterkoImp(bool on)
{
  static bool state = false;
  if (on)
    state = !state;
  
#ifdef OUTPUT2  
  o2.digitalWrite(LUSTERKO, state ? LOW : HIGH);
#endif  
}

void zapalPrysznic(bool on) {
#ifdef OUTPUT1  
  o1.digitalWrite(PRYSZNIC_LEWY_TYLNY, on ? LOW : HIGH);
  o1.digitalWrite(PRYSZNIC_PRAWY_TYLNY, on ? LOW : HIGH);
  o1.digitalWrite(PRYSZNIC_LEWY_PRZOD, on ? LOW : HIGH);
  o1.digitalWrite(PRYSZNIC_PRAWY_PRZOD, on ? LOW : HIGH);
#endif  
}

void wlacz12VMaly(bool on)
{
#ifdef OUTPUT2 
  o2.digitalWrite(ZASILACZ12VMALY, on? LOW : HIGH);
#endif
}

void zapalLazienka(bool on1, bool on2) {
#ifdef OUTPUT1  
  if (on1) {
    o1.digitalWrite(LAZIENKA, LOW);
    o1.digitalWrite(LAZIENKA_LEWE, on1 ? LOW : HIGH);
    o1.digitalWrite(LAZIENKA_PRAWE, on2 ? LOW : HIGH);
    wlacz12VMaly(on1);
  } else {
    o1.digitalWrite(LAZIENKA, HIGH);
    o1.digitalWrite(LAZIENKA_LEWE, HIGH);
    o1.digitalWrite(LAZIENKA_PRAWE, HIGH);
    wlacz12VMaly(false);
  }
#endif  
}

void zapalPokoj(bool on1, bool on2)
{
#ifdef OUTPUT2 
  o2.digitalWrite(POKOJ1, on1? LOW : HIGH);
  o2.digitalWrite(POKOJ2, on2? LOW : HIGH);
#endif
}

void zapalPracownia(bool on1, bool on2)
{
#ifdef OUTPUT2 
  o2.digitalWrite(PRACOWNIA1, on1? LOW : HIGH);
  o2.digitalWrite(PRACOWNIA2, on2? LOW : HIGH);
#endif
}

void wlaczLeweGniazdo(bool on)
{
  static bool state = false;
  if (on) {
    state = !state;
  }
#ifdef OUTPUT2 
  o2.digitalWrite(GNIAZDO_LEWE, state? LOW : HIGH);
  o2.digitalWrite(SYG_GNI_LEWE, state? LOW : HIGH);
#endif
}

void wlaczPraweGniazdo(bool on)
{
  static bool state = false;
  if (on) {
    state = !state;
  }
#ifdef OUTPUT2 
  o2.digitalWrite(GNIAZDO_PRAWE, state? LOW : HIGH);
  o2.digitalWrite(SYG_GNI_PRAWE, state? LOW : HIGH);
#endif
}

void wlaczGniazdoKaloryfer(bool on)
{
#ifdef OUTPUT2 
  o2.digitalWrite(GNIAZDO_KAL, on? LOW : HIGH);
#endif
}

void wlacznadLustremPrawe(bool on)
{
  static bool state = false;
  if (on) {
    state = !state;
  }
#ifdef OUTPUT1
  o1.digitalWrite(LUSTRO_PRAWE, state? LOW : HIGH);
#endif
}

void wlacznadLustremLewe(bool on)
{
  static bool state = false;
  if (on) {
    state = !state;
  }
#ifdef OUTPUT1
  o1.digitalWrite(LUSTRO_LEWE, state? LOW : HIGH);
#endif
}


#define W_LAZ 0
#define W_SED_D_N 1
#define W_SED_D_P 2
#define W_SED_D_S 3
#define W_SED_D_L 4
#define W_SED_G_P 5
#define W_SED_G_S 6
#define W_SED_G_L 7
#define W_LUS_P_P 8 
#define W_LUS_P_L 9  //#10 I #9
#define W_LUS_L_P 10 //#10 I #9
#define W_LUS_L_L 11 //#L_l
#define W_PRAC_L  12 //#PRAC_L
#define W_PRAC_P  13 //#PRAC_P
#define W_POKOJ_L 14
#define W_POKOJ_P 15

char * labels[] = { "Lazienka", "Sedes N", 
                          "Sedes dolny prawy",
                          "Sedes dolny srodkowy",
                          "Sedes dolny lewy",
                          "Sedes gorny prawy",
                          "Sedes gorny srodkowy",
                          "Sedes gorny lewy",
                          "Lustro lewe lewe",
                          "Lustro lewe prawe",
                          "Lustro prawe lewe",
                          "Lustro prawe prawe",
                          "Pracownia lewy",
                          "Pracownia prawy",
                          "Pokoj lewy",
                          "Pokoj prawy"};


uint16_t act = 0xFFF9;
uint16_t prev = 0xFFF9;
bool zLaz = false;

short loopNr = 0;
bool pok1 = false;
bool pok2 = false;
bool pra1 = false;
bool pra2 = false;


void loop() {

  bool wieczor = digitalRead(WIECZOR);
  bool noc = digitalRead(NOC);
  bool taryfa2 = digitalRead(TARYF2);
  bool zas_awar = digitalRead(ZAS_AW);


#ifdef INPUT1  
  // put your main code here, to run repeatedly:
  act = i1.readGPIOAB();
  if (loopNr++ == 100) {
    loopNr = 0;
    Serial.print("IN:");
    Serial.println(act, HEX);
  }
  if (prev != act) {
    uint16_t m = ~act; //bity ustawione
    uint16_t c = act ^ prev ; //bity zmienione
    Serial.println("--- ZMIANA --");
    Serial.print("READ:  ");
    Serial.println(m, HEX);
    Serial.print("CHANGE: ");
    Serial.println(c, HEX);

    if ((m & 0x0001) && (c && 0x0001)) {
      //Serial.println("Klawisz");
      //wcisniecie klawisza lazienkowego
      zLaz = zLaz ? false : true;

      //Serial.print("zaswiec");
      //Serial.println(zLaz, DEC);
      if (zLaz) {
        zapalLazienka(true, m & (1 << W_SED_D_L) );
        zapalRadio(!noc && (m & (1 << W_SED_D_P)));
        zapalMonitor(true);
        zapalPrysznic(m & (1 << W_SED_G_S));
        zapalLustro(m & (1 << W_SED_G_L));
        zapalWanna(m & (1 << W_SED_G_P));
        wlaczGniazdoKaloryfer(true);
        zapalLusterko(true);
      } else {
        zapalLazienka(false, false);
        zapalRadio(false);
        zapalMonitor(false);
        zapalPrysznic(false);
        zapalLustro(false);
        zapalWanna(false);
        wlaczGniazdoKaloryfer(false);
        zapalLusterko(false);
      }
    }

    if (c & (1 << W_SED_D_P))
      zapalRadio(m & (1 << W_SED_D_P));
    
    if (c & (1 << W_SED_G_S))
      zapalPrysznic(m & (1 << W_SED_G_S));
    
    if (c & (1 << W_SED_G_L))    
      zapalLustro(m & (1 << W_SED_G_L));
    
    if (c & (1 << W_SED_D_L))    
      zapalLazienka(true, m & (1 << W_SED_D_L));

    if (c & (1 << W_SED_G_P))    
      zapalWanna(m & (1 << W_SED_G_P));

#define JEDNALAMPAPRACOWNIA 1 
#ifdef JEDNALAMPAPRACOWNIA
    if (c & (1 << W_PRAC_L)) {
      pra2 = (m & (1 << W_PRAC_L)) ? !pra2 : pra2;
      zapalPracownia(false, pra2);
    }

    if (c & (1 << W_PRAC_P)) {
      pra2 = (m & (1 << W_PRAC_P)) ? !pra2 : pra2;
      zapalPracownia(false, pra2);
    }

#else
    if (c & (1 << W_PRAC_L)) {
      pra1 = (m & (1 << W_PRAC_L)) ? !pra1 : pra1;
      zapalPracownia(pra1, pra2);
    }

    if (c & (1 << W_PRAC_P)) {
      pra2 = (m & (1 << W_PRAC_P)) ? !pra2 : pra2;
      zapalPracownia(pra1, pra2);
    }
#endif

#define JEDNALAMPAPOKOJ 1 
#ifdef JEDNALAMPAPOKOJ

    if (c & (1 << W_POKOJ_L)) {
      pok2 = (m & (1 << W_POKOJ_L)) ? !pok2 : pok2;
      zapalPokoj(false, pok2);
    }

    if (c & (1 << W_POKOJ_P)) {
      pok2 = (m & (1 << W_POKOJ_P)) ? !pok2 : pok2;
      zapalPokoj(pok1, pok2);
    }
#else
    if (c & (1 << W_POKOJ_L)) {
      pok1 = (m & (1 << W_POKOJ_L)) ? !pok1 : pok1;
      zapalPokoj(pok1, pok2);
    }

    if (c & (1 << W_POKOJ_P)) {
      pok2 = (m & (1 << W_POKOJ_P)) ? !pok2 : pok2;
      zapalPokoj(pok1, pok2);
    }

#endif

    if (c & (1 << W_LUS_L_L)) {
      wlaczLeweGniazdo(m & (1 << W_LUS_L_L));
    }

    if (c & (1 << W_LUS_L_P)) {
      wlacznadLustremPrawe(m & (1 << W_LUS_L_P));
    }

    if (c & (1 << W_LUS_P_L)) {
      wlacznadLustremLewe(m & (1 << W_LUS_P_L));
    }

    if (c & (1 << W_LUS_P_P)) {
      wlaczPraweGniazdo(m & (1 << W_LUS_P_P));
    }

  }

  prev = act;
#endif

  int nDevices = 0;
  if (Serial.available()) {
    int inByte = Serial.read();
/*
#ifdef OUTPUT1    
    if (inByte >= 'a' && inByte < ('a' + 16)) { o1.digitalWrite(inByte - 'a', HIGH); Serial.print("Zapalam "); Serial.println(inByte-'a', DEC); }
    if (inByte >= 'A' && inByte < ('A' + 16)) { o1.digitalWrite(inByte - 'A', LOW); Serial.print("Gasze "); Serial.println(inByte-'A', DEC); }
#endif 
*/

#ifdef OUTPUT12   
    if (inByte >= 'a' && inByte < ('a' + 16)) { o2.digitalWrite(inByte - 'a', HIGH); Serial.print("Zapalam "); Serial.println(inByte-'a', DEC); }
    if (inByte >= 'A' && inByte < ('A' + 16)) { o2.digitalWrite(inByte - 'A', LOW); Serial.print("Gasze "); Serial.println(inByte-'A', DEC); }
#endif 

    switch(inByte) {
/*      
#ifdef OUTPUT2      
      case '0':
      case '1':
      case '2':
      case '3':
      case '4':
      case '5':
      case '6':
      case '7':
      case '8':
      case '9':
        o2.digitalWrite(inByte - '0', HIGH); Serial.print("Zapalam "); Serial.println(inByte-'0', DEC);
        Serial.println(wyjscia[inByte-'0']);
        break;
      case 'q':
      case 'r':
      case 's':
      case 't':
      case 'u':
      case 'v':
        o2.digitalWrite(inByte - 'q' + 10, HIGH); Serial.print("Zapalam "); Serial.println(inByte-'q'+10, DEC);
        Serial.println(wyjscia[inByte-'q']);
        break;
      case ')':
        o2.digitalWrite(0, LOW); Serial.println("Gasze 0");
        Serial.println(wyjscia[0]);
        break;
      case '!':
        o2.digitalWrite(1, LOW); Serial.println("Gasze 1");
        Serial.println(wyjscia[1]);
        break;
      case '@':
        o2.digitalWrite(2, LOW); Serial.println("Gasze 2");
        Serial.println(wyjscia[2]);
        break;
      case '#':
        o2.digitalWrite(3, LOW); Serial.println("Gasze 3");
        Serial.println(wyjscia[3]);
        break;
      case '$':
        o2.digitalWrite(4, LOW); Serial.println("Gasze 4");
        Serial.println(wyjscia[4]);
        break;
      case '%':
        o2.digitalWrite(5, LOW); Serial.println("Gasze 5");
        Serial.println(wyjscia[5]);
        break;
      case '^':
        o2.digitalWrite(6, LOW); Serial.println("Gasze 6");
        Serial.println(wyjscia[6]);
        break;
      case '&':
        o2.digitalWrite(7, LOW); Serial.println("Gasze 7");
        Serial.println(wyjscia[7]);
        break;
      case '*':
        o2.digitalWrite(8, LOW); Serial.println("Gasze 8");
        Serial.println(wyjscia[8]);
        break;
      case '(':
        o2.digitalWrite(9, LOW); Serial.println("Gasze 9");
        Serial.println(wyjscia[9]);
        break;
      case 'Q':
      case 'R':
      case 'S':
      case 'T':
      case 'U':
      case 'V':
        o2.digitalWrite(inByte - 'Q' + 10, LOW); Serial.print("Gasze "); Serial.println(inByte-'Q'+10, DEC);
        Serial.println(wyjscia[inByte - 'Q' + 10]);
        break;
#endif
*/

      case 'L':
        wlaczLeweGniazdo(true);
        break;
      case 'l':
        wlaczLeweGniazdo(false);
        break;
      case 'P':
        wlaczLeweGniazdo(true);
        break;
      case 'p':
        wlaczLeweGniazdo(false);
        break;
      case 'z':
      case 'Z':
        Serial.println("Scanning...");
        for (byte address = 1; address < 127; ++address) {
          // The i2c_scanner uses the return value of
          // the Write.endTransmisstion to see if
          // a device did acknowledge to the address.
          Wire.beginTransmission(address);
          byte error = Wire.endTransmission();

          if (error == 0) {
            Serial.print("I2C device found at address 0x");
            if (address < 16) {
              Serial.print("0");
            }
            Serial.print(address, HEX);
            Serial.println("  !");

            ++nDevices;
          } else if (error == 4) {
            Serial.print("Unknown error at address 0x");
            if (address < 16) {
              Serial.print("0");
            }
            Serial.println(address, HEX);
          }
        }
        if (nDevices == 0) {
          Serial.println("No I2C devices found\n");
        } else {
          Serial.println("done\n");
        }
        break;
      default:
        break;
    }
  }

  delay(100);
}
  // put your main code here, to run repeatedly:

  delay(1000);
  unsigned short actIndex = index;
  index = (index + 1) % 2;
  for (int j = 0; j < 2; ++j) {
    Serial.print(j, DEC);
    Serial.print(" => ");
    Serial.println(impulse[actIndex][j], DEC);
    impulse[actIndex][j] = 0;
  }
  Serial.println('---');
}

