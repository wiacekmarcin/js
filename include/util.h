#ifndef __UTIL_H__
#define __UTIL_H__

#include <string.h>

#include "Arduino.h"

void printtime(unsigned long mls, char * buf);

#define SEC(X) ((unsigned long)(1000L*(X)))
#define MIN(X) ((unsigned long)(6000L*(X)))

#endif // !__UTIL_H__