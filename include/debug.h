#ifndef _DBG_H
#define _DBG_H
#include <Arduino.h>

#define DEBUG

#ifdef DEBUG

class Wlacznik;
class CzujkaZblizeniowa;
class CzujkaRuchu;
class Drzwi;
class PoraDnia;

void print_wlacznik(const Wlacznik * w);
void print_czujkazblizeniowa(const CzujkaZblizeniowa * cz);
void print_czujkaruchu(const CzujkaRuchu *cr);
void print_drzwi(const Drzwi *d);
void print_poradnia(const PoraDnia * p);

#endif // DEBUG

void print_wejscie(uint8_t prev, uint8_t act);


#endif // !_DBG_H