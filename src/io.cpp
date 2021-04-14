#include "io.h"
struct wejscieconf wconf[] = {
    {NULL, ZASLED,      OUTPUT, LOW},
    {NULL, PRZEK,       OUTPUT, HIGH},
    {NULL, ZAWAPRZ,     OUTPUT, HIGH},
    {NULL, INTER,       INPUT,  LOW},
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
    {&io24, ZAS_AWAR,   INPUT, HIGH},
    {&io24, TARYF2,     INPUT, HIGH},
    {&io24, WIECZOR,    INPUT, HIGH},
    {&io24, NOC,        INPUT, HIGH},
    {&io24, LEDDRZ1,    OUTPUT, LOW},
    {&io24, LEDSUFL,    OUTPUT, LOW},
    {&io24, LEDSUFJ,    OUTPUT, LOW},
    {&io24, RUCH1,      INPUT, LOW},
    {&io24, RUCH2,      INPUT, LOW},
    {NULL,  -1,          -1,      -1}
};

void io_init() {
    short i = 0;
    while(wconf[i].pin != -1) {
        if (wconf[i].ptr == NULL) {
            pinMode(wconf[i].pin, wconf[i].input);
            if (wconf[i].input == OUTPUT) {
                digitalWrite(wconf[i].pin, !wconf[i].lowastrue);
            }
        }
        ++i;
    }
    o20.begin((uint8_t)o20_ADRESS-0x20);
    io24.begin((uint8_t)io24_ADRESS-0x20);

    while(wconf[i].pin != -1) {
        if (wconf[i].ptr != NULL) {
            wconf[i].ptr->pinMode(wconf[i].pin, wconf[i].input);
            if (wconf[i].input == OUTPUT) {
                wconf[i].ptr->digitalWrite(wconf[i].pin, !wconf[i].lowastrue);
            }
        }
        ++i;
    }
}