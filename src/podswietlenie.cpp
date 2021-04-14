#include "podswietlenie.h"


#include "main.h"


#ifndef NEW_BOARD
#include <PCF8574.h>
extern PCF8574 expPozostale;
#else
#include "io.h"
#endif

void Podswietlenie::init() {

#ifndef NEW_BOARD
  expPozostale.pinMode(2, OUTPUT, ho(true)); //podswietlenie szafki
	expPozostale.pinMode(5, OUTPUT, ho(false)); //podwietlenie kuchnia
	expPozostale.pinMode(6, OUTPUT, ho(false)); //podwietlenie jadalnie
#endif // !
	
}

void Podswietlenie::zapalKuchnia(const bool on) {
  if (on == kuchnia)
	return;
  kuchnia = on;
  setPrzekaz();
}

void Podswietlenie::zapalJadalnia(const bool on) {
  if (on == jadalnia)
	return;
  jadalnia = on;
  setPrzekaz();
}

void Podswietlenie::zapalSzafa(const bool on) {
  if (on == szafa)
	return;
  szafa = on;
  setPrzekaz();
}

void Podswietlenie::setPrzekaz()
{
#ifndef NEW_BOARD  
  expPozostale.digitalWrite(2, ho(szafa));
  expPozostale.digitalWrite(6, ho(jadalnia));
  expPozostale.digitalWrite(5, ho(kuchnia));
#else
  zapalSzafki(szafa);
  zapalPodswietKuchnia(kuchnia); 
  zapalPodswietJadalnia(jadalnia);
#endif
}

void Podswietlenie::zapal(bool wieczor, bool sufit, bool jadalnia, bool led)
{
	zapalKuchnia(wieczor && !sufit && !led);
	zapalJadalnia(wieczor && !sufit && !led && !jadalnia);

}
