#ifndef _COMMON_SYP__H_
#define _COMMON_SYP__H_

#include <Arduino.h>

void zasilanieAwaryjne(bool wieczor, bool noc, bool zasAwar);
void podswietlenie(bool wieczor, bool zasAwar);
void inputChange(uint64_t ptrChgR, uint64_t ptrActR);
void rozkaz();
uint8_t parseNum(uint8_t * data, uint8_t * pos, uint8_t *r);

#endif