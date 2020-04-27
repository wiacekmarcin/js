#ifndef _MW_SWIATLO_LED
#define _MW_SWIATLO_LED

#include "wejscia.h"
#include "swiatlosufit.h"
#include "swiatlojadalnia.h"
class SwiatloLED
{


public:
    SwiatloLED(): m_sufit1(false), m_sufit2(false), m_drzwi1(false), m_drzwi2(false)
    { }

	void init();

   	void zapalSufit1(bool on);
	void zapalSufit2(bool on);
	void zapalDrzwi1(bool on);
    void zapalDrzwi2(bool on);

    bool czyZapalone() const;

	void zapal(const Wejscia & w, const SwiatloSufit &s, const SwiatloJadalnia & j);

protected:

    void ustaw_przekaz();
private:
	bool m_sufit1, m_sufit2, m_drzwi1, m_drzwi2;
};



#endif
