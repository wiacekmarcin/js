from customtkinter import CTkImage, CTkFont
from PIL import Image, ImageDraw
import tkinter as tk
import numpy as np
import os, math

from base_plugin import LFrame, LCTkFrame, LCTkLabel 
from base_app import LustroApp
from rss import RssInfo
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

def deg2Short(deg):
    if deg>11.25 and deg<=33.75 : 
        return "\uf05a" #NNE
    elif deg > 33.75 and deg <= 56.25: 
        return "\uf05a" #NE
    elif deg > 56.25 and deg <= 78.75 :
        return "\uf05a" #ENE
    elif deg > 78.75 and deg <= 101.25 :
        return "\uf059" #E
    elif deg > 101.25 and deg <= 123.75 :
        return "\uf05d" #ESE
    elif deg > 123.75 and deg <= 146.25 :
        return "\uf05d" #SE
    elif deg > 146.25 and deg <= 168.75 :
        return "\uf05d" #SSE
    elif deg > 168.75 and deg <= 191.25 :
        return "\uf060" #S
    elif deg > 191.25 and deg <= 213.75 :
        return "\uf05e" #SSW
    elif deg > 213.75 and deg <= 236.25 :
        return "\uf05e" #SW
    elif deg > 236.25 and deg <= 258.75 :
        return "\uf05e" #WSW
    elif deg > 258.75 and deg <= 281.25 :
        return "\uf05b" #W
    elif deg > 281.25 and deg <= 303.75 :
        return "\uf05b" #WNW
    elif deg > 303.75 and deg <= 326.25 :
        return "\uf05b" #NW
    elif deg > 326.25 and deg <= 348.75 :
        return "\uf05b" #NNW
    else :
        return "\uf05c" #N
            
class BigAnalogClock(LFrame):
    def __init__(self, master, app:LustroApp, **kwargs):
        super().__init__(0, 0, 1000, app._max_height, master, app, **kwargs)
        #self.wwidth = 1000
        self.configure(width=self.wwidth)
        self.configure(height=self.wheight)

        self.zwidth = 1000
        self.zheight = 1000


        self.wschod = ''
        self.zachod = ''
        self.today = ''
        self.infolist = ''
        self.x = 0
        self.y = 0
        self.dx = 1
        self.dy = 1

        self.outside_temp = ''
        self.outside_humi = ''
        
        self.pogoda_temp = ''
        self.pogoda_humi = ''

        self.webfont = CTkFont(family="Weather Icons Regular", size=48, weight="normal", slant="roman")
        self.smwebfont = CTkFont(family="Weather Icons Regular", size=40, weight="normal", slant="roman")
        self.tkfont = CTkFont(family="Roboto Regular", size=48, weight="normal", slant="roman")
        self.smfont = CTkFont(family="Roboto Regular", size=40, weight="normal", slant="roman")
        

        dirf = os.path.dirname(os.path.realpath(__file__))
        self.drawRing(min(self.zwidth, self.zheight), self.wwidth)
        self.bottom_left(dirf)
        
        self.top_left(dirf)
        self.top_right(dirf)
        self.bottom_right(dirf)
        self.bottom(app)    
        
        #f0017 f001b f0019
        self.m_names = ['stycznia', 'lutego', 'marca', 'kwietnia', 'maja', 'czerwca', 'lipca', 'sierpnia', 
             'września', 'paździenika', 'listopada', 'grudnia']
        self.t_names = ['poniedziałek', 'wtorek', 'środa', 'czwartek', 'piątek', 'sobota', 'niedziela' ] 

    def drawRing(self, cl_size:int, maxwidth:int):

        self.posx = (maxwidth-cl_size)/2
        self.posy = 0
        center = int(cl_size)/2
        img_pil = Image.new(size=(cl_size, cl_size), mode="RGB", color="black")
        imd = ImageDraw.Draw(img_pil)
        R1a = cl_size*0.800/2
        R1b = cl_size*0.920/2
        R2 =  cl_size*0.980/2
        for m in range(60):
            if m % 5 == 0:
                R = R1a
                w = 3
            else:
                R = R1b
                w = 1
            p1 = (int(center + R*math.sin(m*2*math.pi/60)), int(center + R*math.cos(m*2*math.pi/60)))
            p2 = (int(center + R2*math.sin(m*2*math.pi/60)), int(center + R2*math.cos(m*2*math.pi/60)))
            imd.line((p1, p2), fill="white", width=w)
            self.r_img = img_pil
        

        # Convert the PIL Image to Tkinter PhotoImage
        img = CTkImage(self.r_img, size=self.r_img.size)

        self.photo_label = LCTkLabel(master=self, image=img, text="", width=cl_size, height=cl_size)
        self.photo_label.place(x=0, y=0)
    

    def bottom_left(self, dirf):
        img_m_s = os.path.join(dirf, 'png', 'm_s.png')
        my_image_m_s = CTkImage(light_image=Image.open(img_m_s),
                                        dark_image=Image.open(img_m_s),
                                        size=(23, 32))
        img_mm_godz = os.path.join(dirf, 'png', 'mm_godz.png')
        my_image_mm_godz = CTkImage(light_image=Image.open(img_mm_godz),
                                        dark_image=Image.open(img_mm_godz),
                                        size=(32, 30))
        self.ikona_pogody = LCTkLabel(master=self, text="", 
                                            font=self.webfont, justify="left", anchor="w")
        self.ikona_pogody.place(x=10, y=self.zheight-210)


        bottom_left_frame_1 = LCTkFrame(self, width=190, height=75)
        bottom_left_frame_1.place(x=0, y=self.zheight-140)
        
        self.ikona_deszczu = LCTkLabel(master=bottom_left_frame_1, text="\uf00c", 
                                        font=self.webfont, justify="left", anchor="nw")
        self.ikona_deszczu.pack(side='left', padx=5)
        self.ilosc_deszczu = LCTkLabel(master=bottom_left_frame_1, text="0", 
                                        font=self.smfont, justify="left", anchor="nw")
        self.ilosc_deszczu.pack(side='left', padx=5)
        self.ilosc_deszczu_unit = LCTkLabel(master=bottom_left_frame_1, image= my_image_mm_godz, text="", 
                                            justify="right", anchor="e")
        self.ilosc_deszczu_unit.pack(side='left', padx=5)

        bottom_left_frame_2 = LCTkFrame(self, width=190, height=75)
        bottom_left_frame_2.place(x=0, y=self.zheight-70)
        self.ikona_wiatru = LCTkLabel(master=bottom_left_frame_2, text="", 
                                            font=self.webfont, justify="left", anchor="nw")
        self.ikona_wiatru.pack(side='left', padx=5)
        self.predkosc_wiatru = LCTkLabel(master=bottom_left_frame_2, text="", 
                                        font=self.smfont, justify="left", anchor="nw")
        self.predkosc_wiatru.pack(side='left', padx=5)
        self.ilosc_wiatru_unit = LCTkLabel(master=bottom_left_frame_2, image= my_image_m_s, text="", 
                                           justify="right", anchor="e")
        self.ilosc_wiatru_unit.pack(side='left', padx=5)
        self.kierunek_wiatru = LCTkLabel(master=bottom_left_frame_2, text="", 
                                            font=self.webfont, justify="left", anchor="nw")
        self.kierunek_wiatru.pack(side='left', padx=5)


    def top_left(self, dirf):
        img_path = os.path.join(dirf, 'png', 'ikona_temp_outside.png')
        my_image = CTkImage(light_image=Image.open(img_path),
                                            dark_image=Image.open(img_path),
                                            size=(50, 50))
        top_left_frame = LCTkFrame(self, width=150, height=150)
        top_left_frame.place(x=0, y=0)        
       
        self.e_wschod = LCTkLabel(master=top_left_frame, text="\uf051", 
                                    font=self.webfont, justify="left", anchor="w")
        self.e_wschod.grid(row=0, column=0)
        self.l_wschod = LCTkLabel(master=top_left_frame, text="", 
                                    font=self.tkfont, justify="left", anchor="w")
        self.l_wschod.grid(row=0, column=1)
        self.e_zachod = LCTkLabel(master=top_left_frame, text="\uf052", 
                                font=self.webfont, justify="left", anchor="w")
        self.e_zachod.grid(row=1, column=0)
        self.l_zachod = LCTkLabel(master=top_left_frame, text="", 
                                font=self.tkfont, justify="left", anchor="w")
        self.l_zachod.grid(row=1, column=1)
        self.ikonafeeltemp = LCTkLabel(master=top_left_frame, image=my_image, text="", justify="left", anchor="w")
        self.ikonafeeltemp.grid(row=2, column=0)
        self.feeltemp = LCTkLabel(master=top_left_frame, text="", 
                                        font=self.smfont, justify="left", anchor="w")
        self.feeltemp.grid(row=2, column=1)


    def top_right(self, dirf):
        img_path_tih = os.path.join(dirf, 'png', 'tih_czujnika_2.png')
        my_image_tih = CTkImage(light_image=Image.open(img_path_tih),
                                            dark_image=Image.open(img_path_tih),
                                            size=(60, 60))
        top_right_frame = LCTkFrame(self, width=180, height=150)
        top_right_frame.place(x=self.zwidth-180, y=0)
        self.et_1 = LCTkLabel(master=top_right_frame, image=my_image_tih, text="", justify="right", anchor="e")
        self.et_1.grid(row = 0, column = 0, rowspan=2)
        self.z_temp = LCTkLabel(master=top_right_frame, text="", 
                            font=self.smfont, justify="right", anchor="ne")
        self.z_temp.grid(row=0, column=1)
        self.z_humi = LCTkLabel(master=top_right_frame, text="", 
                                    font=self.smfont, justify="right", anchor="ne")
        self.z_humi.grid(row=1, column=1)
        
    def bottom_right(self, dirf):
        img_path_stacja = os.path.join(dirf, 'png', 'tih_stacja.png')
        my_image_sttih = CTkImage(light_image=Image.open(img_path_stacja),
                                        dark_image=Image.open(img_path_stacja),
                                        size=(60, 80))
        bottom_right_frame = LCTkFrame(self, width=180, height=150)
        bottom_right_frame.place(x=self.zwidth-180, y=self.zheight-150)
        self.et_2 = LCTkLabel(master=bottom_right_frame, image= my_image_sttih, text="", justify="right", anchor="e")
        self.et_2.grid(row = 0, column = 0, rowspan=2)
        self.st_temp = LCTkLabel(master=bottom_right_frame, text="0", 
                            font=self.smfont, justify="right", anchor="ne")
        self.st_temp.grid(row=0, column=1)
        self.st_humi = LCTkLabel(master=bottom_right_frame, text="0", 
                                    font=self.smfont, justify="right", anchor="ne")
        self.st_humi.grid(row=1, column=1)
        self.st_cisnienie = LCTkLabel(master=bottom_right_frame, text="100", 
                                    font=self.smfont, justify="right", anchor="ne")
        self.st_cisnienie.grid(row=2, column=0, columnspan=2)

    def bottom(self, app):
        bottom_frame = LCTkFrame(self, width=self.wwidth, height=700)
        bottom_frame.place(x=0, y=self.zheight)

        font_opispogody = CTkFont("Roboto Condensed Regular", size=48, weight="normal", slant="roman")
        #font_opispogody_bold = CTkFont("Roboto Condensed Regular", size=48, weight="bold", slant="roman")

        font_pogoda_dzisiaj = CTkFont("Roboto Condensed Regular", size=32, weight="normal", slant="roman")
        #font_pogoda_dzisiaj_bold = CTkFont("Roboto Condensed Regular", size=32, weight="bold", slant="roman")

        font_ostrzezenie = CTkFont("Roboto Condensed Regular", size=32, weight="normal", slant="roman")
        font_ostrzezenie_bold = CTkFont("Roboto Condensed Regular", size=32, weight="bold", slant="roman")
        
        self.opisPogody = LCTkLabel(master=bottom_frame, text="", font=font_opispogody,
                justify="left", anchor="w", wraplength=self.wwidth-20)
        self.opisPogody.pack()

        self.pogodaDzisiaj = LCTkLabel(master=bottom_frame, text="", font=font_opispogody,
                        justify="left", anchor="w", wraplength=self.wwidth-20)
        self.pogodaDzisiaj.pack()

        #self.ostrzezenia= LCTkLabel(master=bottom_frame, text="",
        #        bg_color="black",fg_color="black", text_color="white", 
        #        #font=font_opispogody,
        #        font= CTkFont(family="Weather Icons Regular", size=24, weight="normal", slant="roman"),
        #        justify="left", anchor="w", wraplength=self.wwidth-20)
        # = LCTkFrame(self, width=self.wwidth)
        #self.ostrzezenia.pack()

        rss = RssInfo(bottom_frame, app, width=self.wwidth)
        rss.pack()

        self.color_ostrzezenia = ['#ffff00', '#fe7f00', '#ff0000']

        self.ostrzezenia_labels = []
        self.t_ostrzezenia = tk.Text(bottom_frame, width = 54, wrap = 'word', font=font_ostrzezenie, 
                                     height=5, background="black", foreground="white",
                                     borderwidth=0, border=0, highlightthickness = 0)
        self.t_ostrzezenia.pack()

        self.t_ostrzezenia.tag_configure("bold", font=font_ostrzezenie_bold)
        self.t_ostrzezenia.tag_configure("st1", foreground=self.color_ostrzezenia[0])
        self.t_ostrzezenia.tag_configure("st2", foreground=self.color_ostrzezenia[1])
        self.t_ostrzezenia.tag_configure("st3", foreground=self.color_ostrzezenia[2])


    def setWschod(self, hour, min):
        self.wschod = "%d:" % hour
        if min < 10:
            self.wschod += "0"
        self.wschod += "%d" % min

        self.l_wschod.configure(text=self.wschod, text_color="white")
   
    def setZachod(self, hour, min):
        self.zachod = "%d:" % hour
        if min < 10:
            self.zachod += "0"
        self.zachod += "%d" % min
        self.l_zachod.configure(text=self.zachod, text_color="white", )
        

    def receiveNotfication(self, dictValue):

        kier = ''
        wind_speed = 0
        #if 'lazienka_temp' in dictValue:
        #    self.lazienka_tih = ['łazienka %2.1f\u00B0C, %2.0f%%' % (float(dictValue['lazienka_temp']), 
        #                                                               float(dictValue['lazienka_humi']))]
        
        if "sunrise" in dictValue:
            self.setWschod(dictValue["sunrise"].hour, dictValue["sunrise"].minute)
                
        if "sunset" in dictValue:
            self.setZachod(dictValue["sunset"].hour, dictValue["sunset"].minute)
        
       
        if 'outside_temp' in dictValue and dictValue['outside_temp'] is not None:
            self.outside_temp = '%2.1f' % float(dictValue['outside_temp'])
            #self.z_temp_humi.configure(text = '%s\u00B0C %s%%' % (self.outside_temp, self.outside_humi)) 
            self.z_temp.configure(text = '%s\u00B0C' % self.outside_temp) 
            
        if 'outside_humi' in dictValue and dictValue['outside_humi'] is not None:
            self.outside_humi = '%2.0f' % float(dictValue['outside_humi'])
            #self.z_temp_humi.configure(text = '%s\u00B0C %s%%' % (self.outside_temp, self.outside_humi)) 
            self.z_humi.configure(text = '%s%%' % self.outside_humi) 

        if 'temp' in dictValue:
            self.pogoda_temp = '%2.1f\u00B0C' % float(dictValue['temp']) 
            self.st_temp.configure(text = '%s' % self.pogoda_temp) 
            
        if 'huminidity' in dictValue:
            self.pogoda_humi = '%2.0f%%' % float(dictValue['huminidity']) 
            self.st_humi.configure(text = '%s' % self.pogoda_humi)
        

        if 'ikona_pogody' in dictValue:
            #print( dictValue['ikona_pogody'])
            self.ikona_pogody.configure(text = dictValue['ikona_pogody'])

        if 'warunki_pogodowe_dzisiaj' in dictValue:
            if len(dictValue['warunki_pogodowe_dzisiaj']) == 0:   
                self.pogodaDzisiaj.configure(text = "")
            else:
                self.pogodaDzisiaj.configure(text = "Dzisiaj: %s" % ', '.join(dictValue['warunki_pogodowe_dzisiaj']))
                                                

        if 'ostrzezenia' in dictValue:
            self.t_ostrzezenia.delete('1.0', tk.END)
            self.t_ostrzezenia.configure(height=0)
            print(dictValue['ostrzezenia'])
            ltxt = 0
            hei = 0
            for o in dictValue['ostrzezenia']:
                ltxt += len(o['nazwa_zdarzenia']) + 1
                self.t_ostrzezenia.insert(tk.END, o['nazwa_zdarzenia'].upper(), "st%s" % o['stopien'])
                self.t_ostrzezenia.insert(tk.END, " ")
                ltxt += len(o['czas']) + 1
                self.t_ostrzezenia.insert(tk.END, o['czas'], "bold") 
                self.t_ostrzezenia.insert(tk.END, ". ")
                ltxt += len(o['tresc']) + 2
                self.t_ostrzezenia.insert(tk.END, o['tresc'])
                hei += int(ltxt/54)+2
                self.t_ostrzezenia.insert(tk.END, "\n")
            self.t_ostrzezenia.configure(height=hei)
            
        if 'opisPogody' not in dictValue:
            return 

        text = []
        #print(dictValue)
        text.append(dictValue['opisPogody'])

        rtxt = ''
        rain = False
        snow = False
        if 'rain_3h' in dictValue:
            rtxt = getWarningRain(dictValue['rain_3h'], dictValue['opisPogody'])
            #f0017 f001b f0019
            self.ilosc_deszczu.configure(text='%2.1f' % dictValue['rain_3h']/3)
            rain = True

        if 'rain_1h' in dictValue:
            rtxt = getWarningRain(3*dictValue['rain_1h'], dictValue['opisPogody'])
            self.ilosc_deszczu.configure(text='%2.1f' % dictValue['rain_1h'])
            rain = True

        if 'snow_3h' in dictValue:
            rtxt = getWarningSnow(dictValue['snow_3h'], dictValue['opisPogody'])
            self.ilosc_deszczu.configure(text='%2.1f' % dictValue['snow_3h']/3)
            snow = True

        if 'snow_1h' in dictValue:
            rtxt = getWarningSnow(3*dictValue['snow_1h'], dictValue['opisPogody'])
            self.ilosc_deszczu.configure(text='%2.1f' % dictValue['snow_1h']/3)
            snow = True

        if rain and snow:
            self.ikona_deszczu.configure(text='\uf017')
        elif rain:
            self.ikona_deszczu.configure(text='\uf019')
        elif snow:
            self.ikona_deszczu.configure(text='\uf01b')
        else:
            self.ikona_deszczu.configure(text='\uf095')
            self.ilosc_deszczu.configure(text='0')

        if len(rtxt):
            text.append(rtxt)

        if 'feels_like' in dictValue:
            self.feeltemp.configure(text='%2.1f' % dictValue['feels_like'])

        if 'pressure' in dictValue:
            self.st_cisnienie.configure(text='%d hPa' % dictValue['pressure'])

        if 'kierunekwiatru' in dictValue:
            kier = dictValue['kierunekwiatru']

        if 'wind_deg' in dictValue:
            self.kierunek_wiatru.configure(text=deg2Short(float(dictValue['wind_deg'])))
        
        wind_speed = 0
        if 'wind_speed' in dictValue:
            self.predkosc_wiatru.configure(text="%2.1f" % dictValue['wind_speed'])
            wind_speed = dictValue['wind_speed']

        if 'ikonawiatru' in dictValue:
            self.ikona_wiatru.configure(text=dictValue['ikonawiatru'])

    

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

        rot_secsH = 2 * math.pi * ((self.m_h % 12)*3600.0 + self.m_m * 60.0 + self.m_s) / (12.0*3600.0)
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

        if self.m_s == 0:
            self.x += self.dx
            self.y += self.dy
            if self.x + self.zwidth >= self.wwidth:
                self.x = self.wwidth - self.zwidth 
                self.dx = -1
            if self.x <= 0:
                self.dx = 1
                self.x = 0
            if self.y + self.wheight >= self.wheight:
                self.y = 1920 - self.wheight
                self.dy = -1
            if self.y <= 0:
                self.dy = 1
                self.y = 0

            self.place(x=self.x, y=self.y, anchor='nw')


        return




