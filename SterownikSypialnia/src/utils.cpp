#include "utils.hpp"
#include "def_io.h"
//#include "decl_io.h"

#include <Adafruit_MCP23X17.h>
extern Adafruit_MCP23X17 mcp[4];
extern struct _iotable _pins[64];

void print_64val(uint64_t value)
{
  uint8_t val;

  for (int8_t m = 60; m >= 0; m-=4) {
    val = value >> m;
    val &= val & 0xf;
    Serial.print(val, HEX);
    if (m % 16 == 0)
      Serial.print(" ");
  }
}

void print_64bin(uint64_t value, bool input)
{
  uint8_t val;

  for (int8_t m = 63; m >= 0; m--) {
    val = value >> m;
    val &= val & 0x1;
    if ((input && _pins[m].io_type == OUTPUT) || (!input && _pins[m].io_type == INPUT))
      Serial.print("X");
    else 
      Serial.print(val, HEX);
    if (m % 16 == 0)
      Serial.print(" ");
    if (m % 8 == 0)
      Serial.print(" ");
  }
}

void print_64Out(uint64_t value)
{

  uint8_t val;
  Serial.println("**********");
  for (int8_t m = 63; m >= 0; m--) {
    val = value >> m;
    val &= val & 0x1;
    if (_pins[m].io_type == INPUT)
      continue;
    val = (m == GWAR_L || m == GWAR_N || m == Z213_3_LEDY_CH1 || m == Z213_4_LEDY_CH2 
        || m == Z213_5_LEDY_CH3|| m == Z213_6_LEDY_CH4) ? !val : val;
    if (!val)
      continue;
    switch(m) {
      case Z213_3_LEDY_CH1 : Serial.println("Led k. Laz 1"); break;
      case Z213_4_LEDY_CH2 : Serial.println("Led k. Laz 2"); break;
      case Z209_8_CH8 : Serial.println("Hol B3"); break;
      case Z209_7_CH7 : Serial.println("Hol B2"); break;
      case Z209_6_CH6 : Serial.println("Hol B1"); break;
      case Z209_5_CH5 : Serial.println("Hol A4"); break;
      case Z209_4_CH4 : Serial.println("Hol A3"); break;
      case Z209_3_CH3 : Serial.println("Hol A2"); break;
      case Z209_2_CH2 : Serial.println("Hol A1"); break;
      case Z209_1_CH1 : Serial.println("+12V"); break;
      case Z213_6_LEDY_CH4 : Serial.println("Led k. Syp 2"); break;
      case Z213_5_LEDY_CH3 : Serial.println("Led k. Syp 1"); break;
      case SWIATLO_SYPIALNIA : Serial.println("Sw. salon"); break;
      case CZUJKA_RUCHU : Serial.println("Czujka"); break; 
      case PODSW_MIX_C : Serial.println("Pods mix C"); break; 
      case PODSW_HOL_B : Serial.println("Pods holu B"); break; 
      case PODSW_SALON_A : Serial.println("Pods salonu A"); break; 
      case Z211_1_CH1 : Serial.println("Sypialnia 2"); break;  
      case Z211_2_CH2 : Serial.println("Syp. kink."); break;   
      case Z210_4_CH4 : Serial.println("Hol A0"); break;
      case Z210_3_CH3 : Serial.println("Sypialnia 1"); break;  
      case Z210_2_CH2 : Serial.println("Salon 2"); break;  
      case GWAR_N : Serial.println("Gwar. N"); break;  
      case GWAR_L : Serial.println("Gwar. L"); break;  
      case Z210_1_CH1 : Serial.println("salon 1"); break;  
      case SWIATLO_HOL : Serial.println("Sw. hol"); break;  
      case SWIATLO_SALON : Serial.println("Sw. salon"); break;
      default: Serial.println(m); break;  
    }
  }
  Serial.println("**********");

} 

void mcp_pinMode(short ps) {
  mcp[_pins[ps].mod_id].pinMode(_pins[ps].pin_id, _pins[ps].io_type);
}

void mcp_digitalWrite(short ps, short value) {
  Serial.print("pos=");
  Serial.print(ps);
  Serial.print(" (");
  Serial.print(_pins[ps].name);
  Serial.print(") => ");
  Serial.println(value);
  short svalue = (ps == GWAR_L || ps == GWAR_N || ps == Z213_3_LEDY_CH1 || ps == Z213_4_LEDY_CH2 
          || ps == Z213_5_LEDY_CH3|| ps == Z213_6_LEDY_CH4) ? !value : value;
  if (_pins[ps].io_type == OUTPUT) {
    mcp[_pins[ps].mod_id].digitalWrite(_pins[ps].pin_id, svalue);
  }
  //mcp[_pins[ps].mod_id].
}

bool isOutput(short ps) {
  return _pins[ps].io_type == OUTPUT; 
}

void mcp_pinAttactInterrupt(short ps) {
  mcp[_pins[ps].mod_id].setupInterruptPin(_pins[ps].pin_id, CHANGE);
}

void mcp_print(short ps) {
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

short mcp_getPinMode(short ps) {
  return _pins[ps].io_type;
}
