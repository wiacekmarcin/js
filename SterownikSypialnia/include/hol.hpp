#ifndef _HOL_HPP_
#define _HOL_HPP_
#include <Arduino.h>
#include "ledy.hpp"

void Hol(bool wieczor, bool noc, bool awaria, 
    bool kl3L1, bool kl3P1, bool kl3L2, bool kl3P2,
    bool kl4L1, bool kl4P1, bool kl4L2, bool kl4P2,
    bool klPok, bool klWej);

void hol_tiktok();

void hol_req(uint8_t index, bool val);

bool hol_isOn();

#endif