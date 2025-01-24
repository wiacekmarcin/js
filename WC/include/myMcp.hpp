#ifndef _MY_MCP_2317_HPP_
#define _MY_MCP_2317_HPP_
#include <Adafruit_BusIO_Register.h>
#include <Adafruit_MCP23X17.h>
#include <Adafruit_MCP23XXX.h>


class MyMcp2317WC : protected Adafruit_MCP23X17
{
    public:
    MyMcp2317WC();

    bool init_wc_io();
    bool begin_I2C(uint8_t i2c_addr = MCP23XXX_ADDR, TwoWire *wire = &Wire);

    void setSwiatloGorne(bool on);
    void setSwiatloLustro(bool on);
    void setSwiatloBoczne(bool on);
    void setZawor(bool on);
    void setWiatrak(bool on);

    bool isChange();

    void print_wejscie();
    uint8_t getValue() { return actValue; }

    bool czyWlacznik() { return (actValue >> KLAWISZ) & 0x1; }
    bool czyCzujnikLustra() { return (actValue >> CZ_R_LUSTRO) & 0x1; }
    bool czyCzujnikRuchu() { return (actValue >> CZ_R_WC) & 0x1; }
    bool czyZamknieteDrzwi() { return (actValue >> DRZWI) & 0x1; }
    bool czyWieczor() { return (actValue >> WIECZOR) & 0x1; }
    bool czyNoc() { return (actValue >> NOC) & 0x1; }
    bool czyZasilanieAwaryjne() { return (actValue >> Z_AWAR) & 0x1; }
    bool czyZasilanie2Taryf() { return (actValue >> TARYF2) & 0x1; }

    bool getSwiatloGorne() const { return swiatloGorne; }
    bool getSwiatloLustro() const { return swiatloLustro; }
    bool getSwiatloBoczne() const { return swiatloBoczne; }
    bool getSwiatlo() const { return swiatloGorne || swiatloLustro || swiatloBoczne; }


    
    static constexpr uint8_t CZ_R_WC = 1;//jasnozielony
    static constexpr uint8_t CZ_R_LUSTRO = 0;//jansobrazowy
    static constexpr uint8_t DRZWI = 2; //szary
    static constexpr uint8_t KLAWISZ = 3; //pomaranczowy
    static constexpr uint8_t Z_AWAR = 6; //fioletowy
    static constexpr uint8_t TARYF2 = 7; //brazowy
    static constexpr uint8_t WIECZOR = 4; //zolty
    static constexpr uint8_t NOC = 5; //bialy

    static constexpr uint8_t ZAWOR = 5; //fiolet
    static constexpr uint8_t LUSTRO = 4;  //niebieski
    static constexpr uint8_t SWIATLO = 3;  //bialy
    static constexpr uint8_t SZAFKA = 2;   //zolty
    static constexpr uint8_t WY_SWIATLO = 6; //brazowy
    static constexpr uint8_t WIATRAK = 7; //zielony

    



    private:
    bool swiatloGorne;
    bool swiatloLustro;
    bool swiatloBoczne;
    uint8_t prevValue;
    uint8_t actValue;
};

#endif