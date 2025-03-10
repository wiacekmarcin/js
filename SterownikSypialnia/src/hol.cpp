#include "hol.hpp"
#include "def_io.h"
#include "utils.hpp"

void Hol(bool wieczor, bool noc, bool awaria, bool klLA1, bool klPA1, bool klLA2, bool klPA2,
    bool klLB1, bool klPB1, bool klLB2, bool klPB2,
  bool klPok, bool klWej)
{
    Serial.println("Hol");
    Serial.println("ALL ALP APL APP | BLL BLP BPL BPP | POK WEJ");
    Serial.print(" ");
    Serial.print(klLA1);
    Serial.print("   ");
    Serial.print(klPA1);
    Serial.print("   ");
    Serial.print(klLA2);
    Serial.print("   ");
    Serial.print(klPA2);
    Serial.print("  |  ");
    Serial.print(klLB1);
    Serial.print("   ");
    Serial.print(klPB1);
    Serial.print("   ");
    Serial.print(klLB2);
    Serial.print("   ");
    Serial.print(klPB2);
    Serial.print("  |  ");
    Serial.print(klPok);
    Serial.print("   ");
    Serial.println(klWej);


    if (awaria) {
        if (klLA1 || klPA1 || klLA2 || klPA2 || klLB1 || klPB1 || klLB2 || klPB2 || klPok || klWej) {
            bhol = bhol ^ (0x1);
            mcp_digitalWrite(OSW_HOL_0, ((bhol & 0x1) == 0x01) ? HIGH : LOW);
        return;
        }
    }

    if (noc) {
        if ((klLA1 || klPA1 || klLA2 || klPA2 || klLB1 || klPB1 || klLB2 || klPB2 || klPok || klWej) && bhol == 0x00) {
            bhol = bhol ^ (0x1);
            mcp_digitalWrite(OSW_HOL_0, ((bhol & 0x1) == 0x01) ? HIGH : LOW);
        return;
        }
    }

    if (noc) {
        if ((klLA1 || klPA1 || klLA2 || klPA2 || klLB1 || klPB1 || klLB2 || klPB2 || klPok || klWej) && bhol == 0x01) {
            bhol = 0x00;
            mcp_digitalWrite(OSW_HOL_0, LOW);
        }
    }

    if (wieczor) {
        if ((klLA1 || klPA1 || klLA2 || klPA2 || klLB1 || klPB1 || klLB2 || klPB2 || klPok || klWej) && bhol == 0x00) {
            bhol = 0x01;
            mcp_digitalWrite(OSW_HOL_0, HIGH);
            return;
        }
    

        if (klPA1 || klPA2) {
            if ((bhol & 0x1f) == 0x01) {
                bhol |= 0x02;
                mcp_digitalWrite(OSW_HOL_0, LOW);
                mcp_digitalWrite(OSW_HOL_B1, HIGH);
                return;
            }
        }

        if ((bhol & 0x1f) == 0x1e) {
            bhol |= 0xe1;
            mcp_digitalWrite(OSW_HOL_0, HIGH);
            return;
        }

        if ((bhol & 0x1f) == 0x1f) {
            bhol &= 0x01;
            mcp_digitalWrite(OSW_HOL_0, HIGH);
            mcp_digitalWrite(OSW_HOL_B1, LOW);
            mcp_digitalWrite(OSW_HOL_B2, LOW);
            mcp_digitalWrite(OSW_HOL_B3, LOW);
            mcp_digitalWrite(OSW_HOL_B4, LOW);
            return;
        }

        for (uint8_t mask = 0x02; mask < 0x20; mask <<= 1) {
            if ((bhol & mask) == mask)
                continue;

            bhol |= mask;
            break;
        }
    }
}
