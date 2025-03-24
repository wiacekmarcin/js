#ifndef _SALON_HPP_
#define _SALON_HPP_
#include <Arduino.h>
#include "decl_io.hpp"

void SalonJadalnia(bool wieczor, bool noc, bool awaria, bool klLL, bool klLP, bool klPL, bool klPP);

void SalonKuchnia(bool wieczor, bool noc, bool awaria, bool klLL, bool klLP, bool klPL, bool klPP);

void SalonSypialnia(bool wieczor, bool noc, bool awaria, bool klLL, bool klLP, bool klPL, bool klPP);

void Salon(bool wieczor, bool noc, bool awaria, bool klL, bool klP);

void SalonLedLaz(bool wieczor, bool noc, bool awaria, bool klL, bool klP);

void SalonZasAwar(bool wieczor, bool noc, bool zasAwar);

bool salon_isOn();

void salon_off();
#ifdef RS485
void salon_req(uint8_t index, bool val);
#endif

#endif