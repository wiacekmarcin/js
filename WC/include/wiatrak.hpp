#ifndef _WIATRAK_HPP_
#define _WIATRAK_HPP_

#include "myMcp.hpp"
class Wiatrak {
    public:
    explicit Wiatrak(MyMcp2317WC & mcp);

    void setTik(unsigned int tik);
    void tiktok();
    
    private:
        MyMcp2317WC & io;
        unsigned int tik;

};

#endif /* WIATRAK */
