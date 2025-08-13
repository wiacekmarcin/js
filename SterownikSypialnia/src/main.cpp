#include <Arduino.h>
#include <Adafruit_MCP23X17.h>
#include <Wire.h>

#include "decl_io.hpp"
#include "def_io.h"

#include "utils.hpp"
#include "sypialnia.hpp"
#include "salon.hpp"
#include "hol.hpp"

#include "common.hpp"

TwoWire wire;
Adafruit_MCP23X17 mcp[4];

#ifdef TEMP
#include <OneWire.h>
#include <DallasTemperature.h>

// Data wire is plugged into port 2 on the Arduino
#define ONE_WIRE_BUS 4
OneWire oneWire(ONE_WIRE_BUS);

// Pass our oneWire reference to Dallas Temperature.
DallasTemperature sensors(&oneWire);
#endif



volatile bool interr = false;
volatile bool readVal = false;
volatile bool incVal = false;
void inputchg() {
  interr = true;
  readVal = true;
}

volatile bool tiktokInter = false;

ISR(TIMER1_COMPA_vect){
  //interrupt commands for TIMER 0 here
  tiktokInter = true;
}

volatile uint64_t g_actR = 0L;
volatile uint64_t g_prevR = 0L;

#define INIT_PIN_LOW(X) mcp_pinMode(X); mcp_digitalWrite(X, LOW);

uint64_t outputValue = 0x0;
void setup() {
  // start serial port
  
  Serial.begin(115200);
  Serial1.begin(115200);
  Serial1.println("S;D;Begin setup;");
  
  pinMode(RESETPIN, OUTPUT);
  digitalWrite(RESETPIN, HIGH);

  for (short i = 0; i < 4; i++) {
    if (!mcp[i].begin_I2C(0x20+i, &wire)) {
      Serial1.print("S;D;Address ");
      Serial1.print(0x20+i, HEX);
      Serial1.println(" not found;");
    } else {
      mcp[i].setupInterrupts(true, true, LOW);
    }
  }
  
  INIT_PIN_LOW(GWAR_N);
  INIT_PIN_LOW(GWAR_L);
  
  for (short p = 0; p < 64; p++) {
    mcp_pinMode(p);
    if (mcp_getPinMode(p) == OUTPUT)
      mcp_digitalWrite(p, LOW);
    else  {
      mcp_pinAttactInterrupt(p);
    }
  }

  pinMode(INTERRUPTPIN, INPUT);
  attachInterrupt(digitalPinToInterrupt(INTERRUPTPIN), inputchg, FALLING);

  uint64_t act;
  for (short i = 0; i < 4; i++) {
    act = mcp[i].readGPIOAB();
    g_actR |= act << (i*16);
  }
  
  g_prevR = g_actR;

  // TIMER 1 for interrupt frequency 1 Hz:
  cli(); // stop interrupts
  TCCR1A = 0; // set entire TCCR1A register to 0
  TCCR1B = 0; // same for TCCR1B
  TCNT1  = 0; // initialize counter value to 0
  // set compare match register for 1 Hz increments
  OCR1A = 62499; // = 16000000 / (256 * 1) - 1 (must be <65536)
  // turn on CTC mode
  TCCR1B |= (1 << WGM12);
  // Set CS12, CS11 and CS10 bits for 256 prescaler
  TCCR1B |= (1 << CS12) | (0 << CS11) | (0 << CS10);
  // enable timer compare interrupt
  TIMSK1 |= (1 << OCIE1A);
  sei(); // allow interrupts
#ifdef TEMP
  sensors.begin();
#endif  
  Serial1.println("S;D;End setup;");
  interr = true;
  incVal = true;
}



bool ledS1 = false, ledS2 = false, ledL1 = false, ledL2 = false;
bool salon1 = false, salon2 = false;
bool sypialnia1 = false, sypialnia2 = false;



void loop() {

  if (interr || incVal) {
    Serial.print("interr=");
    Serial.println(interr);
    Serial.print("incVal=");
    Serial.println(incVal);
    interr = false;
    incVal = false;
    
    if (readVal) {
      g_prevR = g_actR;
      readVal = false;
      g_actR = 0L;
      uint64_t act;
      for (short i = 0; i < 4; i++) {
        act = mcp[i].readGPIOAB();
        g_actR |= act << (i*16);
      }
    }
    Serial1.print("S;H;Change incoming;");
    if (interr)
      Serial1.print("I;");
    if (incVal)
      Serial1.print("V;");
    print_64val1(g_actR); Serial1.println(";");
    Serial.print("Change incoming;\r\nprev=");
    print_64val(g_prevR); Serial.print("\r\nact_=");
    print_64val(g_actR); Serial.print("\r\nchg_=");
  

    uint64_t chg_R = g_prevR ^ g_actR;
    uint64_t chg_I = chg_R & 0x7f7f7f7f0007000f;

    print_64val(chg_R);Serial.print("\r\nchgi=");
    print_64val(chg_I);Serial.println("");
    print_64Out(g_actR);
    if (chg_I != 0x00) {
      inputChange(chg_I, g_actR);
    }

    Serial1.print("S;H;After output;");
    print_64val1(outputValue); Serial1.println(";");
    Serial.print("End function;\r\nprev=");
    print_64val(g_prevR); Serial.print("\r\nact_=");
    print_64val(g_actR); Serial.println("");
  }
    
  if (tiktokInter) {
    tiktokInter = false;
    hol_tiktok();
  }

  if (Serial1.available()) {
    rozkaz();
  }

  if (Serial.available()) {
    //Serial1.print("S;D;Incoming data;V;");
    uint8_t data[38];
    size_t r = Serial.readBytes(data, 38);
  
    if ( r < 3 )
      return; 

    if((data[0] != 'I' || data[1] != '=' || data[2] != '[')) {
      Serial1.print("Error");
      Serial1.print((char)data[0]);
      Serial1.print((char)data[1]);
      Serial1.print((char)data[2]);
      Serial1.println("'");
      return;
    }

    uint8_t pos = 3;
    uint8_t val = 0;
    uint64_t actR = 0L;
    while (pos < r || data[pos] == ']') {
      if (parseNum(data, &pos, &val)) {
        actR <<= 8;
        actR += val;
      }
    }
    //print_64val1(g_actR);
    //Serial1.println(';');
    Serial.print("Incoming data: prev=");
    print_64val(g_prevR); Serial.print("\r\nact_=");
    print_64val(g_actR); Serial.print("\r\ninc_=");
    print_64val(actR); Serial.println("");
    g_prevR = g_actR;
    g_actR = actR;
    incVal = true;
    readVal = false;
  }
}

