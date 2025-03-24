#include "utils.hpp"
#include "def_io.h"
//#include "decl_io.hpp"

#include <Adafruit_MCP23X17.h>
extern Adafruit_MCP23X17 mcp[4];
extern struct _iotable _pins[64];

#ifdef DEBUG_CODE
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

void mcp_print(short ps) {
  Serial.print(ps);
  Serial.print(":");
  Serial.print(mod_id(ps));
  Serial.print(":");
  if (pin_id(ps) < 8) {
    Serial.print("A");
    Serial.print(pin_id(ps));
  } else {
    Serial.print("B");
    Serial.print(pin_id(ps)-8);
  }
  Serial.print(":");
#ifdef  _EXT_CODE_
  Serial.print(_pins[ps].name);
#endif  
  Serial.println("");
}
#endif

void print1_64bin(uint64_t value)
{
  uint8_t val;

  for (int8_t m = 63; m >= 0; m--) {
    val = value >> m;
    val &= val & 0x1;
    Serial1.print(val, HEX);
    if (m % 16 == 0)
      Serial1.print(" ");
    if (m % 8 == 0)
      Serial1.print(" ");
  }
}

void print1_64val(uint64_t value)
{
  uint8_t val;

  for (int8_t m = 60; m >= 0; m-=4) {
    val = value >> m;
    val &= val & 0xf;
    Serial1.print(val, HEX);
    if (m % 16 == 0)
      Serial1.print(" ");
  }
}

void mcp_pinMode(short ps) {
  mcp[mod_id(ps)].pinMode(pin_id(ps), _pins[ps].io_type);
}

void mcp_digitalWrite(short ps, short value) {
#ifdef DEBUG_CODE  
  Serial.print("pos=");
  Serial.print(ps);
#ifdef _EXT_CODE_
  Serial.print(" (");
  Serial.print(_pins[ps].name);
  Serial.print(") => ");
#else
Serial.print(" => ");
#endif
  
  Serial.println(value);
#endif
  Serial1.print("S;V;");
  Serial1.print(ps, DEC);
  Serial1.print(";");
  Serial1.print(value, DEC);
  Serial1.println(";");
  
  short svalue = (ps == GWAR_L || ps == GWAR_N || ps == Z213_3_LEDY_CH1 || ps == Z213_4_LEDY_CH2 
          || ps == Z213_5_LEDY_CH3|| ps == Z213_6_LEDY_CH4) ? !value : value;
  if (_pins[ps].io_type == OUTPUT) {
    mcp[mod_id(ps)].digitalWrite(pin_id(ps), svalue);
  }
}

bool isOutput(short ps) {
  return _pins[ps].io_type == OUTPUT; 
}

void mcp_pinAttactInterrupt(short ps) {
  mcp[mod_id(ps)].setupInterruptPin(pin_id(ps), CHANGE);
}

short mcp_getPinMode(short ps) {
  return _pins[ps].io_type;
}
