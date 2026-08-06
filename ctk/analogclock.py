from customtkinter import CTkFrame, CTkLabel, CTkImage, CTkFont
from PIL import Image, ImageDraw, ImageFont

import numpy as np
import os, math, datetime

from base_plugin import LSimpleFrame

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

class AnalogClock(LSimpleFrame):
    _wwidth = 350
    _wheight = 450
    #def __init__(self, master, app, **kwargs):
    #    super().__init__(800, 0, 300, 300, master, app, **kwargs)
    def __init__(self, master, app, **kwargs):
        super().__init__(master, app, **kwargs)
        self.setWschodZachod = 0
        self.startArcWschod = 0
        self.startArcZachod = 0
        self.m_h = 0
        self.m_m = 0
        self.m_s = 0
        self.wschod = "0:01"
        self.zachod = "23:59"
        self.minTemp = "\uf07b"
        self.maxTemp = "\uf07b"
        self.configure(width=self._wwidth)
        self.configure(height=self._wheight)
        self.clockXYR = (0, 0, min(self._wheight, self._wwidth))
        cx, cy, clockW = self.clockXYR

        clockR = min(self._wwidth, self._wheight)/2
        self.Rclock = clockR
        img_path = "analog2.png"
        if  1:
            img_pil = Image.new(size=(int(clockW), int(clockW)), mode="RGB", color="black")
            imd = ImageDraw.Draw(img_pil)
            R1a = 0.83*clockR
            R1b = 0.9*clockR
            R2 = 0.93*clockR
            for m in range(60):
                if m % 5 == 0:
                    R = R1a
                    w = 5
                else:
                    R = R1b
                    w = 3
                p1 = (int(clockR + R*math.sin(m*2*math.pi/60)), int(clockR + R*math.cos(m*2*math.pi/60)))
                p2 = (int(clockR + R2*math.sin(m*2*math.pi/60)), int(clockR + R2*math.cos(m*2*math.pi/60)))
                imd.line((p1, p2), fill="white", width=w)
                self.r_img = img_pil

        else:
            img_pil = Image.open(img_path)
            self.r_img = img_pil.resize((self._wwidth, self._wheight))


        #im_s1 = Image.open('sun.png')
        #im_s1 = im_s1.resize((32, 32))
        #self.r_img.paste(im_s1, (1, 30))

        #im_s2 = Image.open('moon.png')
        #im_s2 = im_s2.resize((32, 32))
        #self.r_img.paste(im_s2, (self._wwidth - 32 - 1, 30))

        # use a truetype font
        self.font = ImageFont.truetype("Roboto-Regular.ttf", 32)
        self.webfont = ImageFont.truetype("weathericons-regular-webfont.ttf", 32)

        self.tkfont = CTkFont(family="Roboto Regular", size=32, weight="bold", slant="roman")
        imgd = ImageDraw.Draw(self.r_img)
        
        
        imgd.text((0, 40), text="\uf051", fill="silver", font=self.webfont)
        imgd.text((clockW - 40, 40), text="\uf052", fill="silver", font=self.webfont)

        imgd.text((0, clockW - 75), text="\uf053\uf03c", fill="silver", font=self.webfont)

        txtw = self.webfont.getlength("\uf055\uf03c")
        imgd.text((clockW - txtw, clockW - 75),   text="\uf055\uf03c", fill="silver", font=self.webfont)

        #imgd.text((0,5), text="??:??", fill="white", font=self.font)
        #self.txtw = 45
        #txtw = self.font.getlength("??:??")
        #txtw ~= 45px
        #print("txtw=",txtw)

        #imgd.text((self._wwidth-self.txtw-5,5), text="??:??", fill="white", font=self.font)

        # Convert the PIL Image to Tkinter PhotoImage
        img = CTkImage(self.r_img, size=self.r_img.size)

        self.photo_label = CTkLabel(self, fg_color="black", image=img, text="")
        self.photo_label.place(x=cx, y=cy)
        
        self.l_wschod_s = CTkLabel(self, text="-", fg_color="black", bg_color="black", text_color="#71706E", font=self.tkfont)
        self.l_wschod_s.place(x=cx, y=cy)

        self.l_zachod_s = CTkLabel(self, text="-", fg_color="black", bg_color="black", text_color="#71706E", font=self.tkfont)
        self.l_zachod_s.place(x=cx + clockW - 80, y=cy)


        self.l_temp_min = CTkLabel(self, text="-", fg_color="black", bg_color="black", text_color="#71706E", font=self.tkfont)
        self.l_temp_min.place(x=cx, y=cy + clockW  - 35)

        self.l_temp_max = CTkLabel(self, text="-", fg_color="black", bg_color="black", text_color="#71706E", font=self.tkfont)
        self.l_temp_max.place(x=cx + clockW - 75, y=cy + clockW - 35)

        
        
        #imgd.text((0, self._wheight - 30 - 30),                  text="\uf053", fill="white", font=self.webfont)
        #imgd.text((self._wwidth - 20, self._wheight - 30 - 30),   text="\uf055", fill="white", font=self.webfont)

        #imgd.text((0, self._wheight - 30),                text="\uf07b \uf03c", fill="white", font=self.webfont)
        #imgd.text((self._wwidth - 50, self._wheight - 30), text="\uf07b \uf03c", fill="white", font=self.webfont)

        #self.drawClock()

        self.font_hour_min = CTkFont("Roboto Condensed", size=96, weight="bold", slant="roman")
        self.lhour_min = CTkLabel(self, text="00:00", fg_color="black", bg_color="black", text_color="white", 
                                    font=self.font_hour_min, anchor="nw")
        self.lhour_min.place(x=0, y=clockW)
        whour= self.font_hour_min.measure("00:00")

        font_sec = CTkFont("Roboto Condensed", size=48, weight="normal", slant="roman")
        self.lsecond = CTkLabel(self, text="00", fg_color="black", bg_color="black", text_color="silver", font=font_sec)
        self.lsecond.place(x=whour, y=clockW+25)
   
    def receiveNotfication(self, dictValue):
        
        if "sunrise" in dictValue:
            self.setWschod(dictValue["sunrise"].hour, dictValue["sunrise"].minute)
        
        if "sunset" in dictValue:
            self.setZachod(dictValue["sunset"].hour, dictValue["sunset"].minute)

        if "minimum-temperature" in dictValue:
            self.minTemp = dictValue["minimum-temperature"]
            self.setMinimumTemp(self.minTemp)
        
        if "maximum-temperature" in dictValue:
            self.maxTemp = dictValue["maximum-temperature"]
            self.setMaximumTemp(self.maxTemp)

    def setWschod(self, hour, min):
        self.wschod = "%d:" % hour
        if min < 10:
            self.wschod += "0"
        self.wschod += "%d" % min

        self.l_wschod_s.configure(text=self.wschod, text_color="white")
   
    def setZachod(self, hour, min):
        self.zachod = "%d:" % hour
        if min < 10:
            self.zachod += "0"
        self.zachod += "%d" % min
        zw = self.tkfont.measure(self.zachod)
        self.l_zachod_s.configure(text=self.zachod, text_color="white", )
        self.l_zachod_s.place(x=self._wwidth-zw-2, y=0)
    
    def setMinimumTemp(self, ftemp):
        temp = "%2.1f" % ftemp
        self.l_temp_min.configure(text=temp, text_color="white")
        
    def setMaximumTemp(self, ftemp):
        temp = "%2.1f" % ftemp
        self.l_temp_max.configure(text=temp, text_color="white")

    
    def timeout(self, dt):

        self.m_h = dt.time().hour
        self.m_m = dt.time().minute
        self.m_s = dt.time().second

        shour = ''
        if self.m_h < 10:
            shour+='0'
        shour+='%d:' % self.m_h
        if self.m_m < 10:
            shour+='0'
        shour+='%d' % self.m_m
        self.lhour_min.configure(text=shour)
        self.lsecond.configure(text="%02d" % self.m_s)
        
        self.act_img = self.r_img.copy()
        cx, cy, clockW = self.clockXYR
        R = clockW / 2

        c_x = int(cx+R)
        c_y = int(cy+R)

        rot_secsH = 2 * math.pi * ((self.m_h % 12)*3600.0 + self.m_h * 60.0 + self.m_s) / (12.0*3600.0)
        rot_secsM = 2 * math.pi * (self.m_m * 60.0 + self.m_s) / (3600.0)
        rot_secsS = 2 * math.pi * (self.m_s) / (60.0)

        pHA = (c_x - 4*R/150, c_y - 4*R/150)
        pHB = (c_x - 4*R/150, c_y + 4*R/150)
        pHC = (c_x + 4*R/150, c_y + 4*R/150)
        pHD = (c_x + 4*R/150, c_y - 4*R/150)
        pHE = (c_x + 4*R/150, c_y - 70*R/150)
        pHF = (c_x - 4, c_y - 70*R/150)
        pHG = (c_x, c_y - 83*R/150)

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

        pmA = (c_x - 2*R/150, c_y - 2*R/150)
        pmB = (c_x - 2*R/150, c_y + 2*R/150)
        pmC = (c_x + 2*R/150, c_y + 2*R/150)
        pmD = (c_x + 2*R/150, c_y - 2*R/150)
        pmE = (c_x + 2*R/150, c_y - 100*R/150)
        pmF = (c_x - 2*R/150, c_y - 100*R/150)
        pmG = (c_x, c_y - 120*R/150)

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

        S = 0.9*R
        pSec = (int(c_x + S*math.sin(math.pi-rot_secsS)), int(c_y + S*math.cos(math.pi-rot_secsS)))

        img1.line(((c_x, c_y), pSec), fill="silver", width=2)

        #img.show()
        t_img = CTkImage(self.act_img, size=self.act_img.size)
        self.photo_label.configure(image=t_img)
        return




