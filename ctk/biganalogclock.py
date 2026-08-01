from customtkinter import CTkFrame, CTkLabel, CTkImage, CTkFrame, CTkFont
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

def opisWiatru(windy_ms:float, kier:None|str):
    if kier is None:
        appx = ''
    else:
        appx = ' (%s)' % kier
    if windy_ms < 0.3:
        return ''
    elif windy_ms < 1.6:
        return 'słabe powiewy wiatru%s' % appx
    elif windy_ms < 3.4:
        return 'słaby wiatr%s' % appx
    elif windy_ms < 5.5:
        return 'łagodny wiatr%s' % appx
    elif windy_ms < 8.0:
        return 'umiarkowany wiatr%s' % appx
    elif windy_ms < 10.8:
        return 'dość silny wiatr%s' % appx
    elif windy_ms < 13.9:
        return 'silny wiatr%s' % appx
    elif windy_ms < 17.2:
        return 'bardzo silny wiatr%s' % appx
    elif windy_ms < 20.8:
        return 'sztorm%s' % appx
    elif windy_ms < 24.5:
        return 'silny sztorm%s' % appx
    elif windy_ms < 28.5:
        return 'bardzo silny sztorm%s' % appx
    elif windy_ms < 32.6:
        return 'gwałtowny sztorm%s' % appx
    else:
        return 'huragan%s' % appx

def getWarningRain(rain3_h:float, descr:str):
    if "deszcz" in descr:
        return ''

    if "ulewa" in descr:
        return ''
               #'bardzo lekki deszcz 
    if rain3_h < 3*0.25:
        return 'bardzo lekki deszcz'
    elif rain3_h < 3*1.0:
        return 'lekki deszcz'
    elif rain3_h < 3*4.0:
        return 'umiarkowany deszcz'
    elif rain3_h < 3*12.0:
        return 'ulewny deszcz'
    elif rain3_h < 3*36.0:
        return 'duży ulewny deszcz'
    elif rain3_h < 3*60.0:
        return 'bardzo duży ulewny deszcz'
    elif rain3_h < 3*84.0:
        return 'ulewa'
    elif rain3_h < 3*114.0:
        return 'silna ulewa'
    elif rain3_h < 3*174.0:
        return 'deszcz nawalny'
    elif rain3_h < 3*234.0:
        return 'duży deszcz nawalny'
    elif rain3_h < 3*414.0:
        return 'nawałnica'
    else:
        return 'nawałnica katastrofalna'    

def getWarningSnow(snow3_h:float, descr:str):
    if 'śnieg' in descr:
        return ''
               #'bardzo lekki deszcz 
    return 'opady śniegu'
            
class BigAnalogClock(LFrame):

    
    def __init__(self, master, app, **kwargs):
        super().__init__(0, 0, 1000, 1300, master, app, **kwargs)
        self.configure(width=self.wwidth)
        self.configure(height=self.wheight)

        self.today = ''
        self.infolist = ''
        self.lazienka_tih = []
        self.x = 0
        self.y = 0
        self.dx = 1
        self.dy = 1

        self.posx = (1080-1000)/2
        self.posy = (1920-1000)/2
        self.zwidth = 1000
        self.zheight = 1000
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

        bottom_frame = CTkFrame(self, width=self.wwidth, height=200, bg_color="silver")
        bottom_frame.place(x=0, y=1000)

        font_opispogody = CTkFont("Roboto Condensed Regular", size=48, weight="normal", slant="roman")
        


        self.opisPogody = CTkLabel(bottom_frame, text="",
                bg_color="black",fg_color="black", text_color="white", font=font_opispogody,
                justify="left", anchor="w", wraplength=1000)
        self.opisPogody.pack()

        self.m_names = ['stycznia', 'lutego', 'marca', 'kwietnia', 'maja', 'czerwca', 'lipca', 'sierpnia', 
             'września', 'paździenika', 'listopada', 'grudnia']
        self.t_names = ['poniedziałek', 'wtorek', 'środa', 'czwartek', 'piątek', 'sobota', 'niedziela' ]                                


    def receiveNotfication(self, dictValue):

        kier = ''
        wind_speed = 0
        if 'lazienka_temp' in dictValue:
            self.lazienka_tih = ['łazienka %2.1f\u00B0C, %d%%' % (float(dictValue['lazienka_temp']), 
                                                                      float(dictValue['lazienka_humi']))]

        if 'opisPogody' not in dictValue:
            return 

        text = []
        print(dictValue)
        text.append(dictValue['opisPogody'])

        rtxt = ''
        if 'rain_3h' in dictValue:
            rtxt = getWarningRain(dictValue['rain_3h'], dictValue['opisPogody'])

        if 'rain_1h' in dictValue:
            rtxt = getWarningRain(3*dictValue['rain_1h'], dictValue['opisPogody'])

        if 'snow_3h' in dictValue:
            rtxt = getWarningSnow(dictValue['snow_3h'], dictValue['opisPogody'])

        if 'snow_1h' in dictValue:
            rtxt = getWarningSnow(3*dictValue['snow_1h'], dictValue['opisPogody'])

        if len(rtxt):
            text.append(rtxt)

        if 'temp' in dictValue:
            text.append('temperatura %2.1f\u00B0C' % dictValue['temp'])

        if 'feels_like' in dictValue:
            text.append('odczuwalna %2.1f\u00B0C' % dictValue['feels_like'])

        if 'huminidity' in dictValue:
            text.append('wilgotność %d%%' % dictValue['huminidity'])

        if 'pressure' in dictValue:
            text.append('ciśnienie %dhPa' % dictValue['pressure'])

        if 'kierunekwiatru' in dictValue:
            kier = dictValue['kierunekwiatru']
        
        if 'wind_speed' in dictValue:
            wind_speed = dictValue['wind_speed']

        opis_wiatru = opisWiatru(wind_speed, kier)

        if len(opis_wiatru) > 0:
            text.append(opis_wiatru)

        if 'widocznosc' in dictValue and dictValue['widocznosc'] < 10000:
            text.append('widoczność %dm' % dictValue['widocznosc'])

        self.infolist = text
        self.updateInfo()

    def updateInfo(self):
        text = []
        if self.today != '':
            text.append(self.today)

        if len(self.infolist) > 0:
            text.extend(self.infolist)

        if len(self.lazienka_tih) > 0:
            text.extend(self.lazienka_tih)

        self.opisPogody.configure(text=', '.join(text))


    def timeout(self, dt):
        
        self.m_h = dt.time().hour
        self.m_m = dt.time().minute
        self.m_s = dt.time().second

        d_m = dt.date().month
        d_d = dt.date().day

        st = self.t_names[dt.date().weekday()]
        tday = "%s, %d %s" % (st, d_d, self.m_names[d_m-1])

        if self.today != tday:
            self.today = tday
            self.updateInfo()
        
        self.act_img = self.r_img.copy()
        R = min(self.zwidth, self.zheight) / 2

        c_x = int(self.zwidth / 2)
        c_y = int(self.zheight / 2)

        rot_secsH = 2 * math.pi * ((self.m_h % 12)*3600.0 + self.m_h * 60.0 + self.m_s) / (12.0*3600.0)
        rot_secsM = 2 * math.pi * (self.m_m * 60.0 + self.m_s) / (3600.0)
        rot_secsS = 2 * math.pi * (self.m_s) / (60.0)

        L1 = int(0.3 * self.zwidth)
        L2 = int(0.01 * self.zwidth)
        L3 = int(0.33 * self.zwidth)

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

        M1 = int(0.37 * self.zwidth)
        M2 = int(0.005 * self.zwidth)
        M3 = int(0.4 * self.zwidth)

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

        R = int(0.45*self.zwidth)
        pSec = (int(c_x + R*math.sin(math.pi-rot_secsS)), int(c_y + R*math.cos(math.pi-rot_secsS)))

        img1.line(((c_x, c_y), pSec), fill="silver", width=max(2, int(self.zwidth/300)))

        #img.show()
        t_img = CTkImage(self.act_img, size=self.act_img.size)
        self.photo_label.configure(image=t_img)

        self.x += self.dx
        self.y += self.dy
        if self.x + self.zwidth >= 1080:
            self.x = 1080 - self.zwidth 
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

        self.place(x=self.x, y=self.y, anchor='nw')


        return




