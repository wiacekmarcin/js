#-*- encoding : utf-8 -*-
import sys, os
import datetime
import math

from PIL import Image, ImageDraw, ImageFont, ImageOps, ImageColor

#(600, 127)
beg = (78, 8)

im = Image.open('listopad_11.png')
#print(im.size)

mroznie = [(99, 145, 160, 255), (131, 194, 213, 255), (116, 170, 186, 255), (128, 188, 206, 255), 
           (126, 185, 203, 255), (122, 179, 196, 255), (120, 176, 193, 255), (118, 173, 190, 255),
           (114, 168, 184, 255), (124, 182, 200, 255), (112, 165, 181, 255), 
           (112, 165, 181, 255), (98, 145, 160, 255), (98, 145, 160, 255), (104, 152, 168, 255),
           (95, 135, 96, 255), (99, 142, 100, 255), (98, 140, 98, 255)]
bardzo_zimno = [(116, 165, 180, 255), (104, 149, 105, 255), (93, 133, 94, 255), (94, 135, 95, 255), (94, 135, 95, 255),
                (91, 130, 92, 255), (78, 113, 79, 255), (94, 137, 139, 255), (125, 183, 186, 255),
                (77, 112, 78, 255), (103, 149, 104, 255), (136, 172, 137, 255), (90, 130, 91, 255), (77, 112, 78, 255),
                (96, 137, 97, 255)]
zimno = [(117, 168, 120, 255), (117, 168, 119, 255), (117, 168, 119, 255), (103, 147, 105, 255), (88, 127, 90, 255),
         (134, 179, 137, 255), (110, 157, 113, 255), (94, 135, 96, 255), (99, 143, 102, 255),
         (227, 235, 222, 255), ]

chlodno = [(141, 191, 114, 255), (124, 167, 100, 255), (126, 177, 118, 255), (123, 165, 99, 255), (107, 143, 86, 255),
           (165, 204, 144, 255), (164, 194, 115, 255)]

komfort = [(233, 204, 120, 255), (204, 179, 105, 255), (175, 153, 90, 255), (191, 167, 99, 255), (187, 164, 96, 255),
           (248, 238, 211, 255), (246, 235, 202, 255), (241, 221, 166, 255)]

days = 31
hpy = 1.0*im.height/24
dpx = 1.0*im.width/days
print("m12={")
uC = {}
str = ''
dbg = 0

corr = {
'2.6' : (0, 7), #(102, 147, 103, 255)
'2.12' : (0, 7), #(110, 158, 112, 255)
'2.17' : (0, 7), #(85, 123, 87, 255)
'3.6' : (0, 7), #(101, 144, 102, 255)

}

for d in range(0, days ):
    di = d + 1
    px = int(dpx*d + dpx/2)
    print("'%d' : {" % di)
    for i in range(0, 24):
        py = int(hpy*(23-i) + hpy/2)
        p = im.getpixel((px, py))

        if dbg == 1 and di == 1 and i in [4]:
            print(p)

        if p in mroznie:
            print(f"\t'{i}': (-9, 0),")
        elif p in bardzo_zimno:
            print(f"\t'{i}': (0, 7),")
        elif p in zimno:
            print(f"\t'{i}': (7, 13),")
        elif p in chlodno:
            print(f"\t'{i}': (13, 18),")
        elif p in komfort:
            print(f"\t'{i}': (18, 24),")
        else :
            fc = False
            k = '%d.%d' % (di, i)
            if k in corr:
                print("\t'%d': (%d, %d)," % (i, corr[k][0], corr[k][1]))
            else:
                delta1 = delta2 = delta3 = delta4 = delta5 = 10000000
                for c in mroznie:
                    d = (p[0]-c[0])*(p[0]-c[0])+(p[1]-c[1])*(p[1]-c[1])+(p[2]-c[2])*(p[2]-c[2])
                    delta1 = min(delta1, d)
                    if d < 200:
                        print(f"\t'{i}': (-9, 0),")
                        fc = True
                        break
                
                for c in bardzo_zimno:
                    d = (p[0]-c[0])*(p[0]-c[0])+(p[1]-c[1])*(p[1]-c[1])+(p[2]-c[2])*(p[2]-c[2])
                    delta2 = min(delta2, d)
                    if d < 200:
                        if fc:
                            print("error")
                            str += "'%d.%d' : ( , ), #%s\n" % (di, i, p)
                        print(f"\t'{i}': (0, 7),")
                        fc = True
                        break
                
                for c in zimno:
                    d = (p[0]-c[0])*(p[0]-c[0])+(p[1]-c[1])*(p[1]-c[1])+(p[2]-c[2])*(p[2]-c[2])
                    delta3 = min(delta3, d)
                    if d < 200:
                        if fc:
                            print("error")
                            str += "'%d.%d' : ( , ), #%s\n" % (di, i, p)
                        print(f"\t'{i}': (7, 13),")
                        fc = True
                        break

                for c in chlodno:
                    d = (p[0]-c[0])*(p[0]-c[0])+(p[1]-c[1])*(p[1]-c[1])+(p[2]-c[2])*(p[2]-c[2])
                    delta4 = min(delta4, d)
                    if d < 200:
                        if fc:
                            print("error")
                            str += "'%d.%d' : ( , ), #%s\n" % (di, i, p)
                        print(f"\t'{i}': (13, 18),")
                        fc = True
                        break

                for c in komfort:
                    d = (p[0]-c[0])*(p[0]-c[0])+(p[1]-c[1])*(p[1]-c[1])+(p[2]-c[2])*(p[2]-c[2])
                    delta5 = min(delta5, d)
                    if d < 200:
                        if fc:
                            print("error")
                            str += "'%d.%d' : ( , ), #%s\n" % (di, i, p)
                        print(f"\t'{i}': (18, 24),")
                        fc = True
                        break


                if not fc:
                    print(f"\t'{i}': e,")
                    str += "'%d.%d' : ( , ), #%s\n" % (di, i, p)
                    if p not in uC:
                        uC[p] = 1
                    else:
                        uC[p] += 1
    print("},")
print("}")            

print(str)
print(uC)