#include <Arduino.h>

#include <Adafruit_MCP23X17.h>
Adafruit_MCP23X17 mcp;

#include "msg.h"
FlowMessage flowMsg;

#include "io.h"
#include "wentylator.hpp"
#include "zaworgaz.hpp"
#include "wodomierze.h"
#include "graphic.h"

MyWentylator WentKuch(&mcp, 4, KUCH_WENT, 30, false, 1) ;
MyWentylator WentLaz(&mcp, 2, LAZ_WENT, 30, false, 2) ;
MyWentylator WentWC(&mcp, 3, WC_WENT, 30, false, 3) ;

//MyZaworGaz gaz(&mcp, 3, 0, F_GAZ_1, F_GAZ_2, 1);

void parseCommand(uint8_t * table, uint8_t actIdx, uint8_t lenCmd);

uint8_t index = 0;
uint32_t impulseAll[15];
uint16_t impulse[2][15];

static inline void WentylatorKuchnia()
{
  WentKuch.pushBtn();
}

static inline void WentylatorWC()
{
  WentWC.pushBtn();
}

static inline void WentylatorLazienka()
{
  WentLaz.pushBtn();
}

static inline void WCUmywalkaZ()
{
  impulse[index][WC_UMYW_Z] += 1;
}

static inline void WCUmywalkaC()
{
  impulse[index][WC_UMYW_C] += 1;
}

static inline void WCPralkaZ()
{
  impulse[index][WC_PRALKA_Z] += 1;
}

static inline void WCPralkaC()
{
  impulse[index][WC_PRALKA_C] += 1;
}

static inline void WCSedes()
{
  impulse[index][WC_SEDES] += 1;
}

static inline void LazienkaWannaC()
{
  impulse[index][LAZ_WANNA_C] += 1;
}

static inline void LazienkaWannaZ()
{
  impulse[index][LAZ_WANNA_Z] += 1;
}

static inline void LazienkaUmywalkaC()
{
  impulse[index][LAZ_UMYW_C] += 1;
}

static inline void LazienkaUmywalkaZ()
{
  impulse[index][LAZ_UMYW_Z] += 1;
}

static inline void LazienkaPrysznicC()
{
  impulse[index][LAZ_PRYSZ_C] += 1;
}

static inline void LazienkaPrysznicZ()
{
  impulse[index][LAZ_PRYSZ_Z] += 1;
}

static inline void LazienkaSedes()
{
  impulse[index][LAZ_SEDES] += 1;
}

static inline void KuchniaUmywalkaZ()
{
  impulse[index][KUCH_UMYW_Z] += 1;
}

static inline void KuchniaUmywalkaC()
{
  impulse[index][KUCH_UMYW_C] += 1;
}

static inline void KuchniaZmywarka()
{
  impulse[index][KUCH_ZMYW_Z] += 1;
}

volatile bool Int2Sec = false;
ISR(RTC_PIT_vect)
{ 
  Int2Sec = true; 
  RTC.PITINTFLAGS = RTC_PI_bm;
}

void setupInterrupts() {
  
  RTC.CLKSEL = RTC_CLKSEL_INT32K_gc; // set internal clock @ 32768 Hz
  
  RTC.PITINTCTRL = RTC_PI_bm;  // enable PIT interrupt
  RTC.PITCTRLA = RTC_PERIOD_CYC32768_gc | RTC_PITEN_bm;
  
 
  return;
  
}

unsigned long mss = 0;

bool prev = false;
int passcnt = -1;
bool connectLcd = false;

void setup() {

  Serial.begin(115200);

  for (char i = 0; i < 15; ++i) {
    pinMode(mapsPin[i].pin, INPUT);
    attachInterrupt(digitalPinToInterrupt(mapsPin[i].pin), mapsPin[i].fun, FALLING); 
  }

  mcp.pinMode(LAZ_UMY_W, OUTPUT);
  mcp.pinMode(LAZ_WAN_W, OUTPUT);
  mcp.pinMode(LAZ_PRYSZ_W, OUTPUT);
  mcp.pinMode(LAZ_SEDES_W, OUTPUT);  
  mcp.pinMode(WC_SEDES_W, OUTPUT);
  mcp.pinMode(WC_PRALKA_W, OUTPUT);
  mcp.pinMode(KUCH_ZMYW_W, OUTPUT);
  mcp.pinMode(WC_UMYW_W, OUTPUT);
  mcp.pinMode(KUCH_UMYW_W, OUTPUT);

  WentKuch.init(WentylatorKuchnia);
  WentLaz.init(WentylatorLazienka);
  WentWC.init(WentylatorWC);
  
  setupInterrupts();
  sei();
}

uint16_t deltaImpulse[15];
uint8_t bufforCmd[16];
uint8_t actIdx = 0;
uint8_t lenCmd = 0;
void loop() {

  if (Int2Sec) {
    auto m = millis();
    Int2Sec = false;

    WentKuch.tick();
    WentLaz.tick();
    WentWC.tick();

    unsigned short actIndex = index;
    index = (index + 1) % 2;

    unsigned long sumAll = 0L;
    for (int j = 0; j < 15; ++j) {
      impulseAll[j] += impulse[actIndex][j];
      deltaImpulse[j] = impulse[actIndex][j];
      sumAll += impulse[actIndex][j];
      impulse[actIndex][j] = 0;
      
    }

    mcp.digitalWrite(LAZ_WAN_W, (deltaImpulse[LAZ_WANNA_C] + deltaImpulse[LAZ_WANNA_Z]) > 0);
    mcp.digitalWrite(LAZ_PRYSZ_W, (deltaImpulse[LAZ_PRYSZ_C] + deltaImpulse[LAZ_PRYSZ_Z]) > 0);
    mcp.digitalWrite(LAZ_SEDES_W, (deltaImpulse[LAZ_SEDES]) > 0);
    mcp.digitalWrite(WC_SEDES_W, (deltaImpulse[WC_SEDES]) > 0);
    mcp.digitalWrite(WC_PRALKA_W, (deltaImpulse[WC_PRALKA_C] + deltaImpulse[WC_PRALKA_Z]) > 0);
    mcp.digitalWrite(KUCH_ZMYW_W, (deltaImpulse[KUCH_ZMYW_Z]) > 0);
    mcp.digitalWrite(WC_UMYW_W, (deltaImpulse[WC_UMYW_C] + deltaImpulse[WC_UMYW_Z]) > 0);
    mcp.digitalWrite(KUCH_UMYW_W, (deltaImpulse[KUCH_UMYW_C] + deltaImpulse[KUCH_UMYW_Z]) > 0);
  
    for (uint8_t j = 0; j < 15; ++j) {
      if (deltaImpulse[j] > 0) {
        flowMsg.sendFlow(j+1, deltaImpulse[j], impulseAll[j]);
      }      
    }
  }

  while(Serial.available()) {
    char c = Serial.read();
    if (c == '\n' || c == '\r') {
      if (lenCmd > 0) {
        parseCommand(bufforCmd, actIdx, lenCmd);
      }
      lenCmd = 0;
    } else {
      bufforCmd[actIdx] = c;
      actIdx = (actIdx + 1) & 0x0f;
      lenCmd = (lenCmd + 1) & 0x0f;
    }
  }
}

void parseCommand(uint8_t * table, uint8_t idx, uint8_t len)
{
  uint8_t cmd[16];
  uint8_t * ptrCmd = cmd;
  for (uint8_t i = 0 ; i < len; ++i) {
    *ptrCmd = table[(idx - len + i) & 0x0f];
    ++ptrCmd;
  }

  if (cmd[0] != 'W' && cmd[1] != 'G')
    return;

  if (cmd[1] != ';')
    return;

  if (!isDigit(cmd[2]))
    return;

  uint8_t id = cmd[2] - '0';
  if (cmd[3] != ';')
    return;

  if (!isDigit(cmd[4]))
    return;

  uint8_t val = cmd[4] - '0';
  if (val != 0 && val != 1)
    return;

  if (cmd[5] != ';')
    return;

  if (cmd[0] == 'W') {
    switch(id) {
      case 1:
        WentKuch.set(val ? true: false); break;
      case 2:
        WentLaz.set(val ? true: false); break;
      case 3:
        WentWC.set(val ? true: false); break;
      default: break;
    }
  } else {
    if (id == 1) {
      //gaz.set(val ? true: false); 
      ;
    }
  }
}
