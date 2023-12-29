#include <Arduino.h>

#include <Adafruit_MCP23X17.h>
Adafruit_MCP23X17 mcp;


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


#define MY_GATEWAY_SERIAL
#define MY_DISABLED_SERIAL
#define MY_SERIALDEVICE Serial
#define MY_BAUD_RATE 115200
//#define ARDUINO_ARCH_MEGAAVR
//#define ARDUINO_ARCH_AVR

#include "../lib/MySensors_onlySerialGw/MySensors.h"
#define SLEEP_MODE false                        // flowvalue can only be reported when sleep mode is false.
#define MAX_FLOW 60   

struct flowMsg {
  MyMessage* flowMsg;
  MyMessage* volumeMsg;
  MyMessage* lastCounterMsg;
} flowMessages[15];

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

struct mcpIODigital {
  uint8_t pin;
  uint8_t mode;
};

enum IODigitOutput {
  LAZ_UMY_W = 0,
  MCP_FIRST = LAZ_UMY_W,
  LAZ_WAN_W,
  LAZ_PRYSZ_W,
  LAZ_SEDES_W,
  WC_SEDES_W,
  WC_PRALKA_W,
  KUCH_ZMYW_W,
  KUCH_WENT,
  WC_WENT,
  LAZ_WENT,
  WC_UMYW_W,
  KUCH_UMYW_W,
  F_GAZ_1,
  F_GAZ_2,
  MCP_LAST,
};



unsigned int impulse[2][15];
unsigned short index = 0;
unsigned long impulseAll[15];

static void WCUmywalkaZ() { impulse[index][WC_UMYW_Z] += 1; }
static void WCUmywalkaC() { impulse[index][WC_UMYW_C] += 1; }
static void WCPralkaZ() { impulse[index][WC_PRALKA_Z] += 1; }
static void WCPralkaC() { impulse[index][WC_PRALKA_C] += 1; }
static void WCSedes() { impulse[index][WC_SEDES] += 1; }
static void LazienkaWannaC() { impulse[index][LAZ_WANNA_C] += 1; }
static void LazienkaWannaZ() { impulse[index][LAZ_WANNA_Z] += 1; }
static void LazienkaUmywalkaC() { impulse[index][LAZ_UMYW_C] += 1; }
static void LazienkaUmywalkaZ() { impulse[index][LAZ_UMYW_Z] += 1; }
static void LazienkaPrysznicC() { impulse[index][LAZ_PRYSZ_C] += 1; }
static void LazienkaPrysznicZ() { impulse[index][LAZ_PRYSZ_Z] += 1; }
static void LazienkaSedes() { impulse[index][LAZ_SEDES] += 1; }
static void KuchniaUmywalkaZ() { impulse[index][KUCH_UMYW_Z] += 1; }
static void KuchniaUmywalkaC() { impulse[index][KUCH_UMYW_C] += 1; }
static void KuchniaZmywarka() { impulse[index][KUCH_ZMYW_Z] += 1; }

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

  for (int i = 0; i < 15; ++i) {
    flowMessages[i].flowMsg = new MyMessage(i+1,V_FLOW);
    flowMessages[i].volumeMsg = new MyMessage(i+1,V_VOLUME);
    flowMessages[i].lastCounterMsg = new MyMessage(i+1,V_VAR1);

    request(i+1, V_VAR1);
  }

  if (mcp.begin_I2C()) {
    for (uint8_t i = MCP_FIRST; i < MCP_LAST; ++i) {
      mcp.pinMode(i, OUTPUT);
    }
  }
  Serial.begin(115200);
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
    float val = 0.0025 * impulseAll[ind];
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

void receive(const MyMessage &message)
{
	if (message.getType()==V_VAR1) {
    uint8_t id = message.getSender();

    if (id >= 1 && id <= 15) {
        impulseAll[id-1]=message.getULong();
    }
		
	}
}
