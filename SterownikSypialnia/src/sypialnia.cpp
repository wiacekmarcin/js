#include "sypialnia.hpp"
#include "utils.hpp"
#include "def_io.h"
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









