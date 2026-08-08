from customtkinter import CTkLabel, CTkFont, CTkFrame

from base_plugin import LSimpleFrame
import datetime 
from urllib.request import urlopen
import json

def ms2Beaufort(ms):
    kmh = ms * 60 * 60 / 1000
    speeds = [1, 7, 12, 20, 30, 40, 51, 63, 76, 88, 103, 117]
    if kmh > 117:
        return 12

    if kmh < speeds[0]:
        return 0

    index = 0
    while kmh > speeds[index]:
        index += 1
    return index-1

def deg2Cardinal(deg):
    if deg>11.25 and deg<=33.75 : 
        return "NNE"
    elif deg > 33.75 and deg <= 56.25: 
        return "NE"
    elif deg > 56.25 and deg <= 78.75 :
        return "ENE"
    elif deg > 78.75 and deg <= 101.25 :
        return "E"
    elif deg > 101.25 and deg <= 123.75 :
        return "ESE"
    elif deg > 123.75 and deg <= 146.25 :
        return "SE"
    elif deg > 146.25 and deg <= 168.75 :
        return "SSE"
    elif deg > 168.75 and deg <= 191.25 :
        return "S"
    elif deg > 191.25 and deg <= 213.75 :
        return "SSW"
    elif deg > 213.75 and deg <= 236.25 :
        return "SW"
    elif deg > 236.25 and deg <= 258.75 :
        return "WSW"
    elif deg > 258.75 and deg <= 281.25 :
        return "W"
    elif deg > 281.25 and deg <= 303.75 :
        return "WNW"
    elif deg > 303.75 and deg <= 326.25 :
        return "NW"
    elif deg > 326.25 and deg <= 348.75 :
        return "NNW"
    else :
        return "N"

def deg2Short(deg):
    if deg>11.25 and deg<=33.75 : 
        return "\uf057" # "\uf05a" #NNE
    elif deg > 33.75 and deg <= 56.25: 
        return "\uf057" #"\uf05a" #NE
    elif deg > 56.25 and deg <= 78.75 :
        return "\uf057" #"\uf05a" #ENE
    elif deg > 78.75 and deg <= 101.25 :
        return "\uf059" #E
    elif deg > 101.25 and deg <= 123.75 :
        return "\uf088" #"\uf05d" #ESE
    elif deg > 123.75 and deg <= 146.25 :
        return "\uf088" #"\uf05d" #SE
    elif deg > 146.25 and deg <= 168.75 :
        return "\uf088" #"\uf05d" #SSE
    elif deg > 168.75 and deg <= 191.25 :
        return "\uf044" #"\uf060" #S
    elif deg > 191.25 and deg <= 213.75 :
        return "\uf043" #"\uf05e" #SSW
    elif deg > 213.75 and deg <= 236.25 :
        return "\uf043" #"\uf05e" #SW
    elif deg > 236.25 and deg <= 258.75 :
        return "\uf043" #"\uf05e" #WSW
    elif deg > 258.75 and deg <= 281.25 :
        return "\uf048" #"\uf05b" #W
    elif deg > 281.25 and deg <= 303.75 :
        return "\uf087" #"\uf05b" #WNW
    elif deg > 303.75 and deg <= 326.25 :
        return "\uf087" #"\uf05b" #NW
    elif deg > 326.25 and deg <= 348.75 :
        return "\uf087" #"\uf05b" #NNW
    else :
        return "\uf058" #"\uf05c" #N

def toBeaufortChar(b):
    if b == 0: return "\uF0B7"
    elif b == 1: return "\uF0B8"
    elif b == 2: return "\uF0B9"
    elif b == 3: return "\uF0BA"
    elif b == 4: return "\uF0BB"
    elif b == 5: return "\uF0BC"
    elif b == 6: return "\uF0BD"
    elif b == 7: return "\uF0BE"
    elif b == 8: return "\uF0BF"
    elif b == 9: return "\uF0C0"
    elif b == 10: return "\uF0C1"
    elif b == 11: return "\uF0C2"
    elif b == 12: return "\uF0C3"
    else: return "\uF050"

def B2Description(b):
    if b == 0: return "Cisza"
    elif b == 1: return "Powiew"
    elif b == 2: return "Słaby wiatr"
    elif b == 3: return "Łagodny wiatr"
    elif b == 4: return "Umiarkowany wiatr"
    elif b == 5: return "Dość silny wiatr"
    elif b == 6: return "Silny wiatr"
    elif b == 7: return "Bardzo silny wiatr"
    elif b == 8: return "Wicher"
    elif b == 9: return "Silny sztorm"
    elif b == 10: return "Bardzo silny sztorm"
    elif b == 11: return "Gwałtowny sztorm"
    elif b == 12: return "Huragan"
    return ""

def B2Description2(b):
    if b == 0: return "brak wiatru"
    elif b == 1: return "powiewy wiatru"
    elif b == 2: return "słaby wiatr"
    elif b == 3: return "łagodny wiatr"
    elif b == 4: return "umiarkowany wiatr"
    elif b == 5: return "dość silny wiatr"
    elif b == 6: return "silny wiatr"
    elif b == 7: return "bardzo silny wiatr"
    elif b == 8: return "wicher"
    elif b == 9: return "silny sztorm"
    elif b == 10: return "bardzo silny sztorm"
    elif b == 11: return "gwałtowny sztorm"
    elif b == 12: return "huragan"
    return ""

def toDescrSilaWiatru(ms):
    b = ms2Beaufort(ms)
    ret = "%.1f" % ms
    ret += "m/s (%s)" % B2Description(b)
    return ret

def toDescrSilaWiatru2(ms):
    return B2Description2(ms2Beaufort(ms))

"""
def _isDayTime(self, h, m):
    now = datetime.datetime.now()
    act = datetime.datetime(now.year, now.month, now.day, h, m, 0)
    if self.sunrise is None or self.sunset is None:
        return False
    
    if act > self.sunrise and act < self.sunset:
        return True
    return False
"""

def getRainName(w:float):
    if w == 0:
        return ""
    elif w <= 0.1:
        return "mżawka"
    elif w <= 2.5:
        return "deszcz"
    elif w <= 7.5:
        return "duży deszcz"
    elif w <= 20:
        return "ulewa"
    else:
        return "nawałnica"
    
def getSnowName(w:float):
    if w == 0:
        return ""
    elif w <= 1:
        return "śnieg słaby"
    elif w <= 4:
        return "śnieg umiarkowany"
    else:
        return "śnieg silny"
class TempHumi:
    def __init__(self, frameTiH, font, title:str, key_th:str):

        self.key_temp = '%s_temp' % key_th
        self.key_humi = '%s_humi' % key_th
        self.ltitle = CTkLabel(frameTiH, text=title, bg_color="black", fg_color="black", text_color="white", 
                              font=font, justify="left", anchor="w")

        self.ltemp = CTkLabel(frameTiH, text="-", bg_color="black", fg_color="black", text_color="white", 
                              font=font, justify="right", anchor="e")

        self.lhumi = CTkLabel(frameTiH, text="-", bg_color="black", fg_color="black", text_color="white", 
                              font=font, justify="right", anchor="e")

        self.lastUpdate = 0

        self.temp = None
        self.humi = None

    def grid(self, row:int, column:int, padx:int, pady:int):
        self.ltitle.grid(row=row, column=column, padx=padx, pady=pady)
        self.ltemp.grid(row=row, column=column+1, padx=padx, pady=pady)
        self.lhumi.grid(row=row, column=column+2, padx=padx, pady=pady)

    def timeout(self):
        self.lastUpdate -= 1
        if self.lastUpdate < 0:
            self.temp = None
            self.humi = None
            self.update()

    def update(self):
        if self.temp is None:
            self.ltemp.configure(text='-')                
        else:
            self.ltemp.configure(text='%2.1f' % self.temp)

        if self.humi is None:
            self.lhumi.configure(text='-')                
        else:
            self.lhumi.configure(text='%2.0f' % self.humi)

    def check_and_set(self, data:dict):
        if self.key_temp in data or self.key_humi in data:
            self.lastUpdate = 3600
            if self.key_temp in data:
                self.temp = float(data[self.key_temp])
            if self.key_humi in data:
                self.humi = float(data[self.key_humi])
            self.update()
class TempAll:
    def __init__(self, frameTiH, font):
        self.lst = []

        self.lst.append(TempHumi(frameTiH, font, 'Laz.', 'lazienka'))
        self.lst.append(TempHumi(frameTiH, font, 'Kuch.', 'kuchnia'))
        self.lst.append(TempHumi(frameTiH, font, 'WC', 'wc'))
        self.lst.append(TempHumi(frameTiH, font, 'Hol', 'hol'))
        self.lst.append(TempHumi(frameTiH, font, 'Sal.', 'salon_2'))
        self.lst.append(TempHumi(frameTiH, font, 'Syp.', 'sypialnia'))
        self.lst.append(TempHumi(frameTiH, font, 'Prac.', 'pracownia'))
        self.lst.append(TempHumi(frameTiH, font, 'Dziec.', 'dzieci'))

    def grid(self, padx:int, pady:int):
        for w in self.lst:
            if self.lst.index(w) < 4:
                w.grid(row=self.lst.index(w)+1, column=0, padx=padx, pady=pady)
            else:
                w.grid(row=self.lst.index(w)-3, column=4, padx=padx, pady=pady)
                

    def timeout(self):
        for w in self.lst:
            w.timeout()

    def check_and_set(self, data:dict):
        for w in self.lst:
            w.check_and_set(data)



class TiHOutSide:
    def __init__(self, ltemp:CTkLabel, lhumi:CTkLabel, key1:str, key2:str):
        self.lastUpdate1 = 0
        self.lastUpdate2 = 0

        self.temp1 = 0
        self.humi2 = 0
        self.temp2 = 0
        self.key_temp1 = '%s_temp' % key1
        self.key_humi2 = '%s_humi' % key2
        self.key_temp2 = '%s_temp' % key2
        #outside_1_temp
        
        #outside_2_temp
        #outside_2_humi

        self.ltemp = ltemp
        self.lhumi = lhumi

    def timeout(self):
        self.lastUpdate1 -= 1
        self.lastUpdate2 -= 1
        if self.lastUpdate1 < 0:
            self.temp1 = None
            self.update()
        if self.lastUpdate2 < 0:
            self.temp2 = None
            self.humi2 = None
            self.update()

    def update(self):
        if self.temp1 is None:
            self.ltemp.configure(text='-')                
        else:
            self.ltemp.configure(text='%2.1f\u00B0C' % self.temp1)

        if self.humi2 is None:
            self.lhumi.configure(text='-')                
        else:
            self.lhumi.configure(text='%2.0f%%' % self.humi2)

    def check_and_set(self, data:dict):
        if self.key_temp2 in data or self.key_humi2 in data:
            self.lastUpdate2 = 3600
            #if self.key_temp in data:
            #    self.temp = float(data[self.key_temp])
            if self.key_humi2 in data:
                self.humi2 = float(data[self.key_humi2])
            self.update()

        if self.key_temp1 in data:
            self.lastUpdate1 = 3600
            if self.key_temp1 in data:
                self.temp1 = float(data[self.key_temp1])
            
            self.update()

class Pogoda(LSimpleFrame):
    _wwidth = 400
    def __init__(self, master, app, *args, **kwargs):
        #super().__init__(0, 0, 300, 250, master, app, *args, **kwargs)
        super().__init__(master, app, *args, **kwargs)

        self.configure(width=self._wwidth)

        #QNetworkAccessManager netMng
        self.url = "https://api.openweathermap.org/data/2.5/weather?appid=b176485875db690244cb8acf93637572&id=7532279&lang=pl&units=metric"
        self.sunrise = None
        self.sunset = None
        self.citiname = ""
        self.pog_h = 0
        self.pog_m = 0
        self.lastTime = None
        self.citiname = "Nieznane"

        self.iconMap = {}
        self.iconMap["01d"]="\uf00d" #"wi-day-sunny",
        self.iconMap["02d"]="\uf002" #"wi-day-cloudy",
        self.iconMap["03d"]="\uf013" #"wi-cloudy",
        self.iconMap["04d"]="\uf012" #"wi-cloudy-windy",
        self.iconMap["09d"]="\uf01a" #"wi-showers",
        self.iconMap["10d"]="\uf019" #"wi-rain",
        self.iconMap["11d"]="\uf01e" #"wi-thunderstorm",
        self.iconMap["13d"]="\uf01b" #"wi-snow",
        self.iconMap["50d"]="\uf014" #"wi-fog",
        self.iconMap["01n"]="\uf02e" #"wi-night-clear",
        self.iconMap["02n"]="\uf031" #"wi-night-cloudy",
        self.iconMap["03n"]="\uf031" #"wi-night-cloudy",
        self.iconMap["04n"]="\uf031" #"wi-night-cloudy",
        self.iconMap["09n"]="\uf037" #"wi-night-showers",
        self.iconMap["10n"]="\uf036" #"wi-night-rain",
        self.iconMap["11n"]="\uf03b" #"wi-night-thunderstorm",
        self.iconMap["13n"]="\uf038" #"wi-night-snow",
        self.iconMap["50n"]="\uf023" #"wi-night-alt-cloudy-windy"
        self.configure(width=self._wwidth)

        #Weather Icons
        fwebicons = CTkFont("Weather Icons", size=48, weight="normal", slant="roman")
        fminiwebicons = CTkFont("Weather Icons", size=32, weight="normal", slant="roman")
        fhead_tih = CTkFont("Weather Icons", size=20, weight="normal", slant="roman")
        #self.font_wiatru = CTkFont("Weather Icons", size=32, weight="normal", slant="roman")

        ffeel_temperatura = CTkFont("Roboto Slab Regular", size=48, weight="bold", slant="roman")

        fval_temp_rain_wind = CTkFont("Roboto Regular", size=20, weight="normal", slant="roman")
        fopisPogody = CTkFont("Roboto Slab", size=32, weight="bold", slant="roman")

        fEtWidocznosc = CTkFont("Roboto Condensed", size=14, weight="normal", slant="roman")
        
        f_widocz_cisnienie = CTkFont("Roboto Condensed", size=18, weight="bold", slant="roman")
        f_tih_all = CTkFont("Roboto Condensed", size=24, weight="normal", slant="roman")

        self.top_banner(fminiwebicons, fval_temp_rain_wind, ffeel_temperatura, fwebicons)
        self.opis_pogoda_banner(fopisPogody)
        self.widocznosc_cisnienie_banner(fEtWidocznosc, f_widocz_cisnienie)
        self.outside_temp_humi_banner(fEtWidocznosc, f_widocz_cisnienie)
        self.tih_banner(fhead_tih, f_tih_all)

    def top_banner(self, fminiwebicons, fval_temp_rain_wind, ffeel_temperatura, fwebicons):

        self.topframe = CTkFrame(master=self, bg_color="black",fg_color="black")
        self.topframe.pack(side='top', fill='x', expand=True) 

        self.ikonatemperatury = CTkLabel(self.topframe, text="\uf044\uf053",
                                            bg_color="black",fg_color="black", text_color="white",
                                            font=fminiwebicons, justify="left", anchor="w")
        self.ikonatemperatury.grid(row=0, column=0, padx=2, pady=0)

        self.realtemperatura = CTkLabel(self.topframe, text="-",
                                                    bg_color="black",fg_color="black", text_color="white",
                                                    font=fval_temp_rain_wind, justify="left", anchor="w")
        self.realtemperatura.grid(row=1, column=0, padx=2, pady=0)

        self.feeltemperatura = CTkLabel(self.topframe, text="-",
                                            bg_color="black",fg_color="black", text_color="white",
                                            font=ffeel_temperatura, justify="left", anchor="w")
        self.feeltemperatura.grid(row=0, column=1, rowspan=2, padx=2, pady=0)

        self.ikonapogody = CTkLabel(self.topframe, text=self.iconMap["10n"],
                            bg_color="black", fg_color="black", text_color="white", font=fwebicons,
                            justify="left", anchor="w")
        self.ikonapogody.grid(row=0, column=2, padx=5, pady=0)
        
        self.wielkoscDeszczu = CTkLabel(self.topframe, text='0 mm',
                                            bg_color="black",fg_color="black", text_color="white", font=fval_temp_rain_wind,
                                            justify="left", anchor="w")
        self.wielkoscDeszczu.grid(row=1, column=2, padx=2, pady=0)

        self.ikonawiatru = CTkLabel(self.topframe, text=toBeaufortChar(ms2Beaufort(0)),
                                    bg_color="black",fg_color="black", text_color="white", font=fwebicons,
                                    justify="right", anchor="se")
        self.ikonawiatru.grid(row=0, column=3, padx=2, sticky='s')

        self.kierunekWiatru = CTkLabel(self.topframe, text=deg2Short(0),
                                    bg_color="black",fg_color="black", text_color="white", font=fwebicons,
                                    justify="left", anchor="sw")
        self.kierunekWiatru.grid(row=0, column=4, padx=2, sticky='s')

    
        self.predkoscWiatru = CTkLabel(self.topframe, text='0',
                                            bg_color="black",fg_color="black", text_color="white", font=fval_temp_rain_wind,
                                            justify="left", anchor="nw")
        self.predkoscWiatru.grid(row=1, column=3, columnspan=2, sticky='n')

        self.ikonaWilgotnosci = CTkLabel(self.topframe, text="\uf078",
                                    bg_color="black",fg_color="black", text_color="white", font=fminiwebicons,
                                    justify="right", anchor="se")
        self.ikonaWilgotnosci.grid(row=0, column=5, padx=5, sticky='s')

    
        self.wilgotnosc = CTkLabel(self.topframe, text='0%%',
                                            bg_color="black",fg_color="black", text_color="white", font=fval_temp_rain_wind,
                                            justify="right", anchor="ne")
        self.wilgotnosc.grid(row=1, column=5, padx=5, sticky='n')

    def opis_pogoda_banner(self, fopisPogody):
        
        self.opisPogody = CTkLabel(self, text="",
                                bg_color="black",fg_color="black", text_color="white", font=fopisPogody,
                                justify="left", anchor="w", wraplength=self._wwidth - 10)
        self.opisPogody.pack(side='top', fill='x', expand=True) 

        #self.opisdeszczusniegu = CTkLabel(self, text="Brak deszczu i śniegu",
        #                        bg_color="black",fg_color="black", text_color="silver", font=font_opisPogody,
        #                        justify="left", anchor="w", wraplength=self._wwidth - 10)
        #self.opisdeszczusniegu.pack(side='top', fill='x', expand=True) 

        
        #self.opiswiatru = CTkLabel(self, text=toDescrSilaWiatru(0),
        #                            bg_color="black",fg_color="black", text_color="white", font=font_opisPogody,
        #                            justify="left", anchor="w", wraplength=self._wwidth - 10)
        #self.opiswiatru.pack(side='top', fill='x', expand=True) 

    def widocznosc_cisnienie_banner(self, fEtWidocznosc, f_widocz_cisnienie):
        self.frame = CTkFrame(master=self, bg_color="black",fg_color="black")
        self.frame.pack(side='top', fill='x', expand=True) 

        
        etWidocznosc = CTkLabel(self.frame, text="Widoczność: ",
                                    bg_color="black",fg_color="black", text_color="white", font=fEtWidocznosc,
                                            justify="left", anchor="w")
        etWidocznosc.pack(side='left')

        self.widocznosc = CTkLabel(self.frame, text=" 0 km",
                                    bg_color="black",fg_color="black", text_color="white", font=f_widocz_cisnienie,
                                    justify="left", anchor="w")
        self.widocznosc.pack(side='left')

        self.cisnienie = CTkLabel(self.frame, text="-",
                                    bg_color="black",fg_color="black", text_color="white", font=f_widocz_cisnienie,
                                    justify="left", anchor="w")
        self.cisnienie.pack(side='right')

        etCisnienie = CTkLabel(self.frame, text="Ciśnienie :",
                                    bg_color="black",fg_color="black", text_color="white", font=fEtWidocznosc,
                                    justify="left", anchor="w")
        etCisnienie.pack(side='right')

    def outside_temp_humi_banner(self, fEtWidocznosc, f_widocz_cisnienie):
        
        self.frame2 = CTkFrame(master=self, bg_color="black",fg_color="black")
        self.frame2.pack(side='top', fill='x', expand=True) 

        etTempOutSide = CTkLabel(self.frame2, text="Temperatura: ",
                                    bg_color="black",fg_color="black", text_color="white", font=fEtWidocznosc,
                                    justify="left", anchor="w")
        etTempOutSide.pack(side='left')

        self.tempOutSide = CTkLabel(self.frame2, text="-",
                                    bg_color="black",fg_color="black", text_color="white", font=f_widocz_cisnienie,
                                    justify="left", anchor="w")
        self.tempOutSide.pack(side='left')

        self.humiOutSide = CTkLabel(self.frame2, text="-",
                                    bg_color="black",fg_color="black", text_color="white", font=f_widocz_cisnienie,
                                    justify="left", anchor="w")
        self.humiOutSide.pack(side='right')

        etWilgotnosc = CTkLabel(self.frame2, text="Wilgotność :",
                                    bg_color="black",fg_color="black", text_color="white", font=fEtWidocznosc,
                                    justify="left", anchor="w")
        etWilgotnosc.pack(side='right')

        self.val_tempOutSide = TiHOutSide(self.tempOutSide, self.humiOutSide, 'outside_1', 'outside_2')

    def tih_banner(self, fhead_tih, f_tih_all):        
        self.frameTiH = CTkFrame(master=self, width=self._wwidth, 
                                 bg_color="black", fg_color="black")
        self.frameTiH.pack(side='left', fill='x', expand=True)

        

        self.etTemperatura1 = CTkLabel(self.frameTiH, text="\uf055\uf03c",
                                       bg_color="black",fg_color="black", text_color="white", font=fhead_tih, 
                                       justify="center", anchor="w")
        self.etTemperatura1.grid(row=0, column=1, padx=5, pady=5)

        self.etWilgotnosc1 = CTkLabel(self.frameTiH, text="\uf07a",
                                               bg_color="black",fg_color="black", text_color="white", font=fhead_tih, 
                                               justify="center", anchor="w")
        self.etWilgotnosc1.grid(row=0, column=2, padx=5, pady=5)

        self.etTemperatura2 = CTkLabel(self.frameTiH, text="\uf055\uf03c",
                                               bg_color="black",fg_color="black", text_color="white", font=fhead_tih, 
                                               justify="center", anchor="w")
        self.etTemperatura2.grid(row=0, column=5, padx=5, pady=5)
        
        self.etWilgotnosc2 = CTkLabel(self.frameTiH, text="\uf07a",
                                                       bg_color="black",fg_color="black", text_color="white", font=fhead_tih, 
                                                       justify="center", anchor="w")
        self.etWilgotnosc2.grid(row=0, column=6, padx=5, pady=5)

       
        self.temps = TempAll(self.frameTiH, f_tih_all)
        self.temps.grid(5, 0)
        
        
    def receiveNotfication(self, values):
        print("ok, receiveNotfication.pogoda", values)
        self.temps.check_and_set(values)        

        self.val_tempOutSide.check_and_set(values)

    def timeout(self, dt):
        hour = dt.hour
        min = dt.minute
        sec = dt.second

        self.temps.timeout()
        self.val_tempOutSide.timeout()

        if self.lastTime is None:
            self.lastTime = dt
        else:
            if dt - self.lastTime < datetime.timedelta(seconds=600):
                return

        self.lastTime = dt

        mqtt_vals = {}
        #try :
        if 1:

            response = urlopen(self.url)
            data_json = json.loads(response.read().decode('utf-8'))
            print(data_json)

            self.citiname = data_json["name"]
            utc = data_json["dt"]
            dtw = datetime.datetime.fromtimestamp(utc).time()
            
            self.pog_h = dtw.hour
            self.pog_m = dtw.minute
            vals = {}
            mqtt_vals["time"] = "%02d:%02d" % (self.pog_h, self.pog_m)
            vals["time"] = "%02d:%02d" % (self.pog_h, self.pog_m)


            self.sunrise = datetime.datetime.fromtimestamp(data_json["sys"]["sunrise"])
            self.sunset = datetime.datetime.fromtimestamp(data_json["sys"]["sunset"])
            mqtt_vals["sunrise"] = self.sunrise.strftime("%H:%M:%S")
            mqtt_vals["sunset"] = self.sunset.strftime("%H:%M:%S")

            #print(f"sunrise = {self.sunrise} sunset = {self.sunset}")

            wind_speed = data_json["wind"]["speed"]
            #[1, 7, 12, 20, 30, 40, 51, 63, 76, 88, 103, 117]
            #wind_speed = 40
            wind_deg = data_json["wind"]["deg"]
            mqtt_vals["wind_speed"] = wind_speed
            vals["wind_speed"] = wind_speed
            mqtt_vals["wind_deg"] = wind_deg
            vals["wind_deg"] = wind_deg
            #print(f"wind_speed = {wind_speed}")
            
            self.ikonawiatru.configure(text=toBeaufortChar(ms2Beaufort(wind_speed)))
            vals["ikonawiatru"] = toBeaufortChar(ms2Beaufort(wind_speed))

            txtW = deg2Cardinal(wind_deg)
            #ftxt = self.font_wiatru.measure(txtW)
            vals["kierunekwiatru"] = txtW
            self.predkoscWiatru.configure(text="%2.1f m/s" % wind_speed)

            self.kierunekWiatru.configure(text=deg2Short(wind_deg))
            #self.opiswiatru.configure(text=toDescrSilaWiatru(wind_speed) + ' ' + txtW)
            vals['opiswiatru'] = B2Description(ms2Beaufort(wind_speed))
            #self.opiswiatru.place(x=28 + ftxt, y=0)

            temp = data_json["main"]["temp"]
            feels_like = data_json["main"]["feels_like"]
            mqtt_vals["temp"] = temp
            mqtt_vals["feels_like"] = feels_like
            vals["temp"] = temp
            vals["feels_like"] = feels_like

            if feels_like > temp:
                self.ikonatemperatury.configure(text="\uf058\uf053\uf03c")
            elif feels_like < temp:
                self.ikonatemperatury.configure(text="\uf044\uf053\uf03c")
            else:
                self.ikonatemperatury.configure(text="\uf053\uf03c")

            self.feeltemperatura.configure(text="%.1f" % feels_like)

            weather_icon = data_json["weather"][0]["icon"]
            print(weather_icon)
            print(ord(self.iconMap[weather_icon]))
            self.ikonapogody.configure(text=self.iconMap[weather_icon])

            snowrain_val = 0

            text_unit = ''
            if "snow" in data_json:
                if "1h" in data_json["snow"]:
                    snowrain_val = float(data_json["snow"]["1h"])
                    text_val = "%s" % data_json["rain"]["1h"]
                    text_unit = "mm/1h"
                    text_opis = getSnowName(float(text_val))
                    mqtt_vals["snow_1h"] = data_json["snow"]["1h"]
                    vals["snow_1h"] = data_json["snow"]["1h"]
                elif "3h" in data_json["snow"]:
                    snowrain_val = float(data_json["snow"]["3h"])
                    text_val = "%s" % data_json["rain"]["3h"]
                    text_unit = "mm/3h"
                    text_opis = getSnowName(float(text_val)/3)
                    mqtt_vals["snow_3h"] = data_json["snow"]["3h"]
                    vals["snow_3h"] = data_json["snow"]["3h"]
                else:
                    text_val = ""
                    text_unit = ""
                    text_opis = ""
            elif "rain" in data_json:
                if "1h" in data_json["rain"]:
                    text_val = "%s" % data_json["rain"]["1h"]
                    snowrain_val = float(data_json["rain"]["1h"])
                    text_unit = "mm/h"
                    text_opis = getRainName(float(text_val))
                    mqtt_vals["rain_1h"] = data_json["rain"]["1h"]
                    vals["rain_1h"] = data_json["rain"]["1h"]
                elif "3h" in data_json["rain"]:
                    text_val = "%s" % data_json["rain"]["3h"]
                    snowrain_val = float(data_json["rain"]["3h"])
                    text_unit = "mm/3h"
                    text_opis = getRainName(float(text_val)/3)
                    mqtt_vals["rain_3h"] = data_json["rain"]["3h"]
                    vals["rain_3h"] = data_json["rain"]["3h"]
                else:
                    text_val = ""
                    text_unit = ""
                    text_opis = ""
            else:
                text_val = ""
                text_unit = ""
                text_opis = ""      
                    
            vals['deszczsnieg'] = text_val
            vals['etdeszczsnieg'] = text_unit
            vals['opisdeszczsnieg'] = text_opis

            if snowrain_val > 0:
                #self.opisdeszczusniegu.configure(text=text_opis+ " ( " + text_val + " " + text_unit + " )", text_color="white") 
                self.wielkoscDeszczu.configure(text="%s %s" % (text_val, text_unit), text_color="white")
            else:
                #self.opisdeszczusniegu.configure(text="brak deszczu i śniegu", text_color="gray") 
                self.wielkoscDeszczu.configure(text="0 mm", text_color="gray")
                text_opis = "brak opadów"
                    
            weather_descr = data_json["weather"][0]["description"]
            self.opisPogody.configure(text=weather_descr + ', ' + text_opis + ', ' + toDescrSilaWiatru2(wind_speed))

            pressure = data_json["main"]["pressure"]
            huminidity = data_json["main"]["humidity"]
            mqtt_vals["pressure"] = pressure
            mqtt_vals["huminidity"] = huminidity

            vals["pressure"] = pressure
            vals["huminidity"] = huminidity

            vals["pressure"] = pressure
            self.cisnienie.configure(text="%.0f hPa" % pressure)

            vals['widocznosc']= data_json["visibility"]
            self.widocznosc.configure(text="%d m" % data_json["visibility"])

            #self.realtemperatura.configure(text="%.1f\u00B0C" % temp)
            self.realtemperatura.configure(text="%.1f" % temp)
            self.wilgotnosc.configure(text="%.0f%%" % huminidity)

        
            vals["sunrise"] = self.sunrise.time()
            vals["sunset"] = self.sunset.time() 

            self.sendNotification(vals)
            self.sendMqtt("lustro/pogoda", mqtt_vals)

        #except:
        #    pass
        

    

    def __getTimeRemaing(self, h, m):
        if m < 0:
            h = h - 1
            m += 60
        
        if h < 0:
            h += 24

        if h == 0 and m < 30:
            return "%d min" % m
        else:
            hal = 1.0*h + m/60.0
            h10 = int(10*hal + 5)
            return "%d.%d godz" % (int(h10/10), int(h10) % 10)

