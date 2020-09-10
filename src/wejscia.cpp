#include "wejscia.h"
#include "util.h"

Wejscia::Wejscia() :
    wejscia(0x20)
{

}

void Wejscia::init()
{
    wejscia.begin();      
    wejscia.pinMode(CZ_R_LUSTRO, INPUT);
    wejscia.pinMode(CZ_R_WC, INPUT);
    wejscia.pinMode(DRZWI, INPUT);
    wejscia.pinMode(KLAWISZ, INPUT);
    wejscia.pinMode(NOC, INPUT);
    wejscia.pinMode(WIECZOR, INPUT);
    //wejscia.pinMode(CZ_POZ_WODY, INPUT);
}


void Wejscia::get() 
{
    for (uint8_t i = 0; i < lenWej; ++i) {
        w[i] = wejscia.digitalRead(i);
    }
}

bool Wejscia::isChange() const
{
    for (uint8_t i = 0; i < lenWej; ++i) {
        if (w[i].isChange())
            return true;
    }
    return false;
}

void Wejscia::print() {
    Serial.println("--- Wejscia --- ");
    Serial.print("- isChange : ");
    Serial.println(isChange(), DEC);

    const char et[] = { "| wlacznik |" 
                        "|   lustro |"
                        "| cz. ruchu|" 
                        "|    drzwi |"
                        "|  wieczor |" 
                        "|      noc |"};
    int klucze[] = { KLAWISZ, CZ_R_LUSTRO, CZ_R_WC, DRZWI, WIECZOR, NOC };

    Serial.println(et);
    for (int n = 0; n < lenWej; n++) {
        Serial.print("|     ");
        Serial.print(wejscia.digitalRead(klucze[n]) == LOW ? "L" : "H");
        Serial.print("     ");
    }
    Serial.println("|");
    for (int n = 0; n < lenWej; n++) {
        Serial.print("|     ");
        Serial.print(w[klucze[n]] == true ? "T" : "N");
        Serial.print("     ");
    }
    Serial.println("|");
    for (int n = 0; n < lenWej; n++) {
        Serial.print("|    ");
        Serial.print(w[klucze[n]].isChange() == true ? "CHG" : "NCH");
        Serial.print("    ");
    }
    Serial.println("|");

    char buff[11];
    for (int n = 0; n < lenWej; n++) {
        Serial.print("|");
        printtime(w[klucze[n]].time(), buff);
        Serial.print(buff);
        Serial.print("");
    }
    Serial.println("|");

    for (int n = 0; n < lenWej; n++) {
        Serial.print("|");
        printtime(w[klucze[n]].prevtime(), buff);
        Serial.print(buff);
        Serial.print("");
    }
    Serial.println("|");
}
