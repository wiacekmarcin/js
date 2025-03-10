#ifndef _DEF_IO_H_
#define _DEF_IO_H_
#include <Arduino.h>

struct _iotable {
    unsigned short mod_id;
    unsigned short pin_id;
    unsigned short io_type;
    char name[7];
};

#define INTERRUPTPIN 7
#define RESETPIN 8

#define Z213_6_LEDY_CH4 4
#define Z213_5_LEDY_CH3 5
#define Z213_4_LEDY_CH2 15
#define Z213_3_LEDY_CH1 14

#define Z209_8_CH8 6 
#define Z209_7_CH7 7
#define Z209_6_CH6 8
#define Z209_5_CH5 9
#define Z209_4_CH4 10
#define Z209_3_CH3 11
#define Z209_2_CH2 12
#define Z209_1_CH1 13

#define Z210_4_CH4 26
#define Z210_3_CH3 27
#define Z210_2_CH2 28
#define Z210_1_CH1 31

#define Z211_1_CH1 24
#define Z211_2_CH2 25

#define PODSW_MIX_C 21
#define PODSW_HOL_B 22
#define PODSW_SALON_A 23

#define GWAR_N 29
#define GWAR_L 30

#define SWIATLO_HOL 39
#define SWIATLO_SALON 47
#define SWIATLO_SYPIALNIA 19
#define CZUJKA_RUCHU 20

//mcp 0 
constexpr uint64_t Z059_2 = 0x0008;
constexpr uint64_t Z059_4 = 0x0004;
constexpr uint64_t Z059_6 = 0x0002;
constexpr uint64_t Z059_8 = 0x0001;

// mcp 1
constexpr uint64_t Z24_OFF = (0x0004ull << 16);
constexpr uint64_t CZUJKA1 = (0x0001ull << 16);
constexpr uint64_t CZUJKA2 = (0x0002ull << 16);

// mcp 2
constexpr uint64_t Z058_03 = (0x4000ull << 32); //SALON 4 LEWY
constexpr uint64_t Z058_02 = (0x2000ull << 32); //SALON 3 PRAWY
constexpr uint64_t Z058_01 = (0x1000ull << 32); //SALON 3 LEWY

constexpr uint64_t Z216_08 = (0x0800ull << 32);

constexpr uint64_t Z214_01 = (0x0400ull << 32);  
constexpr uint64_t Z214_02 = (0x0200ull << 32);
constexpr uint64_t Z214_03 = (0x0100ull << 32);    
constexpr uint64_t Z214_04 = (0x0040ull << 32); 
constexpr uint64_t Z214_05 = (0x0020ull << 32);  
constexpr uint64_t Z214_06 = (0x0010ull << 32); 
constexpr uint64_t Z214_07 = (0x0008ull << 32);
constexpr uint64_t Z214_08 = (0x0004ull << 32);
constexpr uint64_t Z214_09 = (0x0002ull << 32);
constexpr uint64_t Z214_10 = (0x0001ull << 32);

//mcp 3

constexpr uint64_t Z217_02 = (0x4000ull << 48);
constexpr uint64_t Z217_03 = (0x2000ull << 48);

constexpr uint64_t Z058_08 = (0x1000ull << 48);
constexpr uint64_t Z058_07 = (0x0800ull << 48);
constexpr uint64_t Z058_06 = (0x0400ull << 48);
constexpr uint64_t Z058_05 = (0x0200ull << 48);
constexpr uint64_t Z058_04 = (0x0100ull << 48);

constexpr uint64_t Z216_01 = (0x0040ull << 48);
constexpr uint64_t Z216_02 = (0x0020ull << 48);
constexpr uint64_t Z216_03 = (0x0010ull << 48);
constexpr uint64_t Z216_04 = (0x0008ull << 48);
constexpr uint64_t Z216_05 = (0x0004ull << 48);
constexpr uint64_t Z216_06 = (0x0002ull << 48);
constexpr uint64_t Z216_07 = (0x0001ull << 48);


#define LED1_LAZIENKA1 Z213_3_LEDY_CH1 
#define LED2_LAZIENKA2 Z213_4_LEDY_CH2
#define LED3_SYPIALNIA1 Z213_5_LEDY_CH3
#define LED4_SYPIALNIA2 Z213_6_LEDY_CH4

#define OSW_SALON1 Z210_1_CH1
#define OSW_SALON2 Z210_2_CH2

#define OSW_SYPIALNIA1 Z210_3_CH3
#define OSW_HOL_0      Z210_4_CH4

#define ZAS12V Z209_1_CH1
#define OSW_HOL_B1 Z209_2_CH2
#define OSW_HOL_B2 Z209_3_CH3
#define OSW_HOL_B3 Z209_4_CH4
#define OSW_HOL_B4 Z209_5_CH5

#define OSW_HOL_A1 Z209_6_CH6
#define OSW_HOL_A2 Z209_7_CH7
#define OSW_HOL_A3 Z209_8_CH8

#define OSW_SYPIALNIA2 Z211_1_CH1
#define OSW_SYPIALNIA3 Z211_2_CH2

#define KL01_SALKUC_PL  Z058_05 
#define KL01_SALKUC_PP  Z058_06 
#define KL02_SALKUC_LL  Z217_02 
#define KL02_SALKUC_LP  Z217_03 
#define KL03_SALJAD_LL  Z058_01 
#define KL03_SALJAD_LP  Z058_02 
#define KL04_SALJAD_PL  Z058_03 
#define KL04_SALJAD_PP  Z058_04 
#define KL05_SYPIAL_P   Z216_01 
#define KL05_SYPIAL_L   Z214_01 
#define KL06_SALSYP_PP  Z216_03 
#define KL06_SALSYP_PL  Z214_03 
#define KL07_SALSYP_LP  Z216_04 
#define KL07_SALSYP_LL  Z214_04 
#define KL08_SALPRZ_LP  Z216_02 
#define KL08_SALPRZ_LL  Z214_02 
#define KL09_HOLSYP_PP  Z216_06 
#define KL09_HOLSYP_PL  Z214_06 
#define KL10_HOLSYP_LP  Z216_07 
#define KL10_HOLSYP_LL  Z214_07 
#define KL11_SALLAZ_L   Z216_07 
#define KL11_SALLAZ_P   Z214_07 
#define KL12_HOLLAZ_P   Z216_08 
#define KL12_HOLLAZ_L   Z214_08 
#define KL13_HOLPOK     Z214_09 
#define KL14_HOLWC_P    Z058_07 
#define KL14_HOLWC_L    Z058_08 
#define KL15_HOLWEJ     Z214_10 

#define SIG_WIECZOR     Z059_2
#define SIG_NOC         Z059_4
#define SIG_2TARYFA     Z059_6
#define SIG_ZAS_AWAR    Z059_8



#endif