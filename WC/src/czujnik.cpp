#include "czujnik.hpp"
#include <Arduino.h>
Czujnik::Czujnik()
{
    val = false;
    prev = false;
    timeStamp = 0L;
}

bool Czujnik::set(bool val, unsigned long tms)
{
    //Serial.print(tms);
    //Serial.print(" ");
    //Serial.print("set Cz=");
    //Serial.println(val, DEC);
    //if (tms - timeStamp < 150)
    //    return false;

    prev = this->val;
    this->val = val;

    return true;
}

bool Czujnik::wykrytoRuch()
{
    return val && !prev;
}