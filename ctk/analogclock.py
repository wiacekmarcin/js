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

class AnalogClock(LFrame):
    
    def __init__(self, master, app, **kwargs):
        super().__init__(800, 0, 300, 300, master, app, **kwargs)
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
        self.configure(width=self.wwidth)
        self.configure(height=self.wheight)

        
        img_path = "analog2.png"
        if  1:
            img_pil = Image.new(size=(300, 300), mode="RGB", color="black")
            imd = ImageDraw.Draw(img_pil)
            R1a = 250/2
            R1b = 270/2
            R2 = 280/2
            for m in range(60):
                if m % 5 == 0:
                    R = R1a
                    w = 3
                else:
                    R = R1b
                    w = 1
                p1 = (int(150 + R*math.sin(m*2*math.pi/60)), int(150 + R*math.cos(m*2*math.pi/60)))
                p2 = (int(150 + R2*math.sin(m*2*math.pi/60)), int(150 + R2*math.cos(m*2*math.pi/60)))
                imd.line((p1, p2), fill="white", width=w)
                self.r_img = img_pil

        else:
            img_pil = Image.open(img_path)
            self.r_img = img_pil.resize((self.wwidth, self.wheight))


        im_s1 = Image.open('sun.png')
        im_s1 = im_s1.resize((24, 24))
        self.r_img.paste(im_s1, (5, 30))

        im_s2 = Image.open('moon.png')
        im_s2 = im_s2.resize((24, 24))
        self.r_img.paste(im_s2, (self.wwidth - 26 - 5, 30))

        # use a truetype font
        self.font = ImageFont.truetype("Roboto-Regular.ttf", 24)

        imgd = ImageDraw.Draw(self.r_img)
        imgd.text((0,5), text="??:??", fill="white", font=self.font)
        self.txtw = 45
        #txtw = self.font.getlength("??:??")
        #txtw ~= 45px
        #print("txtw=",txtw)

        imgd.text((self.wwidth-self.txtw-5,5), text="??:??", fill="white", font=self.font)

        # Convert the PIL Image to Tkinter PhotoImage
        img = CTkImage(self.r_img, size=self.r_img.size)

        self.photo_label = CTkLabel(self, fg_color="black", image=img, text="")
        self.photo_label.place(x=0, y=0)
        
        #self.l_wschod_s = CTkLabel(self, text="?-1", fg_color="black", bg_color="black", text_color="white")
        #self.l_wschod_s.place(x=0, y=0)

        #self.l_zachod_s = CTkLabel(self, text="?-2", fg_color="black", bg_color="black", text_color="white")
        #self.l_zachod_s.place(x=self.wwidth - 25, y=0)


        #self.l_temp_min = CTkLabel(self, text="?-3", fg_color="black", bg_color="black", text_color="white")
        #self.l_temp_min.place(x=0, y=self.wheight - 25)

        #self.l_temp_max = CTkLabel(self, text="?-4", fg_color="black", bg_color="black", text_color="white")
        #self.l_temp_max.place(x=self.wwidth - 25, y=self.wheight - 25)

        self.webfont = ImageFont.truetype("weathericons-regular-webfont.ttf", 24)
        
        imgd.text((0, self.wheight - 30 - 30),                  text="\uf053", fill="white", font=self.webfont)
        imgd.text((self.wwidth - 20, self.wheight - 30 - 30),   text="\uf055", fill="white", font=self.webfont)

        imgd.text((0, self.wheight - 30),                text="\uf07b \uf03c", fill="white", font=self.webfont)
        imgd.text((self.wwidth - 50, self.wheight - 30), text="\uf07b \uf03c", fill="white", font=self.webfont)

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

        imgd = ImageDraw.Draw(self.r_img)
        x = 0
        y = 0
        imgd.rectangle((x, y, x+50, y+25), fill="black", outline="black")

        imgd.text((0,5), text=self.wschod, fill="white", font=self.font)
        
        self.act_img = self.r_img.copy()
        t_img = CTkImage(self.act_img, size=self.act_img.size)
        self.photo_label.configure(image=t_img)
   
    def setZachod(self, hour, min):
        self.zachod = "%d:" % hour
        if min < 10:
            self.zachod += "0"
        self.zachod += "%d" % min
        
        imgd = ImageDraw.Draw(self.r_img)

        x = self.wwidth - self.txtw - 5
        y = 0
        imgd.rectangle((x, y, x + self.txtw + 5, y + 25), fill="black", outline="black")

        imgd.text((self.wwidth - self.txtw, 5), text=self.zachod, fill="white", font=self.font)
        
        self.act_img = self.r_img.copy()
        t_img = CTkImage(self.act_img, size=self.act_img.size)
        self.photo_label.configure(image=t_img)
    
    def setMinimumTemp(self, ftemp):
        temp = "%2.1f\u00B0C" % ftemp
        imgd = ImageDraw.Draw(self.r_img)
        x = 0
        y = self.wheight - 20
        imgd.rectangle((x, y, x+50, y+20), fill="black", outline="black")

        imgd.text((5, self.wheight - 20), text=temp, fill="white", font=self.font)
        
        self.act_img = self.r_img.copy()
        t_img = CTkImage(self.act_img, size=self.act_img.size)
        self.photo_label.configure(image=t_img)
        
    def setMaximumTemp(self, ftemp):
        temp = "%2.1f\u00B0C" % ftemp
        imgd = ImageDraw.Draw(self.r_img)
        x = self.wwidth - 50
        y = self.wheight - 20
        imgd.rectangle((x, y, x + 50, y + 20), fill="black", outline="black")

        imgd.text((self.wwidth - 45, self.wheight - 20), text=temp, fill="white", font=self.font)
        
        self.act_img = self.r_img.copy()
        t_img = CTkImage(self.act_img, size=self.act_img.size)
        self.photo_label.configure(image=t_img)
    
    def timeout(self, dt):

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




