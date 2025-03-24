#ifndef _HOL_HPP_
#define _HOL_HPP_
#include <Arduino.h>
#include "decl_io.hpp"
#include "ledy.hpp"

void Hol(bool wieczor, bool noc, bool awaria, 
    bool kl3L1, bool kl3P1, bool kl3L2, bool kl3P2,
    bool kl4L1, bool kl4P1, bool kl4L2, bool kl4P2,
    bool klPok, bool klWej);


void HolZasAwar(bool wieczor, bool noc, bool on);

void hol_tiktok();
#ifdef RS485
void hol_req(uint8_t index, bool val);
#endif
bool hol_isOn();

void hol_off();

#endif