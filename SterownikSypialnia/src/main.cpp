#include <Arduino.h>
#include <Adafruit_MCP23X17.h>
#include <Wire.h>

#include "decl_io.hpp"
#include "def_io.h"

#include "utils.hpp"
#include "sypialnia.hpp"
#include "salon.hpp"
#include "hol.hpp"

TwoWire wire;
Adafruit_MCP23X17 mcp[4];

#ifdef TEMP
#include <OneWire.h>
#include <DallasTemperature.h>

// Data wire is plugged into port 2 on the Arduino
#define ONE_WIRE_BUS 4
OneWire oneWire(ONE_WIRE_BUS);

// Pass our oneWire reference to Dallas Temperature.
DallasTemperature sensors(&oneWire);
#endif

void zasilanieAwaryjne(bool wieczor, bool noc, bool zasAwar);
void podswietlenie(bool wieczor, bool zasAwar);
void inputChange(uint64_t * ptrChgR, uint64_t * ptrActR);
void rozkaz();
uint8_t parseNum(uint8_t * data, uint8_t * pos);

volatile bool interr = false;

void inputchg() {
  interr = true;
}

volatile bool tiktokInter = false;

ISR(TIMER1_COMPA_vect){
  //interrupt commands for TIMER 0 here
  tiktokInter = true;
}

uint64_t g_actR = 0L;
uint64_t g_prevR = 0L;
uint64_t g_chgR = 0L;


#define INIT_PIN_LOW(X) mcp_pinMode(X); mcp_digitalWrite(X, LOW);

void setup() {
  // start serial port
#ifdef DEBUG_CODE  
  Serial.begin(115200);
#endif  
  Serial1.begin(115200);
  Serial1.println("S;D;Begin setup;");
  
  pinMode(RESETPIN, OUTPUT);
  digitalWrite(RESETPIN, HIGH);

  for (short i = 0; i < 4; i++) {
    if (!mcp[i].begin_I2C(0x20+i, &wire)) {
      Serial1.print("S;D;Address ");
      Serial1.print(0x20+i, HEX);
      Serial1.println(" not found;");
    } else {
      Serial1.print("S;D;Address ");
      Serial1.print(0x20+i, HEX);
      Serial1.println(" initialize successfully;");
      mcp[i].setupInterrupts(true, true, LOW);
    }
  }
  
  INIT_PIN_LOW(GWAR_N);
  INIT_PIN_LOW(GWAR_L);
  
  for (short p = 0; p < 64; p++) {
    mcp_pinMode(p);
    if (mcp_getPinMode(p) == OUTPUT)
      mcp_digitalWrite(p, LOW);
    else  {
      mcp_pinAttactInterrupt(p);
    }
  }

  pinMode(INTERRUPTPIN, INPUT);
  attachInterrupt(digitalPinToInterrupt(INTERRUPTPIN), inputchg, FALLING);

  uint16_t act;
  for (short i = 0; i < 4; i++) {
    act = mcp[i].readGPIOAB();
    g_actR |= act << (i*16);
  }
  
  g_chgR = 0x0l;
  g_prevR = g_actR;

  // TIMER 1 for interrupt frequency 1 Hz:
  cli(); // stop interrupts
  TCCR1A = 0; // set entire TCCR1A register to 0
  TCCR1B = 0; // same for TCCR1B
  TCNT1  = 0; // initialize counter value to 0
  // set compare match register for 1 Hz increments
  OCR1A = 62499; // = 16000000 / (256 * 1) - 1 (must be <65536)
  // turn on CTC mode
  TCCR1B |= (1 << WGM12);
  // Set CS12, CS11 and CS10 bits for 256 prescaler
  TCCR1B |= (1 << CS12) | (0 << CS11) | (0 << CS10);
  // enable timer compare interrupt
  TIMSK1 |= (1 << OCIE1A);
  sei(); // allow interrupts
#ifdef TEMP
  sensors.begin();
#endif  
  Serial1.println("S;D;End setup;");
}



bool led1 = false, led2 = false, led3 = false, led4 = false;
bool salon1 = false, salon2 = false;
bool sypialnia1 = false, sypialnia2 = false;


uint8_t actPos = 100;
uint64_t act;


void loop() {

  if (interr) {
    interr = false;
    Serial1.println("S;D;Change incoming;");
   
    g_prevR = g_actR;
    g_actR = 0L;
    for (short i = 0; i < 4; i++) {
      act = mcp[i].readGPIOAB();
      g_actR |= act << (i*16);
    }

    g_chgR = g_prevR ^ g_actR;
    if (g_chgR != 0x00) {
      inputChange(&g_chgR, &g_actR);
    }
  }
    
  if (tiktokInter) {
    tiktokInter = false;
    hol_tiktok();
  }

  if (Serial1.available()) {
    rozkaz();
  }

  if (Serial.available()) {
    uint8_t data[36];;
    size_t r = Serial.readBytes(data, 36);
    Serial.print("Receive ");
    Serial.print(r);
    Serial.println(" bytes");
    Serial1.print("Receive ");
    Serial1.print(r);
    Serial1.println(" bytes");
  
    if ( r < 2 )
      return; 

    if((data[0] != 'I' || data[1] != '=')) {
      Serial.print("'I='<>'");
      Serial.print(data[0]);
      Serial.print(data[1]);
      Serial.println("'");
      Serial1.print("'I='<>'");
      Serial1.print(data[0]);
      Serial1.print(data[1]);
      Serial1.println("'");
      return;
    }

    uint8_t pos = 2;
    uint64_t actR = 0L;
    while (pos < r) {
      actR += parseNum(data, &pos);
      actR <<= 8;
    }
    print_64val(actR);
    print1_64val(actR);



  }
}

#define IN_KL(V) bool chg_ ## V = (chgR & V) == V; bool val_ ## V = ((~actR) & V) != 0; \
      if (chg_ ## V ) { Serial.print(#V); Serial.print( " => "); Serial.println(val_ ## V); } \
      do { } while(0)
#define C_KL(V) chg_ ## V
#define V_KL(V) val_ ## V


void inputChange(uint64_t * ptrChgR, uint64_t * ptrActR)
{
  uint64_t chgR = *ptrChgR;
  uint64_t actR = *ptrActR;
  bool wieczor, noc, taryfa2, zasAwar;



#ifdef DEBUG_CODE
  Serial.print("act=");
  print_64val(actR);
  Serial.print("\r\nchg=");
  print_64val(chgR);
  Serial.print("\r\nrea=");
  print_64val(actR & chgR);
  Serial.print("\r\nbin=");
  print_64bin(actR, true);
  Serial.println("");

  uint64_t mask_i = 0x1;
  Serial.print("CHG= ");
  for (uint8_t pos = 0; pos < 64; ++pos) {
    if ((chgR & mask_i) == mask_i) {
      Serial.print(' ');
#ifdef _EXT_CODE_      
      Serial.print(_pins[pos].name);
#else      
      Serial.print(pos);
#endif
    }
    mask_i = mask_i << 1;
  }
  Serial.println("");
#endif

#ifdef DEBUG_CODE
  Serial.println("C1R C1V C2R C2V");
  Serial.print((chgR & CZUJKA1) == CZUJKA1);
  Serial.print("  ");
  Serial.print((actR & CZUJKA1) > 0);
  Serial.print("  ");
  Serial.print((chgR & CZUJKA2) == CZUJKA2);
  Serial.print("  ");
  Serial.println((actR & CZUJKA2) > 0);
#endif

  if (((chgR & CZUJKA1) == CZUJKA1) || ((chgR & CZUJKA2) == CZUJKA2)) 
    mcp_digitalWrite(CZUJKA_RUCHU, (((actR & CZUJKA1) | (actR & CZUJKA2)) > 0) ? HIGH : LOW);

  wieczor = !((actR & SIG_WIECZOR) == SIG_WIECZOR);
  noc = !((actR & SIG_NOC) == SIG_NOC);
  taryfa2 = !((actR & SIG_2TARYFA) == SIG_2TARYFA);
  zasAwar = !((actR & SIG_ZAS_AWAR) == SIG_ZAS_AWAR);

#ifdef DEBUG_CODE
  Serial.println("W N 2 A OFF/CH_OFF");
  Serial.print(wieczor);
  Serial.print(' ');
  Serial.print(noc);
  Serial.print(' ');
  Serial.print(taryfa2);
  Serial.print(' ');
  Serial.print(zasAwar);
  Serial.print(' ');
  Serial.print(((actR & Z24_OFF) == 0) ? '0' : '1');
  Serial.print(' ');
  Serial.println((chgR & Z24_OFF) == Z24_OFF);
#else
  (void)taryfa2;
#endif  

  if ((chgR & SIG_ZAS_AWAR) == SIG_ZAS_AWAR) {
    zasilanieAwaryjne(wieczor, noc, zasAwar);
    podswietlenie(wieczor, zasAwar);
    return;
  }

  if ((chgR & Z24_OFF) == Z24_OFF && ((actR & Z24_OFF) == 0)) {
    hol_off();
    sypialnia_off();
    salon_off();
    podswietlenie(wieczor, zasAwar);
    return;
  }

  if ((chgR & Z24_OFF) == Z24_OFF && ((actR & Z24_OFF) == 1)) {
    mcp_digitalWrite(OSW_SYPIALNIA3, HIGH);
  }
  {
    IN_KL(KL03_SALJAD_LL);
    IN_KL(KL03_SALJAD_LP);
    IN_KL(KL04_SALJAD_PL);
    IN_KL(KL04_SALJAD_PP);

    if ( C_KL(KL03_SALJAD_LL) || C_KL(KL03_SALJAD_LP) || C_KL(KL04_SALJAD_PL) || C_KL(KL04_SALJAD_PP) )
        SalonJadalnia(wieczor, noc, zasAwar, 
          V_KL(KL03_SALJAD_LL) , V_KL(KL03_SALJAD_LP), V_KL(KL04_SALJAD_PL), V_KL(KL04_SALJAD_PP));
  }

  {
    IN_KL(KL02_SALKUC_LL);
    IN_KL(KL02_SALKUC_LP);
    IN_KL(KL01_SALKUC_PL);
    IN_KL(KL01_SALKUC_PP);

    if ( C_KL(KL02_SALKUC_LL) || C_KL(KL02_SALKUC_LP) || C_KL(KL01_SALKUC_PL) || C_KL(KL01_SALKUC_PP) )
      SalonKuchnia(wieczor, noc, zasAwar, 
        V_KL(KL02_SALKUC_LL), V_KL(KL02_SALKUC_LP), V_KL(KL01_SALKUC_PL), V_KL(KL01_SALKUC_PP));
  }

  {
    IN_KL(KL07_SALSYP_LL);
    IN_KL(KL07_SALSYP_LP);
    IN_KL(KL06_SALSYP_PL);
    IN_KL(KL06_SALSYP_PP);
    
    if ( C_KL(KL07_SALSYP_LL) || C_KL(KL07_SALSYP_LP) || C_KL(KL06_SALSYP_PL) || C_KL(KL06_SALSYP_PP) )
      SalonSypialnia(wieczor, noc, zasAwar, 
        V_KL(KL07_SALSYP_LL), V_KL(KL07_SALSYP_LP),
        V_KL(KL06_SALSYP_PL), V_KL(KL06_SALSYP_PP));
  }

  {
    IN_KL(KL08_SALPRZ_LL);
    IN_KL(KL08_SALPRZ_LP);

    if ( C_KL(KL08_SALPRZ_LL) || C_KL(KL08_SALPRZ_LP) ) 
      Salon(wieczor, noc, zasAwar, 
        V_KL(KL08_SALPRZ_LL), V_KL(KL08_SALPRZ_LP));
  }

  {
    IN_KL(KL11_SALLAZ_L);
    IN_KL(KL11_SALLAZ_P);

    if ( C_KL(KL11_SALLAZ_L) || C_KL(KL11_SALLAZ_P) ) 
      SalonLedLaz(wieczor, noc, zasAwar, 
        V_KL(KL11_SALLAZ_L), V_KL(KL11_SALLAZ_P));
  }

  {
    IN_KL(KL05_SYPIAL_L);
    IN_KL(KL05_SYPIAL_P);

    //sypialnia
    if ( C_KL(KL05_SYPIAL_L) || C_KL(KL05_SYPIAL_P) ) 
      Sypialnia(wieczor, noc, zasAwar, 
        V_KL(KL05_SYPIAL_L), V_KL(KL05_SYPIAL_P));

  }

  {
    IN_KL(KL10_HOLSYP_LL);
    IN_KL(KL10_HOLSYP_LP);
    IN_KL(KL09_HOLSYP_PL);
    IN_KL(KL09_HOLSYP_PP);
    IN_KL(KL12_HOLLAZ_L);
    IN_KL(KL12_HOLLAZ_P);
    IN_KL(KL14_HOLWC_L);
    IN_KL(KL14_HOLWC_P);
    IN_KL(KL13_HOLPOK);
    IN_KL(KL15_HOLWEJ);

    //hol i przedpokoj
    if ( C_KL(KL10_HOLSYP_LL) || C_KL(KL10_HOLSYP_LP) || C_KL(KL09_HOLSYP_PL) || C_KL(KL09_HOLSYP_PP) ||
         C_KL(KL12_HOLLAZ_L)  || C_KL(KL12_HOLLAZ_P)  || C_KL(KL14_HOLWC_L)   || C_KL(KL14_HOLWC_P)   ||
         C_KL(KL13_HOLPOK)    || C_KL(KL15_HOLWEJ) )
      Hol(wieczor, noc, zasAwar, 
        V_KL(KL10_HOLSYP_LL), V_KL(KL10_HOLSYP_LP), V_KL(KL14_HOLWC_L), V_KL(KL14_HOLWC_P),
        V_KL(KL12_HOLLAZ_L), V_KL(KL12_HOLLAZ_P), V_KL(KL09_HOLSYP_PL), V_KL(KL09_HOLSYP_PP),
        V_KL(KL13_HOLPOK), V_KL(KL15_HOLWEJ));
  }

  podswietlenie(wieczor, zasAwar);
}

void zasilanieAwaryjne(bool wieczor, bool noc, bool zasAwar)
{
  for (short p = 0; p < 64; p++) {
    if (p == GWAR_L || p == GWAR_N)
      continue;
    if (mcp_getPinMode(p) == OUTPUT)
      mcp_digitalWrite(p, LOW);
  }
  
  delay(50);
  mcp_digitalWrite(GWAR_N, zasAwar ? HIGH : LOW);
  mcp_digitalWrite(GWAR_L, zasAwar ? HIGH : LOW);
  delay(50);
  SypialniaZasAwar(wieczor, noc, zasAwar);
  SalonZasAwar(wieczor, noc, zasAwar);
  HolZasAwar(wieczor, noc, zasAwar);


  return;
}


void podswietlenie(bool wieczor, bool zasAwar)
{
  bool w1 = !zasAwar && wieczor;
  bool a = w1 && !salon_isOn();
  bool b = w1 && !hol_isOn();
  bool c = a && b;
  mcp_digitalWrite(PODSW_SALON_A, a ? LOW : HIGH);
  mcp_digitalWrite(PODSW_HOL_B,  b ? LOW : HIGH);
  mcp_digitalWrite(PODSW_MIX_C, c ? LOW : HIGH);

  mcp_digitalWrite(SWIATLO_SALON, salon_isOn() ? HIGH : LOW); //wyjscia opto
  mcp_digitalWrite(SWIATLO_SYPIALNIA, sypialnia_isOn() ? HIGH : LOW); //wyjscia opto
  mcp_digitalWrite(SWIATLO_HOL, hol_isOn() ? HIGH : LOW); //wyjscia opto
}

void rozkaz()
{
#ifdef RS485
  uint8_t data[16] = {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0};
  size_t r = Serial1.readBytes(data, 16);

  if ( r < 2 ) {
    return;
  }

  if (data[0] == 'I'  && data[1] == ';') {
    Serial1.println("S;");
    return;
  }
  
  if (data[0] == 'S' && data[1] != ';') {
    Serial1.print("S;E;");
    Serial1.print(__LINE__, DEC);
    Serial1.println(";");
    return;
  }

  if (data[2] == 'I' && data[3] == ';') {
#ifdef DEBUG_CODE
    Serial.print("act=");
    print_64val(g_actR);
    Serial.print("\r\nchg=");
    print_64val(g_chgR);
    Serial.print("\r\nrea=");
    print_64val(g_actR & g_chgR);
    Serial.print("\r\nbin=");
    print_64bin(g_actR, true);
    Serial.println("");
#endif
    Serial1.print("S;I;");
    print1_64val(g_actR);
    Serial1.println(";");
  }

  if (data[2] == 'F' && data[3] == ';') {
    uint8_t valPos = 6;
    uint8_t index = data[4] - '0';
    if (data[5] >= '0' && data[5] <= '9') {
      index = index * 10 + data[5] - '0';
      ++valPos;
      if (data[6] != ';') {
        Serial1.print("S;E;");
        Serial1.print(__LINE__, DEC);
        Serial1.print(";");
        return; 
      }
    } else if (data[5] != ';') {
      Serial1.print("S;E;");
      Serial1.print(__LINE__, DEC);
      Serial1.print(";");
      return;
    }

    Serial.print("k_index=");
    Serial.println(index, DEC);
    
    uint8_t val = 0;
    if (data[valPos] != '0' && data[valPos] != '1' && data[valPos+1] != ';') {
      Serial1.print("S;E;");
      Serial1.print(__LINE__, DEC);
      Serial1.print(";");
      return;
    } else {
      val = data[valPos] - '0';
    }
    
    Serial1.println("S;A;");

    //uint64_t actR = g_actR;
    //uint64_t chgR = g_chgR;
    switch(index) {
      case 0:
        g_chgR |= Z216_01;
        g_actR = val ? (g_actR | Z216_01) : (g_actR & ~Z216_01);
        inputChange(&g_chgR, &g_actR);
        break;

      default:
        break;
    }
    g_actR = 0L;
    for (short i = 0; i < 4; i++) {
      act = mcp[i].readGPIOAB();
      g_actR |= act << (i*16);
    }
  }
  
  if (data[2] == 'S' && data[3] == ';') {
    uint8_t valPos = 6;
    uint8_t index = data[4] - '0';
    if (data[5] >= '0' && data[5] <= '9') {
      index = index * 10 + data[5] - '0';
      ++valPos;
      if (data[6] != ';') {
        Serial1.print("S;E;");
        Serial1.print(__LINE__, DEC);
        Serial1.print(";");
        return; 
      }
    } else if (data[5] != ';') {
      Serial1.print("S;E;");
      Serial1.print(__LINE__, DEC);
      Serial1.print(";");
      return;
    }

    Serial.print("index=");
    Serial.println(index, DEC);
    
    //TODO dodac algo wlaczania swiatla
    uint8_t val = 0;
    if (data[valPos] != '0' && data[valPos] != '1' && data[valPos+1] != ';') {
      Serial1.print("S;E;");
      Serial1.print(__LINE__, DEC);
      Serial1.print(";");
      return;
    } else {
      val = data[valPos] - '0';
    }
    
    Serial1.println("S;A;");

    switch(index) {
      case 4: //ledy kolo lazienki 1
      case 5: //ledy kolo lazienki 2
      case 14: //ledy kolo salonu 2
      case 15: //ledy kolo salonu 1
      case 16+12: //Salon 2
      case 16+15: //Salon 1
        salon_req(index, val); break;
      
      case 6: //hol 3.1
      case 7: //hol 3.2
      case 8: //hol 3.3 
      case 9: //hol 4.4
      case 10: //hol 4.3
      case 11: //hol 4.2
      case 12: //hol 4.1
      case 16+10: //Przedpokoj A0
        hol_req(index, val); break;

      case 16+8: //sypialnia 2
      case 16+9: //sypialnia kinkiety
      case 16+11: //sypialnia 1
        sypialnia_req(index, val); break;

      case 16+5: //podswitelenie mix
        mcp_digitalWrite(PODSW_MIX_C, val); break; 
        
      case 16+6: //podswitelenie holu
        mcp_digitalWrite(PODSW_HOL_B, val); break;

      case 16+7: //podswitelenie salonu
        mcp_digitalWrite(PODSW_SALON_A, val); break;

      default: break;
    }
  }

#ifdef TEMP
  if (data[2] == 'T' && data[3] == ';') {
    sensors.requestTemperatures(); // Send the command to get temperatures
    
    Serial1.print("S;T;");
    Serial1.print(sensors.getTempCByIndex(0));
    Serial1.print(";");
  }
#endif  
#endif  
}

uint8_t parseNum(uint8_t * data, uint8_t * pos)
{
  uint8_t r = 0;
  if (data[*pos] == ' ' || data[*pos] == '\r' || data[*pos] == '\n' || data[*pos] == '\0') {
    (*pos)++;
    return r;
  }

  r = data[*pos] - '0';
  (*pos)++;

  if (data[*pos] == ' ') {
    (*pos)++;
    return r;
  }
  r = 10 * r + data[*pos] - '0';
  (*pos)++;

  if (data[*pos] == ' ') {
    (*pos)++;
    return r;
  }
  r = 10 * r + data[*pos] - '0';
  (*pos)++;
  return r;
}