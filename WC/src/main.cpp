#include <Arduino.h>

#include "util.h"
#include "debug.h"
#include "wejscia.h"
#include "wyjscia.h"
#include "swiatlo.h"
#include "temperatura.h"
#include "lcd.h"

#include <Wire.h>
#include <Adafruit_MCP23X17.h>

constexpr unsigned short DELAY = 200; //50;
constexpr unsigned long TIMEBEFORESLEEP = SEC(5);
constexpr unsigned int CNTMAXLOOP = TIMEBEFORESLEEP / DELAY;


Adafruit_MCP23X17 wejsciawyjscia;
Wejscia expWejscia(wejsciawyjscia);
Wyjscia expWyjscia(wejsciawyjscia);
Swiatlo lampa(expWejscia, expWyjscia);


volatile uint8_t cntLoop = 0;
//volatile bool awakenByInterrupt = false;
unsigned long tik = 0;
volatile unsigned long timeInt = 0L;

void keyPressedOn()
{
    cli();
    cntLoop = CNTMAXLOOP;
    sei();
}

bool mydelay(unsigned long ms)
{
	uint32_t start = micros();

	while (ms > 0 && !cntLoop) {
		while ( ms > 0 && (micros() - start) >= 1000 && !cntLoop)
            yield();
        
		ms--;
		start += 1000;
	}
    return cntLoop > 0;
}

void setup() {  
    Serial.begin(115200);
    delay(10000);
    if (!wejsciawyjscia.begin_I2C()) {
        Serial.println("Error.");
        while (1);
    }
    
    expWejscia.init(keyPressedOn);
    expWyjscia.init();
  
    
   

    temp_init();
#ifdef LCD_DEBUG    
    lcd_init();
#endif
    cntLoop = 0;
    expWejscia.get(0, 0);
    delay(2000);
    sei();
}

unsigned long mls = 0L;
unsigned long prevmls = 0L;

uint8_t prevLcd = 1;
void loop()
{

#ifdef MYINTERUPTS
    if (cntLoop == CNTMAXLOOP) {
        timeInt = millis();  //nastapilo przerwanie
    }

    if (cntLoop > 0) {
        //Serial.print("cntLoop=");
        //Serial.println(cntLoop, DEC);
        --cntLoop;
        mls = millis();
        expWejscia.get(timeInt, mls - timeInt);
#ifdef DEBUG        
        expWejscia.print();
#endif  
        if (expWejscia.czyZasilAwar()) {
            expWyjscia.off();
        } else {
            lampa.set(mls);
        }
        mydelay(50);
        if (cntLoop == 0) {
            expWejscia.czysc();
        }

#ifdef DEBUG    
        if (mls - prevmls > 15000) {
            prevmls = mls;
            expWejscia.print();
            expWyjscia.print("Czas");
        }
        Serial.print('*');
#endif        
    } else if (expWyjscia.tiktok()) {
        mydelay(1000); //co 1s
#ifdef DEBUG        
        Serial.print('+');
#endif        
    } else {
        if (mydelay(600L*1000)) {
            print_temp();
        }
    }
#else 
    mls = millis();
    if (mls - timeInt > 15000) {
        timeInt = mls;
        expWejscia.czysc();
    }
    
    expWejscia.get(mls, mls);
    if (expWejscia.czyZasilAwar()) {
        expWyjscia.off();
    } else {
        lampa.set(mls);
    }

    delay(500);
    

#ifdef DEBUG    
    if (mls - prevmls > 15000) {
        prevmls = mls;
        expWejscia.print();
        expWyjscia.print("Czas");
    }
    //Serial.print('*');
#endif 
    static unsigned long prevtittok = 0L;
    if (mls - prevtittok > 1000) {
        prevtittok = mls;
        expWyjscia.tiktok();
    }
#endif
}


