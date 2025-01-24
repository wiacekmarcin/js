#ifndef _WODOMIERZE_HPP_
#define _WODOMIERZE_HPP_

enum Wodomierz { 
  WC_UMYW_Z = 0,
  WC_UMYW_C,
  WC_SEDES,
  WC_PRALKA_Z,
  WC_PRALKA_C,
  LAZ_SEDES,
  LAZ_PRYSZ_Z,
  LAZ_PRYSZ_C,
  LAZ_UMYW_Z,
  LAZ_UMYW_C,
  LAZ_WANNA_Z,
  LAZ_WANNA_C,
  KUCH_UMYW_Z,
  KUCH_UMYW_C,
  KUCH_ZMYW_Z
};

const char info[15][9] = {
  "WC_UMY_Z",
  "WC_UMY_C",
  "WC_SEDES",
  "WC_PRA_Z",
  "WC_PRA_C",
  "LA_SEDES",
  "LA_PRY_Z",
  "LA_PRY_C",
  "LA_UMY_Z",
  "LA_UMY_C",
  "LA_WAN_Z",
  "LA_WAN_C",
  "KU_UMY_Z",
  "KU_UMY_C",
  "KU_ZMYWA",
};

extern unsigned int impulse[2][15];
extern unsigned short index;

extern void WCUmywalkaZ();
extern void WCUmywalkaC();
extern void WCPralkaZ();
extern void WCPralkaC();
extern void WCSedes();
extern void LazienkaWannaC();
extern void LazienkaWannaZ();
extern void LazienkaUmywalkaC();
extern void LazienkaUmywalkaZ();
extern void LazienkaPrysznicC();
extern void LazienkaPrysznicZ();
extern void LazienkaSedes();
extern void KuchniaUmywalkaZ();
extern void KuchniaUmywalkaC();
extern void KuchniaZmywarka();


struct PinInterr {
  short pin;
  void (*fun)();
};

PinInterr mapsPin[15] = {
  { 39, WCUmywalkaZ },
  { 14, WCUmywalkaC },
  { 15, WCSedes },
  { 16, WCPralkaZ },
  { 17, WCPralkaC },
  { 10, LazienkaPrysznicC },
  { 11, LazienkaPrysznicZ },
  { 9, LazienkaWannaC },
  { 21, LazienkaWannaZ },
  { 12, LazienkaUmywalkaC },
  { 11, LazienkaUmywalkaZ },
  { 8, LazienkaSedes },
  { 7, KuchniaUmywalkaC },
  { 6, KuchniaUmywalkaZ },
  { 5, KuchniaZmywarka }
};

#endif //_WODOMIERZE_HPP_


