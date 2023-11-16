#include <Arduino.h>

#define U8X8_HAVE_HW_I2C

#ifdef U8X8_HAVE_HW_SPI
#include <SPI.h>
#endif
#ifdef U8X8_HAVE_HW_I2C
#include <Wire.h>
#endif
// put function declarations here:

#include <U8g2lib.h>
// U8g2 Contructor List (Frame Buffer)
// The complete list is available here: https://github.com/olikraus/u8g2/wiki/u8g2setupcpp
// Please update the pin numbers according to your setup. Use U8X8_PIN_NONE if the reset pin is not connected

U8G2_SH1106_128X64_NONAME_F_HW_I2C u8g2(U8G2_R0, /* reset=*/ U8X8_PIN_NONE);

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
  KUCH_ZMYW
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

unsigned int impulse[2][15];
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

void setup()
{
  u8g2.begin();
  for (int i = 0; i < 2; ++i) {
    for (int j = 0; j < 15; ++j) {
      impulse[i][j] = 0;
      impulseAll[j] = 0;
    }
  }
  for (int i = 0; i < 15; ++i) {
    pinMode(mapsPin[i].pin, INPUT);
    attachInterrupt(digitalPinToInterrupt(mapsPin[i].pin), mapsPin[i].fun, FALLING); 
  }
  //Serial.begin(115200);
  sei();
}

unsigned short textPos = 0;
void loop() {
  // put your main code here, to run repeatedly:

  u8g2.clearBuffer();
  
  unsigned short actIndex = index;
  index = (index + 1) % 2;

  u8g2.setFontDirection(0);
  u8g2.setFont(u8g_font_courR08);

  for (int j = 0; j < 15; ++j) {
    impulseAll[j] += impulse[actIndex][j];
    impulse[actIndex][j] = 0;
  }

  for (int j = 0 ; j < 4; ++j)
  {
    short ind = ( textPos + j ) % 15;
    float val = 0.0025 * impulseAll[j];
    u8g2.drawStr(0,j*16,info[ind]);
    u8g2.setCursor(64, j*16);
    u8g2.print(val,2);
  }
  
  u8g2.sendBuffer();
  textPos++;
  if (textPos > 15)
    textPos = 0;
  delay(10000);

}

