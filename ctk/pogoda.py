#*-* coding:utf-8 *-*
from customtkinter import CTkLabel, CTkFont, CTkFrame

from base_plugin import LFrame
import datetime 
from urllib.request import urlopen
import json


class Pogoda(LFrame):
    def __init__(self, master, app, *args, **kwargs):
        super().__init__(0, 110, 300, 250, master, app, *args, **kwargs)

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

        self.font_wiatru = CTkFont("Weather Icons", size=24, weight="normal", slant="roman")
        self.ikonawiatru = CTkLabel(self, text=self._toBeaufortChar(self._ms2Beaufort(0)),
                                    bg_color="black",fg_color="black", text_color="white", font=self.font_wiatru,
                                    justify="left", anchor="w")

        self.kierunekWiatru = CTkLabel(self, text=self._deg2Cardinal(0),
                                    bg_color="black",fg_color="black", text_color="white", font=self.font_wiatru,
                                    justify="left", anchor="w")

        font_opiswiatru = CTkFont("Roboto Condensed Light", size=14, weight="normal", slant="roman")
        self.opiswiatru = CTkLabel(self, text=self._toDescrSilaWiatru(0),
                                    bg_color="black",fg_color="black", text_color="white", font=font_opiswiatru,
                                    justify="left", anchor="w")
                
                
        font_pogoda = CTkFont("Weather Icons", size=28, weight="bold", slant="roman")
        self.ikonapogody = CTkLabel(self, text=self.iconMap["01d"],
                                    bg_color="black",fg_color="black", text_color="white", font=font_pogoda,
                                    justify="left", anchor="w")
        

        font_opisPogody = CTkFont("Roboto Slab", size=24, weight="bold", slant="roman")
        self.opisPogody = CTkLabel(self, text="",
                                    bg_color="black",fg_color="black", text_color="white", font=font_opisPogody,
                                    justify="left", anchor="w", wraplength=270)

        
        
        self.font_deszczsnieg = CTkFont("Roboto Condensed", size=16, weight="bold", slant="roman")
        self.deszczsnieg = CTkLabel(self, text="-",
                                    bg_color="black",fg_color="black", text_color="white", font=self.font_deszczsnieg,
                                    justify="left", anchor="w")
        
        self.opisdeszczsnieg = CTkLabel(self, text="",
                                    bg_color="black",fg_color="black", text_color="white", font=self.font_deszczsnieg,
                                    justify="left", anchor="s")
        
        self.font_e_deszczsnieg = CTkFont("Roboto Condensed", size=10, weight="normal", slant="roman")
        self.etdeszczsnieg = CTkLabel(self, text="-",
                                    bg_color="black",fg_color="black", text_color="white", font=self.font_e_deszczsnieg,
                                    justify="left", anchor="s")
        
        self.w_deszczsnieg = max(self.font_deszczsnieg.measure("0"), self.font_e_deszczsnieg.measure("-")) + 5

        self.font_temperatura = CTkFont("RobotoBlack", size=36, weight="bold", slant="roman")
        self.temperatura = CTkLabel(self, text="0.0\u00B0C",
                                    bg_color="black",fg_color="black", text_color="white", font=self.font_temperatura,
                                    justify="left", anchor="w")
        
        self.font_e_feeltemp = CTkFont("Roboto Condensed", size=14, weight="normal", slant="roman")
        #self.e_feeltemp = CTkLabel(self, text="Temperatura odczuwalna",
        #                            bg_color="black",fg_color="black", text_color="white", font=self.font_e_feeltemp,
        #                            justify="left", anchor="n")
        
        self.frame = CTkFrame(master=self, width=self.wwidth, bg_color="black",fg_color="black")
        self.frame.grid_propagate(False)

        font_etWidocznosc = CTkFont("Roboto Condensed", size=14, weight="normal", slant="roman")
        self.etWidocznosc = CTkLabel(self.frame, text="Widoczność",
                                    bg_color="black",fg_color="black", text_color="white", font=font_etWidocznosc,
                                    justify="left", anchor="w")
        self.etWidocznosc.grid(row=0, column=0)

        font_widocznosc = CTkFont("Roboto Condensed", size=18, weight="bold", slant="roman")
        self.widocznosc = CTkLabel(self.frame, text=" 0 km",
                                    bg_color="black",fg_color="black", text_color="white", font=font_widocznosc,
                                    justify="left", anchor="w")
        self.widocznosc.grid(row=1, column=0)

        font_etWilgotnosc = CTkFont("Roboto Condensed", size=14, weight="normal", slant="roman")
        self.etWilgotnosc = CTkLabel(self.frame, text="Wilgotność",
                                    bg_color="black",fg_color="black", text_color="white", font=font_etWilgotnosc,
                                    justify="left", anchor="w")
        self.etWilgotnosc.grid(row=2, column=2)

        font_wilgotnosc = CTkFont("Roboto Condensed", size=18, weight="bold", slant="roman")
        self.wilgotnosc = CTkLabel(self.frame, text="-",
                                    bg_color="black",fg_color="black", text_color="white", font=font_wilgotnosc,
                                    justify="left", anchor="w")
        self.wilgotnosc.grid(row=3, column=2)

        font_etCisnienie = CTkFont("Roboto Condensed", size=14, weight="normal", slant="roman")
        self.etCisnienie = CTkLabel(self.frame, text="Ciśnienie",
                                    bg_color="black",fg_color="black", text_color="white", font=font_etCisnienie,
                                    justify="left", anchor="w")
        self.etCisnienie.grid(row=2, column=0)

        font_cisnienie = CTkFont("Roboto Condensed", size=18, weight="bold", slant="roman")
        self.cisnienie = CTkLabel(self.frame, text="-",
                                    bg_color="black",fg_color="black", text_color="white", font=font_cisnienie,
                                    justify="left", anchor="w")
        self.cisnienie.grid(row=3, column=0)


        font_etTempReal = CTkFont("Roboto Condensed", size=14, weight="normal", slant="roman")
        self.etTempReal = CTkLabel(self.frame, text="Temperatura",
                                    bg_color="black",fg_color="black", text_color="white", font=font_etTempReal,
                                    justify="left", anchor="w")
        self.etTempReal.grid(row=0, column=2)

        font_tempreal = CTkFont("Roboto Condensed", size=18, weight="bold", slant="roman")
        self.tempreal = CTkLabel(self.frame, text="-",
                                    bg_color="black",fg_color="black", text_color="white", font=font_tempreal,
                                    justify="left", anchor="w")
        self.tempreal.grid(row=1, column=2)
        
        
        font_etTempLaz = CTkFont("Roboto Condensed", size=14, weight="normal", slant="roman")
        self.etTempLaz = CTkLabel(self.frame, text="Temp. Łazienka",
                                    bg_color="black",fg_color="black", text_color="white", font=font_etTempLaz,
                                    justify="left", anchor="w")
        self.etTempLaz.grid(row=0, column=4)

        font_templaz = CTkFont("Roboto Condensed", size=18, weight="bold", slant="roman")
        self.templaz = CTkLabel(self.frame, text="-",
                                    bg_color="black",fg_color="black", text_color="white", font=font_templaz,
                                    justify="left", anchor="w")
        self.templaz.grid(row=1, column=4)
        
        space = CTkLabel(self.frame, text="",
                                    bg_color="black",fg_color="black", text_color="white", font=font_tempreal,
                                    justify="left", anchor="w")
        space2 = CTkLabel(self.frame, text="",
                                    bg_color="black",fg_color="black", text_color="white", font=font_tempreal,
                                    justify="left", anchor="w")

        font_etHumiLaz = CTkFont("Roboto Condensed", size=14, weight="normal", slant="roman")
        self.etHumiLaz = CTkLabel(self.frame, text="Wilg. Łazienka",
                                    bg_color="black",fg_color="black", text_color="white", font=font_etHumiLaz,
                                    justify="left", anchor="w")
        self.etHumiLaz.grid(row=2, column=4)

        font_humilaz = CTkFont("Roboto Condensed", size=18, weight="bold", slant="roman")
        self.humilaz = CTkLabel(self.frame, text="-",
                                    bg_color="black",fg_color="black", text_color="white", font=font_humilaz,
                                    justify="left", anchor="w")
        self.humilaz.grid(row=3, column=4)
                                          
        
        space.grid(row=0, column=1, padx=5)
        space2.grid(row=0, column=3, padx=5)

        self.setPlace(True)



        

        #self.etWidocznosc.place(x=160, y=60)
        
        
        #self.PogodaUi.tempIcon.setText("\uf055")
        #self.PogodaUi.lazienkaTempIkona.setText("\uf055")
        #self.PogodaUi.ikonaCisnienia.setText("\uf079")
        #self.PogodaUi.ikonaWilgotnosci.setText("\uf07a")
        #self.PogodaUi.lazienkaHumiIkona.setText("\uf07a")
        #self.PogodaUi.ikonaWidocznosci.setText("\uf075")

        self.temperaturaLazienka = 0.0
        self.wilgotnoscLazienka = 0
        
    def receiveNotfication(self, values):
        if  'lazienka_temp' in values:
            self.temperaturaLazienka = values['lazienka_temp']
            self.templaz.configure(text="%s\u00B0C" % self.temperaturaLazienka)
        if  'lazienka_humi' in values:
            self.wilgotnoscLazienka = values['lazienka_humi']
            self.humilaz.configure(text="%s %%" % self.wilgotnoscLazienka)

    def setPlace(self, init=False):
        if init:
            self.ikonawiatru.place(x=0, y=0)
            self.kierunekWiatru.place(x=32, y=0)
            self.ikonapogody.place(x=0, y=36)
            self.opisPogody.place(x=38, y=36)
            self.deszczsnieg.place(x=0, y=78)
            self.opisdeszczsnieg.place(x=0, y=105)
            #self.w_odcztemp = self.font_e_feeltemp.measure("Temperatura odczuwalna")
            #self.e_feeltemp.place(x=self.wwidth - self.w_odcztemp - 5, y=71)
            self.frame.place(x=0, y=140)
            self.frame.configure(height=self.wheight - 140)
        
        wtemp = self.font_temperatura.measure(self.temperatura.cget("text"))
        self.temperatura.place(x=self.wwidth - wtemp - 5, y=95)
            
        wdeszcz = self.font_deszczsnieg.measure(self.deszczsnieg.cget("text"))
        self.etdeszczsnieg.place(x=wdeszcz+3, y=78)

        pxf = self.font_wiatru.measure(self.kierunekWiatru.cget("text"))
        self.opiswiatru.place(x=25 + pxf, y=0)

        #ftxt = self.font_wiatru.measure(self.kierunekWiatru.cget("text"))
        #self.opiswiatru.place(x=35 + ftxt, y=0)

        
        
    
    def timeout(self, dt):
        hour = dt.hour
        min = dt.minute
        sec = dt.second

        #self.PogodaUi.frameTemp2.setVisible(sec >= 15)
        #self.PogodaUi.frameTempLaz.setVisible(sec < 15)

        #il_sec = hour*3600 + 60*min + sec
        #if il_sec < 30:
        #   self.lastTime = None
        #   return 

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
            
            self.ikonawiatru.configure(text=self._toBeaufortChar(self._ms2Beaufort(wind_speed)))
            vals["ikonawiatru"] = self._toBeaufortChar(self._ms2Beaufort(wind_speed))

            txtW = self._deg2Cardinal(wind_deg)
            #ftxt = self.font_wiatru.measure(txtW)
            vals["kierunekwiatru"] = txtW

            self.kierunekWiatru.configure(text=txtW)
            self.opiswiatru.configure(text=self._toDescrSilaWiatru(wind_speed))
            vals['opiswiatru'] = self.B2Description(self._ms2Beaufort(wind_speed))
            #self.opiswiatru.place(x=28 + ftxt, y=0)

            temp = data_json["main"]["temp"]
            feels_like = data_json["main"]["feels_like"]
            mqtt_vals["temp"] = temp
            mqtt_vals["feels_like"] = feels_like
            vals["temp"] = temp
            vals["feels_like"] = feels_like

            self.temperatura.configure(text="%.1f\u00B0C" % feels_like)
            self.tempreal.configure(text="%.1f\u00B0C" % temp)
            #self.PogodaUi.temperaturaOdczuwalna.setText("%.1f\u00B0C" % feels_like)

            pressure = data_json["main"]["pressure"]
            huminidity = data_json["main"]["humidity"]
            mqtt_vals["pressure"] = pressure
            mqtt_vals["huminidity"] = huminidity

            vals["pressure"] = pressure
            vals["huminidity"] = huminidity

            self.wilgotnosc.configure(text="%.0f%%" % huminidity)
            self.cisnienie.configure(text="%.0f hPa" % pressure)

            #weather_main = data_json["weather"][0]["main"]
            weather_descr = data_json["weather"][0]["description"]
            weather_icon = data_json["weather"][0]["icon"]
            self.ikonapogody.configure(text=self.iconMap[weather_icon])
            self.opisPogody.configure(text=weather_descr)
            vals['ikonapogody']= self.iconMap[weather_icon]
            vals['opisPogody']= weather_descr
            vals['widocznosc']= data_json["visibility"]
            self.widocznosc.configure(text="%d m" % data_json["visibility"])
            #self.clouds.setText("%d%%" % data_json["clouds"]["all"])
            text_val = ""
            text_unit = ""
            text_opis = ""
            
            if "snow" in data_json:
                if "1h" in data_json["snow"]:
                    text_val = "%s" % data_json["snow"]["1h"]
                    text_unit = "mm/h"
                    text_opis = self._getSnowName(float(text_val))
                    mqtt_vals["snow_1h"] = data_json["snow"]["1h"]
                    vals["snow_1h"] = data_json["snow"]["1h"]
                elif "3h" in data_json["snow"]:
                    text_val = "%s" % data_json["snow"]["3h"]
                    text_unit = "mm/3h"
                    text_opis = self._getSnowName(float(text_val)/3)
                    mqtt_vals["snow_3h"] = data_json["snow"]["3h"]
                    vals["snow_3h"] = data_json["snow"]["3h"]
            elif "rain" in data_json:
                if "1h" in data_json["rain"]:
                    text_val = "%s" % data_json["rain"]["1h"]
                    text_unit = "mm/h"
                    text_opis = self._getRainName(float(text_val))
                    mqtt_vals["rain_1h"] = data_json["rain"]["1h"]
                    vals["rain_1h"] = data_json["rain"]["1h"]
                elif "3h" in data_json["rain"]:
                    text_val = "%s" % data_json["rain"]["3h"]
                    text_unit = "mm/h"
                    text_opis = self._getRainName(float(text_val)/3)
                    mqtt_vals["rain_3h"] = data_json["rain"]["3h"]
                    vals["rain_3h"] = data_json["rain"]["3h"]
            elif "clouds" in data_json:
                text_val = "%s" % data_json["clouds"]["all"]
                text_unit = "%"
                mqtt_vals["clouds"] = data_json["clouds"]["all"]
                vals["clouds"] = data_json["clouds"]["all"]
            else:
                self.deszczsnieg.configure(text="")
                self.etdeszczsnieg.configure(text="")
                pass
            vals['deszczsnieg'] = text_val
            vals['etdeszczsnieg'] = text_unit
            vals['opisdeszczsnieg'] = text_opis
            self.deszczsnieg.configure(text=text_val)
            self.etdeszczsnieg.configure(text=text_unit)
            self.opisdeszczsnieg.configure(text=text_opis)
            #self.w_deszczsnieg = max(self.font_deszczsnieg.measure(text_val), 
            #                         self.font_e_deszczsnieg.measure(text_unit))

            #self.e_feeltemp.place(x=self.w_deszczsnieg+10, y=75)
            #self.temperatura.place(x=self.w_deszczsnieg+100, y=75)
            self.setPlace()
            self.frame.update()

            vals["sunrise"] = self.sunrise.time()
            vals["sunset"] = self.sunset.time() 
            #vals['minimum-temperature'] = data_json['main']['temp_min']
            #vals['maximum-temperature'] = data_json['main']['temp_max']
            #mqtt_vals['minimum-temperature'] = data_json['main']['temp_min']
            #mqtt_vals['maximum-temperature'] = data_json['main']['temp_max']
            #print(vals)
            self.sendNotification(vals)
            #self.sendMqtt("lustro/pogoda", mqtt_vals)

        #except:
        #    pass


    def _ms2Beaufort(self, ms):
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

    def _deg2Cardinal(self, deg):
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

    def _toBeaufortChar(self, b):
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
    
    def B2Description(self, b):
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

    def _toDescrSilaWiatru(self, ms):
        b = self._ms2Beaufort(ms)
        ret = "%.1f" % ms
        ret += "m/s (%s)" % self.B2Description(b)
        return ret

    def _isDayTime(self, h, m):
        now = datetime.datetime.now()
        act = datetime.datetime(now.year, now.month, now.day, h, m, 0)
        if self.sunrise is None or self.sunset is None:
            return False
        
        if act > self.sunrise and act < self.sunset:
            return True
        return False
    
    def _getRainName(self, w:float):
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
        
    def _getSnowName(self, w:float):
        if w == 0:
            return ""
        elif w <= 1:
            return "śnieg słaby"
        elif w <= 4:
            return "śnieg umiarkowany"
        else:
            return "śnieg silny"

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

