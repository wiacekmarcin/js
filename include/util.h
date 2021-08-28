#ifndef __UTIL_H__
#define __UTIL_H__

#include <string.h>

#include "Arduino.h"

void printtime(unsigned long mls, char * buf);

#define SEC(X) ((unsigned long)( 1000L*(X)))
#define MIN(X) ((unsigned long)(60000L*(X)))

#define L_SEC(X) ((unsigned long)( 1L*(X)))
#define L_MIN(X) ((unsigned long)(60L*(X)))

#define MASK(X, M) (((0x01 << (M)) & (X)) >> M)
#define CHAN(X, Y, M) (((X)^(Y)) & (0x01 << (M)))

//#define MYINTERUPTS

#endif // !__UTIL_H__