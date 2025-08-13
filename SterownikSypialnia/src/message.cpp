#include "message.hpp"
#include "utils.hpp"
#include "def_io.h"
#include "common.hpp"
#include "hol.hpp"
#include "salon.hpp"
#include "sypialnia.hpp"
#include <Arduino.h>

extern uint64_t g_actR;
extern uint64_t outputValue;

static void rozkaz2(uint8_t* off, size_t * r, uint8_t data[]);
static uint8_t getPos(uint8_t* off, size_t * r, uint8_t data[], uint8_t * val);
static bool getVal(uint8_t* off, size_t * r, uint8_t data[], uint8_t * val);
static void setVal(uint8_t index, uint8_t val);

void rozkaz()
{
  uint8_t data[16] = {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0};
  size_t r = Serial1.readBytes(data, 16);

  if ( r < 2 ) {
    return;
  }
  uint8_t off = 0;
  while (r > 0) {
    switch(data[0+off]) {
      case 'I':
        if (data[1+off] == ';') {
          Serial1.println("S;");
          r -= 2;
          off += 2;
        }
        break;

      case 'S':
        if (data[1+off] != ';') {
          Serial1.print("S;E;");
          Serial1.print(__LINE__, DEC);
          Serial1.println(";");
          r -= 2;
          off += 2;
        } else {
          r -= 2;
          off += 2;
          rozkaz2(&off, &r, data + off + 2);
        }
        break;
      
      default:
        r -= 1;
        off += 1;
        break;
    }
  }
}

static void rozkaz2(uint8_t* off, size_t * r, uint8_t * data)
{
  uint8_t val = 0, res = 0, index = 0;
  switch(data[0]) {
    case 'I':
      if (data[1] == ';') {
#ifdef DEBUG_CODE
        Serial.print("act=");
        print_64val(g_actR);
        Serial.println("");
#endif
        Serial1.print("S;I;");
        print1_64val(g_actR);
        Serial1.println(";");
        print1_64val(outputValue);
        Serial1.println(";");
      } else {
        Serial1.print("S;E;");
        Serial1.print(__LINE__, DEC);
        Serial1.print(";");
      }
      *r -= 2;
      *off += 2;
      return;
  
    case 'S':  
      if (data[1] == ';') {
        res = getPos(off, r, data+1, &val);
        if (res > 0) {
          Serial.print("index=");
          Serial.println(val, DEC);
          *r -= 2;
          *off += 2;
          index = val;
          if (getVal(off, r, data+1+res, &val)) {
            setVal(index, val);
            Serial1.print("S;A;");
          }
        return;
        }
      } else {
        Serial1.print("S;E;");
        Serial1.print(__LINE__, DEC);
        Serial1.print(";");
        *r -= 2;
        *off += 2;
        return;
      }
      return;

    default:
      break;
  }
}

static uint8_t getPos(uint8_t* off, size_t * r, uint8_t * data, uint8_t * val)
{
  if (data[0] < '0' || data[0] > '9') {
    Serial1.print("S;E;");
    Serial1.print(__LINE__, DEC);
    Serial1.print(";");
    *r -= 1;
    *off += 1;
    return 0;
  }

  if (data[1] == ';') {
    *val = data[0] - '0';
    *r -= 1;
    *off += 1;
    return 1;
  }

  if (data[1] < '0' || data[1] > '9') {
    Serial1.print("S;E;");
    Serial1.print(__LINE__, DEC);
    Serial1.print(";");
    *r -= 2;
    *off += 2;
    return 2;
  }
  
  if (data[2] == ';') {
    *val = 10*(data[0]-'0') + (data[1]-'0');
    *r -= 2;
    *off += 2;
    return 2;
  }
  Serial1.print("S;E;");
  Serial1.print(__LINE__, DEC);
  Serial1.print(";");
  *r -= 2;
  *off += 2;
  return 0;
}

static bool getVal(uint8_t* off, size_t * r, uint8_t * data, uint8_t * val)
{

  if ((data[0] == '0' || data[0] != '1') && data[1] == ';') {
    *val = data[0] - '0';
    *r -= 2;
    *off += 2;
    return true;
  } else {
    Serial1.print("S;E;");
    Serial1.print(__LINE__, DEC);
    Serial1.print(";");
    *r -= 2;
    *off += 2;
  }
  return false;
}
    
static void setVal(uint8_t index, uint8_t val)
{
  switch(index) {
    case LED1_LAZIENKA1: //ledy kolo lazienki 1
    case LED2_LAZIENKA2: //ledy kolo lazienki 2
    case LED3_SYPIALNIA1: //ledy kolo salonu 1
    case LED4_SYPIALNIA2: //ledy kolo salonu 2
    case OSW_SALON1: //Salon 2
    case OSW_SALON2: //Salon 1
      salon_req(index, val); break;
        
    case OSW_HOL_A1: //hol 3.1
    case OSW_HOL_A2: //hol 3.2
    case OSW_HOL_A3: //hol 3.3 
    case OSW_HOL_B1: //hol 4.4
    case OSW_HOL_B2: //hol 4.3
    case OSW_HOL_B3: //hol 4.2
    case OSW_HOL_B4: //hol 4.1
    case OSW_HOL_0: //Przedpokoj A0
      hol_req(index, val); break;

    case OSW_SYPIALNIA1: //sypialnia 2
    case OSW_SYPIALNIA2: //sypialnia 1
    case OSW_SYPIALNIA3: //sypialnia kinkiety
      sypialnia_req(index, val); break;

    case PODSW_MIX_C: //podswitelenie mix
      mcp_digitalWrite(PODSW_MIX_C, val); break; 
      
    case PODSW_HOL_B: //podswitelenie holu
      mcp_digitalWrite(PODSW_HOL_B, val); break;

    case PODSW_SALON_A: //podswitelenie salonu
      mcp_digitalWrite(PODSW_SALON_A, val); break;

    default: break;
  }
}

#ifdef TEMP
  if (data[2] == 'T' && data[3] == ';') {
    sensors.requestTemperatures(); // Send the command to get temperatures
    
    Serial.print("S;T;");
    Serial.print(sensors.getTempCByIndex(0));
    Serial.print(";");
  }
#endif  
