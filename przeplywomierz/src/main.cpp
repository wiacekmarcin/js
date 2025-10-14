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

MyWentylator WentKuch(&mcp, 4, KUCH_WENT, 30, false, 40) ;
MyWentylator WentLaz(&mcp, 2, LAZ_WENT, 30, false, 41) ;
MyWentylator WentWC(&mcp, 3, WC_WENT, 30, false, 42) ;


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

volatile bool Int1Sec = false;
ISR(RTC_PIT_vect) { Int1Sec = true; RTC.PITINTFLAGS = 1; }

void setupInterrupts() {

  //To operate the PIT, follow these steps:
  //1. Configure the RTC clock CLK_RTC as described in   Configure the Clock CLK_RTC.
  RTC.CLKSEL = 0x00; //Use OSCULP32K oscillator
    
  //2. Enable the interrupt by writing a '1' to the Periodic Interrupt bit (PI) in the PIT Interrupt Control
  //register (RTC.PITINTCTRL).
  while (1 & RTC.PITSTATUS); //check if register isn't busy
  
  RTC.PITINTCTRL = 0x01; //Enable interrupts
  
  //3. Select the period for the interrupt and enable the PIT by writing the desired value to the PERIOD bit
  //field and a '1' to the PIT Enable bit (PITEN) in the PIT Control A register (RTC.PITCTRLA).

  while (1 & RTC.PITSTATUS); //check if register isn't busy

  RTC.PITCTRLA = RTC_PERIOD_CYC32768_gc | 0x01; //0xFD; //This should set the clock to trigger an interrupt every 128 clock cycles (The clock frequency is 32768Hz, so every 1/256 seconds)

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
void loop() {
  
  if (Int1Sec) {
    auto m = millis();
    Int1Sec = false;
    Serial.println(m, DEC);

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
}

