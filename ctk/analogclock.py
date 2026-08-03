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
    _wheight = 350
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

        minR = min(self._wwidth, self._wheight)
        self.Rclock = minR
        img_path = "analog2.png"
        if  1:
            img_pil = Image.new(size=(minR, minR), mode="RGB", color="black")
            imd = ImageDraw.Draw(img_pil)
            R1a = 0.83*minR/2
            R1b = 0.9*minR/2
            R2 = 0.93*minR/2
            for m in range(60):
                if m % 5 == 0:
                    R = R1a
                    w = 5
                else:
                    R = R1b
                    w = 3
                p1 = (int(minR/2 + R*math.sin(m*2*math.pi/60)), int(minR/2 + R*math.cos(m*2*math.pi/60)))
                p2 = (int(minR/2 + R2*math.sin(m*2*math.pi/60)), int(minR/2 + R2*math.cos(m*2*math.pi/60)))
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
        self.tkfont = CTkFont(family="Roboto-Regular", size=32, weight="bold", slant="roman")
        self.webfont = ImageFont.truetype("weathericons-regular-webfont.ttf", 32)
        imgd = ImageDraw.Draw(self.r_img)
        
        
        imgd.text((0, 40), text="\uf051", fill="white", font=self.webfont)
        imgd.text((self._wheight - 40, 40), text="\uf052", fill="white", font=self.webfont)

        imgd.text((0, self._wheight - 75), text="\uf053\uf03c", fill="white", font=self.webfont)

        txtw = self.webfont.getlength("\uf055\uf03c")
        imgd.text((self._wwidth - txtw, self._wheight - 75),   text="\uf055\uf03c", fill="white", font=self.webfont)

        #imgd.text((0,5), text="??:??", fill="white", font=self.font)
        self.txtw = 45
        #txtw = self.font.getlength("??:??")
        #txtw ~= 45px
        #print("txtw=",txtw)

        #imgd.text((self._wwidth-self.txtw-5,5), text="??:??", fill="white", font=self.font)

        # Convert the PIL Image to Tkinter PhotoImage
        img = CTkImage(self.r_img, size=self.r_img.size)

        self.photo_label = CTkLabel(self, fg_color="black", image=img, text="")
        self.photo_label.place(x=(self._wwidth - self.Rclock)/2, y=(self._wheight - self.Rclock)/2)
        
        self.l_wschod_s = CTkLabel(self, text="7:51", fg_color="black", bg_color="black", text_color="white", font=self.tkfont)
        self.l_wschod_s.place(x=0, y=0)

        self.l_zachod_s = CTkLabel(self, text="22:35", fg_color="black", bg_color="black", text_color="white", font=self.tkfont)
        self.l_zachod_s.place(x=self._wwidth - 80, y=0)


        self.l_temp_min = CTkLabel(self, text="n/a", fg_color="black", bg_color="black", text_color="white", font=self.tkfont)
        self.l_temp_min.place(x=0, y=self._wheight - 35)

        self.l_temp_max = CTkLabel(self, text="n/a", fg_color="black", bg_color="black", text_color="white", font=self.tkfont)
        self.l_temp_max.place(x=self._wwidth - 75, y=self._wheight - 35)

        
        
        #imgd.text((0, self._wheight - 30 - 30),                  text="\uf053", fill="white", font=self.webfont)
        #imgd.text((self._wwidth - 20, self._wheight - 30 - 30),   text="\uf055", fill="white", font=self.webfont)

        #imgd.text((0, self._wheight - 30),                text="\uf07b \uf03c", fill="white", font=self.webfont)
        #imgd.text((self._wwidth - 50, self._wheight - 30), text="\uf07b \uf03c", fill="white", font=self.webfont)

        #self.drawClock()

   
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

        self.l_wschod_s.configure(text=self.wschod)
   
    def setZachod(self, hour, min):
        self.zachod = "%d:" % hour
        if min < 10:
            self.zachod += "0"
        self.zachod += "%d" % min
        self.l_zachod_s.configure(text=self.zachod)
    
    def setMinimumTemp(self, ftemp):
        temp = "%2.1f" % ftemp
        self.l_temp_min.configure(text=temp)
        
    def setMaximumTemp(self, ftemp):
        temp = "%2.1f" % ftemp
        self.l_temp_max.configure(text=temp)

    
    def timeout(self, dt):

        self.m_h = dt.time().hour
        self.m_m = dt.time().minute
        self.m_s = dt.time().second

        #if self.m_s != 0:
        #    return
        
        self.act_img = self.r_img.copy()
        R = min(self._wwidth, self._wheight) / 2

        c_x = int(self._wwidth / 2)
        c_y = int(self._wheight / 2)

        rot_secsH = 2 * math.pi * ((self.m_h % 12)*3600.0 + self.m_h * 60.0 + self.m_s) / (12.0*3600.0)
        rot_secsM = 2 * math.pi * (self.m_m * 60.0 + self.m_s) / (3600.0)
        rot_secsS = 2 * math.pi * (self.m_s) / (60.0)

        pHA = (c_x - 4, c_y - 4)
        pHB = (c_x - 4, c_y + 4)
        pHC = (c_x + 4, c_y + 4)
        pHD = (c_x + 4, c_y - 4)
        pHE = (c_x + 4, c_y - 70)
        pHF = (c_x - 4, c_y - 70)
        pHG = (c_x, c_y - 85)

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

        pmA = (c_x - 2, c_y - 2)
        pmB = (c_x - 2, c_y + 2)
        pmC = (c_x + 2, c_y + 2)
        pmD = (c_x + 2, c_y - 2)
        pmE = (c_x + 2, c_y - 90)
        pmF = (c_x - 2, c_y - 90)
        pmG = (c_x, c_y - 100)

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

        R = 117
        pSec = (int(c_x + R*math.sin(math.pi-rot_secsS)), int(c_y + R*math.cos(math.pi-rot_secsS)))

        img1.line(((c_x, c_y), pSec), fill="silver", width=2)

        #img.show()
        t_img = CTkImage(self.act_img, size=self.act_img.size)
        self.photo_label.configure(image=t_img)
        return




