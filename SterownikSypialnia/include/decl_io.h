#ifndef _DECLARE_IO_H_
#define _DECLARE_IO_H_
#include <Arduino.h>
#include "def_io.h"


struct _iotable _pins[64] {
    {0,  0,  INPUT,  " 57.08"},  //57.8 zasilanie awaryjne
    {0,  1,  INPUT,  " 57.06"},  //57.6 2 taryfa
    {0,  2,  INPUT,  " 57.04"},  //57.4 noc 
    {0,  3,  INPUT,  " 57.02"},  //57.2 wieczor
    {0,  4,  OUTPUT, "213.01"},  //213.1 ledy kolo lazienki 1
    {0,  5,  OUTPUT, "213.02"},  //213.2 ledy kolo lazienki 2
    {0,  6,  OUTPUT, "209.06"},  //209.6 hol 3.1
    {0,  7,  OUTPUT, "209.07"},  //209.7 hol 3.2
    {0,  8,  OUTPUT, "209.08"},  //209.8 hol 3.3
    {0,  9,  OUTPUT, "209.05"},  //209.5 hol 4.4
    {0, 10,  OUTPUT, "209.04"},  //209.4 hol 4.3
    {0, 11,  OUTPUT, "209.03"},  //209.3 hol 4.2
    {0, 12,  OUTPUT, "209.02"},  //209.2 hol 4.1
    {0, 13,  OUTPUT, "209.01"},  //209.1 zasilacz 12V
    {0, 14,  OUTPUT, "213.04"},  //213.4 ledy kolo salonu 2
    {0, 15,  OUTPUT, "213.03"},  //213.3 ledy kolo salonu 1

    {1,  0,  INPUT,  " 55.02"},  //Czujka ruchu 1 IN
    {1,  1,  INPUT,  " 55.03"},  //Czujka ruchu 2 IN
    {1,  2,  INPUT,  "24_OFF"},  //Zasilanie 24_OFF
    {1,  3,  OUTPUT, " 59.05"},  //Wlaczone swiatlo w salonie
    {1,  4,  OUTPUT, " 59.06"},  //Czujka ruchu OUT  
    {1,  5,  OUTPUT, "Pods_C"},  //Podswietelenie mix 
    {1,  6,  OUTPUT, "Pods_B"},  //Podswietlenie holu
    {1,  7,  OUTPUT, "Pods_A"},  //Podswietlenie salonu
    {1,  8,  OUTPUT, "211.01"},  //211.1 sypialnia 1
    {1,  9,  OUTPUT, "211.02"},  //211.2 sypialnia kinkiety
    {1, 10,  OUTPUT, "210.04"},  //210.4 Przedpokoj A0  
    {1, 11,  OUTPUT, "210.03"},  //210.3 Sypialnia 1
    {1, 12,  OUTPUT, "210.02"},  //210.2 Salon 2
    {1, 13,  OUTPUT, "212.02"},  //212.2 Gwarantowane L
    {1, 14,  OUTPUT, "212.01"},  //212.1 gwarantowane N
    {1, 15,  OUTPUT, "210.01"},  //210.1 Salon 1

    {2,  0,  INPUT,  "214.10"},  //214.10 29 15 Klawisz przy drzwiach wejsciowych
    {2,  1,  INPUT,  "214.09"},  //214.9 28 13 Hol na scianie pokoi 
    {2,  2,  INPUT,  "214.08"},  //214.8 27 12 Hol na ścianie łazienki klawisz prawy
    {2,  3,  INPUT,  "214.07"},  //214.7 26 10 Hol na ścianie sypialnie lewy klawisz prawy
    {2,  4,  INPUT,  "214.06"},  //214.6 25 9 Hol na ścianie sypialnie prawy klawisz prawy
    {2,  5,  INPUT,  "214.05"},  //214.5 24 11 Salon na ścieanie łazienki klawisz prawy
    {2,  6,  INPUT,  "214.04"},  //214.4 23 7 Salon na ścianie sypialni lewy klawisz prawy
    {2,  7,  OUTPUT, " 59.03"},  //Wlaczone swiatlo w holu
    {2,  8,  INPUT,  "214.03"},  //214.3 22 6 Salon na ścianie sypialni prawy klawisz prawy
    {2,  9,  INPUT,  "214.02"},  //214.2 21 Salon klawisz prawy
    {2, 10,  INPUT,  "214.01"},  //214.1 20 Sypialnia klawisz prawy
    {2, 11,  INPUT,  "216.08"},  //216.8 7 12 Hol na ścianie łazienki klawisz lewy
    {2, 12,  INPUT,  " 58.01"},  //58.1 - 4 Salon obok jadalni lewy klawisz lewy
    {2, 13,  INPUT,  " 58.02"},  //58.2 - 4 Salon obok jadalni lewy klawisz prawy
    {2, 14,  INPUT,  " 58.03"},  //58.3 - 3 Salon obok jadalni prawy klawisz lewy
    {2, 15,  OUTPUT, " 59.04"},  //Wlaczone swiatlo w salonie 

    {3,  0,  INPUT,  "216.07"},  //216.7 6 10 Hol na ścianie sypialnie lewy klawisz lewy
    {3,  1,  INPUT,  "216.06"},  //216.6 5 9 Hol na ścianie sypialnie prawy klawisz lewy
    {3,  2,  INPUT,  "216.05"},  //216.5 4 11 Salon na ścieanie łazienki klawisz lewy
    {3,  3,  INPUT,  "216.04"},  //216.4 3 7 Salon na ścianie sypialni lewy klawisz lewy
    {3,  4,  INPUT,  "216.03"},  //216.3 2 6 Salon na ścianie sypialni prawy klawisz lewy
    {3,  5,  INPUT,  "216.02"},  //216.2 1 Salon klawisz lewy
    {3,  6,  INPUT,  "216.01"},  //216.1 0 Sypialnia klawisz lewy
    {3,  7,  OUTPUT, "------"},  //x
    {3,  8,  INPUT,  " 58.04"},  //58.4 - 3 Salon obok jadalni prawy klawisz prawy
    {3,  9,  INPUT,  " 58.05"},  //58.5 - 10 kuchnia prawy klawisz lewy
    {3, 10,  INPUT,  " 58.06"},  //58.6 - 10 kuchnia prawy klawisz prawy
    {3, 11,  INPUT,  " 58.07"},  //58.7 - 14 Hol na scianie WC klawisz lewy
    {3, 12,  INPUT,  " 58.08"},  //58.8 - 14 Hol na scianie WC klawisz prawy
    {3, 13,  INPUT,  "217.03"},  //217.3 105 9 kuchnia lewy klawisz lewy
    {3, 14,  INPUT,  "217.02"},  //217.2 107 9 kuchnia lewy klawisz prawy
    {3, 15,  OUTPUT, "------"},  //Uszkodzone ?
};

#endif