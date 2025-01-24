#ifndef MW_MAIN_H
#define MW_MAIN_H
#include <Arduino.h>

inline uint8_t lo(bool val) { return val ? LOW : HIGH; }
inline uint8_t ho(bool val) { return val ? HIGH : LOW; }

inline bool li(uint8_t val) { return val == LOW; }
inline bool hi(uint8_t val) { return val == HIGH; }

#define NEW_BOARD 1



#define DBG




#endif
