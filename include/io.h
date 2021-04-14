#ifndef IO_PINS_H
#define IO_PINS_H

#include "main.h"

#ifdef NEW_BOARD
#include <Arduino.h>
#include <Wire.h>
#include <Adafruit_MCP23017.h>

extern Adafruit_MCP23017 o20;
extern Adafruit_MCP23017 io24;

#define o20_ADRESS  0x20
#define io24_ADRESS 0x24

#define    PRZEK1    0        //A0 OUT
#define    PRZEK2    1        //A1 OUT
#define    PRZEK3    2        //A2 OUT
#define    PRZEK4    3        //A3 OUT
#define    PRZEK5    4        //A4 OUT
#define    PRZEK6    5        //A5 OUT
#define    PRZEK7    6        //A6 OUT
#define    PRZEK8    7        //A7 OUT
#define    PRZEK9    8        //B0 OUT
#define    PRZEK10   9        //B1 OUT
#define    PRZEK11  10        //B2 OUT
#define    PRZEK12  11        //B3 OUT
#define    PRZEK13  12        //B4 OUT
#define    OSWKUCH  13        //B5 OUT
#define    OSWJAD   14        //B6 OUT
#define    LEDDRZ2  15        //B7 OUT    



#define    KONTAKT    0   //A0 IN
#define    ZAS_AWAR   1   //A1 IN 
#define    TARYF2     2   //A2 IN 
#define    WIECZOR    3   //A3 IN 
#define    NOC        4   //A4 IN
#define    LEDDRZ1    5   //A5 OUT
#define    LEDSUFL    6   //A6 OUT
#define    LEDSUFJ    7   //A7 OUT
#define    JAD2       8   //B0 IN
#define    JAD1       9   //B1 IN
#define    KUCHB2    10   //B2 IN
#define    KUCHB1    11   //B3 IN
#define    KUCHA2    12   //B4 IN
#define    KUCHA1    13   //B5 IN
#define    RUCH1     14   //B6 IN
#define    RUCH2     15   //B7 IN

#define    PRZEK      5
#define    ZAWAPRZ    6
#define    INTER      7
#define    ZASLED     8

struct wejscieconf {
//public:    
    /*wejscieconf(Adafruit_MCP23017 * pt, int pi, int in, int lo) :
        ptr(pt), pin(pi), input(in), lowastrue(lo)
     { }*/
    Adafruit_MCP23017 * ptr;
    short pin;
    short input;
    short lowastrue;
};

extern struct wejscieconf wconf[];


void io_init();

inline void zapalJadalnia(short nr, bool zapal) {
    //przekazniki 11,12,13
    if (nr < 1 || nr > 3)
        return;
    static const uint8_t mapPins[3] = {9, 8, 12};    
    o20.digitalWrite(mapPins[nr-1], zapal ? HIGH : LOW);
}

inline void zapalKuchnia(short nr, bool zapal) {
    if (nr < 1 || nr > 9)
        return;
    //na listwie               2 7 1 6 8 4 9 3 | 5 10 11 12 | 13
    //wejscia na przekaznikach 8 7 6 5 4 3 2 1 | 4  3  2  1 |  1
    //wejscia na expanderach   7 6 5 4 3 2 1 0 | 11 10 9  8 |  12
    static const uint8_t mapPins[9] = {5, 7, 0, 2, 11, 4, 6, 3, 1};
    o20.digitalWrite(mapPins[nr-1], zapal ? HIGH : LOW);
}           

inline void zapalSzafki(bool zapal) {
    o20.digitalWrite(PRZEK10, zapal ? HIGH : LOW);
}

inline void zapalLEDZasilacz(bool zapal) {
    digitalWrite(ZASLED, zapal ? LOW : HIGH);
}

inline void zapalPrzekazniki(bool zapal) {
    digitalWrite(PRZEK, zapal ? HIGH : LOW);
}

inline void zapalZasAwar(bool zapal) {
    digitalWrite(ZAWAPRZ, zapal ? HIGH : LOW);
}

inline void zapalLedDrzwi1(bool zapal) {
    io24.digitalWrite(LEDDRZ1, zapal ? LOW : HIGH);
}

inline void zapalPodswietKuchnia(bool zapal) {
    o20.digitalWrite(OSWKUCH, zapal ? HIGH : LOW);
}

inline void zapalPodswietJadalnia(bool zapal) {
    o20.digitalWrite(OSWJAD, zapal ? HIGH : LOW);
}

inline void zapalLedDrzwi2(bool zapal) {
    o20.digitalWrite(LEDDRZ2, zapal ? LOW : HIGH);
}

inline void zapalLedSufitLod(bool zapal) {
    io24.digitalWrite(LEDSUFL, zapal ? LOW : HIGH);
}

inline void zapalLedSufitJad(bool zapal) {
    io24.digitalWrite(LEDSUFJ, zapal ? LOW : HIGH);
}

inline uint16_t readWejscia() {
    return io24.readGPIOAB();
}


#endif
#endif // !IO_PINS_H
