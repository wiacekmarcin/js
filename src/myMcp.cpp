#include "myMcp.hpp"

#include "debug.h"
#define SET_OUTPUT(X, LH) pinMode(X, OUTPUT); digitalWrite(X, LH);

MyMcp2317WC::MyMcp2317WC() :
    swiatloGorne(false),
    swiatloLustro(false),
    swiatloBoczne(false),
    prevValue(0),
    actValue(0)

{

}


bool MyMcp2317WC::begin_I2C(uint8_t addr, TwoWire* two)
{
    return Adafruit_MCP23XXX::begin_I2C(addr, two);
}

bool MyMcp2317WC::init_wc_io ()
{
    pinMode(8 + CZ_R_WC, INPUT); //= 1;//jasnozielony
    pinMode(8 + CZ_R_LUSTRO, INPUT); //= 0;//jansobrazowy
    pinMode(8 + DRZWI, INPUT); //= 2; //szary
    pinMode(8 + KLAWISZ, INPUT); //= 3; //pomaranczowy
    pinMode(8 + Z_AWAR, INPUT); //= 6; //fioletowy
    pinMode(8 + TARYF2, INPUT); //= 7; //brazowy
    pinMode(8 + WIECZOR, INPUT); //= 4; //zolty
    pinMode(8 + NOC, INPUT); //= 5; //bialy)

    SET_OUTPUT(ZAWOR, HIGH); //= 5; //fiolet
    SET_OUTPUT(LUSTRO, HIGH); //= 4;  //niebieski
    SET_OUTPUT(SWIATLO, HIGH); //= 3;  //bialy
    SET_OUTPUT(SZAFKA, HIGH); //= 2;   //zolty
    SET_OUTPUT(WY_SWIATLO, LOW); //= 6; //brazowy
    SET_OUTPUT(WIATRAK, LOW); //= 7; //zielony
    
    Adafruit_BusIO_Register IPOLB(Adafruit_MCP23XXX::i2c_dev, Adafruit_MCP23XXX::spi_dev, MCP23XXX_SPIREG,
                            Adafruit_MCP23XXX::getRegister(MCP23XXX_IPOL, 1)); //1 to port B
    
    Adafruit_BusIO_RegisterBits poiLustro(&IPOLB, 1, CZ_R_LUSTRO);
    Adafruit_BusIO_RegisterBits poiCzujnik(&IPOLB, 1, CZ_R_WC);
    Adafruit_BusIO_RegisterBits poiDrzwi(&IPOLB, 1, DRZWI);
    Adafruit_BusIO_RegisterBits poiKlawisz(&IPOLB, 1, KLAWISZ);
    
    poiCzujnik.write(0);
    poiLustro.write(0);
    poiDrzwi.write(1); 
    poiKlawisz.write(1);

    return true;
}

void MyMcp2317WC::setSwiatloGorne(bool on)
{
    swiatloGorne = on;
    digitalWrite(SWIATLO, on ? LOW : HIGH);
    digitalWrite(WY_SWIATLO, (swiatloGorne || swiatloBoczne || swiatloLustro) ? HIGH : LOW);
}

void MyMcp2317WC::setSwiatloLustro(bool on)
{
    swiatloLustro = on;
    digitalWrite(LUSTRO, on ? LOW : HIGH);
    digitalWrite(WY_SWIATLO, (swiatloGorne || swiatloBoczne || swiatloLustro) ? HIGH : LOW);
}

void MyMcp2317WC::setSwiatloBoczne(bool on)
{
    swiatloBoczne = on;
    digitalWrite(SZAFKA, on ? LOW : HIGH);
    digitalWrite(WY_SWIATLO, (swiatloGorne || swiatloBoczne || swiatloLustro) ? HIGH : LOW);
}

void MyMcp2317WC::setZawor(bool on)
{
    digitalWrite(ZAWOR, on ? LOW : HIGH);
}

void MyMcp2317WC::setWiatrak(bool on)
{
    digitalWrite(WIATRAK, on ? HIGH : LOW);
}

bool MyMcp2317WC::isChange()
{
    prevValue = actValue;
    actValue = readGPIOB();
    return actValue != prevValue;
}

void MyMcp2317WC::print_wejscie()
{
    debug_print_wejscie(prevValue, actValue);
}