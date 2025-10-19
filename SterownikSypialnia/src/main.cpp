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

uint16_t maskInput[4] {
  0x000F,
  0x0007,
  0x7F7F,
  0x7F7F
};


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
  g_actR = 0;
  for (short i = 0; i < 4; i++) {
    act = mcp[i].readGPIOAB();
    print_64val(act);
    Serial.print(" & ");
    Serial.print(maskInput[i], HEX);
    Serial.print(" => ");
    act &= maskInput[i];
    print_64val(act);
    Serial.println();
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

uint16_t act;
uint64_t chg_R;
void loop() {

  if (interr || incVal) {
    
    if (readVal) {
      g_prevR = g_actR;
      readVal = false;
      g_actR = 0L;
      act = 0;
      for (short i = 3; i>=0; i--) {
        act = mcp[i].readGPIOAB() & maskInput[i];
        Serial.print(act, HEX);
        Serial.print(", ");
        g_actR |= act;
        print_64val(g_actR); Serial.print(" =>");
        if (i)
          g_actR <<= 16;
        print_64val(g_actR); Serial.println("");
      }
    }

    Serial1.print("S;H;");
    if (interr)
      Serial1.print("I;");
    if (incVal)
      Serial1.print("V;");
    Serial1.print("Chg in;");
    print_64val1(g_actR); Serial1.println(";");
    interr = false;
    incVal = false;

    Serial.print("Change incoming;\r\nprev=");
    print_64val(g_prevR); Serial.print("\r\nact_=");
    print_64val(g_actR); Serial.print("\r\nchg_=");
  

    chg_R = g_prevR ^ g_actR;


    print_64val(chg_R);Serial.print("\r\n");
    print_64Out(g_actR);

    if (chg_R != 0x00) {
      inputChange(&chg_R);
    }

    Serial1.print("S;H;Chg out;");
    print_64val1(outputValue); Serial1.println(";");
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
    actR &= 0x7F7F7F7F0007000F;

    Serial.print("Incoming data: ");
    print_64val(actR); Serial.println("");
    g_prevR = g_actR;
    g_actR = actR;
    incVal = true;
    readVal = false;
  }
}

