#ifndef TIMERCLASS
#define TIMERCLASS
#ifndef _MY_TIMERCLASS_WENT_HPP_
#define _MY_TIMERCLASS_WENT_HPP_

class MyTimerClass {
public:
    explicit MyTimerClass(unsigned int time_s, void (*funptr_)(void)) : maxtick1s(time_s), tick1s(0), enable(false), funptr(funptr_) { }
    
    inline void tick() {
        if (enable)
            return;
        if (tick1s == 0) {
            tick1s = maxtick1s;
            (*funptr)();
            return;
        }
        tick1s--;
    }
private:
    unsigned int tick1s;
    unsigned int maxtick1s;
    bool enable;
    void (*funptr)(void);
};

#endif //_MY_TIMERCLASS_WENT_HPP_



#endif /* TIMERCLASS */
