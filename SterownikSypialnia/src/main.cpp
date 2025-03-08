#include <Arduino.h>
#include <Adafruit_MCP23X17.h>
#include <Wire.h>
#include "def_io.h"

TwoWire wire;
Adafruit_MCP23X17 mcp[4];
inline void mcp_pinMode(short ps) {
  mcp[_pins[ps].mod_id].pinMode(_pins[ps].pin_id, _pins[ps].io_type);
}

inline void mcp_digitalWrite(short ps, short value) {
  short svalue = (ps == GWAR_L || ps == GWAR_N || ps == LEDY_CH1 || ps == LEDY_CH2|| ps == LEDY_CH3|| ps == LEDY_CH4) ? !value : value;
  if (_pins[ps].io_type == OUTPUT) {
    mcp[_pins[ps].mod_id].digitalWrite(_pins[ps].pin_id, svalue);
  }
  //mcp[_pins[ps].mod_id].
}

inline void mcp_pinAttactInterrupt(short ps) {
  mcp[_pins[ps].mod_id].setupInterruptPin(_pins[ps].pin_id, CHANGE);
}

inline void mcp_print(short ps) {
  Serial.print(ps);
  Serial.print(":");
  Serial.print(_pins[ps].mod_id);
  Serial.print(":");
  if (_pins[ps].pin_id < 8) {
    Serial.print("A");
    Serial.print(_pins[ps].pin_id);
  } else {
    Serial.print("B");
    Serial.print(_pins[ps].pin_id-8);
  }
  Serial.print(":");
  Serial.println(_pins[ps].name);

}

inline short mcp_getPinMode(short ps) {
  return _pins[ps].io_type;
}

volatile bool interr = false;

void inputchg() {
  interr = true;
}

void setup() {
  Serial.begin(57600);
  //while (!Serial)
  //  delay(100);
  

  pinMode(RESETPIN, OUTPUT);
  digitalWrite(RESETPIN, HIGH);


  for (short i = 0; i < 4; i++) {
    if (!mcp[i].begin_I2C(0x20+i, &wire)) {
      Serial.print("Address ");
      Serial.print(0x20+i, HEX);
      Serial.println(" not found");
    } else {
      Serial.print("Address ");
      Serial.print(0x20+i, HEX);
      Serial.println(" initialize successfully");
      mcp[i].setupInterrupts(false, true, LOW);
    }
  }

  Serial.println("Configuring pins...");

  mcp[3].pinMode(7, OUTPUT);
  mcp[3].pinMode(14, OUTPUT);

  //Konfiguracja pinow gwarantowanych i od ledow (wyzwalane poziomem niskim)
  mcp_digitalWrite(GWAR_L, LOW);
  mcp_digitalWrite(GWAR_N, LOW);
  mcp_digitalWrite(LEDY_CH1, LOW);
  mcp_digitalWrite(LEDY_CH2, LOW);
  mcp_digitalWrite(LEDY_CH3, LOW);
  mcp_digitalWrite(LEDY_CH4, LOW);

  mcp_pinMode(GWAR_L);
  mcp_pinMode(GWAR_N);
  mcp_pinMode(LEDY_CH1);
  mcp_pinMode(LEDY_CH2);
  mcp_pinMode(LEDY_CH3);
  mcp_pinMode(LEDY_CH4);

  mcp_digitalWrite(GWAR_L, LOW);
  mcp_digitalWrite(GWAR_N, LOW);
  mcp_digitalWrite(LEDY_CH1, LOW);
  mcp_digitalWrite(LEDY_CH2, LOW);
  mcp_digitalWrite(LEDY_CH3, LOW);
  mcp_digitalWrite(LEDY_CH4, LOW);

  
  for (short p = 0; p < 64; p++) {
    mcp_pinMode(p);
    if (mcp_getPinMode(p) == OUTPUT)
      mcp_digitalWrite(p, LOW);
    else {
      //mcp_pinAttactInterrupt(p);
    }
  }

  Serial.println("Done");

  //pinMode(INTERRUPTPIN, INPUT);
  //attachInterrupt(digitalPinToInterrupt(INTERRUPTPIN), inputchg, FALLING);
}
 
uint8_t actPos = 100;
uint16_t prev[4] = {0, 0, 0, 0};
uint16_t chg[4];
uint16_t act[4];

void loop() {

  // put your main code here, to run repeatedly:
  //for (short i = 0; i < 4; ++i) {
  //  Serial.print(i, DEC);
  //  Serial.print(" ");
  //  Serial.print(mcp[i].readGPIO(0), HEX);
  //  Serial.print(" ");
  //  Serial.println(mcp[i].readGPIO(1), HEX);
  //}
  #if 1
  if (Serial.available()) {
    Serial.read();
    if (actPos < 64) {
      //Serial.print("L-> ");
      //mcp_print(actPos);
      mcp_digitalWrite(actPos, LOW);
    }
    do {
      actPos = (actPos >= 63) ? 0 : actPos+1;
      if (_pins[actPos].io_type == OUTPUT)
        break;

    } while (true);
    Serial.print("H-> ");
    mcp_print(actPos);
    mcp_digitalWrite(actPos, HIGH);
  }
  delay(50);
#else

  if (true || interr) {
    interr = false;
    uint16_t s = 0;
    for (uint8_t t = 0; t < 4; ++t) {
      act[t] = mcp[t].readGPIOAB();
      //mcp[t].clearInterrupts(); 
      chg[t] = prev[t] ^ act[t];
      prev[t] = act[t];
      s+= chg[t];
    }
    if (s != 0) {
      Serial.println("");
      for (uint8_t t = 0; t < 4; ++t) {
        Serial.print(chg[t], HEX);
        Serial.print(" ");
      }
      Serial.println();
    }

  }
  delay(200);
  Serial.print(".");
  #endif
}
