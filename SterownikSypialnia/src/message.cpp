#include "message.hpp"
#include "utils.hpp"
#include "def_io.h"
#include "common.hpp"
#include "hol.hpp"
#include "salon.hpp"
#include "sypialnia.hpp"
#include <Arduino.h>

extern uint64_t g_actR;
void rozkaz()
{
#ifdef RS485
  uint8_t data[16] = {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0};
  size_t r = Serial1.readBytes(data, 16);

  if ( r < 2 ) {
    return;
  }

  if (data[0] == 'I'  && data[1] == ';') {
    Serial1.println("S;");
    return;
  }
  
  if (data[0] == 'S' && data[1] != ';') {
    Serial1.print("S;E;");
    Serial1.print(__LINE__, DEC);
    Serial1.println(";");
    return;
  }

  if (data[2] == 'I' && data[3] == ';') {
#ifdef DEBUG_CODE
    Serial.print("act=");
    print_64val(g_actR);
    Serial.println("");
#endif
    Serial1.print("S;I;");
    print1_64val(g_actR);
    Serial1.println(";");
  }

  if (data[2] == 'F' && data[3] == ';') {
    uint8_t valPos = 6;
    uint8_t index = data[4] - '0';
    if (data[5] >= '0' && data[5] <= '9') {
      index = index * 10 + data[5] - '0';
      ++valPos;
      if (data[6] != ';') {
        Serial1.print("S;E;");
        Serial1.print(__LINE__, DEC);
        Serial1.print(";");
        return; 
      }
    } else if (data[5] != ';') {
      Serial1.print("S;E;");
      Serial1.print(__LINE__, DEC);
      Serial1.print(";");
      return;
    }

    Serial.print("k_index=");
    Serial.println(index, DEC);
    
    uint8_t val = 0;
    if (data[valPos] != '0' && data[valPos] != '1' && data[valPos+1] != ';') {
      Serial1.print("S;E;");
      Serial1.print(__LINE__, DEC);
      Serial1.print(";");
      return;
    } else {
      val = data[valPos] - '0';
    }
    
    Serial1.println("S;A;");
    uint64_t chgR;
    switch(index) {
      case 0:
        chgR |= Z216_01;
        g_actR = val ? (g_actR | Z216_01) : (g_actR & ~Z216_01);
        inputChange(chgR, g_actR);
        break;

      default:
        break;
    }
  }
  
  if (data[2] == 'S' && data[3] == ';') {
    uint8_t valPos = 6;
    uint8_t index = data[4] - '0';
    if (data[5] >= '0' && data[5] <= '9') {
      index = index * 10 + data[5] - '0';
      ++valPos;
      if (data[6] != ';') {
        Serial1.print("S;E;");
        Serial1.print(__LINE__, DEC);
        Serial1.print(";");
        return; 
      }
    } else if (data[5] != ';') {
      Serial1.print("S;E;");
      Serial1.print(__LINE__, DEC);
      Serial1.print(";");
      return;
    }

    Serial.print("index=");
    Serial.println(index, DEC);
    
    //TODO dodac algo wlaczania swiatla
    uint8_t val = 0;
    if (data[valPos] != '0' && data[valPos] != '1' && data[valPos+1] != ';') {
      Serial1.print("S;E;");
      Serial1.print(__LINE__, DEC);
      Serial1.print(";");
      return;
    } else {
      val = data[valPos] - '0';
    }
    
    Serial1.println("S;A;");

    switch(index) {
      case 4: //ledy kolo lazienki 1
      case 5: //ledy kolo lazienki 2
      case 14: //ledy kolo salonu 2
      case 15: //ledy kolo salonu 1
      case 16+12: //Salon 2
      case 16+15: //Salon 1
        salon_req(index, val); break;
      
      case 6: //hol 3.1
      case 7: //hol 3.2
      case 8: //hol 3.3 
      case 9: //hol 4.4
      case 10: //hol 4.3
      case 11: //hol 4.2
      case 12: //hol 4.1
      case 16+10: //Przedpokoj A0
        hol_req(index, val); break;

      case 16+8: //sypialnia 2
      case 16+9: //sypialnia kinkiety
      case 16+11: //sypialnia 1
        sypialnia_req(index, val); break;

      case 16+5: //podswitelenie mix
        mcp_digitalWrite(PODSW_MIX_C, val); break; 
        
      case 16+6: //podswitelenie holu
        mcp_digitalWrite(PODSW_HOL_B, val); break;

      case 16+7: //podswitelenie salonu
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
#endif  
}
