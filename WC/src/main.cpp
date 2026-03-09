#include <Arduino.h>

#include <OneWire.h>
#include <DallasTemperature.h>

#include <Adafruit_MCP23X17.h>

#include "version.h"
#include "wejscia.h"
#include "wyjscia.h"

#define INTERRUPTPIN 7
#define RESETPIN A3

//#define DEBUG

Adafruit_MCP23X17 mcp;
Wejscia in_p(&mcp);
Wyjscia out_p(&mcp, &in_p);

// Data wire is plugged into port 2 on the Arduino
#define ONE_WIRE_BUS 4

// Setup a oneWire instance to communicate with any OneWire devices (not just Maxim/Dallas temperature ICs)
OneWire oneWire(ONE_WIRE_BUS);

// Pass our oneWire reference to Dallas Temperature.
DallasTemperature sensors(&oneWire);

volatile bool mcp_interrupt = false;
void io_interrupted()
{
  mcp_interrupt = true;
}

void setupTimer3() {
  noInterrupts();
  // Clear registers
  TCCR3A = 0;
  TCCR3B = 0;
  TCNT3 = 0;

  // 100.16025641025641 Hz (16000000/((155+1)*1024))
  OCR3A = 62499; // = 16000000 / (256 * 1) - 1 (must be <65536)
  // turn on CTC mode
  TCCR3B |= (1 << WGM32);
  // Set CS12, CS11 and CS10 bits for 256 prescaler
  TCCR3B |= (1 << CS32) | (0 << CS31) | (0 << CS30);
  // enable timer compare interrupt
  TIMSK3 |= (1 << OCIE3A);
  interrupts();
}

volatile uint32_t timerTick3 = 0;
volatile bool timer_int3 = false;

ISR(TIMER3_COMPA_vect) {
  ++timerTick3;
  timer_int3 = true;
}

void print_version()
{
  Serial1.print("V;");
  Serial1.print(DEVICE);
  Serial1.print(";");
  Serial1.print(MAJOR);
  Serial1.print(".");
  Serial1.print(MINOR);
  Serial1.print(".");
  Serial1.println(NUMBER);
}


void setup() {
  

  pinMode(RESETPIN, OUTPUT);
  digitalWrite(RESETPIN, HIGH);  

  pinMode(INTERRUPTPIN, INPUT);
  attachInterrupt(digitalPinToInterrupt(INTERRUPTPIN), io_interrupted, FALLING);

  setupTimer3();
 
  Serial.begin(115200);

  Serial1.begin(115200);
  print_version();


  // Start up the library
  //sensors.begin();

  int idx = 10;
  if (!mcp.begin_I2C()) {
    Serial1.println("I;2;E;NO-MCP");
    while (idx--) {
      Serial1.println("No mcp");
      delay(1000);
    }
  } else {
    Serial1.println("D;2;Found MCP");
    in_p.init();
  }
  //out_p.init();

}
uint8_t count_idx = 0;

uint8_t debug_bufor[32];
bool chInput = false;

void loop(void)
{
#ifdef DEBUG  
  if (Serial.available()) {
    uint8_t r = Serial.readBytes(debug_bufor, 32);
    if (r < 6)
      return;
    if (!(debug_bufor[0] == 'D' && debug_bufor[1] == ';' 
        && debug_bufor[2] == 'W' && debug_bufor[3] == ';'
        && debug_bufor[4] == 'I' && debug_bufor[5] == ';' )) 
      return;
    uint8_t val = 0;
    Serial1.print("D;W;I;");
    for (uint8_t i = 0; i < 8 && i+6 < r; ++i) {
      val += (debug_bufor[i] == '1') ? (1 << i) : 0;
      Serial1.print(debug_bufor[i]);
    }
    Serial1.print(";");
    Serial1.println(val);
    chInput = in_p.set_input(val);
  }
#endif

  if (Serial1.available()) {
    size_t r = Serial.readBytes(debug_bufor, 32);
    
    if (r >= 2 && debug_bufor[0] == 'V' && debug_bufor[1] == ';' ) {
      print_version();
      return;  
    }

    if (r < 6)
      return;
    
    if (!(debug_bufor[0] == 'S' && debug_bufor[1] == ';'  &&
        debug_bufor[2] == 'W' && debug_bufor[3] == ';' &&
        debug_bufor[5] == ';')) {
      return;
    }

    if (debug_bufor[4] < '1' || debug_bufor[4] > '4')
      return;

    if (debug_bufor[4] != '0' && debug_bufor[4] != '1')
      return;
      
    
    uint8_t val = debug_bufor[6] - '0';
    uint8_t id = debug_bufor[4] - '0';
      
    out_p.setExternal(id, val);
  }


  if (timer_int3) {
    timer_int3 = false;
    ++count_idx;
#ifdef DEBUG    
    //Serial.println(".");
#endif    
    /*
    if (count_idx % 30 == 0) {
      sensors.requestTemperatures(); // Send the command to get temperatures
    } else if (count_idx % 30 == 1) {

#ifdef DEBUG
      Serial.print("Temp:");
      Serial.println(sensors.getTempCByIndex(0));
#endif      
      Serial1.print("T;");
      Serial1.print(DEVICE);
      Serial1.print(";");
      Serial1.println(sensors.getTempCByIndex(0));
    }*/
    //in_p.read();
    //out_p.tiktok();
    //delay(100)
  }

  if (mcp_interrupt) {
#ifdef DEBUG
    Serial.print("Interr:");
#endif        
    mcp_interrupt = false;
    chInput = in_p.read();
  }

  if (chInput) {
    //TODO
  }

}









#if 0





volatile uint8_t cntLoop = 0;
void setup() {  
  
  expWejscia.init();

  expWyjscia.init();
  
  Serial.begin(115200);

  
    // Start up the library
  //sensors.begin();

  //if (!sensors.getAddress(insideThermometer, 0)) //Serial.println("Unable to find address for Device 0"); 
  
  // set the resolution to 9 bit (Each Dallas/Maxim device is capable of several different resolutions)
  //sensors.setResolution(insideThermometer, 9);

  
  //delay(10000); //czekaj 10s az czujniki sie ustabilizuja

    cntLoop = 0;
    expWejscia.get(0, 0);
}
/*
// function to print the temperature for a device
void printTemperature(DeviceAddress deviceAddress)
{
  // method 1 - slower
  ////Serial.print("Temp C: ");
  ////Serial.print(sensors.getTempC(deviceAddress));
  ////Serial.print(" Temp F: ");
  ////Serial.print(sensors.getTempF(deviceAddress)); // Makes a second call to getTempC and then converts to Fahrenheit

  // method 2 - faster
  float tempC = sensors.getTempC(deviceAddress);
  if(tempC == DEVICE_DISCONNECTED_C) 
  {
    //Serial.println("Error: Could not read temperature data");
    return;
  }
  //Serial.print("Temp C: ");
  //Serial.print(tempC);
}

unsigned long tik = 0;

// function to print a device address
void printAddress(DeviceAddress deviceAddress)
{
  for (uint8_t i = 0; i < 8; i++)
  {
    if (deviceAddress[i] < 16) //Serial.print("0");
    //Serial.print(deviceAddress[i], HEX);
    ;
  }
}
*/

volatile unsigned long timeInt = 0L;
void keyPressedOnPCF8574()
{
    cli();
    if (cntLoop == 0)
        timeInt = millis();  
    cntLoop = CNTMAXLOOP;
    sei();
}



void mydelay(unsigned long ms)
{
	uint32_t start = micros();

	while (ms > 0 && !cntLoop) {
		yield();
		while ( ms > 0 && (micros() - start) >= 1000) {
			ms--;
			start += 1000;
		}
	}
}

unsigned long mls = 0L;
void loop() {

    if (cntLoop > 0) {
        //Serial.print("cntLoop=");
        //Serial.println(cntLoop, DEC);
        --cntLoop;
        mls = millis();
        expWejscia.get(timeInt, mls - timeInt);
        //expWejscia.print();
        
        Wlacznik wl = expWejscia.getWlacznik();
        bool onS = expWyjscia.getSwiatlo();

        if (wl.nacisniety()) {
          expWyjscia.setSwiatlo(!onS, 30*60); //30 min
          expWyjscia.setLustro(false);
        }        

        delay(50);
        if (cntLoop == 0) {
            expWejscia.clear();
        }

    } else if (expWyjscia.tiktok()) {
        mydelay(1000); //co 1s
    } else {
        mydelay(60L*1000); //co 1min
        //Serial.println(".");
    }

    
}

    /*
    if (++tik % 100 == 0) {
      ////Serial.print("Requesting temperatures...");
      sensors.requestTemperatures(); // Send the command to get temperatures
      ////Serial.println("DONE");
  
      // It responds almost immediately. Let's print out the data
      printTemperature(insideThermometer); // Use a simple function to print out the data
     
     expWejscia.print();
     expWyjscia.print("loop");
    }

    */
    
    

/*
    Klawisz klawisz(expWejscia.getWlacznik());
    bool onS = expWyjscia.getSwiatlo();
    bool onL = expWejscia.getLustro();
    Czujka c(expWejscia.getCzRuchu());
    Drzwi d(expWejscia.getDrzwi());
    Czujka czL(expWejscia.getLustro());
    */
/*
    if (klawisz.isChange() && klawisz.czyNacisniety()) {
        expWyjscia.setSwiatlo(!onS, 30*60); //30 min
        expWyjscia.setLustro(false);
    }

    if (!onS && c.isChange() && c.czyRuch()) {
        expWyjscia.setLustro(true, 2*60);
    }

    if (!onL && czL.czyRuch() && czL.czasRuchu() > 500) {
        expWyjscia.setLustro(true, 4*60);
    }

    if (!onL && !onS && d.isChange() && d.czyOtwarte()) {
        expWyjscia.setLustro(true, 2*60);
    }

    if (onL && d.isChange() && !d.czyOtwarte()) {
        expWyjscia.setLustro(false, 0);
    }
  */  

#if 0    
  //  if (isChange) {
        Serial.println(millis(), DEC);
        expWejscia.print();
        lampa.set(false);
        expWyjscia.print("main:155");
    //if (isChange) {
     //   lampa.set(false);
      /*
          //Serial.println("------------------------------------------------\nWykroto zmiany: Wyjscie przed:");
          //expWyjscia.print("MAIN BEFORE");
          Serial.println(loopCnt, DEC);
          //loopCnt = 10;
          expWejscia.print();
          
          //lampa.set(true);
    
        //Serial.println("\nWyjscie po:");
        //expWyjscia.print("MAIN AFTER");
        Serial.println("------------------------------------------------\n\n");

        if (klawisz.isChange() && klawisz.czyNacisniety()) {
          switch(loopCnt) {
            case 0:
              expWyjscia.setZawor(true, 100);
              expWyjscia.setLustro(false);
              expWyjscia.setSwiatlo(false);
              expWyjscia.setSzafka(false);
              loopCnt++;
              break;
            case 1:
              expWyjscia.setLustro(true, 100);
              expWyjscia.setZawor(false);
              expWyjscia.setSwiatlo(false);
              expWyjscia.setSzafka(false);
              loopCnt++;
              break;
            case 2:
              expWyjscia.setSwiatlo(true, 100);
              expWyjscia.setZawor(false);
              expWyjscia.setLustro(false);
              expWyjscia.setSzafka(false);
              loopCnt++;
              break;
            case 3:
              expWyjscia.setSzafka(true, 100);
              expWyjscia.setZawor(false);
              expWyjscia.setLustro(false);
              expWyjscia.setSwiatlo(false);
              loopCnt++;
              break;
            case 4:
              expWyjscia.setSzafka(false);
              expWyjscia.setZawor(false);
              expWyjscia.setLustro(false);
              expWyjscia.setSwiatlo(false);
              loopCnt = 0;
          }
         
        }*/

  //  }

    if (expWyjscia.tiktok()) {
      expWyjscia.print("tiktok");
    }
    

    //delay(100 - (millis() - mls));
//}
#endif

#endif