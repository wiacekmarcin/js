#include "util.h"

void printtime(unsigned long mls, char * buf) {
    unsigned long m = mls / 100;
       
    buf[11] = '\0';

    buf[10] = m % 10 + '0';
    buf[9] = '.';
    
    m /= 10;
    buf[8] = m % 10 + '0';
        

    m /= 10;
    if (m > 0) {
        buf[7] = m % 10 + '0';
    } else
    {
        buf[7] = ' ';
    }

    m /= 10;
    if (m > 0) {
        buf[6] = m % 10 + '0';
    } else
    {
        buf[6] = ' ';
    }

    m /= 10;
    if (m > 0) {
        buf[5] = m % 10 + '0';
    } else
    {
        buf[5] = ' ';
    }

    m /= 10;
    if (m > 0) {
        buf[4] = m % 10 + '0';
    } else
    {
        buf[4] = ' ';
    }

    m /= 10;
    if (m > 0) {
        buf[3] = m % 10 + '0';
    } else
    {
        buf[3] = ' ';
    }

    m /= 10;
    if (m > 0) {
        buf[2] = m % 10 + '0';
    } else
    {
        buf[2] = ' ';
    }

    m /= 10;
    if (m > 0) {
        buf[1] = m % 10 + '0';
    } else
    {
        buf[1] = ' ';
    }

    m /= 10;
    if (m > 0) {
        buf[0] = m % 10 + '0';
    } else
    {
        buf[0] = ' ';
    }
}

