#include "salon.hpp"
#include "utils.hpp"
#include "def_io.h"

void SalonJadalnia(bool wieczor, bool noc, bool awaria, bool klLL, bool klLP, bool klPL, bool klPP)
{
    static unsigned long mls = 0;
    if (millis() - mls < 50)
        return;

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
    mls = millis();

    if (awaria)
    {
        if (klLL || klLP || klPL || klPP)
        {
            salon1 = !salon1;
            mcp_digitalWrite(OSW_SALON1, (salon1) ? HIGH : LOW);
            return;
        }
    }

    if (noc)
    {
        if ((klLL || klLP || klPL || klPP) && !led1 && !led2 && !led3 && !led4 && !salon1 && !salon2)
        {
            led3 = true;
            mcp_digitalWrite(LED3_SYPIALNIA1, (led3) ? HIGH : LOW);
            return;
        }
    }

    if (klLL)
    {
        led3 = !led3;
        mcp_digitalWrite(LED3_SYPIALNIA1, (led3) ? HIGH : LOW);
    }

    if (klLP)
    {
        led4 = !led4;
        mcp_digitalWrite(LED4_SYPIALNIA2, (led4) ? HIGH : LOW);
    }

    if (klPL)
    {
        salon1 = !salon1;
        mcp_digitalWrite(OSW_SALON1, (salon1) ? HIGH : LOW);
    }

    if (klLP)
    {
        salon2 = !salon2;
        mcp_digitalWrite(OSW_SALON2, (salon2) ? HIGH : LOW);
    }

    return;
}

void SalonKuchnia(bool wieczor, bool noc, bool awaria, bool klLL, bool klLP, bool klPL, bool klPP)
{
    static unsigned long mls = 0;
    if (millis() - mls < 50)
        return;

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
    mls = millis();

    if (awaria)
    {
        if (klLL || klLP || klPL || klPP)
        {
            salon1 = !salon1;
            mcp_digitalWrite(OSW_SALON1, (salon1) ? HIGH : LOW);
            return;
        }
    }

    if (noc)
    {
        if ((klLL || klLP || klPL || klPP) && !led1 && !led2 && !led3 && !led4 && !salon1 && !salon2)
        {
            led1 = true;
            mcp_digitalWrite(LED1_LAZIENKA1, (led1) ? HIGH : LOW);
            return;
        }
    }

    if (klLL)
    {
        led1 = !led1;
        mcp_digitalWrite(LED1_LAZIENKA1, (led1) ? HIGH : LOW);
    }

    if (klLP)
    {
        led2 = !led2;
        mcp_digitalWrite(LED2_LAZIENKA2, (led2) ? HIGH : LOW);
    }

    if (klPL)
    {
        salon1 = !salon1;
        mcp_digitalWrite(OSW_SALON1, (salon1) ? HIGH : LOW);
    }

    if (klLP)
    {
        salon2 = !salon2;
        mcp_digitalWrite(OSW_SALON2, (salon2) ? HIGH : LOW);
    }

    return;
}

void SalonSypialnia(bool wieczor, bool noc, bool awaria, bool klLL, bool klLP, bool klPL, bool klPP)
{
    static unsigned long mls = 0;
    if (millis() - mls < 50)
        return;

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
    mls = millis();

    if (awaria)
    {
        if (klLL || klLP || klPL || klPP)
        {
            salon1 = !salon1;
            mcp_digitalWrite(OSW_SALON1, (salon1) ? HIGH : LOW);
        }
        return;
    }

    if (noc)
    {
        if ((klLL || klLP || klPL || klPP) && !led1 && !led2 && !led3 && !led4 && !salon1 && !salon2)
        {
            led3 = true;
            mcp_digitalWrite(LED3_SYPIALNIA1, (led3) ? HIGH : LOW);
            return;
        }
    }

    if (klLL)
    {
        led3 = !led3;
        mcp_digitalWrite(LED3_SYPIALNIA1, (led3) ? HIGH : LOW);
    }

    if (klLP)
    {
        led4 = !led4;
        mcp_digitalWrite(LED4_SYPIALNIA2, (led4) ? HIGH : LOW);
    }

    if (klPL)
    {
        salon1 = !salon1;
        mcp_digitalWrite(OSW_SALON1, (salon1) ? HIGH : LOW);
    }

    if (klLP)
    {
        salon2 = !salon2;
        mcp_digitalWrite(OSW_SALON2, (salon2) ? HIGH : LOW);
    }

    return;
}

void Salon(bool wieczor, bool noc, bool awaria, bool klL, bool klP)
{
    static unsigned long mls = 0;
    if (millis() - mls < 50)
        return;

    Serial.println("Salon");
    Serial.println("L P");
    Serial.print(klL);
    Serial.print(" ");
    Serial.println(klP);
    mls = millis();

    if (awaria)
    {
        if (klL || klP)
        {
            salon1 = !salon1;
            mcp_digitalWrite(OSW_SALON1, (salon1) ? HIGH : LOW);
            return;
        }
    }

    if (noc)
    {
        if ((klL || klP) && !led1 && !led2 && !led3 && !led4 && !salon1 && !salon2)
        {
            led3 = true;
            mcp_digitalWrite(LED3_SYPIALNIA1, (led3) ? HIGH : LOW);
            return;
        }
    }

    if (klL)
    {
        salon1 = !salon1;
        mcp_digitalWrite(OSW_SALON1, (salon1) ? HIGH : LOW);
    }

    if (klP)
    {
        salon2 = !salon2;
        mcp_digitalWrite(OSW_SALON2, (salon2) ? HIGH : LOW);
    }

    return;
}

void SalonLedLaz(bool wieczor, bool noc, bool awaria, bool klL, bool klP)
{
    static unsigned long mls = 0;
    if (millis() - mls < 50)
        return;

    Serial.println("SalonLedLaz");
    Serial.println("L P");
    Serial.print(klL);
    Serial.print(" ");
    Serial.println(klP);
    mls = millis();

    if (awaria)
    {
        if (klL || klP)
        {
            salon1 = !salon1;
            mcp_digitalWrite(OSW_SALON1, (salon1) ? HIGH : LOW);
            return;
        }
    }

    if (noc)
    {
        if ((klL || klP) && !led1 && !led2 && !led3 && !led4 && !salon1 && !salon2)
        {
            led3 = true;
            mcp_digitalWrite(LED1_LAZIENKA1, (led3) ? HIGH : LOW);
            return;
        }
    }

    if (klL)
    {
        led1 = !led1;
        mcp_digitalWrite(LED1_LAZIENKA1, (led1) ? HIGH : LOW);
    }

    if (klP)
    {
        led2 = !led2;
        mcp_digitalWrite(LED2_LAZIENKA2, (led2) ? HIGH : LOW);
    }

    return;
}

void SalonZasAwar(bool wieczor, bool zasAwar)
{
    if (zasAwar) {
        salon2 = false;
        led1 = false;
        led2 = false;
        led3 = false;
        led4 = false;

        if (!wieczor) { //dla wieczora utrzymaj swiatlo dla innej pory dnia wylacz
            salon1 = false;
        } 
        mcp_digitalWrite(OSW_SALON1, salon1 ? HIGH : LOW);
        mcp_digitalWrite(OSW_SALON2, LOW);
        mcp_digitalWrite(ZAS12V, LOW); 
        mcp_digitalWrite(LED1_LAZIENKA1, LOW);
        mcp_digitalWrite(LED2_LAZIENKA2, LOW);
        mcp_digitalWrite(LED3_SYPIALNIA1, LOW);
        mcp_digitalWrite(LED4_SYPIALNIA2, LOW);


    } else {
        salon2 = salon1;
        mcp_digitalWrite(OSW_SALON1, salon1 ? HIGH : LOW);
        mcp_digitalWrite(OSW_SALON2, salon2 ? HIGH : LOW);
    }   
}
