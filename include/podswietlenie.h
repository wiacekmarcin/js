#ifndef MW_PODSW_H
#define MW_PODSW_H

#include "wejscia.h"
#include "swiatloled.h"
#include "swiatlosufit.h"
#include "swiatlojadalnia.h"

class Podswietlenie {


public:
  Podswietlenie() : kuchnia(false), jadalnia(false), szafa(true)
  { }

  void init();


  	void zapalKuchnia(const bool on);

  	void zapalJadalnia(const bool on);

  	void zapalSzafa(const bool on);

	void zapal(const Wejscia & w, bool s, bool j, bool l );

	bool czySzafaZapalona() { return szafa; }
protected:
    void setPrzekaz();

private:
  	bool kuchnia, jadalnia, szafa;
};
#endif
