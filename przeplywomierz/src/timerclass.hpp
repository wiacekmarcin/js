#ifndef TIMERCLASS
#define TIMERCLASS
#ifndef _MY_TIMERCLASS_WENT_HPP_
#define _MY_TIMERCLASS_WENT_HPP_

class MyTimerClass {
public:
    explicit MyTimerClass(unsigned int time_s, void (*funptr_)(bool)) : tick1s(0), maxtick1s(time_s), enable(false), funptr(funptr_) { }
    
    inline void tick() {
        if (enable)
            return;
        if (tick1s == 0) {
            enable = false;
            (*funptr)(false);
            return;
        }
        tick1s--;
    }

    inline void start() {
        enable = true;
        tick1s = maxtick1s;
        (*funptr)(true);

    }
    inline bool isEnable() const {
        return enable;
    }
    
    inline void stop() {
        enable = false;
        tick1s = 0;
        (*funptr)(false);
    }
private:
    unsigned int tick1s;
    unsigned int maxtick1s;
    bool enable;
    void (*funptr)(bool);
};

#endif //_MY_TIMERCLASS_WENT_HPP_



#endif /* TIMERCLASS */
