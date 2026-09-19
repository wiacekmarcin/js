#ifndef WLACZNIK
#define WLACZNIK

class Wlacznik {
    public:
    Wlacznik();

    void set(bool on, unsigned long timelaps);

    bool getHoldOn() { bool val = holdOn; holdOn = false; return val;  }
    bool getJedenKlik() { bool val = jedenKlik; jedenKlik = false; return val;  }
    bool getDwuKlik() { bool val = dwuKlik; dwuKlik = false; return val;  }
    bool getTrojKlik() { bool val = trojKlik; trojKlik = false; return val;  }
    bool get() const { return holdOn || jedenKlik || dwuKlik || trojKlik; }

    void print();

    private:
    bool prevVal;
    bool holdOn;
    bool jedenKlik;
    bool dwuKlik;
    bool trojKlik;
    short cntKlik;
//#ifdef DEBUG    
    unsigned long printmask;
//#endif    
    unsigned long timeLastEvent;
    
};










#endif /* WLACZNIK */
