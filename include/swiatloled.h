#ifndef MW_SWIATLO_LED
#define MW_SWIATLO_LED

#include "wejscia.h"

class SwiatloLED
{


public:
    SwiatloLED(): m_sufit1(false), m_sufit2(false), m_drzwi1(false), m_drzwi2(false)
    { }

	static constexpr unsigned long czasSwiecenieLED = 1ul*1000*60*5;

	
	void init();

   	void zapalSufit1(bool on);
	void zapalSufit2(bool on);
	void zapalDrzwi1(bool on);
    void zapalDrzwi2(bool on);

    bool czyZapalone() const;

	bool czyZapalonySufit() const;
	bool czyZapalonySufit1() const;
	bool czyZapalonySufit2() const;

	void zapal(const Wejscia & w, bool s);

	inline void zapalSufit(bool on1, bool on2 = false) { zapalSufit1(on1); zapalSufit2(on2); }

protected:

    void ustaw_przekaz();
#ifndef NEW_BOARD


	static constexpr uint8_t ALL = 4;
	static constexpr uint8_t SUFIT1 = 0;
	static constexpr uint8_t SUFIT2 = 1;
	static constexpr uint8_t DRZWI1 = 2;
	static constexpr uint8_t DRZWI2 = 3;

#endif // !NEW_BOARD

private:
	bool m_sufit1, m_sufit2, m_drzwi1, m_drzwi2;
};



#endif
