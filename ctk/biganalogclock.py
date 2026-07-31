from customtkinter import CTkFrame, CTkLabel, CTkImage
from PIL import Image, ImageDraw, ImageFont

import numpy as np
import os, math, datetime

from base_plugin import LFrame

def R(angle):
    cos_a = np.cos(angle)
    sin_a = np.sin(angle)
    return np.array([[cos_a, -sin_a],
                    [sin_a,  cos_a]])

def rotate(poly, angle, Center):   
    poly_new = (poly - Center).dot(R(angle).T) + Center
    return poly_new

def organize(poly):
    P = np.empty(( len(poly), 2), dtype=float)
    for i in range(len(poly)):
        P[i,0] = poly[i][0]
        P[i,1] = poly[i][1]
    return P  

def deaorganize(P):
    poly = []
    for i in range(len(P)):
        poly.append((P[i,0], P[i,1]))
    return poly

class BigAnalogClock(LFrame):
    
    def __init__(self, master, app, **kwargs):
        super().__init__(0, 0, 1000, 1000, master, app, **kwargs)
        self.configure(width=self.wwidth)
        self.configure(height=self.wheight)

        self.x = 0
        self.y = 0
        self.dx = 1
        self.dy = 1

        self.posx = (1080-1000)/2
        self.posy = (1920-1000)/2
        img_pil = Image.new(size=(1000, 1000), mode="RGB", color="black")
        imd = ImageDraw.Draw(img_pil)
        R1a = 800/2
        R1b = 920/2
        R2 = 980/2
        for m in range(60):
            if m % 5 == 0:
                R = R1a
                w = 3
            else:
                R = R1b
                w = 1
            p1 = (int(500 + R*math.sin(m*2*math.pi/60)), int(500 + R*math.cos(m*2*math.pi/60)))
            p2 = (int(500 + R2*math.sin(m*2*math.pi/60)), int(500 + R2*math.cos(m*2*math.pi/60)))
            imd.line((p1, p2), fill="white", width=w)
            self.r_img = img_pil
        

        # Convert the PIL Image to Tkinter PhotoImage
        img = CTkImage(self.r_img, size=self.r_img.size)

        self.photo_label = CTkLabel(self, fg_color="black", image=img, text="")
        self.photo_label.place(x=0, y=0)
        
    def timeout(self, dt):
        print("timeout")
        self.m_h = dt.time().hour
        self.m_m = dt.time().minute
        self.m_s = dt.time().second

        #if self.m_s != 0:
        #    return
        
        self.act_img = self.r_img.copy()
        R = min(self.wwidth, self.wheight) / 2

        c_x = int(self.wwidth / 2)
        c_y = int(self.wheight / 2)

        rot_secsH = 2 * math.pi * ((self.m_h % 12)*3600.0 + self.m_h * 60.0 + self.m_s) / (12.0*3600.0)
        rot_secsM = 2 * math.pi * (self.m_m * 60.0 + self.m_s) / (3600.0)
        rot_secsS = 2 * math.pi * (self.m_s) / (60.0)

        L1 = int(0.3 * self.wwidth)
        L2 = int(0.01 * self.wwidth)
        L3 = int(0.33 * self.wwidth)

        pHA = (c_x - L2, c_y - L2)
        pHB = (c_x - L2, c_y + L2)
        pHC = (c_x + L2, c_y + L2)
        pHD = (c_x + L2, c_y - L2)
        pHE = (c_x + L2, c_y - L1)
        pHF = (c_x - L2, c_y - L1)
        pHG = (c_x, c_y - L3)

        xyH = [
            pHA,
            pHB,
            pHC,
            pHD,
            pHE,
            pHG,
            pHF,
            pHA,
        ]

        img1 = ImageDraw.Draw(self.act_img)  
        #img1.polygon(xyH, fill ="white", outline ="white") 

        
        P = organize(xyH)
        Cntr = np.array([c_x, c_y])
        P_new = rotate(P, rot_secsH, Cntr)

        pointsH = deaorganize(P_new)
        img1.polygon(pointsH, fill ="darkgrey", outline ="darkgrey") 

        M1 = int(0.37 * self.wwidth)
        M2 = int(0.005 * self.wwidth)
        M3 = int(0.4 * self.wwidth)

        pmA = (c_x - M2, c_y - M2)
        pmB = (c_x - M2, c_y + M2)
        pmC = (c_x + M2, c_y + M2)
        pmD = (c_x + M2, c_y - M2)
        pmE = (c_x + M2, c_y - M1)
        pmF = (c_x - M2, c_y - M1)
        pmG = (c_x, c_y - M3)

        xym = [
            pmA,
            pmB,
            pmC,
            pmD,
            pmE,
            pmG,
            pmF,
            pmA,
        ]

        P = organize(xym)   
        Cntr = np.array([c_x, c_y])
        P_new = rotate(P, rot_secsM, Cntr)

        pointsm = deaorganize(P_new)
        img1.polygon(pointsm, fill ="white", outline ="white") 

        R = int(0.45*self.wwidth)
        pSec = (int(c_x + R*math.sin(math.pi-rot_secsS)), int(c_y + R*math.cos(math.pi-rot_secsS)))

        img1.line(((c_x, c_y), pSec), fill="silver", width=max(2, int(self.wwidth/300)))

        #img.show()
        t_img = CTkImage(self.act_img, size=self.act_img.size)
        self.photo_label.configure(image=t_img)

        self.x += self.dx
        self.y += self.dy
        if self.x + self.wwidth >= 1080:
            self.x = 1080 - self.wwidth 
            self.dx = -1
        if self.x <= 0:
            self.dx = 1
            self.x = 0
        if self.y + self.wheight >= 1920:
            self.y = 1920 - self.wheight
            self.dy = -1
        if self.y <= 0:
            self.dy = 1
            self.y = 0

        self.place(x=self.x, y=self.y)


        return




