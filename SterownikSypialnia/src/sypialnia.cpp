#include "sypialnia.hpp"
#include "utils.hpp"
#include "def_io.h"

extern bool sypialnia1;
extern bool sypialnia2;

void Sypialnia(bool wieczor, bool noc, bool awaria, bool klL, bool klP)
{
  static unsigned long mls = 0;
  if (millis() - mls < 50)
    return;
#ifdef DEBUG_CODE
  Serial.println("Sypialnia");
  Serial.println("L P");
  Serial.print(klL);
  Serial.print(" ");
  Serial.println(klP);
#endif

  mls = millis();

  if (awaria) {
    if (klL || klP) {
      sypialnia1 = !sypialnia1;
      mcp_digitalWrite(OSW_SYPIALNIA1, (sypialnia1) ? HIGH : LOW);
      return;
    }
  }


  if (klL) {
    sypialnia1 = !sypialnia1;
    mcp_digitalWrite(OSW_SYPIALNIA1, (sypialnia1) ? HIGH : LOW);
  }

  if (klP) {
    sypialnia2 = !sypialnia2;
    mcp_digitalWrite(OSW_SYPIALNIA2, (sypialnia2) ? HIGH : LOW);
  }

  return;
}

void SypialniaZasAwar(bool wieczor, bool noc, bool on)  {
    if (on) {
        sypialnia2 = false;
        sypialnia1 = sypialnia1 && wieczor && !noc;

        mcp_digitalWrite(OSW_SYPIALNIA1, sypialnia1 ? HIGH : LOW);
        mcp_digitalWrite(OSW_SYPIALNIA2, LOW);
        mcp_digitalWrite(OSW_SYPIALNIA3, LOW); //kinkiety

    } else {
        sypialnia1 = sypialnia1 && wieczor && !noc;
        sypialnia2 = false;
        mcp_digitalWrite(OSW_SYPIALNIA1, sypialnia1 ? HIGH : LOW);
        mcp_digitalWrite(OSW_SYPIALNIA2, sypialnia2 ? HIGH : LOW);
        mcp_digitalWrite(OSW_SYPIALNIA3, HIGH); //kinkiety
    }
}

bool sypialnia_isOn()
{
  return sypialnia1 || sypialnia2;
}

void sypialnia_off()
{
  sypialnia1 = sypialnia2 = false;
  mcp_digitalWrite(OSW_SYPIALNIA1, LOW);
  mcp_digitalWrite(OSW_SYPIALNIA2, LOW);
  mcp_digitalWrite(OSW_SYPIALNIA3, LOW); 

}
#ifdef RS485
void sypialnia_req(uint8_t index, bool val)
{
  switch(index) {
    case OSW_SYPIALNIA2: //sypialnia 2
      sypialnia2 = val;
      mcp_digitalWrite(OSW_SYPIALNIA2, sypialnia2 ? HIGH : LOW);
      mcp_digitalWrite(SWIATLO_SYPIALNIA, (sypialnia1 || sypialnia2) ? HIGH : LOW); 
      break;

    case OSW_SYPIALNIA3: //sypialnia kinkiety
      mcp_digitalWrite(OSW_SYPIALNIA3, val ? HIGH : LOW);
      mcp_digitalWrite(SWIATLO_SYPIALNIA, (sypialnia1 || sypialnia2) ? HIGH : LOW); 
      break; 
      
    case OSW_SYPIALNIA1: //sypialnia 1
      sypialnia1 = val;
      mcp_digitalWrite(OSW_SYPIALNIA1, sypialnia1 ? HIGH : LOW);
      break;
    default: return;
  }
}
#endif