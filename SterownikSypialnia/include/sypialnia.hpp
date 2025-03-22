#ifndef _SYPIALIA_H_
#define _SYPIALIA_H_
#include <Arduino.h>

void Sypialnia(bool wieczor, bool noc, bool awaria, bool klL, bool klP);

void SypialniaZasAwar(bool wieczor, bool on);

void sypialnia_req(uint8_t index, bool val);

#endif