#include "common.hpp"
#include "def_io.h"
#include "utils.hpp"
#include "hol.hpp"
#include "salon.hpp"
#include "sypialnia.hpp"
#include <Adafruit_MCP23X17.h>

extern uint64_t g_actR;

extern Adafruit_MCP23X17 mcp[4];

#define IN_KL(V) bool chg_ ## V = (*chgR & V) == V; bool val_ ## V = ((~(g_actR)) & V) != 0; \
      if (chg_ ## V ) { Serial.print(#V); Serial.print( "=>"); Serial.println(val_ ## V); } \
      do { } while(0)
#define C_KL(V) chg_ ## V
#define V_KL(V) val_ ## V


void inputChange(uint64_t *chgR)
{
  bool wieczor, noc, taryfa2, zasAwar;

#ifdef DEBUG_CODE
  uint64_t mask_i = 0x1;
  Serial.print("CHG= ");
  for (uint8_t pos = 0; pos < 64; ++pos) {
    if ((*chgR & mask_i) == mask_i) {
      Serial.print(' ');
      Serial.print(pos);
    }
    mask_i = mask_i << 1;
  }
  Serial.println("");


  Serial.println("C1R C1V C2R C2V");
  Serial.print((*chgR & CZUJKA1) == CZUJKA1);
  Serial.print("  ");
  Serial.print((g_actR & CZUJKA1) > 0);
  Serial.print("  ");
  Serial.print((*chgR & CZUJKA2) == CZUJKA2);
  Serial.print("  ");
  Serial.println((g_actR & CZUJKA2) > 0);
#endif

  if (((*chgR & CZUJKA1) == CZUJKA1) || ((*chgR & CZUJKA2) == CZUJKA2)) {
    Serial.println("zmiana czujki");
    mcp_digitalWrite(CZUJKA_RUCHU, (((g_actR & CZUJKA1) | (g_actR & CZUJKA2)) > 0) ? HIGH : LOW);
  }

  wieczor = !((g_actR & SIG_WIECZOR) == SIG_WIECZOR);
  noc = !((g_actR & SIG_NOC) == SIG_NOC);
  taryfa2 = !((g_actR & SIG_2TARYFA) == SIG_2TARYFA);
  zasAwar = !((g_actR & SIG_ZAS_AWAR) == SIG_ZAS_AWAR);

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
  Serial.print(((g_actR & Z24_OFF) == 0) ? '0' : '1');
  Serial.print(' ');
  Serial.println((*chgR & Z24_OFF) == Z24_OFF);
#else
  (void)taryfa2;
#endif  

  if ((*chgR & SIG_ZAS_AWAR) == SIG_ZAS_AWAR) {
    Serial.println("Zasilanie awaryjne");
    zasilanieAwaryjne(wieczor, noc, zasAwar);
    podswietlenie(wieczor, zasAwar);
    return;
  }

  if ((*chgR & Z24_OFF) == Z24_OFF) {
      if ((g_actR & Z24_OFF) == 0) {
        Serial.println("Zmiana 24V");
        hol_off();
        sypialnia_off();
        salon_off();
        podswietlenie(wieczor, zasAwar);
        return;
      } else {
        Serial.println("Kinkiet on");
        mcp_digitalWrite(OSW_SYPIALNIA3, HIGH);
      }
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
      SalonSalon(wieczor, noc, zasAwar, 
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
  Serial.println("Podsietlenie");
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
  Serial.print("wieczor=");
  Serial.println(wieczor);
  Serial.print("zasAwar=");
  Serial.println(zasAwar);
  Serial.print("w1=");
  Serial.println(w1);
  Serial.print("a=");
  Serial.println(a);
  Serial.print("b=");
  Serial.println(b);
  Serial.print("c=");
  Serial.println(c);
  mcp_digitalWrite(PODSW_SALON_A, a ? HIGH : LOW);
  mcp_digitalWrite(PODSW_HOL_B,  b ? HIGH : LOW);
  mcp_digitalWrite(PODSW_MIX_C, c ? HIGH : LOW);

  mcp_digitalWrite(SWIATLO_SALON, salon_isOn() ? HIGH : LOW); //wyjscia opto
  mcp_digitalWrite(SWIATLO_SYPIALNIA, sypialnia_isOn() ? HIGH : LOW); //wyjscia opto
  mcp_digitalWrite(SWIATLO_HOL, hol_isOn() ? HIGH : LOW); //wyjscia opto
}

uint8_t parseNum(uint8_t * data, uint8_t * pos, uint8_t *r)
{
  *r = 0;
  if (data[*pos] < '0' || data[*pos] > '9') {
    ++(*pos);
    return false;
  }

  while(data[*pos] >= '0' && data[*pos] <= '9') {
    *r = 10 * *r + data[*pos] - '0';
    ++(*pos);
  }
 return true;
}