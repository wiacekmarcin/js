#include "drzwi.hpp"

Drzwi::Drzwi()
{
    prev = val = false;
}

void Drzwi::set(bool val)
{
    prev = this->val;
    this->val = val;
}