#include <Arduino.h>
#include <Adafruit_MCP23X17.h>
#include <Wire.h>
#include "def_io.h"

TwoWire wire;
Adafruit_MCP23X17 mcp[4];
inline void mcp_pinMode(short ps) {
  mcp[_pins[ps].mod_id].pinMode(_pins[ps].pin_id, _pins[ps].io_type);
}

inline void mcp_digitalWrite(short ps, short value) {
  short svalue = (ps == GWAR_L || ps == GWAR_N || ps == Z213_3_LEDY_CH1 || ps == Z213_4_LEDY_CH2 
          || ps == Z213_5_LEDY_CH3|| ps == Z213_6_LEDY_CH4) ? !value : value;
  if (_pins[ps].io_type == OUTPUT) {
    mcp[_pins[ps].mod_id].digitalWrite(_pins[ps].pin_id, svalue);
  }
  //mcp[_pins[ps].mod_id].
}

inline bool isOutput(short ps) {
  return _pins[ps].io_type == OUTPUT; 
}

inline void mcp_pinAttactInterrupt(short ps) {
  mcp[_pins[ps].mod_id].setupInterruptPin(_pins[ps].pin_id, CHANGE);
}

inline void mcp_print(short ps) {
  Serial.print(ps);
  Serial.print(":");
  Serial.print(_pins[ps].mod_id);
  Serial.print(":");
  if (_pins[ps].pin_id < 8) {
    Serial.print("A");
    Serial.print(_pins[ps].pin_id);
  } else {
    Serial.print("B");
    Serial.print(_pins[ps].pin_id-8);
  }
  Serial.print(":");
  Serial.println(_pins[ps].name);

}

inline short mcp_getPinMode(short ps) {
  return _pins[ps].io_type;
}

volatile bool interr = false;

void inputchg() {
  interr = true;
}

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
    else {
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
}
 
bool wieczor, noc, taryfa2, zasAwar;

bool led1 = false, led2 = false, led3 = false, led4 = false;
bool salon1 = false, salon2 = false;
bool sypialnia1 = false, sypialnia2 = false;
uint8_t bhol = 0x00;

void SalonJadalnia(bool wieczor, bool noc, bool awaria, bool klLL, bool klLP, bool klPL, bool klPP)
{
  static unsigned long mls = 0;
  if (millis() - mls < 50)
    return;

  Serial.println("SalonJadalnia");
  Serial.println("LL LP PL PP");
  Serial.print(" ");
  Serial.print(klLL);
  Serial.print("  ");
  Serial.print(klLP);
  Serial.print("  ");
  Serial.print(klPL);
  Serial.print("  ");
  Serial.println(klPP);
  mls = millis();

  if (awaria) {
    if (klLL || klLP || klPL || klPP) { 
      salon1 = !salon1;
      mcp_digitalWrite(OSW_SALON1, (salon1) ? HIGH : LOW);
      return;
    }
  }

  if (noc) {
    if ((klLL || klLP || klPL || klPP) && !led1 && !led2 && !led3 && !led4 && !salon1 && !salon2) {
      led3 = true;
      mcp_digitalWrite(LED3_SYPIALNIA1, (led3) ? HIGH : LOW);
      return;
    }
  }

  if (klLL) {
    led3 = !led3;
    mcp_digitalWrite(LED3_SYPIALNIA1, (led3) ? HIGH : LOW);
  }

  if (klLP) {
    led4 = !led4;
    mcp_digitalWrite(LED4_SYPIALNIA2, (led4) ? HIGH : LOW);
  }

  if (klPL) {
    salon1 = !salon1;
    mcp_digitalWrite(OSW_SALON1, (salon1) ? HIGH : LOW);
  }

  if (klLP) {
    salon2 = !salon2;
    mcp_digitalWrite(OSW_SALON2, (salon2) ? HIGH : LOW);
  }

  return;
}

void SalonKuchnia(bool wieczor, bool noc, bool awaria, bool klLL, bool klLP, bool klPL, bool klPP)
{
  static unsigned long mls = 0;
  if (millis() - mls < 50)
    return;

  Serial.println("SalonKuchnia");
  Serial.println("LL LP PL PP");
  Serial.print(" ");
  Serial.print(klLL);
  Serial.print("  ");
  Serial.print(klLP);
  Serial.print("  ");
  Serial.print(klPL);
  Serial.print("  ");
  Serial.println(klPP);
  mls = millis();

  if (awaria) {
    if (klLL || klLP || klPL || klPP) {
      salon1 = !salon1;
      mcp_digitalWrite(OSW_SALON1, (salon1) ? HIGH : LOW);
      return;
    }
  }

  if (noc) {
    if ((klLL || klLP || klPL || klPP) && !led1 && !led2 && !led3 && !led4 && !salon1 && !salon2) {
      led1 = true;
      mcp_digitalWrite(LED1_LAZIENKA1, (led1) ? HIGH : LOW);
      return;
    }
  }

  if (klLL) {
    led1 = !led1;
    mcp_digitalWrite(LED1_LAZIENKA1, (led1) ? HIGH : LOW);
  }

  if (klLP) {
    led2 = !led2;
    mcp_digitalWrite(LED2_LAZIENKA2, (led2) ? HIGH : LOW);
  }

  if (klPL) {
    salon1 = !salon1;
    mcp_digitalWrite(OSW_SALON1, (salon1) ? HIGH : LOW);
  }

  if (klLP) {
    salon2 = !salon2;
    mcp_digitalWrite(OSW_SALON2, (salon2) ? HIGH : LOW);
  }

  return;
}

void SalonSypialnia(bool wieczor, bool noc, bool awaria, bool klLL, bool klLP, bool klPL, bool klPP)
{
  static unsigned long mls = 0;
  if (millis() - mls < 50)
    return;

  Serial.println("SalonSypialnia");
  Serial.println("LL LP PL PP");
  Serial.print(" ");
  Serial.print(klLL);
  Serial.print("  ");
  Serial.print(klLP);
  Serial.print("  ");
  Serial.print(klPL);
  Serial.print("  ");
  Serial.println(klPP);
  mls = millis();

  if (awaria) {
    if (klLL || klLP || klPL || klPP) {
      salon1 = !salon1;
      mcp_digitalWrite(OSW_SALON1, (salon1) ? HIGH : LOW);
    }
    return;
  }

  if (noc) {
    if ((klLL || klLP || klPL || klPP) && !led1 && !led2 && !led3 && !led4 && !salon1 && !salon2) {
      led3 = true;
      mcp_digitalWrite(LED3_SYPIALNIA1, (led3) ? HIGH : LOW);
      return;
    }
  }

  if (klLL) {
    led3 = !led3;
    mcp_digitalWrite(LED3_SYPIALNIA1, (led3) ? HIGH : LOW);
  }

  if (klLP) {
    led4 = !led4;
    mcp_digitalWrite(LED4_SYPIALNIA2, (led4) ? HIGH : LOW);
  }

  if (klPL) {
    salon1 = !salon1;
    mcp_digitalWrite(OSW_SALON1, (salon1) ? HIGH : LOW);
  }

  if (klLP) {
    salon2 = !salon2;
    mcp_digitalWrite(OSW_SALON2, (salon2) ? HIGH : LOW);
  }

  return;
}

void Salon(bool wieczor, bool noc, bool awaria, bool klL, bool klP)
{
  static unsigned long mls = 0;
  if (millis() - mls < 50)
    return;

  Serial.println("Salon");
  Serial.println("L P");
  Serial.print(klL);
  Serial.print(" ");
  Serial.print(klP);
  mls = millis();

  if (awaria) {
    if (klL || klP) {
      salon1 = !salon1;
      mcp_digitalWrite(OSW_SALON1, (salon1) ? HIGH : LOW);
      return;
    }
  }

  if (noc) {
    if ((klL || klP) && !led1 && !led2 && !led3 && !led4 && !salon1 && !salon2) {
      led3 = true;
      mcp_digitalWrite(LED3_SYPIALNIA1, (led3) ? HIGH : LOW);
      return;
    }
  }

  if (klL) {
    salon1 = !salon1;
    mcp_digitalWrite(OSW_SALON1, (salon1) ? HIGH : LOW);
  }

  if (klP) {
    salon2 = !salon2;
    mcp_digitalWrite(OSW_SALON2, (salon2) ? HIGH : LOW);
  }

  return;
}

void SalonLedLaz(bool wieczor, bool noc, bool awaria, bool klL, bool klP)
{
  static unsigned long mls = 0;
  if (millis() - mls < 50)
    return;

  Serial.println("SalonLedLaz");
  Serial.println("L P");
  Serial.print(klL);
  Serial.print(" ");
  Serial.print(klP);
  mls = millis();

  if (awaria) {
    if (klL || klP) {
      salon1 = !salon1;
      mcp_digitalWrite(OSW_SALON1, (salon1) ? HIGH : LOW);
      return;
    }
  }

  if (noc) {
    if ((klL || klP) && !led1 && !led2 && !led3 && !led4 && !salon1 && !salon2) {
      led3 = true;
      mcp_digitalWrite(LED1_LAZIENKA1, (led3) ? HIGH : LOW);
      return;
    }
  }

  if (klL) {
    led1 = !led1;
    mcp_digitalWrite(LED1_LAZIENKA1, (led1) ? HIGH : LOW);
  }

  if (klP) {
    led2 = !led2;
    mcp_digitalWrite(LED2_LAZIENKA2, (led2) ? HIGH : LOW);
  }

  return;
}

void Sypialnia(bool wieczor, bool noc, bool awaria, bool klL, bool klP)
{
  static unsigned long mls = 0;
  if (millis() - mls < 50)
    return;

  Serial.println("Sypialnia");
  Serial.println("L P");
  Serial.print(klL);
  Serial.print(" ");
  Serial.print(klP);
  mls = millis();

  if (awaria) {
    if (klL || klP) {
      sypialnia1 = !sypialnia1;
      mcp_digitalWrite(OSW_SYPIALNIA1, (sypialnia1) ? HIGH : LOW);
      return;
    }
  }


  if (klL) {
    sypialnia1 = !sypialnia1;
    mcp_digitalWrite(OSW_SYPIALNIA1, (sypialnia1) ? HIGH : LOW);
  }

  if (klP) {
    sypialnia2 = !sypialnia2;
    mcp_digitalWrite(OSW_SYPIALNIA2, (sypialnia2) ? HIGH : LOW);
  }

  return;
}

void Hol(bool wieczor, bool noc, bool awaria, bool klLA1, bool klPA1, bool klLA2, bool klPA2,
                                              bool klLB1, bool klPB1, bool klLB2, bool klPB2,
                                            bool klPok, bool klWej)
{
  Serial.println("Hol");
  Serial.println("ALL ALP APL APP | BLL BLP BPL BPP | POK WEJ");
  Serial.print(" ");
  Serial.print(klLA1);
  Serial.print("   ");
  Serial.print(klPA1);
  Serial.print("   ");
  Serial.print(klLA2);
  Serial.print("   ");
  Serial.print(klPA2);
  Serial.print("  |  ");
  Serial.print(klLB1);
  Serial.print("   ");
  Serial.print(klPB1);
  Serial.print("   ");
  Serial.print(klLB2);
  Serial.print("   ");
  Serial.print(klPB2);
  Serial.print("  |  ");
  Serial.print(klPok);
  Serial.print("   ");
  Serial.print(klWej);
  if (awaria) {
    if (klLA1 || klPA1 || klLA2 || klPA2 || klLB1 || klPB1 || klLB2 || klPB2 || klPok || klWej) {
      bhol = bhol ^ (0x1);
      mcp_digitalWrite(OSW_HOL_0, ((bhol & 0x1) == 0x01) ? HIGH : LOW);
      return;
    }
  }

  if (noc) {
    if ((klLA1 || klPA1 || klLA2 || klPA2 || klLB1 || klPB1 || klLB2 || klPB2 || klPok || klWej) && bhol == 0x00) {
      bhol = bhol ^ (0x1);
      mcp_digitalWrite(OSW_HOL_0, ((bhol & 0x1) == 0x01) ? HIGH : LOW);
      return;
    }
  }

  if (noc) {
    if ((klLA1 || klPA1 || klLA2 || klPA2 || klLB1 || klPB1 || klLB2 || klPB2 || klPok || klWej) && bhol == 0x01) {
      bhol = 0x00;
      mcp_digitalWrite(OSW_HOL_0, LOW);
    }
  }

  if (wieczor) {
    if ((klLA1 || klPA1 || klLA2 || klPA2 || klLB1 || klPB1 || klLB2 || klPB2 || klPok || klWej) && bhol == 0x00) {
      bhol = 0x01;
      mcp_digitalWrite(OSW_HOL_0, HIGH);
      return;
    }

    if (klPA1 || klPA2) {
      if ((bhol & 0x1f) == 0x01) {
        bhol |= 0x02;
        mcp_digitalWrite(OSW_HOL_0, LOW);
        mcp_digitalWrite(OSW_HOL_B1, HIGH);
        return;
      }

      if (bhol & 0x1f == 0x1e) {
        bhol |= 0xe1;
        mcp_digitalWrite(OSW_HOL_0, HIGH);
        return;
      }

      if (bhol & 0x1f == 0x1f) {
        bhol &= 0x01;
        mcp_digitalWrite(OSW_HOL_0, HIGH);
        mcp_digitalWrite(OSW_HOL_B1, LOW);
        mcp_digitalWrite(OSW_HOL_B2, LOW);
        mcp_digitalWrite(OSW_HOL_B3, LOW);
        mcp_digitalWrite(OSW_HOL_B4, LOW);
        return;
      }

      for (uint8_t mask = 0x02; mask < 0x20; mask <<= 1) {
        if ((bhol & mask) == mask)
          continue;
        
        bhol |= mask;
        break;
      }
    }
  }
}

uint64_t actR = 0L;
uint64_t prevR = 0L;
uint64_t chgR = 0L;
uint8_t actPos = 100;
void loop() {

  if (interr) {
    interr = false;
    prevR = actR;
    actR = 0L;
    uint64_t act;
    for (short i = 0; i < 4; i++) {
      act = mcp[i].readGPIOAB();
      actR |= act << (i*16);
    }
    
    chgR = prevR ^ actR;
    if (chgR == 0x00)
      return;

    Serial.print((unsigned long)(chgR>>32), HEX);
    Serial.println((unsigned long)chgR&0xffffffff, HEX);
    if ((chgR & SIG_WIECZOR) == SIG_WIECZOR)
      wieczor = actR & SIG_WIECZOR;

    if ((chgR & SIG_NOC) == SIG_NOC)
      noc = actR & SIG_NOC;

    if ((chgR & SIG_2TARYFA) == SIG_2TARYFA)
      taryfa2 = actR & SIG_2TARYFA;

    if ((chgR & SIG_ZAS_AWAR) == SIG_ZAS_AWAR)
      zasAwar = actR & SIG_ZAS_AWAR;
    
    if ((chgR & Z24_OFF) == Z24_OFF) {
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
      mcp_digitalWrite(CZUJKA_RUCHU, ((actR & CZUJKA1) == CZUJKA1) || ((actR & CZUJKA2) == CZUJKA2) ? HIGH : LOW);

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
           (chgR & KL09_HOLSYP_PL) == KL09_HOLSYP_PL) || ( (chgR & KL09_HOLSYP_PP) == KL09_HOLSYP_PL) ||
           (chgR & KL12_HOLLAZ_L)  == KL12_HOLLAZ_L)  || ( (chgR & KL12_HOLLAZ_P)  == KL12_HOLLAZ_P) ||
           (chgR & KL14_HOLWC_L)   == KL14_HOLWC_L)   || ( (chgR & KL14_HOLWC_P)   == KL14_HOLWC_P) ||
           (chgR & KL13_HOLPOK)    == KL13_HOLPOK)    || ( (chgR & KL15_HOLWEJ)    == KL15_HOLWEJ) ||
          )
          Hol(wieczor, noc, zasAwar, 
            !((actR & & KL10_HOLSYP_LL) == KL10_HOLSYP_LL), !((actR & KL10_HOLSYP_LP) == KL10_HOLSYP_LP),
            !((actR & & KL14_HOLWC_L) == KL14_HOLWC_L), !((actR & KL14_HOLWC_L) == KL14_HOLWC_L),
            !((actR & & KL12_HOLLAZ_L) == KL12_HOLLAZ_L), !((actR & KL12_HOLLAZ_P) == KL12_HOLLAZ_P),
            !((actR & & KL09_HOLSYP_PL) == KL09_HOLSYP_PL), !((actR & KL09_HOLSYP_PP) == KL09_HOLSYP_PP),
            !((actR & & KL13_HOLPOK) == KL13_HOLPOK), !((actR & KL15_HOLWEJ) == KL15_HOLWEJ)
          );
    
    mcp_digitalWrite(ZAS12V, (led1 || led2 || led3 || led4) ? HIGH : LOW);
    mcp_digitalWrite(SWIATLO_SALON, (led1 || led2 || led3 || led4 || salon1 || salon2) ? HIGH : LOW);
    mcp_digitalWrite(SWIATLO_SYPIALNIA, (sypialnia1 || sypialnia2) ? HIGH : LOW);
    mcp_digitalWrite(SWIATLO_HOL, (bhol != 0) ? HIGH : LOW);

    if (!zasAwar && wieczor) {
      mcp_digitalWrite(PODSW_SALON_A, (led1 || led2 || led3 || led4 || salon1 || salon2) ? LOW : HIGH);
      mcp_digitalWrite(PODSW_HOL_B, (bhol != 0x00) ? LOW : HIGH);
      mcp_digitalWrite(PODSW_MIX_C, (led1 || led2 || led3 || led4 || salon1 || salon2 || bhol != 0x00) ? LOW : HIGH);
    }
  }



  

  return;
  // put your main code here, to run repeatedly:
  //for (short i = 0; i < 4; ++i) {
  //  Serial.print(i, DEC);
  //  Serial.print(" ");
  //  Serial.print(mcp[i].readGPIO(0), HEX);
  //  Serial.print(" ");
  //  Serial.println(mcp[i].readGPIO(1), HEX);
  //}
  #if 1
  if (Serial.available()) {
    Serial.read();
    if (actPos < 64) {
      //Serial.print("L-> ");
      //mcp_print(actPos);
      mcp_digitalWrite(actPos, LOW);
    }
    do {
      actPos = (actPos >= 63) ? 0 : actPos+1;
      if (_pins[actPos].io_type == OUTPUT)
        break;

    } while (true);
    Serial.print("H-> ");
    mcp_print(actPos);
    mcp_digitalWrite(actPos, HIGH);
  }
  delay(50);
#else

  if (true || interr) {
    interr = false;
    uint16_t s = 0;
    for (uint8_t t = 0; t < 4; ++t) {
      act[t] = mcp[t].readGPIOAB();
      //mcp[t].clearInterrupts(); 
      chg[t] = prev[t] ^ act[t];
      prev[t] = act[t];
      s+= chg[t];
    }
    if (s != 0) {
      Serial.println("");
      for (uint8_t t = 0; t < 4; ++t) {
        Serial.print(chg[t], HEX);
        Serial.print(" ");
      }
      Serial.println();
    }

  }
  delay(200);
  Serial.print(".");
  #endif
}
