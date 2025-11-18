#include <Arduino.h>

struct IOS {
  int8_t pin;
  bool set;
};

#define P_SALON_TV 26

#define P_SW_KW_PRYSZNIC 27
#define P_SW_KW_WANNA 28
#define P_T_KALORYFER 29
#define P_T_SALON 30
#define P_OSW_WANNA 31
#define P_T_KUCHNIA 32
#define P_T_LAZIENKA 33
#define P_POMPA 34

#define P_HOL_C 35
#define P_WC 36
#define P_HOL_A 37
#define P_HOL_B 38

#define P_WIATRAK_1 39
#define P_WIATRAK_2 40

struct IOS table[] = {
  { P_SALON_TV, false },
  { P_SW_KW_WANNA, false },
  { P_SW_KW_PRYSZNIC, false },
  { P_T_KALORYFER, false },
  { P_T_SALON, false },
  { P_OSW_WANNA, false },
  { P_T_KUCHNIA, false },
  { P_T_LAZIENKA, false },
  { P_POMPA, false },
  { P_HOL_C, false },
  { P_WC, false },
  { P_HOL_A, false },
  { P_HOL_B, false },
  { P_WIATRAK_1, false },
  { P_WIATRAK_2, false },
  { -1, false}
};



static uint8_t isSet(uint8_t id)
{
  uint8_t idx = 0;
  while (table[idx].pin > 0) {
    if (table[idx].pin == id)
      return table[idx].set ? 1 : 0;
    ++idx;
  }
  return 0;
}

static bool setSet(uint8_t id, uint8_t val)
{
  uint8_t idx = 0;
  while (table[idx].pin > 0) {
    if (table[idx].pin == id) {
      table[idx].set = ! (val == 0);
      digitalWrite(table[idx].pin, val);
      return true;
    }
    ++idx;
  }
  return false;
}


void setup() {
  uint8_t idx = 0;
  while (table[idx].pin > 0) {
    pinMode(table[idx].pin, OUTPUT);
    digitalWrite(table[idx].pin, LOW);
    table[idx].set = false;
    ++idx;
  }

  Serial.begin(115200);
}

uint8_t pos = 0;
bool set_cmd = false;
bool get_cmd = false;
uint8_t idx = 0;
uint8_t val;

#define PRINTS(x) do { Serial.print(x); } while(false)

void loop() {
  
  if (Serial.available()) {
    char c = Serial.read();
    //Serial.print(c);
    switch(pos) {
      case 0:
        if ( c == 'S') {
          ++pos;
          set_cmd = true;
          get_cmd = false;
        } else if ( c == 'G') {
          ++pos;
          get_cmd = true;
          set_cmd = false;
        } else {
          set_cmd = false;
          get_cmd = false;
        }
        break;
      
      case 1:
        if (c < '0' || c > '9') {
          pos = 0;
        } else {
          idx = c - '0';
          ++pos;
        }
        break;
      
      case 2:
        if (c < '0' || c > '9') {
          pos = 0;
        } else {
          idx *= 10;
          idx += c - '0';
          if (set_cmd) {
            pos = 3;
          } else if (get_cmd) {
            pos = 5;
          }
        }
        break;

      case 3:
        pos = c == '=' ? 4 : 0;
        break;

      case 4:
        if (c == '0' || c == '1') {
          pos = 5;
          val = c - '0';
        } else {
          pos = 0;
        }
        break;

      case 5:
        if (c == ';') {
          pos = 6;
        } else {
          pos = 0;
        }
        break;

      case 6:
        if (c == '\r') ++pos;
        else pos = 0;
        break;

      case 7:
        pos = 0;
        if (get_cmd) {
            PRINTS('G');
            PRINTS(idx);
            PRINTS('=');
            PRINTS(isSet(idx));
            PRINTS(';');
            PRINTS('\r');
            PRINTS('\n');
          } else if (set_cmd) {
            if (setSet(idx, val)) {
              PRINTS('O');
              PRINTS('K');
            } else {
              PRINTS('E');
              PRINTS('R');
            }
            PRINTS(';');
            PRINTS('\r');
            PRINTS('\n');
          }
        break;
      
      default:
        pos = 0;
        break;
    } //switch
  } //if avaible
} //loop
