#ifndef _SYPIALIA_H_
#define _SYPIALIA_H_
#include <Arduino.h>
#include "decl_io.hpp"

void Sypialnia(bool wieczor, bool noc, bool awaria, bool klL, bool klP);

void SypialniaZasAwar(bool wieczor, bool noc, bool on);

bool sypialnia_isOn();

void sypialnia_off();
#ifdef RS485
void sypialnia_req(uint8_t index, bool val);
#endif
#endif