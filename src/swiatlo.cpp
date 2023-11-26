#include "swiatlo.hpp"
#include <Arduino.h>
Swiatlo::Swiatlo(MyMcp2317WC & mcp, Wiatrak & wiat, unsigned short delay) : 
    io(mcp), wiatrak(wiat)
{
    swiatloGorneOff = 0L;
    swiatloBoczneOff = 0L;
    swiatloLustroOff = 0L;
    div = delay;
    stateHoldOn = false;
}

void Swiatlo::setWlacznik(Wlacznik & wl)
{
    bool holdOn = wl.getHoldOn();
    bool klik1 = wl.getJedenKlik();
    bool klik2 = wl.getDwuKlik();
    bool klik3 = wl.getTrojKlik();

    //Serial.print("HoldOn = ");
    //Serial.println(holdOn, DEC);

    //Serial.print("klik1 = ");
    //Serial.println(klik1, DEC);

    //Serial.print("klik2 = ");
    //Serial.println(klik2, DEC);

    //Serial.print("klik3 = ");
    //Serial.println(klik3, DEC);

    //Serial.print("Noc = ");
    //Serial.println(io.czyNoc(), DEC);

    //Serial.print("Wieczor = ");
    //Serial.println(io.czyWieczor(), DEC);

    //Serial.print("Zas.awaryjne = ");
    //Serial.println(io.czyZasilanieAwaryjne(), DEC);

    //Serial.print("2Taryf = ");
    //Serial.println(io.czyZasilanie2Taryf(), DEC);

    //czy pory 
    //1 dzien -> wieczor
    //2 wieczor < 22.00 -> 22.00
    //3. 22.00 -> 6.00
    //4. 6.00 -> Swit

    if (holdOn) {
        if (io.czyZasilanieAwaryjne())
        {
            return;
        }

        if (stateHoldOn)
        {
            stateHoldOn = false;
            io.setSwiatloLustro(false);
            swiatloLustroOff = 0;
            io.setSwiatloGorne(false);
            swiatloGorneOff = 0;
            return;
        } else {
            stateHoldOn = true;
            io.setSwiatloLustro(true);
            swiatloLustroOff = getTikCnt(5, 0);
            io.setSwiatloGorne(true);
            swiatloGorneOff = getTikCnt(5, 0);
            return;
        }
        return;
    }


    if (klik3)
    {
        if (io.czyZasilanieAwaryjne())
        {
            return;
        }
        io.setWiatrak(true);
        wiatrak.setTik(getTikCnt(15, 0));
        return;
    }

    if (klik2)
    {
        if (io.czyZasilanieAwaryjne())
        {
            return;
        }
            
        if (io.getSwiatloBoczne()) 
        {
            io.setSwiatloLustro(true);
            io.setSwiatloBoczne(false);
            swiatloBoczneOff = 0;
            swiatloLustroOff = getTikCnt(3, 0);
            return;
        }
        
        if (io.getSwiatloLustro())
        {
            io.setSwiatloGorne(true);
            io.setSwiatloLustro(false);
            swiatloLustroOff = 0;
            swiatloGorneOff = getTikCnt(3, 0);
            return;
        }
        
        if (io.getSwiatloGorne())
        {
            swiatloGorneOff = getTikCnt(5, 0);
            return;
        }
        return;
    }
    
    if (klik1)
    {
        if (io.getSwiatlo())
        {
            if (io.czyNoc() && io.czyWieczor()) {
                swiatloGorneOff = getTikCnt(0, 10);
                io.setSwiatloGorne(true);
            } else {
                swiatloGorneOff = 0;
                io.setSwiatloGorne(false);
            }
            
            io.setSwiatloBoczne(false);
            io.setSwiatloLustro(false);
            swiatloBoczneOff = 0;
            swiatloLustroOff = 0;
            
            return;
        } 
        
        if (io.czyZasilanieAwaryjne()) 
        {
            io.setSwiatloBoczne(true);
            swiatloBoczneOff = getTikCnt(1, 0);
            return;
        } 
        
        if (!io.czyNoc() && !io.czyWieczor()) // 1
        {
            io.setSwiatloLustro(true);
            swiatloLustroOff = getTikCnt(3, 0);
            return;
        }
        
        if (!io.czyNoc() && io.czyWieczor()) // 2
        {
            io.setSwiatloGorne(true);
            swiatloGorneOff = getTikCnt(3, 0);
            return;
        }

        if (io.czyNoc() && io.czyWieczor()) // 3
        {
            io.setSwiatloBoczne(true);
            swiatloGorneOff = getTikCnt(2, 0);
            return;
        }
        
        if (!io.czyNoc() && io.czyWieczor()) // 4
        {
            io.setSwiatloLustro(true);
            swiatloGorneOff = getTikCnt(3, 0);
            return;
        }
        return;
    }
}

void Swiatlo::tiktok ()
{
    if (swiatloBoczneOff == 0 && swiatloGorneOff == 0 && swiatloLustroOff == 0) 
        return;

    if (swiatloBoczneOff == 1) {
        stateHoldOn = false;
        io.setSwiatloBoczne(false);
    }
    if (swiatloLustroOff > 0)
        swiatloBoczneOff -= 1;

    if (swiatloGorneOff == 1) {
        if (stateHoldOn) {
            swiatloBoczneOff = getTikCnt(10, 0);
            io.setSwiatloBoczne(true);
        }
        io.setSwiatloGorne(false);
    }
    if (swiatloBoczneOff > 0)
        swiatloGorneOff -= 1;

    if (swiatloLustroOff == 1) {
        if (stateHoldOn) {
            swiatloBoczneOff = getTikCnt(10, 0);
            io.setSwiatloBoczne(true);
        }
        io.setSwiatloLustro(false);
    }
    if (swiatloLustroOff > 0)
        swiatloLustroOff -= 1;
}

unsigned int Swiatlo::getTikCnt(unsigned short min, unsigned short sec)
{
    unsigned fut = min * 60 * 1000 + sec * 1000;
    return fut / div + 1;
}

void Swiatlo::setDrzwi(Drzwi & drzwi)
{
    if (drzwi.czyZostalyZamkniete()) {
        if (swiatloGorneOff > 0)
            swiatloGorneOff += getTikCnt(1, 0);
        if (swiatloBoczneOff > 0)
            swiatloBoczneOff += getTikCnt(1, 0);
        if (swiatloLustroOff > 0)
            swiatloLustroOff += getTikCnt(1, 0);
    } 
    else if (drzwi.czyZostalyOtwarte()) {
        unsigned int tik1m = getTikCnt(1, 0);
        if (swiatloGorneOff > tik1m)
            swiatloGorneOff -= tik1m;
        if (swiatloBoczneOff > tik1m)
            swiatloBoczneOff -= tik1m;
        if (swiatloLustroOff > tik1m)
            swiatloLustroOff -= tik1m;
    }
}

void Swiatlo::zwiekszCzasy(unsigned int tik)
{
    unsigned int m10 = getTikCnt(10, 0);
    if (swiatloGorneOff > 0) {
        swiatloGorneOff += tik;
        if (swiatloGorneOff > m10)
            swiatloGorneOff = m10;
    }

    if (swiatloBoczneOff > 0) {
        swiatloBoczneOff += tik;
        if (swiatloBoczneOff > m10)
            swiatloBoczneOff = m10;
    }

    if (swiatloLustroOff > 0) {
        swiatloLustroOff += tik;
        if (swiatloLustroOff > m10)
            swiatloLustroOff = m10;

    }
}

void Swiatlo::setCzujnikRuchu(bool ruch, bool otwarteDrzwi)
{

    if (!ruch)
        return;
    //Serial.print("Cz R = ");
    //Serial.println(ruch, DEC);

    unsigned int tik = getTikCnt(otwarteDrzwi ? 1 : 3, 0);
    zwiekszCzasy(tik);
    if (!io.getSwiatlo()) {
        io.setSwiatloGorne(true);
        swiatloGorneOff = getTikCnt(0, otwarteDrzwi ? 30 : 60);
    }
}

void Swiatlo::setCzujkaLustro(bool ruch, bool otwarteDrzwi)
{
    if (!ruch)
        return;
    //Serial.print("Cz Lustro ");
    //Serial.println(ruch, DEC);

    unsigned int tik = getTikCnt(otwarteDrzwi ? 1 : 3, 0);
    zwiekszCzasy(tik);

    if (!io.getSwiatloLustro()) {
        swiatloLustroOff = getTikCnt(0, otwarteDrzwi ? 30 : 60);
        io.setSwiatloLustro(true);
        
    }
}
