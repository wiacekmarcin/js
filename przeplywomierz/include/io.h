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

#define    LAMPA2    0        //A0 OUT
#define    LAMPA7    1        //A1 OUT
#define    LAMPA1    2        //A2 OUT
#define    LAMPA6    3        //A3 OUT
#define    LAMPA8    4        //A4 OUT
#define    LAMPA4    5        //A5 OUT
#define    LAMPA9    6        //A6 OUT
#define    LAMPA3    7        //A7 OUT
#define    LAMPA5    8        //B0 OUT
#define    OSSZAFEK  9        //B1 OUT
#define    JADAL1   10        //B2 OUT
#define    JADAL2   11        //B3 OUT
#define    JADAL3   12        //B4 OUT
#define    OSWKUCH  13        //B5 OUT
#define    OSWJAD   14        //B6 OUT
#define    LEDDRZ2  15        //B7 OUT    



#define    KONTAKT    0   //A0 IN
#define    NOC        3   //A1 IN 
#define    ZAS_AWAR   2   //A2 IN
#define    TARYF2     1   //A3 IN 
#define    WIECZOR    4   //A4 IN
#define    LEDSUFL    5   //A6 OUT
#define    LEDSUFJ    6   //A7 OUT
#define    LEDDRZ1    7   //A5 OUT
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
    static const uint8_t mapPins[3] = {JADAL1, JADAL2, JADAL3};    
    o20.digitalWrite(mapPins[nr-1], zapal ? HIGH : LOW);
}

inline void zapalKuchnia(short nr, bool zapal) {
    //Serial.print("pin=");
    //Serial.print(nr, DEC);
    //Serial.print(" io=");
   
    if (nr < 0 || nr >= 9)
        return;
    //na listwie               2 7 1 6 8 4 9 3 | 5 10 11 12 | 13
    //wejscia na przekaznikach 8 7 6 5 4 3 2 1 | 4  3  2  1 |  1
    //wejscia na expanderach   7 6 5 4 3 2 1 0 | 8  9 10 11 | 12
    static const uint8_t mapPins[9] = 
    { LAMPA1, LAMPA2, LAMPA3, LAMPA4, LAMPA5, LAMPA6, LAMPA7, LAMPA8, LAMPA9 };
    o20.digitalWrite(mapPins[nr], zapal ? HIGH : LOW);
    //Serial.println(mapPins[nr], DEC);
}           

inline void zapalSzafki(bool zapal) {
    o20.digitalWrite(OSSZAFEK, zapal ? HIGH : LOW);
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


//void test(short pos);

#endif
#endif // !IO_PINS_H
#ifndef MY_IO_MCP23017_H_
#define MY_IO_MCP23017_H_

enum IODigitOutput {
  LAZ_UMY_W = 0,
  MCP_FIRST = LAZ_UMY_W,
  LAZ_WAN_W,
  LAZ_PRYSZ_W,
  LAZ_SEDES_W,  
  WC_SEDES_W,
  WC_PRALKA_W,
  KUCH_ZMYW_W,
  KUCH_WENT,
  WC_WENT,
  LAZ_WENT,
  WC_UMYW_W,
  KUCH_UMYW_W,
  F_GAZ_1,
  F_GAZ_2,
  MCP_LAST,
};

#endif //MY_IO_MCP23017_H_



