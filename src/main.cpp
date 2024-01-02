#include <Arduino.h>

#include <Adafruit_MCP23X17.h>
Adafruit_MCP23X17 mcp;

#include <Wire.h>
// put function declarations here:
#include <U8g2lib.h>
// U8g2 Contructor List (Frame Buffer)
// The complete list is available here: https://github.com/olikraus/u8g2/wiki/u8g2setupcpp
// Please update the pin numbers according to your setup. Use U8X8_PIN_NONE if the reset pin is not connected

#include "io.h"
#include "my_sens.h"
//#include "timerclass.hpp"
#include "wodomierze.h"
#include "wentylator.hpp"

Wentylator WentKuch(&mcp, KUCH_WENT, 30, false, 40) ;
Wentylator WentLaz(&mcp, LAZ_WENT, 30, false, 41) ;
Wentylator WentWC(&mcp, WC_WENT, 30, false, 42) ;

MyMessage zaworGazu

struct flowMsg {
  MyMessage* flowMsg;
  MyMessage* volumeMsg;
  MyMessage* lastCounterMsg;
} flowMessages[15];

U8G2_SH1106_128X64_NONAME_F_HW_I2C u8g2(U8G2_R0, /* reset=*/ U8X8_PIN_NONE);


unsigned int impulse[2][15];
unsigned short index = 0;
unsigned long impulseAll[15];

void WCUmywalkaZ() { impulse[index][WC_UMYW_Z] += 1; }
void WCUmywalkaC() { impulse[index][WC_UMYW_C] += 1; }
void WCPralkaZ() { impulse[index][WC_PRALKA_Z] += 1; }
void WCPralkaC() { impulse[index][WC_PRALKA_C] += 1; }
void WCSedes() { impulse[index][WC_SEDES] += 1; }
void LazienkaWannaC() { impulse[index][LAZ_WANNA_C] += 1; }
void LazienkaWannaZ() { impulse[index][LAZ_WANNA_Z] += 1; }
void LazienkaUmywalkaC() { impulse[index][LAZ_UMYW_C] += 1; }
void LazienkaUmywalkaZ() { impulse[index][LAZ_UMYW_Z] += 1; }
void LazienkaPrysznicC() { impulse[index][LAZ_PRYSZ_C] += 1; }
void LazienkaPrysznicZ() { impulse[index][LAZ_PRYSZ_Z] += 1; }
void LazienkaSedes() { impulse[index][LAZ_SEDES] += 1; }
void KuchniaUmywalkaZ() { impulse[index][KUCH_UMYW_Z] += 1; }
void KuchniaUmywalkaC() { impulse[index][KUCH_UMYW_C] += 1; }
void KuchniaZmywarka() { impulse[index][KUCH_ZMYW_Z] += 1; }

void WentylatorKuchnia(bool on)
{
  mcp.digitalWrite(KUCH_WENT, on ? HIGH : LOW);
  WentKuchMsg.set(on);
  send(WentKuchMsg);
}

void WentylatorWC(bool on)
{
  mcp.digitalWrite(WC_WENT, on ? HIGH : LOW);
  WentWcMsg.set(on);
  send(WentWcMsg);
}

void WentylatorLazienka(bool on)
{
  mcp.digitalWrite(LAZ_WENT, on ? HIGH : LOW);
  WentLazMsg.set(on);
  send(WentLazMsg);
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



void setup()
{
  Serial.begin(115200);

#ifdef OLED
  u8g2.begin();
  for (int i = 0; i < 2; ++i) {
    for (int j = 0; j < 15; ++j) {
      impulse[i][j] = 0;
      impulseAll[j] = 0;
    }
  }
#endif

#ifdef IOFLOW 
  for (int i = 0; i < 15; ++i) {
    pinMode(mapsPin[i].pin, INPUT);
    attachInterrupt(digitalPinToInterrupt(mapsPin[i].pin), mapsPin[i].fun, FALLING); 
  }
#endif

#ifdef MSENS
  for (int i = 0; i < 15; ++i) {
    flowMessages[i].flowMsg = new MyMessage(i+1,V_FLOW);
    flowMessages[i].volumeMsg = new MyMessage(i+1,V_VOLUME);
    flowMessages[i].lastCounterMsg = new MyMessage(i+1,V_VAR1);

    request(i+1, V_VAR1);
  }
#endif

#ifdef MCPIO
  if (mcp.begin_I2C()) {
    for (uint8_t i = MCP_FIRST; i < MCP_LAST; ++i) {
      mcp.pinMode(i, OUTPUT);
    }
  }
#endif

  WentKuch.init();
  WentLaz.init();
  WentWC.init();
  
  WentKuch.set(false);
  WentLaz.set(false);
  WentWC.set(false);

  setupInterrupts();
  sei();
}

void presentation()
{
	// Send the sketch version information to the gateway and Controller
	sendSketchInfo("Water Meter", "1.1");

	// Register this device as Water flow sensor
	for (int i = 0; i < 15; ++i) {
    present(i+1, S_WATER);
  }

  present(40, S_BINARY);
  present(41, S_BINARY);
  present(42, S_BINARY);
}

unsigned short textPos = 0;
unsigned long prevm = 0L;
void loop() {
  
  
  // put your main code here, to run repeatedly:
  unsigned int deltaImpulse[15];
  if (Int1Sec) {

    Int1Sec = false;
    Serial.println(millis(), DEC);
    return;

    unsigned short actIndex = index;
    index = (index + 1) % 2;

    u8g2.setFontDirection(0);
    u8g2.setFont(u8g_font_courR08);

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
  
    for (int j = 0; j < 15; ++j) {
      if (deltaImpulse[j] > 0) {
        flowMessages[j].flowMsg->set(60 * 0.0025 * deltaImpulse[j], 2); //[l/min]
        flowMessages[j].lastCounterMsg->set(impulseAll[j]);
        flowMessages[j].volumeMsg->set(impulseAll[j]* 0.0025, 1);
        send(*flowMessages[j].flowMsg);
        send(*flowMessages[j].lastCounterMsg);
        send(*flowMessages[j].volumeMsg);
      }      
    }

    u8g2.clearBuffer();
    for (int j = 0 ; j < 4; ++j)
    {
      short ind = ( textPos + j ) % 15;
      float val = 0.0025 * impulseAll[ind];
      u8g2.drawStr(0,j*16,info[ind]);
      u8g2.setCursor(64, j*16);
      u8g2.print(val,2);
    }
  
    u8g2.sendBuffer();
    textPos++;
    if (textPos > 15)
      textPos = 0;
  }
  if (millis() - prevm > 5000)
  {
    Serial.println("+");
    prevm = millis();
  }

}

void receive(const MyMessage &message)
{
	if (message.getType()==V_VAR1) {
    uint8_t id = message.getSender();

    if (id >= 1 && id <= 15) {
        impulseAll[id-1]=message.getULong();
    }
		
	}
}
