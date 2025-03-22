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

  Serial.println("Sypialnia");
  Serial.println("L P");
  Serial.print(klL);
  Serial.print(" ");
  Serial.println(klP);

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

void SypialniaZasAwar(bool wieczor, bool on)  {
    if (on) {
        sypialnia2 = false;
        if (!wieczor) { //dla wieczora utrzymaj swiatlo dla innej pory dnia wylacz
            sypialnia1 = false;
        } 
        mcp_digitalWrite(OSW_SYPIALNIA1, sypialnia1 ? HIGH : LOW);
        mcp_digitalWrite(OSW_SYPIALNIA2, LOW);
        mcp_digitalWrite(OSW_SYPIALNIA3, LOW); //kinkiety

    } else {
        mcp_digitalWrite(OSW_SYPIALNIA1, sypialnia1 ? HIGH : LOW);
        mcp_digitalWrite(OSW_SYPIALNIA2, sypialnia2 ? HIGH : LOW);
        mcp_digitalWrite(OSW_SYPIALNIA3, HIGH); //kinkiety
    }
}

void sypialnia_req(uint8_t index, bool val)
{
  switch(index) {
    case 16+8: //sypialnia 2
      sypialnia2 = val;
      mcp_digitalWrite(OSW_SYPIALNIA2, sypialnia2 ? HIGH : LOW);
      mcp_digitalWrite(SWIATLO_SYPIALNIA, (sypialnia1 || sypialnia2) ? HIGH : LOW); 
      break;

    case 16+9: //sypialnia kinkiety
      mcp_digitalWrite(OSW_SYPIALNIA3, val ? HIGH : LOW);
      mcp_digitalWrite(SWIATLO_SYPIALNIA, (sypialnia1 || sypialnia2) ? HIGH : LOW); 
      break; 
      
    case 16+11: //sypialnia 1
      sypialnia1 = val;
      mcp_digitalWrite(OSW_SYPIALNIA1, sypialnia1 ? HIGH : LOW);
      break;
    default: return;
  }
}
