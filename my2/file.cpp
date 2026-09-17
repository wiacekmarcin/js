#include "decl_io.hpp"
#include <Arduino.h>
#if 0
struct _iotable _pins[64] {
  {0,  0,  INPUT
#ifdef _EXT_CODE_
        ," 57.08"
#endif
                }, //57.8 zasilanie awaryjne
  {0,  1,  INPUT
#ifdef _EXT_CODE_
        ," 57.06"
#endif
                }, //57.6 2 taryfa
  {0,  2,  INPUT
#ifdef _EXT_CODE_
        ," 57.04"
#endif
                }, //57.4 noc
  {0,  3,  INPUT
#ifdef _EXT_CODE_
        ," 57.02"
#endif
                }, //57.2 wieczor
  {0,  4,  OUTPUT
#ifdef _EXT_CODE_
        ,"213.01"
#endif
                }, //213.1 ledy kolo lazienki 1
  {0,  5,  OUTPUT
#ifdef _EXT_CODE_
        ,"213.02"
#endif
                }, //213.2 ledy kolo lazienki 2
  {0,  6,  OUTPUT
#ifdef _EXT_CODE_
        ,"209.06"
#endif
                }, //209.6 hol 3.1
  {0,  7,  OUTPUT
#ifdef _EXT_CODE_
        ,"209.07"
#endif
                }, //209.7 hol 3.2
  {0,  8,  OUTPUT
#ifdef _EXT_CODE_
        ,"209.08"
#endif
                }, //209.8 hol 3.3
  {0,  9,  OUTPUT
#ifdef _EXT_CODE_
        ,"209.05"
#endif
                }, //209.5 hol 4.4
  {0,  10,  OUTPUT
#ifdef _EXT_CODE_
        ,"209.04"
#endif
                }, //209.4 hol 4.3
  {0,  11,  OUTPUT
#ifdef _EXT_CODE_
        ,"209.03"
#endif
                }, //209.3 hol 4.2
  {0,  12,  OUTPUT
#ifdef _EXT_CODE_
        ,"209.02"
#endif
                }, //209.2 hol 4.1
  {0,  13,  OUTPUT
#ifdef _EXT_CODE_
        ,"209.01"
#endif
                }, //209.1 zasilacz 12V
  {0,  14,  OUTPUT
#ifdef _EXT_CODE_
        ,"213.04"
#endif
                }, //213.4 ledy kolo salonu 2
  {0,  15,  OUTPUT
#ifdef _EXT_CODE_
        ,"213.03"
#endif
                }, //213.3 ledy kolo salonu 1
  {1,  0,  INPUT
#ifdef _EXT_CODE_
        ," 55.02"
#endif
                }, //Czujka ruchu 1 IN
  {1,  1,  INPUT
#ifdef _EXT_CODE_
        ," 55.03"
#endif
                }, //Czujka ruchu 2 IN
  {1,  2,  INPUT
#ifdef _EXT_CODE_
        ,"24_OFF"
#endif
                }, //Zasilanie 24_OFF
  {1,  3,  OUTPUT
#ifdef _EXT_CODE_
        ," 59.05"
#endif
                }, //Wlaczone swiatlo w salonie
  {1,  4,  OUTPUT
#ifdef _EXT_CODE_
        ," 59.06"
#endif
                }, //Czujka ruchu OUT
  {1,  5,  OUTPUT
#ifdef _EXT_CODE_
        ,"Pods_C"
#endif
                }, //Podswietelenie mix
  {1,  6,  OUTPUT
#ifdef _EXT_CODE_
        ,"Pods_B"
#endif
                }, //Podswietlenie holu
  {1,  7,  OUTPUT
#ifdef _EXT_CODE_
        ,"Pods_A"
#endif
                }, //Podswietlenie salonu
  {1,  8,  OUTPUT
#ifdef _EXT_CODE_
        ,"211.01"
#endif
                }, //211.1 sypialnia 1
  {1,  9,  OUTPUT
#ifdef _EXT_CODE_
        ,"211.02"
#endif
                }, //211.2 sypialnia kinkiety
  {1,  10,  OUTPUT
#ifdef _EXT_CODE_
        ,"210.04"
#endif
                }, //210.4 Przedpokoj A0
  {1,  11,  OUTPUT
#ifdef _EXT_CODE_
        ,"210.03"
#endif
                }, //210.3 Sypialnia 1
  {1,  12,  OUTPUT
#ifdef _EXT_CODE_
        ,"210.02"
#endif
                }, //210.2 Salon 2
  {1,  13,  OUTPUT
#ifdef _EXT_CODE_
        ,"212.02"
#endif
                }, //212.2 Gwarantowane L
  {1,  14,  OUTPUT
#ifdef _EXT_CODE_
        ,"212.01"
#endif
                }, //212.1 gwarantowane N
  {1,  15,  OUTPUT
#ifdef _EXT_CODE_
        ,"210.01"
#endif
                }, //210.1 Salon 1
  {2,  0,  INPUT
#ifdef _EXT_CODE_
        ,"214.10"
#endif
                }, //214.10 29 15 Klawisz przy drzwiach wejsciowych
  {2,  1,  INPUT
#ifdef _EXT_CODE_
        ,"214.09"
#endif
                }, //214.9 28 13 Hol na scianie pokoi
  {2,  2,  INPUT
#ifdef _EXT_CODE_
        ,"214.08"
#endif
                }, //214.8 27 12 Hol na ścianie łazienki klawisz prawy
  {2,  3,  INPUT
#ifdef _EXT_CODE_
        ,"214.07"
#endif
                }, //214.7 26 10 Hol na ścianie sypialnie lewy klawisz prawy
  {2,  4,  INPUT
#ifdef _EXT_CODE_
        ,"214.06"
#endif
                }, //214.6 25 9 Hol na ścianie sypialnie prawy klawisz prawy
  {2,  5,  INPUT
#ifdef _EXT_CODE_
        ,"214.05"
#endif
                }, //214.5 24 11 Salon na ścieanie łazienki klawisz prawy
  {2,  6,  INPUT
#ifdef _EXT_CODE_
        ,"214.04"
#endif
                }, //214.4 23 7 Salon na ścianie sypialni lewy klawisz prawy
  {2,  7,  OUTPUT
#ifdef _EXT_CODE_
        ," 59.03"
#endif
                }, //Wlaczone swiatlo w holu
  {2,  8,  INPUT
#ifdef _EXT_CODE_
        ,"214.03"
#endif
                }, //214.3 22 6 Salon na ścianie sypialni prawy klawisz prawy
  {2,  9,  INPUT
#ifdef _EXT_CODE_
        ,"214.02"
#endif
                }, //214.2 21 Salon klawisz prawy
  {2,  10,  INPUT
#ifdef _EXT_CODE_
        ,"214.01"
#endif
                }, //214.1 20 Sypialnia klawisz prawy
  {2,  11,  INPUT
#ifdef _EXT_CODE_
        ,"216.08"
#endif
                }, //216.8 7 12 Hol na ścianie łazienki klawisz lewy
  {2,  12,  INPUT
#ifdef _EXT_CODE_
        ," 58.01"
#endif
                }, //58.1 - 4 Salon obok jadalni lewy klawisz lewy
  {2,  13,  INPUT
#ifdef _EXT_CODE_
        ," 58.02"
#endif
                }, //58.2 - 4 Salon obok jadalni lewy klawisz prawy
  {2,  14,  INPUT
#ifdef _EXT_CODE_
        ," 58.03"
#endif
                }, //58.3 - 3 Salon obok jadalni prawy klawisz lewy
  {2,  15,  OUTPUT
#ifdef _EXT_CODE_
        ," 59.04"
#endif
                }, //Wlaczone swiatlo w salonie
  {3,  0,  INPUT
#ifdef _EXT_CODE_
        ,"216.07"
#endif
                }, //216.7 6 10 Hol na ścianie sypialnie lewy klawisz lewy
  {3,  1,  INPUT
#ifdef _EXT_CODE_
        ,"216.06"
#endif
                }, //216.6 5 9 Hol na ścianie sypialnie prawy klawisz lewy
  {3,  2,  INPUT
#ifdef _EXT_CODE_
        ,"216.05"
#endif
                }, //216.5 4 11 Salon na ścieanie łazienki klawisz lewy
  {3,  3,  INPUT
#ifdef _EXT_CODE_
        ,"216.04"
#endif
                }, //216.4 3 7 Salon na ścianie sypialni lewy klawisz lewy
  {3,  4,  INPUT
#ifdef _EXT_CODE_
        ,"216.03"
#endif
                }, //216.3 2 6 Salon na ścianie sypialni prawy klawisz lewy
  {3,  5,  INPUT
#ifdef _EXT_CODE_
        ,"216.02"
#endif
                }, //216.2 1 Salon klawisz lewy
  {3,  6,  INPUT
#ifdef _EXT_CODE_
        ,"216.01"
#endif
                }, //216.1 0 Sypialnia klawisz lewy
  {3,  7,  OUTPUT
#ifdef _EXT_CODE_
        ,"------"
#endif
                }, //x
  {3,  8,  INPUT
#ifdef _EXT_CODE_
        ," 58.04"
#endif
                }, //58.4 - 3 Salon obok jadalni prawy klawisz prawy
  {3,  9,  INPUT
#ifdef _EXT_CODE_
        ," 58.05"
#endif
                }, //58.5 - 10 kuchnia prawy klawisz lewy
  {3,  10,  INPUT
#ifdef _EXT_CODE_
        ," 58.06"
#endif
                }, //58.6 - 10 kuchnia prawy klawisz prawy
  {3,  11,  INPUT
#ifdef _EXT_CODE_
        ," 58.07"
#endif
                }, //58.7 - 14 Hol na scianie WC klawisz lewy
  {3,  12,  INPUT
#ifdef _EXT_CODE_
        ," 58.08"
#endif
                }, //58.8 - 14 Hol na scianie WC klawisz prawy
  {3,  13,  INPUT
#ifdef _EXT_CODE_
        ,"217.03"
#endif
                }, //217.3 105 9 kuchnia lewy klawisz lewy
  {3,  14,  INPUT
#ifdef _EXT_CODE_
        ,"217.02"
#endif
                }, //217.2 107 9 kuchnia lewy klawisz prawy
  {3,  15,  OUTPUT
#ifdef _EXT_CODE_
        ,"------"
#endif
                }, //x
};
#else
struct _iotable _pins[64] {
  { INPUT
#ifdef _EXT_CODE_
    ," 57.08"
#endif
        }, //57.8 zasilanie awaryjne
  { INPUT
#ifdef _EXT_CODE_
    ," 57.06"
#endif
        }, //57.6 2 taryfa
  { INPUT
#ifdef _EXT_CODE_
    ," 57.04"
#endif
        }, //57.4 noc
  { INPUT
#ifdef _EXT_CODE_
    ," 57.02"
#endif
        }, //57.2 wieczor
  { OUTPUT
#ifdef _EXT_CODE_
    ,"213.01"
#endif
        }, //213.1 ledy kolo lazienki 1
  { OUTPUT
#ifdef _EXT_CODE_
    ,"213.02"
#endif
        }, //213.2 ledy kolo lazienki 2
  { OUTPUT
#ifdef _EXT_CODE_
    ,"209.06"
#endif
        }, //209.6 hol 3.1
  { OUTPUT
#ifdef _EXT_CODE_
    ,"209.07"
#endif
        }, //209.7 hol 3.2
  { OUTPUT
#ifdef _EXT_CODE_
    ,"209.08"
#endif
        }, //209.8 hol 3.3
  { OUTPUT
#ifdef _EXT_CODE_
    ,"209.05"
#endif
        }, //209.5 hol 4.4
  { OUTPUT
#ifdef _EXT_CODE_
    ,"209.04"
#endif
        }, //209.4 hol 4.3
  { OUTPUT
#ifdef _EXT_CODE_
    ,"209.03"
#endif
        }, //209.3 hol 4.2
  { OUTPUT
#ifdef _EXT_CODE_
    ,"209.02"
#endif
        }, //209.2 hol 4.1
  { OUTPUT
#ifdef _EXT_CODE_
    ,"209.01"
#endif
        }, //209.1 zasilacz 12V
  { OUTPUT
#ifdef _EXT_CODE_
    ,"213.04"
#endif
        }, //213.4 ledy kolo salonu 2
  { OUTPUT
#ifdef _EXT_CODE_
    ,"213.03"
#endif
        }, //213.3 ledy kolo salonu 1
  { INPUT
#ifdef _EXT_CODE_
    ," 55.02"
#endif
        }, //Czujka ruchu 1 IN
  { INPUT
#ifdef _EXT_CODE_
    ," 55.03"
#endif
        }, //Czujka ruchu 2 IN
  { INPUT
#ifdef _EXT_CODE_
    ,"24_OFF"
#endif
        }, //Zasilanie 24_OFF
  { OUTPUT
#ifdef _EXT_CODE_
    ," 59.05"
#endif
        }, //Wlaczone swiatlo w salonie
  { OUTPUT
#ifdef _EXT_CODE_
    ," 59.06"
#endif
        }, //Czujka ruchu OUT
  { OUTPUT
#ifdef _EXT_CODE_
    ,"Pods_C"
#endif
        }, //Podswietelenie mix
  { OUTPUT
#ifdef _EXT_CODE_
    ,"Pods_B"
#endif
        }, //Podswietlenie holu
  { OUTPUT
#ifdef _EXT_CODE_
    ,"Pods_A"
#endif
        }, //Podswietlenie salonu
  { OUTPUT
#ifdef _EXT_CODE_
    ,"211.01"
#endif
        }, //211.1 sypialnia 1
  { OUTPUT
#ifdef _EXT_CODE_
    ,"211.02"
#endif
        }, //211.2 sypialnia kinkiety
  { OUTPUT
#ifdef _EXT_CODE_
    ,"210.04"
#endif
        }, //210.4 Przedpokoj A0
  { OUTPUT
#ifdef _EXT_CODE_
    ,"210.03"
#endif
        }, //210.3 Sypialnia 1
  { OUTPUT
#ifdef _EXT_CODE_
    ,"210.02"
#endif
        }, //210.2 Salon 2
  { OUTPUT
#ifdef _EXT_CODE_
    ,"212.02"
#endif
        }, //212.2 Gwarantowane L
  { OUTPUT
#ifdef _EXT_CODE_
    ,"212.01"
#endif
        }, //212.1 gwarantowane N
  { OUTPUT
#ifdef _EXT_CODE_
    ,"210.01"
#endif
        }, //210.1 Salon 1
  { INPUT
#ifdef _EXT_CODE_
    ,"214.10"
#endif
        }, //214.10 29 15 Klawisz przy drzwiach wejsciowych
  { INPUT
#ifdef _EXT_CODE_
    ,"214.09"
#endif
        }, //214.9 28 13 Hol na scianie pokoi
  { INPUT
#ifdef _EXT_CODE_
    ,"214.08"
#endif
        }, //214.8 27 12 Hol na ścianie łazienki klawisz prawy
  { INPUT
#ifdef _EXT_CODE_
    ,"214.07"
#endif
        }, //214.7 26 10 Hol na ścianie sypialnie lewy klawisz prawy
  { INPUT
#ifdef _EXT_CODE_
    ,"214.06"
#endif
        }, //214.6 25 9 Hol na ścianie sypialnie prawy klawisz prawy
  { INPUT
#ifdef _EXT_CODE_
    ,"214.05"
#endif
        }, //214.5 24 11 Salon na ścieanie łazienki klawisz prawy
  { INPUT
#ifdef _EXT_CODE_
    ,"214.04"
#endif
        }, //214.4 23 7 Salon na ścianie sypialni lewy klawisz prawy
  { OUTPUT
#ifdef _EXT_CODE_
    ," 59.03"
#endif
        }, //Wlaczone swiatlo w holu
  { INPUT
#ifdef _EXT_CODE_
    ,"214.03"
#endif
        }, //214.3 22 6 Salon na ścianie sypialni prawy klawisz prawy
  { INPUT
#ifdef _EXT_CODE_
    ,"214.02"
#endif
        }, //214.2 21 Salon klawisz prawy
  { INPUT
#ifdef _EXT_CODE_
    ,"214.01"
#endif
        }, //214.1 20 Sypialnia klawisz prawy
  { INPUT
#ifdef _EXT_CODE_
    ,"216.08"
#endif
        }, //216.8 7 12 Hol na ścianie łazienki klawisz lewy
  { INPUT
#ifdef _EXT_CODE_
    ," 58.01"
#endif
        }, //58.1 - 4 Salon obok jadalni lewy klawisz lewy
  { INPUT
#ifdef _EXT_CODE_
    ," 58.02"
#endif
        }, //58.2 - 4 Salon obok jadalni lewy klawisz prawy
  { INPUT
#ifdef _EXT_CODE_
    ," 58.03"
#endif
        }, //58.3 - 3 Salon obok jadalni prawy klawisz lewy
  { OUTPUT
#ifdef _EXT_CODE_
    ," 59.04"
#endif
        }, //Wlaczone swiatlo w salonie
  { INPUT
#ifdef _EXT_CODE_
    ,"216.07"
#endif
        }, //216.7 6 10 Hol na ścianie sypialnie lewy klawisz lewy
  { INPUT
#ifdef _EXT_CODE_
    ,"216.06"
#endif
        }, //216.6 5 9 Hol na ścianie sypialnie prawy klawisz lewy
  { INPUT
#ifdef _EXT_CODE_
    ,"216.05"
#endif
        }, //216.5 4 11 Salon na ścieanie łazienki klawisz lewy
  { INPUT
#ifdef _EXT_CODE_
    ,"216.04"
#endif
        }, //216.4 3 7 Salon na ścianie sypialni lewy klawisz lewy
  { INPUT
#ifdef _EXT_CODE_
    ,"216.03"
#endif
        }, //216.3 2 6 Salon na ścianie sypialni prawy klawisz lewy
  { INPUT
#ifdef _EXT_CODE_
    ,"216.02"
#endif
        }, //216.2 1 Salon klawisz lewy
  { INPUT
#ifdef _EXT_CODE_
    ,"216.01"
#endif
        }, //216.1 0 Sypialnia klawisz lewy
  { OUTPUT
#ifdef _EXT_CODE_
    ,"------"
#endif
        }, //x
  { INPUT
#ifdef _EXT_CODE_
    ," 58.04"
#endif
        }, //58.4 - 3 Salon obok jadalni prawy klawisz prawy
  { INPUT
#ifdef _EXT_CODE_
    ," 58.05"
#endif
        }, //58.5 - 10 kuchnia prawy klawisz lewy
  { INPUT
#ifdef _EXT_CODE_
    ," 58.06"
#endif
        }, //58.6 - 10 kuchnia prawy klawisz prawy
  { INPUT
#ifdef _EXT_CODE_
    ," 58.07"
#endif
        }, //58.7 - 14 Hol na scianie WC klawisz lewy
  { INPUT
#ifdef _EXT_CODE_
    ," 58.08"
#endif
        }, //58.8 - 14 Hol na scianie WC klawisz prawy
  { INPUT
#ifdef _EXT_CODE_
    ,"217.03"
#endif
        }, //217.3 105 9 kuchnia lewy klawisz lewy
  { INPUT
#ifdef _EXT_CODE_
    ,"217.02"
#endif
        }, //217.2 107 9 kuchnia lewy klawisz prawy
  { OUTPUT
#ifdef _EXT_CODE_
    ,"------"
#endif
        }, //x
};
#endif
const char * info(uint8_t pos) {
  switch(pos) {
    case 0: return "57.8 zasilanie awaryjne";
    case 1: return "57.6 2 taryfa";
    case 2: return "57.4 noc";
    case 3: return "57.2 wieczor";
    case 4: return "213.1 ledy kolo lazienki 1";
    case 5: return "213.2 ledy kolo lazienki 2";
    case 6: return "209.6 hol 3.1";
    case 7: return "209.7 hol 3.2";
    case 8: return "209.8 hol 3.3";
    case 9: return "209.5 hol 4.4";
    case 10: return "209.4 hol 4.3";
    case 11: return "209.3 hol 4.2";
    case 12: return "209.2 hol 4.1";
    case 13: return "209.1 zasilacz 12V";
    case 14: return "213.4 ledy kolo salonu 2";
    case 15: return "213.3 ledy kolo salonu 1";
    case 16: return "Czujka ruchu 1 IN";
    case 17: return "Czujka ruchu 2 IN";
    case 18: return "Zasilanie 24_OFF";
    case 19: return "Wlaczone swiatlo w salonie";
    case 20: return "Czujka ruchu OUT";
    case 21: return "Podswietelenie mix";
    case 22: return "Podswietlenie holu";
    case 23: return "Podswietlenie salonu";
    case 24: return "211.1 sypialnia 1";
    case 25: return "211.2 sypialnia kinkiety";
    case 26: return "210.4 Przedpokoj A0";
    case 27: return "210.3 Sypialnia 1";
    case 28: return "210.2 Salon 2";
    case 29: return "212.2 Gwarantowane L";
    case 30: return "212.1 gwarantowane N";
    case 31: return "210.1 Salon 1";
    case 32: return "214.10 29 15 Klawisz przy drzwiach wejsciowych";
    case 33: return "214.9 28 13 Hol na scianie pokoi";
    case 34: return "214.8 27 12 Hol na ścianie łazienki klawisz prawy";
    case 35: return "214.7 26 10 Hol na ścianie sypialnie lewy klawisz prawy";
    case 36: return "214.6 25 9 Hol na ścianie sypialnie prawy klawisz prawy";
    case 37: return "214.5 24 11 Salon na ścieanie łazienki klawisz prawy";
    case 38: return "214.4 23 7 Salon na ścianie sypialni lewy klawisz prawy";
    case 39: return "Wlaczone swiatlo w holu";
    case 40: return "214.3 22 6 Salon na ścianie sypialni prawy klawisz prawy";
    case 41: return "214.2 21 Salon klawisz prawy";
    case 42: return "214.1 20 Sypialnia klawisz prawy";
    case 43: return "216.8 7 12 Hol na ścianie łazienki klawisz lewy";
    case 44: return "58.1 - 4 Salon obok jadalni lewy klawisz lewy";
    case 45: return "58.2 - 4 Salon obok jadalni lewy klawisz prawy";
    case 46: return "58.3 - 3 Salon obok jadalni prawy klawisz lewy";
    case 47: return "Wlaczone swiatlo w salonie";
    case 48: return "216.7 6 10 Hol na ścianie sypialnie lewy klawisz lewy";
    case 49: return "216.6 5 9 Hol na ścianie sypialnie prawy klawisz lewy";
    case 50: return "216.5 4 11 Salon na ścieanie łazienki klawisz lewy";
    case 51: return "216.4 3 7 Salon na ścianie sypialni lewy klawisz lewy";
    case 52: return "216.3 2 6 Salon na ścianie sypialni prawy klawisz lewy";
    case 53: return "216.2 1 Salon klawisz lewy";
    case 54: return "216.1 0 Sypialnia klawisz lewy";
    case 55: return "x";
    case 56: return "58.4 - 3 Salon obok jadalni prawy klawisz prawy";
    case 57: return "58.5 - 10 kuchnia prawy klawisz lewy";
    case 58: return "58.6 - 10 kuchnia prawy klawisz prawy";
    case 59: return "58.7 - 14 Hol na scianie WC klawisz lewy";
    case 60: return "58.8 - 14 Hol na scianie WC klawisz prawy";
    case 61: return "217.3 105 9 kuchnia lewy klawisz lewy";
    case 62: return "217.2 107 9 kuchnia lewy klawisz prawy";
    case 63: return "x";
    default: return "-";
  }
}
