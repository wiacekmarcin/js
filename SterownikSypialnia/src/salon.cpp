#include "salon.hpp"
#include "utils.hpp"
#include "def_io.h"
#include "hol.hpp"

extern bool salon1;
extern bool salon2;
extern bool ledL1;
extern bool ledL2;
extern bool ledS1;
extern bool ledS2;

void SalonJadalnia(bool wieczor, bool noc, bool awaria, bool klLL, bool klLP, bool klPL, bool klPP)
{
    static unsigned long mls = 0;
    if (millis() - mls < 50 || !(klLL || klLP || klPL || klPP))
        return;
#ifdef DEBUG_CODE
    Serial.println("SalonJadalnia");
    Serial.println("LL LP PL PP");
    Serial.print(" ");
    Serial.print(klLL);
    Serial.print("  ");
    Serial.print(klLP);
    Serial.print("  ");
    Serial.print(klPL);
    Serial.print("  ");
    Serial.println(klPP);
#endif    
    mls = millis();

    SalonMain(wieczor, noc, awaria, false, false, klPL, klPP, klLL, klLP, true);
}

void SalonKuchnia(bool wieczor, bool noc, bool awaria, bool klLL, bool klLP, bool klPL, bool klPP)
{
    static unsigned long mls = 0;
    if (millis() - mls < 50 || !(klLL || klLP || klPL || klPP))
        return;
#ifdef DEBUG_CODE
    Serial.println("SalonKuchnia");
    Serial.println("LL LP PL PP");
    Serial.print(" ");
    Serial.print(klLL);
    Serial.print("  ");
    Serial.print(klLP);
    Serial.print("  ");
    Serial.print(klPL);
    Serial.print("  ");
    Serial.println(klPP);
#endif    
    mls = millis();

    SalonMain(wieczor, noc, awaria, klLL, klLP, klPL, klPP, false, false, false);
}

void SalonSypialnia(bool wieczor, bool noc, bool awaria, bool klLL, bool klLP, bool klPL, bool klPP)
{
    static unsigned long mls = 0;
    if (millis() - mls < 50)
        return;
#ifdef DEBUG_CODE        
    Serial.println("SalonSypialnia");
    Serial.println("LL LP PL PP");
    Serial.print(" ");
    Serial.print(klLL);
    Serial.print("  ");
    Serial.print(klLP);
    Serial.print("  ");
    Serial.print(klPL);
    Serial.print("  ");
    Serial.println(klPP);
#endif    
    mls = millis();

    SalonMain(wieczor, noc, awaria, false, false, klLL, klLP, klPL, klPP, true);
}

void SalonSalon(bool wieczor, bool noc, bool awaria, bool klL, bool klP)
{
    static unsigned long mls = 0;
    if (millis() - mls < 50)
        return;
#ifdef DEBUG_CODE
    Serial.println("SalonSalon");
    Serial.println("L P");
    Serial.print(klL);
    Serial.print(" ");
    Serial.println(klP);
#endif

    mls = millis();

    SalonMain(wieczor, noc, awaria, false, false, klL, klP, false, false, false);
}

void SalonLedLaz(bool wieczor, bool noc, bool awaria, bool klL, bool klP)
{
    static unsigned long mls = 0;
    if (millis() - mls < 50)
        return;

#ifdef DEBUG_CODE
    Serial.println("SalonLedLaz");
    Serial.println("L P");
    Serial.print(klL);
    Serial.print(" ");
    Serial.println(klP);
#endif    
    mls = millis();

    SalonMain(wieczor, noc, awaria, klL, klP, false, false, false, false, false);
}
#define PR(val) Serial.print(#val);Serial.print("=");Serial.println(val)
void SalonMain(bool wieczor, bool noc, bool awaria, 
    bool klL_Laz, bool klP_Laz, bool klL_sal, bool klP_sal, bool klL_Syp, bool klP_Syp,
    bool ledSyp)
{
#ifdef DEBUG_CODE
    Serial.println("SalonMain");
    PR(wieczor);
    PR(noc);
    PR(awaria);
    PR(klL_Laz);
    PR(klP_Laz);
    PR(klL_sal);
    PR(klP_sal);
    PR(klL_Syp);
    PR(klP_Syp);
    PR(ledSyp);
#endif
    if (awaria)
    {
        if (klL_Laz || klP_Laz || klL_sal || klP_sal || klL_Syp || klP_Syp)
        {
            salon1 = !salon1;
            mcp_digitalWrite(OSW_SALON1, (salon1) ? HIGH : LOW);
            return;
        }
    }

    if (noc && !ledL1 && !ledL2 && !ledS1 && !ledS2 && !salon1 && !salon2)
    {
        if (klL_Laz || klP_Laz)
        {
            ledL1 = true;
            mcp_digitalWrite(LED1_LAZIENKA1, (ledL1) ? HIGH : LOW);
            mcp_digitalWrite(ZAS12V, (ledL1 || ledL2 || ledS1 || ledS2) ? HIGH : LOW);
            return;
        }

        if (klL_Syp || klP_Syp)
        {
            ledS1 = true;
            mcp_digitalWrite(LED3_SYPIALNIA1, (ledS1) ? HIGH : LOW);
            mcp_digitalWrite(ZAS12V, (ledL1 || ledL2 || ledS1 || ledS2) ? HIGH : LOW);
            return;
        }

        if (klL_sal || klP_sal) 
        {
            ledL1 = !ledSyp;
            ledS1 = ledSyp;
            mcp_digitalWrite(LED1_LAZIENKA1, (ledL1) ? HIGH : LOW);
            mcp_digitalWrite(LED3_SYPIALNIA1, (ledS1) ? HIGH : LOW);
            mcp_digitalWrite(ZAS12V, (ledL1 || ledL2 || ledS1 || ledS2) ? HIGH : LOW);
            return;
        }
    }

    if (klL_Syp)
    {
        ledS1 = !ledS1;
        mcp_digitalWrite(LED3_SYPIALNIA1, (ledS1) ? HIGH : LOW);
    }

    if (klP_Syp)
    {
        ledS2 = !ledS2;
        mcp_digitalWrite(LED4_SYPIALNIA2, (ledS2) ? HIGH : LOW);
    }

    if (klL_sal)
    {
        salon1 = !salon1;
        mcp_digitalWrite(OSW_SALON1, (salon1) ? HIGH : LOW);
    }

    if (klP_sal)
    {
        salon2 = !salon2;
        mcp_digitalWrite(OSW_SALON2, (salon2) ? HIGH : LOW);
    }

    if (klL_Laz)
    {
        ledL1 = !ledL1;
        mcp_digitalWrite(LED1_LAZIENKA1, (ledL1) ? HIGH : LOW);
    }

    if (klP_Laz)
    {
        ledL2 = !ledL2;
        mcp_digitalWrite(LED2_LAZIENKA2, (ledL2) ? HIGH : LOW);
    }

    mcp_digitalWrite(ZAS12V, (ledL1 || ledL2 || ledS1 || ledS2) ? HIGH : LOW);
    return;
}


void SalonZasAwar(bool wieczor, bool noc, bool zasAwar)
{
    if (zasAwar) {
        salon2 = false;
        ledL1 = false;
        ledL2 = false;
        ledS1 = false;
        ledS2 = false;

        salon1 = salon1 && wieczor && !noc;
        mcp_digitalWrite(OSW_SALON1, salon1 ? HIGH : LOW);
        mcp_digitalWrite(OSW_SALON2, LOW);
        mcp_digitalWrite(ZAS12V, LOW); 
        mcp_digitalWrite(LED1_LAZIENKA1, LOW);
        mcp_digitalWrite(LED2_LAZIENKA2, LOW);
        mcp_digitalWrite(LED3_SYPIALNIA1, LOW);
        mcp_digitalWrite(LED4_SYPIALNIA2, LOW);
    } else {
        salon1 = salon1 && wieczor && !noc;
        salon2 = salon1;
        ledL1 = false;
        ledL2 = false;
        ledS1 = false;
        ledS2 = false;
        mcp_digitalWrite(OSW_SALON1, salon1 ? HIGH : LOW);
        mcp_digitalWrite(OSW_SALON2, salon2 ? HIGH : LOW);
        mcp_digitalWrite(ZAS12V, LOW); 
        mcp_digitalWrite(LED1_LAZIENKA1, LOW);
        mcp_digitalWrite(LED2_LAZIENKA2, LOW);
        mcp_digitalWrite(LED3_SYPIALNIA1, LOW);
        mcp_digitalWrite(LED4_SYPIALNIA2, LOW);
    }   
}

bool salon_isOn()
{
    return salon1 || salon2 || ledL1 || ledL2 || ledS1 || ledS2;
}

void salon_off()
{
    salon1 = salon2 = ledL1 = ledL2 = ledS1 = ledS2 = false;
    mcp_digitalWrite(OSW_SALON1, LOW);
    mcp_digitalWrite(OSW_SALON2, LOW);
    mcp_digitalWrite(ZAS12V, LOW); 
    mcp_digitalWrite(LED1_LAZIENKA1, LOW);
    mcp_digitalWrite(LED2_LAZIENKA2, LOW);
    mcp_digitalWrite(LED3_SYPIALNIA1, LOW);
    mcp_digitalWrite(LED4_SYPIALNIA2, LOW);
}

#ifdef RS485
void salon_req(uint8_t index, bool val)
{

    switch(index) {
        case 4: //ledy kolo lazienki 1
            ledL1 = val; 
            mcp_digitalWrite(LED1_LAZIENKA1, val ? HIGH : LOW);
            mcp_digitalWrite(ZAS12V, (ledL1 || ledL2 || ledS1 || ledS2) ? HIGH : LOW);
            mcp_digitalWrite(SWIATLO_SALON, (ledL1 || ledL2 || ledS1 || ledS2 || salon1 || salon2) ? HIGH : LOW);
            mcp_digitalWrite(PODSW_MIX_C, (ledL1 || ledL2 || ledS1 || ledS2 || salon1 || salon2 || hol_isOn()) ? LOW : HIGH);
            break;

        case 5: //ledy kolo lazienki 2
            ledL2 = val; 
            mcp_digitalWrite(LED2_LAZIENKA2, val ? HIGH : LOW);
            mcp_digitalWrite(ZAS12V, (ledL1 || ledL2 || ledS1 || ledS2) ? HIGH : LOW);
            mcp_digitalWrite(SWIATLO_SALON, (ledL1 || ledL2 || ledS1 || ledS2 || salon1 || salon2) ? HIGH : LOW);
            mcp_digitalWrite(PODSW_MIX_C, (ledL1 || ledL2 || ledS1 || ledS2 || salon1 || salon2 || hol_isOn()) ? LOW : HIGH);
            break;

        case 14: //ledy kolo salonu 2
            ledS2 = val; 
            mcp_digitalWrite(LED4_SYPIALNIA2, val ? HIGH : LOW);
            mcp_digitalWrite(ZAS12V, (ledL1 || ledL2 || ledS1 || ledS2) ? HIGH : LOW);
            mcp_digitalWrite(SWIATLO_SALON, (ledL1 || ledL2 || ledS1 || ledS2 || salon1 || salon2) ? HIGH : LOW);
            mcp_digitalWrite(PODSW_MIX_C, (ledL1 || ledL2 || ledS1 || ledS2 || salon1 || salon2 || hol_isOn()) ? LOW : HIGH);
            break;

        case 15: //ledy kolo salonu 1
            ledS1 = val; 
            mcp_digitalWrite(LED3_SYPIALNIA1, val ? HIGH : LOW);
            mcp_digitalWrite(ZAS12V, (ledL1 || ledL2 || ledS1 || ledS2) ? HIGH : LOW);
            mcp_digitalWrite(SWIATLO_SALON, (ledL1 || ledL2 || ledS1 || ledS2 || salon1 || salon2) ? HIGH : LOW);
            mcp_digitalWrite(PODSW_MIX_C, (ledL1 || ledL2 || ledS1 || ledS2 || salon1 || salon2 || hol_isOn()) ? LOW : HIGH);
            break;

        case 16+12: //Salon 2
            salon2 = val; 
            mcp_digitalWrite(OSW_SALON2, val ? HIGH : LOW);
            mcp_digitalWrite(SWIATLO_SALON, (ledL1 || ledL2 || ledS1 || ledS2 || salon1 || salon2) ? HIGH : LOW);
            mcp_digitalWrite(PODSW_MIX_C, (ledL1 || ledL2 || ledS1 || ledS2 || salon1 || salon2 || hol_isOn()) ? LOW : HIGH);
            break;

        case 16+15: //Salon 1
            salon1 = val;
            mcp_digitalWrite(OSW_SALON1, val ? HIGH : LOW);
            mcp_digitalWrite(SWIATLO_SALON, (ledL1 || ledL2 || ledS1 || ledS2 || salon1 || salon2) ? HIGH : LOW);
            mcp_digitalWrite(PODSW_MIX_C, (ledL1 || ledL2 || ledS1 || ledS2 || salon1 || salon2 || hol_isOn()) ? LOW : HIGH);
            break;
        
        default :
            return;
    }
}
#endif    
