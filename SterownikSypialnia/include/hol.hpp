#ifndef _HOL_HPP_
#define _HOL_HPP_
#include <Arduino.h>

extern uint8_t bhol;
void Hol(bool wieczor, bool noc, bool awaria, bool klLA1, bool klPA1, bool klLA2, bool klPA2,
    bool klLB1, bool klPB1, bool klLB2, bool klPB2,
    bool klPok, bool klWej);

#endif