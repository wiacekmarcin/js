#include "wiatrak.hpp"

Wiatrak::Wiatrak(MyMcp2317WC & mcp) : 
    io(mcp)
{
    tik = 0;
}

void Wiatrak::setTik(unsigned int tik)
{
    this->tik = tik;
}
    
void Wiatrak::tiktok()
{
    if (tik == 0)
        return;

    if (tik == 1)
    {
        io.setWiatrak(false);
    }     

    tik -= 1;
}