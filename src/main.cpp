#include <Arduino.h>
#include <Wire.h>
#include <Adafruit_MCP23017.h>

Adafruit_MCP23017 o1;
Adafruit_MCP23017 o2;
Adafruit_MCP23017 i1;

void zapalRaspberry(bool on);
void setup() {

  Serial.begin(9600);

  // put your setup code here, to run once:
  o1.begin((uint8_t)0);
  i1.begin(1);
  o2.begin(2);

  for (int i = 0; i < 16; i++) {
    delay(5);
    if (i != 3) {
      o1.pinMode(i, OUTPUT);
      o1.digitalWrite(i, HIGH);
    }
    o2.pinMode(i, OUTPUT);
    o2.digitalWrite(i, LOW);
    if (i != 4 && i != 7)
      i1.pinMode(i, INPUT);
  }

  zapalRaspberry(true);
}
#define LAZIENKA_LEWE        1
#define LAZIENKA_PRAWE       2

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

void zapalRaspberry(bool on) {
  o1.digitalWrite(RASPBERRY, on ? LOW : HIGH);
}

void zapalMonitor(bool on) {
  o1.digitalWrite(MONITOR, on ? LOW : HIGH);
}

void zapalRadio(bool on) {
  o1.digitalWrite(RADIO, on ? LOW : HIGH);
}

void zapalWanna(bool on) {
  o1.digitalWrite(WANNA_LEWE, on ? LOW : HIGH);
  o1.digitalWrite(WANNA_PRAWE, on ? LOW : HIGH);
}

void zapalLustro(bool on) {
  o1.digitalWrite(LUSTRO_LEWE, on ? LOW : HIGH);
  o1.digitalWrite(LUSTRO_PRAWE, on ? LOW : HIGH);
}

void zapalPrysznic(bool on) {
  o1.digitalWrite(PRYSZNIC_LEWY_TYLNY, on ? LOW : HIGH);
  o1.digitalWrite(PRYSZNIC_PRAWY_TYLNY, on ? LOW : HIGH);
  o1.digitalWrite(PRYSZNIC_LEWY_PRZOD, on ? LOW : HIGH);
  o1.digitalWrite(PRYSZNIC_PRAWY_PRZOD, on ? LOW : HIGH);
}

void zapalLazienka(bool on1, bool on2) {
  
  if (on1) {
    o1.digitalWrite(LAZIENKA, LOW);
    o1.digitalWrite(LAZIENKA_LEWE, on1 ? LOW : HIGH);
    o1.digitalWrite(LAZIENKA_PRAWE, on2 ? LOW : HIGH);
  } else {
    o1.digitalWrite(LAZIENKA, HIGH);
    o1.digitalWrite(LAZIENKA_LEWE, HIGH);
    o1.digitalWrite(LAZIENKA_PRAWE, HIGH);
  }
}

#define W_LAZ 0
#define W_SED_D_N 1
#define W_SED_D_P 2
#define W_SED_D_S 3
#define W_SED_D_L 4
#define W_SED_G_P 5
#define W_SED_G_S 6
#define W_SED_G_L 7
#define W_LUS_L_L 8
#define W_LUS_L_P 9
#define W_LUS_P_L 10
#define W_LUS_P_P 11
#define W_PRAC_L  12
#define W_PRAC_P  13
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


uint16_t act = 0x0000;
uint16_t prev = 0x0000;
bool zLaz = false;
void loop() {
  
  // put your main code here, to run repeatedly:
  act = i1.readGPIOAB();
  if (prev != act) {
    uint16_t m = ~act; //bity ustawione
    uint16_t c = act ^ prev ; //bity zmienione
    //Serial.println("---");
    //Serial.println(m, HEX);
    //Serial.println(c, HEX);

    if ((m & 0x0001) && (c && 0x0001)) {
      //Serial.println("Klawisz");
      //wcisniecie klawisza lazienkowego
      zLaz = zLaz ? false : true;

      //Serial.print("zaswiec");
      //Serial.println(zLaz, DEC);
      if (zLaz) {
        zapalLazienka(true, m & (1 << W_SED_D_L) );
        zapalRadio(m & (1 << W_SED_D_P));
        zapalMonitor(true);
        zapalPrysznic(m & (1 << W_SED_G_S));
        zapalLustro(m & (1 << W_SED_G_L));
        zapalWanna(m & (1 << W_SED_G_P));
      } else {
        zapalLazienka(false, false);
        zapalRadio(false);
        zapalMonitor(false);
        zapalPrysznic(false);
        zapalLustro(false);
        zapalWanna(false);
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
  }

  prev = act;
  if (Serial.available()) {
    int inByte = Serial.read();
    if (inByte >= 'a' && inByte < ('a' + 16)) { o1.digitalWrite(inByte - 'a', HIGH); Serial.print("Zapalam "); Serial.println(inByte-'a', DEC); }
    if (inByte >= 'A' && inByte < ('A' + 16)) { o1.digitalWrite(inByte - 'A', LOW); Serial.print("Gasze "); Serial.println(inByte-'A', DEC); }
    switch(inByte) {
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
        break;
      case 'q':
      case 'r':
      case 's':
      case 't':
      case 'u':
      case 'v':
        o2.digitalWrite(inByte - 'q' + 10, HIGH); Serial.print("Zapalam "); Serial.println(inByte-'q'+10, DEC);
        break;
      case ')':
        o2.digitalWrite(0, LOW); Serial.println("Gasze 0");
        break;
      case '!':
        o2.digitalWrite(1, LOW); Serial.println("Gasze 1");
        break;
      case '@':
        o2.digitalWrite(2, LOW); Serial.println("Gasze 2");
        break;
      case '#':
        o2.digitalWrite(3, LOW); Serial.println("Gasze 3");
        break;
      case '$':
        o2.digitalWrite(4, LOW); Serial.println("Gasze 4");
        break;
      case '%':
        o2.digitalWrite(5, LOW); Serial.println("Gasze 5");
        break;
      case '^':
        o2.digitalWrite(6, LOW); Serial.println("Gasze 6");
        break;
      case '&':
        o2.digitalWrite(7, LOW); Serial.println("Gasze 7");
        break;
      case '*':
        o2.digitalWrite(8, LOW); Serial.println("Gasze 8");
        break;
      case '(':
        o2.digitalWrite(9, LOW); Serial.println("Gasze 9");
        break;
      case 'Q':
      case 'R':
      case 'S':
      case 'T':
      case 'U':
      case 'V':
        o2.digitalWrite(inByte - 'Q' + 10, LOW); Serial.print("Gasze "); Serial.println(inByte-'Q'+10, DEC);
        break;
      default:
        break;
    }
  }

  delay(50);
}