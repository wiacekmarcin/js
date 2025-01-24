#ifndef _DBG_H
#define _DBG_H
#include <Arduino.h>

//#define DEBUG

#define SEC(X) ((unsigned long)( 1000L*(X)))
#define MIN(X) ((unsigned long)(60000L*(X)))

#define L_SEC(X) ((unsigned long)( 1L*(X)))
#define L_MIN(X) ((unsigned long)(60L*(X)))

#define MASK(X, M) (((0x01 << (M)) & (X)) >> M)
#define CHAN(X, Y, M) (((X)^(Y)) & (0x01 << (M)))
void debug_print_wejscie(uint8_t prev, uint8_t act);


#endif // !_DBG_H