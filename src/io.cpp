#include "io.h"
struct wejscieconf wconf[] = {
    {NULL, ZASLED,      OUTPUT, LOW},
    {NULL, PRZEK,       OUTPUT, LOW},
    {NULL, ZAWAPRZ,     OUTPUT, LOW},
    {NULL, INTER,       INPUT_PULLUP,  HIGH},
    {&o20, PRZEK1,      OUTPUT, HIGH},
    {&o20, PRZEK2,      OUTPUT, HIGH},
    {&o20, PRZEK3,      OUTPUT, HIGH},
    {&o20, PRZEK4,      OUTPUT, HIGH},
    {&o20, PRZEK5,      OUTPUT, HIGH},
    {&o20, PRZEK6,      OUTPUT, HIGH},
    {&o20, PRZEK7,      OUTPUT, HIGH},
    {&o20, PRZEK8,      OUTPUT, HIGH},
    {&o20, PRZEK9,      OUTPUT, HIGH},
    {&o20, PRZEK10,     OUTPUT, HIGH},
    {&o20, PRZEK11,     OUTPUT, HIGH},
    {&o20, PRZEK12,     OUTPUT, HIGH},
    {&o20, PRZEK13,     OUTPUT, HIGH},
    {&o20, OSWKUCH,     OUTPUT, HIGH},
    {&o20, OSWJAD,      OUTPUT, HIGH},
    {&o20, LEDDRZ2,     OUTPUT, LOW},
    {&io24, KONTAKT,    INPUT,  LOW},
    {&io24, ZAS_AWAR,   INPUT,  HIGH},
    {&io24, TARYF2,     INPUT,  HIGH},
    {&io24, WIECZOR,    INPUT,  HIGH},
    {&io24, NOC,        INPUT,  HIGH},
    {&io24, LEDDRZ1,    OUTPUT, LOW},
    {&io24, LEDSUFL,    OUTPUT, LOW},
    {&io24, LEDSUFJ,    OUTPUT, LOW},
    {&io24, JAD2,       INPUT,  LOW},
    {&io24, JAD1,       INPUT,  LOW},
    {&io24, KUCHB2,     INPUT,  LOW},
    {&io24, KUCHB1,     INPUT,  LOW},
    {&io24, KUCHA2,     INPUT,  LOW},
    {&io24, KUCHA1,     INPUT,  LOW},
    {&io24, RUCH1,      INPUT,  LOW},
    {&io24, RUCH2,      INPUT,  LOW},
    {NULL,  -1,          -1,      -1}
};

void io_init() {
    short i = 0;
    o20.begin((uint8_t)0);
    io24.begin((uint8_t)4);
    while(wconf[i].pin != -1) {
        if (wconf[i].ptr == NULL) {
            pinMode(wconf[i].pin, wconf[i].input);
            if (wconf[i].input == OUTPUT) {
                digitalWrite(wconf[i].pin, !wconf[i].lowastrue);
            }
        }
        ++i;
    }

    i = 0;
    while(wconf[i].pin != -1) {
        if (wconf[i].ptr != NULL) {
            wconf[i].ptr->pinMode(wconf[i].pin, wconf[i].input);
                delay(5);
            if (wconf[i].input == OUTPUT) {
                wconf[i].ptr->digitalWrite(wconf[i].pin, !wconf[i].lowastrue);
                delay(5);
            }
        }
        ++i;
    }
}

void test(short pos) {
    if (pos < 0 || pos > 36)
        return;
    int i = 0;
    while(wconf[i].pin != -1) {
        bool z = false;
        if (i == pos) {
            z = true;
            Serial.print("pos=");
            Serial.print(i,DEC);
            Serial.print(" pin=");
            Serial.println(wconf[i].pin,DEC);
        }

        if (wconf[i].ptr != NULL) {
            if (wconf[i].input == OUTPUT) {
                wconf[i].ptr->digitalWrite(wconf[i].pin, z ? !wconf[i].lowastrue : wconf[i].lowastrue);
                Serial.print(wconf[i].ptr == &o20 ? "0x20." : "0x24.");
                Serial.print(wconf[i].pin, DEC);
                Serial.print(" = ");
                Serial.print(z, DEC);
                Serial.println((wconf[i].lowastrue ^ z) ? " H " : " L ");
            }
        } else {
            if (wconf[i].input == OUTPUT) {
                digitalWrite(wconf[i].pin, z ? wconf[i].lowastrue : !wconf[i].lowastrue);
                Serial.print("CPU.");
                Serial.print(wconf[i].pin, DEC);
                Serial.print(" ");
                Serial.print(z, DEC);
                Serial.println((wconf[i].lowastrue ^ z) ? " H " : " L ");
            }
        }
        ++i;
    }
}