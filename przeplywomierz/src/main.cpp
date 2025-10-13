#include <Arduino.h>
#define U8X8_HAVE_HW_I2C

#ifdef U8X8_HAVE_HW_SPI
#include <SPI.h>
#endif
#ifdef U8X8_HAVE_HW_I2C
#include <Wire.h>
#endif
// put function declarations here:


#include <Adafruit_MCP23X17.h>
Adafruit_MCP23X17 mcp;

#include <Wire.h>
// put function declarations here:
#include <U8g2lib.h>
// U8g2 Contructor List (Frame Buffer)
// The complete list is available here: https://github.com/olikraus/u8g2/wiki/u8g2setupcpp
// Please update the pin numbers according to your setup. Use U8X8_PIN_NONE if the reset pin is not connected


U8G2_SH1106_128X64_NONAME_F_HW_I2C u8g2(U8G2_R0, /* reset=*/ U8X8_PIN_NONE);

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
  KUCH_ZMYW,
};

#include "io.h"
#include "my_sens.h"
#include "wentylator.hpp"
#include "zaworgaz.hpp"

MyWentylator WentKuch(&mcp, 4, KUCH_WENT, 30, false, 40) ;
MyWentylator WentLaz(&mcp, 2, LAZ_WENT, 30, false, 41) ;
MyWentylator WentWC(&mcp, 3, WC_WENT, 30, false, 42) ;



struct flowMsg {
  MyMessage* flowMsg;
  MyMessage* volumeMsg;
  MyMessage* lastCounterMsg;
} flowMessages[15];

U8G2_SH1106_128X64_NONAME_F_HW_I2C u8g2(U8G2_R0, /* reset=*/ U8X8_PIN_NONE);


unsigned short index = 0;
unsigned long impulseAll[15];

static void WCUmywalkaZ()
{
  impulse[index][WC_UMYW_Z] += 1;
}

static void WCUmywalkaC()
{
  impulse[index][WC_UMYW_C] += 1;
}

static void WCPralkaZ()
{
  impulse[index][WC_PRALKA_Z] += 1;
}

static void WCPralkaC()
{
  impulse[index][WC_PRALKA_C] += 1;
}

static void WCSedes()
{
  impulse[index][WC_SEDES] += 1;
}

static void LazienkaWannaC()
{
  impulse[index][LAZ_WANNA_C] += 1;
}

static void LazienkaWannaZ()
{
  impulse[index][LAZ_WANNA_Z] += 1;
}

static void LazienkaUmywalkaC()
{
  impulse[index][LAZ_UMYW_C] += 1;
}

static void LazienkaUmywalkaZ()
{
  impulse[index][LAZ_UMYW_Z] += 1;
}

static void LazienkaPrysznicC()
{
  impulse[index][LAZ_PRYSZ_C] += 1;
}

static void LazienkaPrysznicZ()
{
  impulse[index][LAZ_PRYSZ_Z] += 1;
}

static void LazienkaSedes()
{
  impulse[index][LAZ_SEDES] += 1;
}

static void KuchniaUmywalkaZ()
{
  impulse[index][KUCH_UMYW_Z] += 1;
}

static void KuchniaUmywalkaC()
{
  impulse[index][KUCH_UMYW_C] += 1;
}

static void KuchniaZmywarka()
{
  impulse[index][KUCH_ZMYW] += 1;
}


struct PinInterr {
  short pin;
  void (*fun)();
};

PinInterr mapsPin[15] = {
  { 39, WCUmywalkaZ},
  { 14, WCUmywalkaC},
  { 15, WCSedes},
  { 16, WCPralkaZ},
  { 17, WCPralkaC},
  { 10, LazienkaPrysznicC},
  { 11, LazienkaPrysznicZ},
  { 9, LazienkaWannaC},
  { 21, LazienkaWannaZ},
  { 12, LazienkaUmywalkaC},
  { 11, LazienkaUmywalkaZ},
  { 8, LazienkaSedes},
  { 7, KuchniaUmywalkaC },
  { 6, KuchniaUmywalkaZ },
  { 5, KuchniaZmywarka },
};

void WentylatorKuchnia()
{
  WentKuch.pushBtn();
}

void WentylatorWC(bool on)
{
  WentWC.pushBtn();
}

void WentylatorLazienka(bool on)
{
  WentLaz.pushBtn();
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
#endif

  for (int i = 0; i < 15; ++i) {
    pinMode(mapsPin[i].pin, INPUT);
    attachInterrupt(digitalPinToInterrupt(mapsPin[i].pin), mapsPin[i].fun, FALLING); 
  }
  //Serial.begin(115200);
  sei();
}
void drawLogo(void)
{
    u8g2.setFontMode(1);	// Transparent
#ifdef MINI_LOGO

    u8g2.setFontDirection(0);
    u8g2.setFont(u8g2_font_inb16_mf);
    u8g2.drawStr(0, 22, "U");
    
    u8g2.setFontDirection(1);
    u8g2.setFont(u8g2_font_inb19_mn);
    u8g2.drawStr(14,8,"8");
    
    u8g2.setFontDirection(0);
    u8g2.setFont(u8g2_font_inb16_mf);
    u8g2.drawStr(36,22,"g");
    u8g2.drawStr(48,22,"\xb2");
    
    u8g2.drawHLine(2, 25, 34);
    u8g2.drawHLine(3, 26, 34);
    u8g2.drawVLine(32, 22, 12);
    u8g2.drawVLine(33, 23, 12);
#else

    u8g2.setFontDirection(0);
    u8g2.setFont(u8g2_font_inb24_mf);
    u8g2.drawStr(0, 30, "U");
    
    u8g2.setFontDirection(1);
    u8g2.setFont(u8g2_font_inb30_mn);
    u8g2.drawStr(21,8,"8");
        
    u8g2.setFontDirection(0);
    u8g2.setFont(u8g2_font_inb24_mf);
    u8g2.drawStr(51,30,"g");
    u8g2.drawStr(67,30,"\xb2");
    
    u8g2.drawHLine(2, 35, 47);
    u8g2.drawHLine(3, 36, 47);
    u8g2.drawVLine(45, 32, 12);
    u8g2.drawVLine(46, 33, 12);
    
#endif
}

void drawURL(void)
{
#ifndef MINI_LOGO
  u8g2.setFont(u8g2_font_4x6_tr);
  if ( u8g2.getDisplayHeight() < 59 )
  {
    u8g2.drawStr(89,20,"github.com");
    u8g2.drawStr(73,29,"/olikraus/u8g2");
  }
  else
  {
    u8g2.drawStr(1,54,"github.com/olikraus/u8g2");
  }
#endif
}

void loop() {
  // put your main code here, to run repeatedly:

  u8g2.clearBuffer();
  
  unsigned short actIndex = index;
  index = (index + 1) % 2;

  u8g2.setFontDirection(0);
  u8g2.setFont(u8g_font_5x7);

  for (int j = 0; j < 15; ++j) {
    impulseAll[j] += impulse[actIndex][j];
    impulse[actIndex][j] = 0;
    u8g2.setCursor(j > 7 ? 62 : 0, (j % 8) * 8);
    u8g2.print(impulseAll[j]);
  }
  
  u8g2.sendBuffer();
  delay(1000);

}

LiquidCrystal_I2C lcd(0x3F,16,2);  



unsigned long mss = 0;

bool prev = false;
int passcnt = -1;
bool connectLcd = false;

void setup() {

  mcp.pinMode(LAZ_UMY_W, OUTPUT);
  mcp.pinMode(LAZ_WAN_W, OUTPUT);
  mcp.pinMode(LAZ_PRYSZ_W, OUTPUT);
  mcp.pinMode(LAZ_SEDES_W, OUTPUT);  
  mcp.pinMode(WC_SEDES_W, OUTPUT);
  mcp.pinMode(WC_PRALKA_W, OUTPUT);
  mcp.pinMode(KUCH_ZMYW_W, OUTPUT);
  mcp.pinMode(WC_UMYW_W, OUTPUT);
  mcp.pinMode(KUCH_UMYW_W, OUTPUT);

  for (int i = 0; i < 15; ++i) {
    flowMessages[i].flowMsg = new MyMessage(i+1,V_FLOW);
    flowMessages[i].volumeMsg = new MyMessage(i+1,V_VOLUME);
    flowMessages[i].lastCounterMsg = new MyMessage(i+1,V_VAR1);

    request(i+1, V_VAR1);
  }

  WentKuch.init(WentylatorKuchnia);
  WentLaz.init(WentylatorLazienka);
  WentWC.init(WentylatorWC);
  
  setupInterrupts();
  sei();
}

void presentation()
{
	// Send the sketch version information to the gateway and Controller
	sendSketchInfo("Water Meter", "1.1");

	// Register this device as Water flow sensor
	for (int i = 0; i < 15; ++i) {
    present(i+1, S_WATER, info[i]);
  }

  WentKuch.presentation("Went. Kuch");
  WentLaz.presentation("Went. Laz");
  WentWC.presentation("Went. WC");

}

unsigned short textPos = 0;
unsigned long prevm = 0L;
void loop() {
  
  
  // put your main code here, to run repeatedly:
  unsigned int deltaImpulse[15];
  if (Int1Sec) {

    Int1Sec = false;
    Serial.println(millis(), DEC);

    WentKuch.tick();
    WentLaz.tick();
    WentWC.tick();
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
