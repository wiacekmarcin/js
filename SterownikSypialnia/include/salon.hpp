#ifndef _SALON_HPP_
#define _SALON_HPP_

extern bool salon1;
extern bool salon2;
extern bool led1;
extern bool led2;
extern bool led3;
extern bool led4;

void SalonJadalnia(bool wieczor, bool noc, bool awaria, bool klLL, bool klLP, bool klPL, bool klPP);

void SalonKuchnia(bool wieczor, bool noc, bool awaria, bool klLL, bool klLP, bool klPL, bool klPP);

void SalonSypialnia(bool wieczor, bool noc, bool awaria, bool klLL, bool klLP, bool klPL, bool klPP);

void Salon(bool wieczor, bool noc, bool awaria, bool klL, bool klP);

void SalonLedLaz(bool wieczor, bool noc, bool awaria, bool klL, bool klP);














#endif