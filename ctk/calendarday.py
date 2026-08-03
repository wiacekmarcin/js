from customtkinter import CTkLabel, CTkFont, CTkScrollableFrame, CTkTextbox

import datetime
import urllib3
from bs4  import BeautifulSoup

from base_plugin import LFrame, LSimpleFrame
from customtkinter import CTk, CTkFrame
from base_app import LustroApp
#class CalendarDay(LFrame):
class CalendarDay(LSimpleFrame):
    _wwidth = 300
    def __init__(self, master:CTkFrame, app, *args, **kwargs):
        #super().__init__(320, 5, 500, 600, master, app, *args, **kwargs)
        super().__init__(master, app, *args, **kwargs)
        
        #self.configure(fg_color = "lightgray")
        self.dayCalc = None
        self.days = ["Poniedziałek",
                "Wtorek",
                "Środa",
                "Czwartek",
                "Piątek",
                "Sobota",
                "Niedziela"]
        
        self.monts = ["", "styczeń",
                   "luty",
                   "marzec",
                   "kwiecień",
                   "maj",
                   "czerwiec",
                   "lipiec",
                   "sierpień",
                   "wrzesień",
                   "październik",
                   "listopad",
                   "grudzień"]
        
        font_mr = CTkFont("Roboto Condensed", size=24, weight="bold", slant="roman")
        self.miesiac_rok = CTkLabel(self, text="miesiąć", fg_color="black", bg_color="black", text_color="white", font=font_mr)
        self.miesiac_rok.pack()
        
        font_info = CTkFont("Roboto Condensed", size=14, weight="normal", slant="roman")
        self.info_day = CTkLabel(self, text="Kolejny dzień w raju", fg_color="black", bg_color="black", text_color="white", font=font_info)
        self.info_day.pack()
        
        font_dzien = CTkFont("Roboto Condensed Light", size=24, weight="bold", slant="roman")
        self.dzien = CTkLabel(self, text="Dzień tygodnia", fg_color="black", bg_color="black", text_color="white", font=font_dzien)
        self.dzien.pack()

        font_day = CTkFont("Roboto", size=80, weight="bold", slant="roman")
        self.day = CTkLabel(self, text="00", fg_color="black", bg_color="black", text_color="white", 
                            font=font_day)
        self.day.pack()

        font_swieto = CTkFont("Roboto", size=20, weight="bold", slant="roman")
        self.swieto = CTkLabel(self, text="", fg_color="black", bg_color="black", text_color="white", 
                            font=font_swieto)
        self.swieto.pack()

    
        self.textbox = CTkTextbox(master=self, height=200, width=self._wwidth-30, corner_radius=0, 
                                  bg_color="black", fg_color="black", text_color="white",
                                  activate_scrollbars=False,
                                  )
        self.textbox.pack()

        self.txtInfoList = []

        
        #self.swieto = CTkLabel(self, text="??", fg_color="black", bg_color="black", text_color="white", 
        #                    font=font_swieto)
        #self.swieto.grid(row=4, column=0)

        #font_imieniny = CTkFont("Roboto Condensed Light", size=16, weight="normal", slant="roman")
        #self.imieniny =  CTkLabel(self, text="??", fg_color="black", bg_color="black", text_color="white", 
        #                    font=font_imieniny, wraplength=self._wwidth)
        #self.imieniny.grid(row=5, column=0)

        #font_przyslowia = CTkFont("Roboto Condensed Light", size=14, weight="normal", slant="roman")
        #self.przyslowia =  CTkLabel(self, text="??", fg_color="black", bg_color="black", text_color="white", 
        #                    font=font_przyslowia, wraplength=self._wwidth-10)
        #self.przyslowia.grid(row=6, column=0)

        #font_cytat = CTkFont("Roboto Condensed Light", size=12, weight="normal", slant="roman")
        #self.cytat =  CTkLabel(self, text="??", fg_color="black", bg_color="black", text_color="white", 
        #                    font=font_cytat, wraplength=self._wwidth-10)
        #self.cytat.grid(row=7, column=0)

        #font_inneS = CTkFont("Roboto Condensed Light", size=10, weight="normal", slant="roman")
        #self.inneS =  CTkLabel(self, text="??", fg_color="black", bg_color="black", text_color="white", 
        #                    font=font_inneS, wraplength=self._wwidth-10)
        #self.inneS.grid(row=8, column=0)


    def timeout(self, dt):
        
        dday = dt.date().day
        dmonth = dt.date().month
        dyear = dt.date().year
        second = dt.time().second

        if self.dayCalc is None or self.dayCalc != dday:
            if self.dayCalc is not None:
                return
            self.dayCalc = dday
            yday = (dt - datetime.datetime(dyear, 1, 1, dt.hour, dt.minute, dt.second)).days + 1
            yweek = int(yday / 7) + 1

            t1 = self.days[dt.date().weekday()]
            t2 = "%d" % dday

            self.dzien.configure(text=t1)
            self.day.configure(text=t2)

            self.miesiac_rok.configure(text="%s %d" % (self.monts[dmonth], dyear))
            self.info_day.configure(text="%d dzień, %d tydzień, %d miesiąc" % (yday, yweek, dmonth))
            #print("w3", self.info_day.cget("width"))
            
            self.getData()    
        
        if second % 10 == 0:
            idx = int( second / 10) % len(self.txtInfoList)
            text, font = self.txtInfoList[idx]
            self.textbox.delete("0.0", "end") 
            self.textbox.insert("0.0", text)
            self.textbox.configure(font=font)

        #secs = int((24 * hour + 60 * min + sec) / 30) % 4
        #self.CalendarDayUi.imieniny.setVisible(secs == 0)
        #self.CalendarDayUi.przyslowia.setVisible(secs == 1)
        #self.CalendarDayUi.cytat.setVisible(secs == 2)
        #self.CalendarDayUi.inneSwieta.setVisible(secs == 3)
           
        
    def getData(self):

        http = urllib3.PoolManager()
        r = http.request('GET', 'https://www.kalbi.pl/')
        if r.status != 200:
            return
        html = r.data
        parsed_html = BeautifulSoup(html, features='html.parser')
        #print(parsed_html)
        if parsed_html.body is None:
            return
        
        div_slonce = parsed_html.body.find('div', attrs={'class':'calCard-astro-hours'})
        if div_slonce is not None and div_slonce.text is not None:
            #print(div_slonce.text)
            i = 1
            for l in div_slonce.text.strip().split("\n"):
                l = l.strip()
                if ":" in l:
                    keys = l.split(":")
                    if keys[0] == "Wsch. Sł.":
                        self.sendNotification({'sunrise' : datetime.time(int(keys[1]), int(keys[2]), 0)})
                    if keys[0] == "Zach. Sł.":
                        self.sendNotification({'sunset' : datetime.time(int(keys[1]), int(keys[2]), 0)})
                i += 1
            #swit, wschod, gorowanie, zachod, zmierzch, dlugosc, _ = div_slonce.text.split("\n")
            #print(swit, wschod, gorowanie, zachod, zmierzch, dlugosc)            

        divSwieto = parsed_html.body.find('div', attrs={'class':'calCard-fete'})

        self.txtInfoList = []
        if divSwieto is not None:
            swieto = divSwieto.text.strip()
            #font_swieto = CTkFont("Roboto Condensed Light", size=32, weight="normal", slant="roman")
            #self.txtInfoList.append((swieto, font_swieto))
            self.swieto.configure(text=swieto)
        

        divPrzyslowia = parsed_html.body.find('section', attrs={'class':'calCard_proverb'})
        divCytat = parsed_html.body.find('section', attrs={'class':'calCard-quotes'})
        

        div_imieniny = parsed_html.body.find('section', attrs={'class':'calCard-name-day'}) 
        if div_imieniny is not None:
            font_imieniny = CTkFont("Roboto Condensed Light", size=18, weight="normal", slant="roman")
            imieniny = self.convertString(div_imieniny.text, self._wwidth-40, font_imieniny)                                      
            self.txtInfoList.append((imieniny, font_imieniny))
        
        if divPrzyslowia is not None:
            font_przyslowia = CTkFont("Roboto Condensed Light", size=18, weight="normal", slant="roman")
            div_przyslowia = divPrzyslowia.find('div', attrs={'class':'calCard_proverb-content'})                
            if div_przyslowia is not None:
                przyslowia = self.convertString(div_przyslowia.text,
                                        self._wwidth-40, font_przyslowia)
                self.txtInfoList.append((przyslowia, font_przyslowia))
        
        if divCytat is not None:
            font_cytat = CTkFont("Roboto Condensed Light", size=16, weight="normal", slant="roman")
            div_cytat = divCytat.find('div', attrs={'class':'calCard_proverb-content'})
            if div_cytat is not None:
                cytat = self.convertString(div_cytat.text,
                                   self._wwidth-40, font_cytat)
                self.txtInfoList.append((cytat, font_cytat))

        font_inneS = CTkFont("Roboto Condensed Light", size=16, weight="bold", slant="roman")
        inneS_div = parsed_html.body.find('section', attrs={'class':'calCard-ententa'})
        if inneS_div is not None:
            inneS = self.convertString(inneS_div.text,
                                    self._wwidth-45, font_inneS)
            self.txtInfoList.append((inneS, font_inneS))        

        self.textbox.insert("0.0", "")

    def convertString(self, txt:str|None, width:float, font:CTkFont):
        nwidth = 0
        ret = ''
        if txt is None:
            return ''
        txt  = txt.strip()
        line = ''
        for w in txt.split():
            if len(w) == 0 or w == ' ':
                continue

            fm = font.measure(w)

            if nwidth + fm > width:
                ret += line
                ret += '\n'
                line = ''
                nwidth = 0
            else:
                line += ' '
            line += w
            nwidth = font.measure(line)

        ret += line
        ret += '\n'
        #print("[%s]" % txt)
        #print("[%s]" % ret)
        return ret