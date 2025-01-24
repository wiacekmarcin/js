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
  KUCH_ZMYW,
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


void setup() {
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

#include "main.h"

#ifndef NEW_BOARD
#include <PCF8574.h>
#else
#include <Adafruit_MCP23017.h>
#include "io.h"
#endif

#include <LiquidCrystal_I2C.h>
#define ISLCD 9


LiquidCrystal_I2C lcd(0x3F,16,2);  

#include "wejscia.h"
#include "podswietlenie.h"
#include "swiatloled.h"
#include "swiatlojadalnia.h"
#include "swiatlosufit.h"

#ifdef NEW_BOARD
Adafruit_MCP23017 o20;
Adafruit_MCP23017 io24;
#else
PCF8574 expWejscia(0x20);
PCF8574 expLedy(0x25);
PCF8574 expOczka(0x26);
PCF8574 expPozostale(0x27);
#endif



Wejscia w;
Podswietlenie swPod;
SwiatloLED swLED;
SwiatloSufit swSufit;
SwiatloJadalnia swJadalnia;

bool change(unsigned long timeinsKuchnia, unsigned long timeimsDrzwi) {
	static unsigned long prevmaskawejsc = 0x00;
	unsigned long maskawejsc = 0x00;

	maskawejsc |= w.czyklJadDown() << 1;
	maskawejsc |= w.czyklJadUp() << 2;
	maskawejsc |= w.czyklKuchADown() << 3;
	maskawejsc |= w.czyklKuchAUp() << 4;
	maskawejsc |= w.czyklKuchBDown() << 5;
	maskawejsc |= w.czyklKuchUp() << 6;
	maskawejsc |= w.czyDrzwiOtwarte() << 7;
	maskawejsc |= w.czyNoc() << 8;
	maskawejsc |= w.czyWieczor() << 9;
	maskawejsc |= w.czyRuchDrzwi(SwiatloLED::czasSwiecenieLED) << 10;
	maskawejsc |= w.czyRuchKuchnia(1000*timeinsKuchnia) << 11;
	

	if (prevmaskawejsc == maskawejsc)
		return false;

	if (maskawejsc & 0x3f) { // jaki kolwiek klawsz to znaczy jest ruch w kuchni 
		w.setRuch();
	}
	prevmaskawejsc = maskawejsc;
	return true;
}

void printW(const long & t, const Wejscia &w, bool force = false) 
{
/*	
	Serial.println(t);
	Serial.println("JAD UP | JAD DOWN | KUCH A UP | KUCH A DOWN | KUCH B UP | KUCH B DOWN | DRZWI_OTW | WIE | NOC | RUCH_DRZWI | RUCH_KUCH ");
	Serial.print  ("      ");
	Serial.print (w.czyklJadUp(), DEC);
	Serial.print ("|         ");
	Serial.print (w.czyklJadDown(), DEC);
	Serial.print ("|          ");
	Serial.print (w.czyklKuchAUp(), DEC);
	Serial.print ("|            ");
	Serial.print (w.czyklKuchADown(), DEC);
	Serial.print ("|          ");
	Serial.print (w.czyklKuchBUp(), DEC);
	Serial.print ("|            ");
	Serial.print (w.czyklKuchBDown(), DEC);
	Serial.print ("|          ");
	Serial.print (w.czyDrzwiOtwarte());
	Serial.print ("|    ");
	Serial.print (w.czyWieczor());
	Serial.print ("|    ");
	Serial.print (w.czyNoc());
	Serial.print ("|          ");
	Serial.print (w.czyRuchDrzwi(2000));
	Serial.print ("|         ");
	Serial.println (w.czyRuchKuchnia(2000));
	Serial.println('-');
*/	
}

unsigned long t = 0;


void setup() {

#ifdef NEW_BOARD

	zapalPrzekazniki(false);
	zapalZasAwar(false);
	zapalLEDZasilacz(false);
	io_init();
	Serial.begin(115200);
	delay(500);
	w.read(false, NULL);
	//if (w.czyZasilanieAwaryjne) { zapalZasAwar(true); delay(50); }
	zapalPrzekazniki(true);
	zapalSzafki(true);
	//if (w.czyWieczor()) {
	//	zapalLedSufitLod(true);
	//	zapalLEDZasilacz(true);
	//}

#else
	expPozostale.begin();
	
	 //expOczka.begin(); -- w srodku jest funkcja begin

	swJadalnia.init();
    swPod.init();
	swLED.init();
	w.init();
	 
	expLedy.begin();
	swPod.zapalSzafa(true);
#endif

	swSufit.init();
	t = millis();

	w.read(false, NULL);
	//printW(t, w, true);

}



unsigned long mss = 0;

bool prev = false;
int passcnt = -1;
bool connectLcd = false;

void loop() {
#if 0
	//5, 6,  8
	digitalWrite(5, HIGH);
	o20.writeGPIOAB(0xffff);
	delay(5000);
	o20.writeGPIOAB(0x0000);
	Serial.println("5 - LOW");
	for (int i=0; i< 16;i++) {
		delay(400);
		o20.digitalWrite(i, LOW);
	}
	io24.digitalWrite(LEDDRZ1, LOW);
	io24.digitalWrite(LEDSUFL, LOW);
	io24.digitalWrite(LEDSUFJ, LOW);	
	

	delay(5000);
	Serial.println("5 - HIGH");
	for (int i=0; i< 16;i++) {
		delay(400);
		o20.digitalWrite(i, HIGH);
	}
	io24.digitalWrite(LEDDRZ1, HIGH);
	io24.digitalWrite(LEDSUFL, HIGH);
	io24.digitalWrite(LEDSUFJ, HIGH);

	digitalWrite(5, LOW);
	
	return;

	if (Serial.available() > 0) {
		uint8_t inc = Serial.read();
		if (inc == 'a') {
			Serial.print(inc, DEC);
			Serial.print(" ");
			printW(t, w, true);	
		}

		if (inc == 'u') {
			++passcnt;
			test(passcnt);
		} else if (inc == 'd') {
			--passcnt;
			test(passcnt);
		}


	}
#endif

	 if (digitalRead(ISLCD) == LOW) {
        if (!connectLcd) {
            Serial.println("Inicjalizacja LCD");
            lcd.init();                      // initialize the lcd 
            lcd.clear();
            
            // Print a message to the LCD.
            lcd.print("Staritng!");
            connectLcd = true;
			lcd.clear();
            lcd.setBacklight(true);
            lcd.setCursor(0,0);
            lcd.print('1');
            lcd.print(' ');
            lcd.print('2');
            lcd.print(' ');
            lcd.print('3');
            lcd.print(' ');
            lcd.print('4');
        } 
    } else if (connectLcd) {
        connectLcd = false;
        Serial.println("Rozlaczenie LCD");
    }

	w.read(connectLcd, &lcd);
	//lcd.setCursor(0,1);


	//delay(110);
	//return;

	t = millis();
	swSufit.rotate();
	swSufit.tiktok(t);
	if (!change(30*60, 5*60)) {
		delay(100);
		return;
	}
#ifdef DBG
	printW(t, w);
#endif	
	swJadalnia.zapal(w);
	swSufit.zapal(w, swLED);
	swLED.zapal(w, swSufit.czyZapalone());
	swPod.zapal(w.czyZasilanieAwaryjne(), w.czyWieczor(), swSufit.czyZapalone(), swJadalnia.czyZapalone(), swLED.czyZapalonySufit());
	
	delay(100 - (millis() - t));


}
