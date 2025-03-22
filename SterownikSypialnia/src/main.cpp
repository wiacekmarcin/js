#include <Arduino.h>
#include <Adafruit_MCP23X17.h>
#include <Wire.h>

#include "decl_io.h"
#include "def_io.h"

#include "utils.hpp"
#include "sypialnia.hpp"
#include "salon.hpp"
#include "hol.hpp"

TwoWire wire;
Adafruit_MCP23X17 mcp[4];

volatile bool interr = false;

void inputchg() {
  interr = true;
}

uint64_t actR = 0L;
uint64_t prevR = 0L;
uint64_t chgR = 0L;

bool wieczor = false, noc = false, taryfa2 = false, zasAwar = false;

void setup() {
  Serial.begin(57600);
  //while (!Serial)
  //  delay(100);
  

  pinMode(RESETPIN, OUTPUT);
  digitalWrite(RESETPIN, HIGH);

  for (short i = 0; i < 4; i++) {
    if (!mcp[i].begin_I2C(0x20+i, &wire)) {
      Serial.print("Address ");
      Serial.print(0x20+i, HEX);
      Serial.println(" not found");
    } else {
      Serial.print("Address ");
      Serial.print(0x20+i, HEX);
      Serial.println(" initialize successfully");
      mcp[i].setupInterrupts(true, true, LOW);
    }
  }

  Serial.println("Configuring pins...");

  mcp[3].pinMode(7, OUTPUT);
  mcp[3].pinMode(14, OUTPUT);

  //Konfiguracja pinow gwarantowanych i od ledow (wyzwalane poziomem niskim)
  mcp_digitalWrite(GWAR_L, LOW);
  mcp_digitalWrite(GWAR_N, LOW);
  mcp_digitalWrite(Z213_3_LEDY_CH1, LOW);
  mcp_digitalWrite(Z213_4_LEDY_CH2, LOW);
  mcp_digitalWrite(Z213_5_LEDY_CH3, LOW);
  mcp_digitalWrite(Z213_6_LEDY_CH4, LOW);

  mcp_pinMode(GWAR_L);
  mcp_pinMode(GWAR_N);
  mcp_pinMode(Z213_3_LEDY_CH1);
  mcp_pinMode(Z213_4_LEDY_CH2);
  mcp_pinMode(Z213_5_LEDY_CH3);
  mcp_pinMode(Z213_6_LEDY_CH4);

  mcp_digitalWrite(GWAR_L, LOW);
  mcp_digitalWrite(GWAR_N, LOW);
  mcp_digitalWrite(Z213_3_LEDY_CH1, LOW);
  mcp_digitalWrite(Z213_4_LEDY_CH2, LOW);
  mcp_digitalWrite(Z213_5_LEDY_CH3, LOW);
  mcp_digitalWrite(Z213_6_LEDY_CH4, LOW);

  
  for (short p = 0; p < 64; p++) {
    mcp_pinMode(p);
    if (mcp_getPinMode(p) == OUTPUT)
      mcp_digitalWrite(p, LOW);
    else  {
      mcp_pinAttactInterrupt(p);
    }
  }

  for (short i = 0; i < 4; i++) {
    Serial.print(i);
    Serial.print(" ");
    Serial.println(mcp[i].getCapturedInterrupt(), HEX);
  }

  Serial.println("Done");

  pinMode(INTERRUPTPIN, INPUT);
  attachInterrupt(digitalPinToInterrupt(INTERRUPTPIN), inputchg, FALLING);

  uint16_t act;
  for (short i = 0; i < 4; i++) {
    act = mcp[i].readGPIOAB();
    actR |= act << (i*16);
  }
  
  chgR = 0x0l;
  prevR = actR;

  wieczor = !((actR & SIG_WIECZOR) == SIG_WIECZOR);
  noc = !((actR & SIG_NOC) == SIG_NOC);
  taryfa2 = !((actR & SIG_2TARYFA) == SIG_2TARYFA);
  zasAwar = !((actR & SIG_ZAS_AWAR) == SIG_ZAS_AWAR);

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

  Serial1.begin(115200);

}

volatile bool tiktokInter = false;
ISR(TIMER0_COMPA_vect){
  //interrupt commands for TIMER 0 here
  tiktokInter = true;
}

bool led1 = false, led2 = false, led3 = false, led4 = false;
bool salon1 = false, salon2 = false;
bool sypialnia1 = false, sypialnia2 = false;


uint8_t actPos = 100;
uint64_t act;
void loop() {

  if (interr) {
    interr = false;
    prevR = actR;
    actR = 0L;
  
    for (short i = 0; i < 4; i++) {
      act = mcp[i].readGPIOAB();
      actR |= act << (i*16);
    }
    
    chgR = prevR ^ actR;
    if (chgR == 0x00)
      return;

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
        Serial.print(" ");
        Serial.print(_pins[pos].name);
      }
      mask_i = mask_i << 1;
    }
    Serial.println("");

    if ((chgR & SIG_WIECZOR) == SIG_WIECZOR)
      wieczor = !((actR & SIG_WIECZOR) == SIG_WIECZOR);

    if ((chgR & SIG_NOC) == SIG_NOC)
      noc = !((actR & SIG_NOC) == SIG_NOC);

    if ((chgR & SIG_2TARYFA) == SIG_2TARYFA)
      taryfa2 = !((actR & SIG_2TARYFA) == SIG_2TARYFA);

    if ((chgR & SIG_ZAS_AWAR) == SIG_ZAS_AWAR) {
      zasAwar = !((actR & SIG_ZAS_AWAR) == SIG_ZAS_AWAR);
      for (short p = 0; p < 64; p++) {
        if (p == GWAR_L || p == GWAR_N)
          continue;
        if (mcp_getPinMode(p) == OUTPUT)
          mcp_digitalWrite(p, LOW);
      }
      
      delay(50);
      mcp_digitalWrite(GWAR_N, zasAwar ? HIGH : LOW);
      mcp_digitalWrite(GWAR_L, zasAwar ? HIGH : LOW);
      
      SypialniaZasAwar(wieczor, zasAwar);
      SalonZasAwar(wieczor, zasAwar);

      if (wieczor) {
        mcp_digitalWrite(OSW_SALON1, HIGH);
      }
      return;
    }
    
    Serial.println("W N 2 A OFF");
    Serial.print(wieczor);
    Serial.print(" ");
    Serial.print(noc);
    Serial.print(" ");
    Serial.print(taryfa2);
    Serial.print(" ");
    Serial.print(zasAwar);
    Serial.print(" ");
    Serial.println((chgR & Z24_OFF) == Z24_OFF);

    if ((chgR & Z24_OFF) == Z24_OFF && ((actR & Z24_OFF) == 0)) {
      for (uint8_t i = 0; i < 64; i++) {
        if (!isOutput(i))
          continue;
        
        if (i == GWAR_N || i == GWAR_L || i == CZUJKA_RUCHU)
          continue;

        if (i > SWIATLO_SALON)
          break;        
          
        mcp_digitalWrite(i, LOW);
      }
      return;
    }

    if (((chgR & CZUJKA1) == CZUJKA1) || ((chgR & CZUJKA2) == CZUJKA2)) 
      mcp_digitalWrite(CZUJKA_RUCHU, ((actR & CZUJKA1) | (actR & CZUJKA2)) ? HIGH : LOW);

    if ( ( (chgR & KL03_SALJAD_LL) == KL03_SALJAD_LL) || ( (chgR & KL03_SALJAD_LP) == KL03_SALJAD_LP) || 
         ( (chgR & KL04_SALJAD_PL) == KL04_SALJAD_PL) || ( (chgR & KL04_SALJAD_PP) == KL04_SALJAD_PP) )
        SalonJadalnia(wieczor, noc, zasAwar, 
         !((actR & KL03_SALJAD_LL) == KL03_SALJAD_LL), !((actR & KL03_SALJAD_LP) == KL03_SALJAD_LP),
         !((actR & KL04_SALJAD_PL) == KL04_SALJAD_PL), !((actR & KL04_SALJAD_PP) == KL04_SALJAD_PP));

    if ( ( (chgR & KL02_SALKUC_LL) == KL02_SALKUC_LL) || ( (chgR & KL02_SALKUC_LP) == KL02_SALKUC_LP) || 
         ( (chgR & KL01_SALKUC_PL) == KL01_SALKUC_PL) || ( (chgR & KL01_SALKUC_PP) == KL01_SALKUC_PP) )
        SalonKuchnia(wieczor, noc, zasAwar, 
         !((actR & KL02_SALKUC_LL) == KL02_SALKUC_LL), !((actR & KL02_SALKUC_LP) == KL02_SALKUC_LP),
         !((actR & KL01_SALKUC_PL) == KL01_SALKUC_PL), !((actR & KL01_SALKUC_PP) == KL01_SALKUC_PP));

    if ( ( (chgR & KL07_SALSYP_LL) == KL07_SALSYP_LL) || ( (chgR & KL07_SALSYP_LP) == KL07_SALSYP_LP) || 
         ( (chgR & KL06_SALSYP_PL) == KL06_SALSYP_PL) || ( (chgR & KL06_SALSYP_PP) == KL06_SALSYP_PP) )
        SalonSypialnia(wieczor, noc, zasAwar, 
         !((actR & KL07_SALSYP_LL) == KL07_SALSYP_LL), !((actR & KL07_SALSYP_LP) == KL07_SALSYP_LP),
         !((actR & KL06_SALSYP_PL) == KL06_SALSYP_PL), !((actR & KL06_SALSYP_PP) == KL06_SALSYP_PP));
    
    if ( ( (chgR & KL08_SALPRZ_LL) == KL08_SALPRZ_LL) || ( (chgR & KL08_SALPRZ_LP) == KL08_SALPRZ_LP) ) 
        Salon(wieczor, noc, zasAwar, 
          !((actR & KL08_SALPRZ_LL) == KL08_SALPRZ_LL), !((actR & KL08_SALPRZ_LP) == KL08_SALPRZ_LP));
    
    if ( ( (chgR & KL11_SALLAZ_L) == KL11_SALLAZ_L) || ( (chgR & KL11_SALLAZ_P) == KL11_SALLAZ_P) ) 
          SalonLedLaz(wieczor, noc, zasAwar, 
            !((actR & KL11_SALLAZ_L) == KL11_SALLAZ_L), !((actR & KL11_SALLAZ_P) == KL11_SALLAZ_P));
    
    //sypialnia
    if ( ( (chgR & KL05_SYPIAL_L) == KL05_SYPIAL_L) || ( (chgR & KL05_SYPIAL_P) == KL05_SYPIAL_P) ) 
          Sypialnia(wieczor, noc, zasAwar, 
            !((actR & KL05_SYPIAL_L) == KL05_SYPIAL_L), !((actR & KL05_SYPIAL_P) == KL05_SYPIAL_P));
    
    
    //hol i przedpokoj
    if ( ( (chgR & KL10_HOLSYP_LL) == KL10_HOLSYP_LL) || ( (chgR & KL10_HOLSYP_LP) == KL10_HOLSYP_LP) ||
         ( (chgR & KL09_HOLSYP_PL) == KL09_HOLSYP_PL) || ( (chgR & KL09_HOLSYP_PP) == KL09_HOLSYP_PL) ||
         ( (chgR & KL12_HOLLAZ_L)  == KL12_HOLLAZ_L)  || ( (chgR & KL12_HOLLAZ_P)  == KL12_HOLLAZ_P) ||
         ( (chgR & KL14_HOLWC_L)   == KL14_HOLWC_L)   || ( (chgR & KL14_HOLWC_P)   == KL14_HOLWC_P) ||
         ( (chgR & KL13_HOLPOK)    == KL13_HOLPOK)    || ( (chgR & KL15_HOLWEJ)    == KL15_HOLWEJ) )
          Hol(wieczor, noc, zasAwar, 
            !((actR & KL10_HOLSYP_LL) == KL10_HOLSYP_LL), !((actR & KL10_HOLSYP_LP) == KL10_HOLSYP_LP),
            !((actR & KL14_HOLWC_L) == KL14_HOLWC_L), !((actR & KL14_HOLWC_L) == KL14_HOLWC_L),
            !((actR & KL12_HOLLAZ_L) == KL12_HOLLAZ_L), !((actR & KL12_HOLLAZ_P) == KL12_HOLLAZ_P),
            !((actR & KL09_HOLSYP_PL) == KL09_HOLSYP_PL), !((actR & KL09_HOLSYP_PP) == KL09_HOLSYP_PP),
            !((actR & KL13_HOLPOK) == KL13_HOLPOK), !((actR & KL15_HOLWEJ) == KL15_HOLWEJ)
          );
    
    mcp_digitalWrite(ZAS12V, (led1 || led2 || led3 || led4) ? HIGH : LOW);
    mcp_digitalWrite(SWIATLO_SALON, (led1 || led2 || led3 || led4 || salon1 || salon2) ? HIGH : LOW); //wyjscia opto
    mcp_digitalWrite(SWIATLO_SYPIALNIA, (sypialnia1 || sypialnia2) ? HIGH : LOW); //wyjscia opto
    mcp_digitalWrite(SWIATLO_HOL, hol_isOn() ? HIGH : LOW); //wyjscia opto


    if (!zasAwar && wieczor) {
      mcp_digitalWrite(PODSW_SALON_A, (led1 || led2 || led3 || led4 || salon1 || salon2) ? LOW : HIGH);
      mcp_digitalWrite(PODSW_HOL_B, hol_isOn() ? LOW : HIGH);
      mcp_digitalWrite(PODSW_MIX_C, (led1 || led2 || led3 || led4 || salon1 || salon2 || hol_isOn()) ? LOW : HIGH);
    }

    mcp_digitalWrite(OSW_SYPIALNIA3, zasAwar ? LOW : HIGH);

    actR = 0L;
    for (short i = 0; i < 4; i++) {
      act = mcp[i].readGPIOAB();
      actR |= act << (i*16);
    }
    Serial.print("output=");
    print_64bin(actR, false);
    Serial.println("");
    print_64Out(actR);
  }


  if (tiktokInter) {
    tiktokInter = false;
    hol_tiktok();
    Serial.println("tik tok");

  }

  if (Serial1.available()) {
    uint8_t data[32] = {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0};
    size_t r = Serial1.readBytes(data, 31);
    if ( r < 2 )
      return;
    if (data[0] == 'I'  && data[1] != ';') {
      Serial1.println("S;");
      return;
    }
    
    if (data[0] != 'S' && data[1] != ';') {
      Serial1.print("S;E;");
      Serial1.print(__LINE__, DEC);
      Serial1.print(";");
      return;
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
  }
}
