
import os
from m01 import m01
from m02 import m02
from m03 import m03
from m04 import m04
from m05 import m05
from m06 import m06
from m07 import m07
from m08 import m08
from m09 import m09
from m10 import m10
from m11 import m11
from m12 import m12

def getAvgMinMax(m, d, h) -> tuple[float, float]:
    if m <= 0 or m > 12:
        return (0, 0)
    mounth = [m01, m02, m03, m04, m05, m06, m07, m08, m09, m10, m11, m12]

    day = mounth[m-1]['%d' % d]
    minT  = day['%d' % h][0]
    maxT  = day['%d' % h][1]
    for i in range(2):
        minT = min(minT, day['%d' % (h+1+i)][0])
        maxT = max(maxT, day['%d' % (h+1+i)][1])
    return (minT, maxT)    

def getWarningTemp(temp:float, txt:str) -> tuple[bool, str, float, float]:
    sdate, stime = txt.split(" ")
    _, sm, sd = sdate.split("-")
    sh, _, _ = stime.split(":") 
    sm = int(sm)
    sd = int(sd)
    sh = int(sh)
    
    #'lodowato' , -9,
    #'mroźnie' , 0,
    #'bardzo zimno' , 7,
    #'zimno' , 13,
    #'chłodno' , 18,
    #'komfortowo' , 24,
    #'ciepło' , 29,
    #'gorąco' , 35,
    #'upalnie' , 50

    if temp <= -9:
        #return (True, 'lodowato [%2.1f < 9]\u00B0C' % temp, temp)
        return (True, 'lodowato' , -9, temp)

    if temp >= 35:
        #return (True, 'upalnie [%2.1f > 35]\u00B0C' % temp, temp)
        return (True, 'upalnie', 35, temp)

    minT, maxT = getAvgMinMax(sm, sd, sh)
    if temp >= minT and temp <= maxT:
        return (False, '', 0, 0)
    
    descr = ''
    if temp < minT:
        if temp < 0:
            #descr = 'mroźnie [%2.1f<%2.1f]\u00B0C' % (temp, minT)
            descr = 'mroźnie'
        elif temp < 7:
            descr = 'bardzo zimno'
        elif temp < 13:
            descr = 'zimno'
        elif temp < 18:
            descr = 'chłodno'
        elif temp < 24:
            descr = 'komfortowo'
        elif temp < 29:
            descr = 'ciepło'
        elif temp < 35:
            descr = 'gorąco'
        else:
            descr = '%f < %f' % (temp, minT)
        ret = (True, descr, minT, temp)
    elif temp > maxT:
        if temp < 0:
            #descr = 'mroźnie [%2.1f>%2.1f]\u00B0C' % (temp, maxT)
            descr = 'mroźnie'
        elif temp < 7:
            descr = 'bardzo zimno'
        elif temp < 13:
            descr = 'zimno'
        elif temp < 18:
            descr = 'chłodno'
        elif temp < 24:
            descr = 'komfortowo'
        elif temp < 29:
            descr = 'ciepło'
        elif temp < 35:
            descr = 'gorąco'
        else:
            descr = '%f > %f' % (temp, maxT)
        ret = (True, descr, maxT, temp)
    else:
        ret = (False, '', 0, 0)
    return ret

def getWarningWind(w:float, d:float) -> tuple[bool, str, float, float]:
    silaW = [(0, 'cisza', 0.2),
            (1, 'bardzo słaby', 1.5),
            (2, 'słaby wiatr', 1.6),
            (3, 'łagodny wiatr', 3),
            (4, 'umiarkowany wiatr', 5.5),
            (5, 'żywszy wiatr', 8.0),
            (6, 'silny wiatr', 10.8),
            (7, 'bardzo silny wiatr', 13.9),
            (8, 'sztorm', 17.2),
            (9, 'silny sztorm', 17.2),
            (10, 'bardzo silny sztorm', 24.5),
            (11, 'gwałtowny sztorm', 28.5),
            (12, 'huragan', 32.7)
    ]
    #print(f"w={w} d={d}")
    if w < 10.0 and d < 17.0:
        return (False, '', 0, 0)
    
    val = silaW[0][2]
    descr = silaW[0][1]
    idx = 1
    while idx < len(silaW) and val > silaW[idx][2]:
        descr = silaW[idx][1]
        #print(f"val={val} < [{idx}]={silaW[idx][2]}")
        idx += 1

    return (True, descr, w, d)