#include "podswietlenie.h"

#include <PCF8574.h>
#include "main.h"
extern PCF8574 expPozostale;


void Podswietlenie::init() {
	expPozostale.pinMode(2, OUTPUT, ho(false)); //podswietlenie szafki
	expPozostale.pinMode(5, OUTPUT, ho(false)); //podwietlenie kuchnia
	expPozostale.pinMode(6, OUTPUT, ho(false)); //podwietlenie jadalnie
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

void Podswietlenie::setPrzekaz() {
  expPozostale.digitalWrite(2, ho(szafa));
  expPozostale.digitalWrite(6, lo(jadalnia));
  expPozostale.digitalWrite(5, lo(kuchnia));
}

void Podswietlenie::zapal(const Wejscia & w, bool sufit, bool jadalnia, bool led)
{
	if (!w.czyNoc() && !czySzafaZapalona()) {
		zapalSzafa(true);
	}

	if (w.czyNoc() && w.czyRuchKuchnia(10*60))
		zapalSzafa(true);
	else
		zapalSzafa(false);

	if (!w.czyWieczor()) {
		zapalJadalnia(false);
		zapalKuchnia(false);
	} else {
		zapalKuchnia(!sufit && !led);
		zapalJadalnia(!sufit && !led && !jadalnia);
	}
}
