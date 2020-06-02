#ifndef MW_SWIATLO_LED
#define MW_SWIATLO_LED

#include "wejscia.h"

class SwiatloLED
{


public:
    SwiatloLED(): m_sufit1(false), m_sufit2(false), m_drzwi1(false), m_drzwi2(false)
    { }

	constexpr uint8_t ALL 4;
	constexpr uint8_t SUFIT1 0;
	constexpr uint8_t SUFIT2 1;
	constexpr uint8_t DRZWI1 2;
	constexpr uint8_t DRZWI2 3;
	void init();

   	void zapalSufit1(bool on);
	void zapalSufit2(bool on);
	void zapalDrzwi1(bool on);
    void zapalDrzwi2(bool on);

    bool czyZapalone() const;

	bool czyZapalonySufit() const;

	void zapal(const Wejscia & w, bool s);

	inline void zapalSufit(bool on) { zapalSufit1(on); zapalSufit2(on); }

protected:

    void ustaw_przekaz();
private:
	bool m_sufit1, m_sufit2, m_drzwi1, m_drzwi2;
};



#endif
