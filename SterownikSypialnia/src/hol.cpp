#include "hol.hpp"
#include "def_io.h"
#include "utils.hpp"
uint8_t A[3]{OSW_HOL_A1, OSW_HOL_A2, OSW_HOL_A3};
uint8_t B[4]{OSW_HOL_B1, OSW_HOL_B2, OSW_HOL_B3, OSW_HOL_B4};

LampaLed holL3(3, A);
LampaLed holL4(4, B);
bool l4_230 = false;

void Hol(bool wieczor, bool noc, bool awaria, 
    bool kl3L1, bool kl3P1, bool kl3L2, bool kl3P2,
    bool kl4L1, bool kl4P1, bool kl4L2, bool kl4P2,
    bool klPok, bool klWej)
{
    Serial.println("Hol");
    Serial.println("3L1 3P1 3L2 3P2 | 4L1 4P1 4L2 4P2 | POK WEJ | WIE NOC AWA");
    Serial.print(" ");
    Serial.print(kl3L1);
    Serial.print("   ");
    Serial.print(kl3P1);
    Serial.print("   ");
    Serial.print(kl3L2);
    Serial.print("   ");
    Serial.print(kl3P2);
    Serial.print("  |  ");
    Serial.print(kl4L1);
    Serial.print("   ");
    Serial.print(kl4P1);
    Serial.print("   ");
    Serial.print(kl4L2);
    Serial.print("   ");
    Serial.print(kl4P2);
    Serial.print("  |  ");
    Serial.print(klPok);
    Serial.print("   ");
    Serial.print(klWej);
    Serial.print("  |  ");
    Serial.print(wieczor);
    Serial.print("   ");
    Serial.print(noc);
    Serial.print("   ");
    Serial.print(awaria);
    Serial.print("   ");

    if (awaria) {
        holL3.off();
        holL4.off();

        if (kl3L1 || kl3P1 || kl3L2 || kl3P2 || kl4L1 || kl4P1 || kl4L2 || kl4P2 || klPok || klWej) {
            l4_230 = ! l4_230;
            mcp_digitalWrite(OSW_HOL_0, l4_230 ? HIGH : LOW);
        return;
        }
    }

    bool allOff = !holL3.isOn() && !holL4.isOn() && !l4_230;
    if (noc) {
        
        if ((kl3L1 || kl3P1 || kl3L2 || kl3P2 || kl4L1 || kl4P1 || kl4L2 || kl4P2 || klPok || klWej) && allOff) {
            //dowolny klawisz bez swiatla
            l4_230 = true;
            mcp_digitalWrite(OSW_HOL_0, HIGH);
        return;
        }

    }

    if (! allOff && (klPok || klWej) ) {
        //klawisz przy pokojach przy wlaczonym swietle
        l4_230 = false;
        mcp_digitalWrite(OSW_HOL_0, LOW);
        holL3.off();
        holL4.off();
    }

    if (kl3P1 || kl3P2) {
        l4_230 = false;
        mcp_digitalWrite(OSW_HOL_0, LOW);
        holL3.on1();
    }

    if (kl3L1 || kl3L2) {
        holL3.off1();
    }

    if ((kl3L1 && kl3P1) || (kl3L2 && kl3P2)) {
        holL3.off();
    }  

    if (kl4P1 || kl4P2) {
        if (noc && !holL4.isAll()) {
            l4_230 = false;
            mcp_digitalWrite(OSW_HOL_0, LOW);
        } else if (holL4.isAll() && !l4_230) {
            l4_230 = true;
            mcp_digitalWrite(OSW_HOL_0, HIGH);
        } else if (holL4.isAll() && l4_230) {
            holL4.off();
        } else {
            holL4.on1();
        }
    }

    if (kl4L1 || kl4L2) {
        if (l4_230) { 
            l4_230 = false;
            mcp_digitalWrite(OSW_HOL_0, LOW);
        } else {
            holL4.off1();
        }
    }

    if ((kl4L1 && kl4P1) || (kl4L2 && kl4P2)) {
        holL4.off();
        l4_230 = false;
        mcp_digitalWrite(OSW_HOL_0, LOW);
    }      
}

void hol_tiktok()
{
    holL4.tiktok();
    holL3.tiktok();
}