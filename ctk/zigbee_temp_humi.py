from customtkinter import CTkFont

from base_plugin import LSimpleFrame, LCTkLabel
import math


class TempHumi:
    def __init__(self, frameTiH, font, title:str, key_th:str):

        self.key_temp = '%s_temp' % key_th
        self.key_humi = '%s_humi' % key_th
        self.ltitle = LCTkLabel(master=frameTiH, text=title, 
                              font=font, justify="left", anchor="w")

        self.ltemp = LCTkLabel(master=frameTiH, text="-", 
                              font=font, justify="right", anchor="e")

        self.lhumi = LCTkLabel(master=frameTiH, text="-", 
                              font=font, justify="right", anchor="e")

        self.lastUpdate = 0

        self.temp = None
        self.humi = None

    def grid(self, row:int, column:int, padx:int, pady:int):
        self.ltitle.grid(row=row, column=column, padx=padx, pady=pady)
        self.ltemp.grid(row=row, column=column+1, padx=padx, pady=pady)
        self.lhumi.grid(row=row, column=column+2, padx=padx, pady=pady)

    def timeout(self, dt):
        self.lastUpdate -= 1
        if self.lastUpdate < 0:
            self.temp = None
            self.humi = None
            self.update()

    def update(self):
        if self.temp is None:
            self.ltemp.configure(text='-')                
        else:
            self.ltemp.configure(text='%2.1f\u00B0C' % self.temp)

        if self.humi is None:
            self.lhumi.configure(text='-')                
        else:
            self.lhumi.configure(text='%2.0f%%' % self.humi)

    def check_and_set(self, data:dict):
        if self.key_temp in data or self.key_humi in data:
            self.lastUpdate = 3600
            if self.key_temp in data:
                self.temp = float(data[self.key_temp])
            if self.key_humi in data:
                self.humi = float(data[self.key_humi])
            self.update()

class TempZTiHAll(LSimpleFrame):
    _wwidth = 350
    def __init__(self, master, app, *args, **kwargs):
        #super().__init__(0, 0, 300, 250, master, app, *args, **kwargs)
        super().__init__(master, app, *args, **kwargs)

        self.configure(width=self._wwidth)
        font = CTkFont("Roboto Condensed", size=24, weight="normal", slant="roman")
        
                
        self.lst = []

        self.lst.append(TempHumi(self, font, 'Laz.', 'lazienka'))
        self.lst.append(TempHumi(self, font, 'Kuch.', 'kuchnia'))
        self.lst.append(TempHumi(self, font, 'WC', 'wc'))
        self.lst.append(TempHumi(self, font, 'Hol', 'hol'))
        self.lst.append(TempHumi(self, font, 'Sal.', 'salon_2'))
        self.lst.append(TempHumi(self, font, 'Syp.', 'sypialnia'))
        self.lst.append(TempHumi(self, font, 'Prac.', 'pracownia'))
        self.lst.append(TempHumi(self, font, 'Dziec.', 'dzieci'))

        fhead_tih = CTkFont("Weather Icons", size=20, weight="normal", slant="roman")
        row_max = math.ceil(len(self.lst) / 2)
        etTemperatura1 = LCTkLabel(master=self, text="\uf055\uf03c",
                                        
                                       justify="center")
        etTemperatura1.grid(row=row_max, column=1, ipadx=20, pady=5)
        etWilgotnosc1 = LCTkLabel(master=self, text="\uf07a", justify="center")
        etWilgotnosc1.grid(row=row_max, column=2, ipadx=20, pady=5)
        space = LCTkLabel(master=self, text=" ", justify="center")
        space.grid(row=row_max, column=3, padx=5)
        
        etTemperatura2 = LCTkLabel(master=self, text="\uf055\uf03c", justify="center")
        etTemperatura2.grid(row=row_max, column=5, ipadx=20, pady=5)

        
        etWilgotnosc2 = LCTkLabel(master=self, text="\uf07a", justify="center")
        etWilgotnosc2.grid(row=row_max, column=6, ipadx=20, pady=5)

        self.grid(0, 0, row_max)

    def grid(self, padx:int, pady:int, row_max:int):
        for w in self.lst:
            if self.lst.index(w) < row_max:
                w.grid(row=self.lst.index(w), column=0, padx=padx, pady=pady)
            else:
                w.grid(row=self.lst.index(w)-row_max, column=4, padx=padx, pady=pady)
                

    def timeout(self, dt):
        for w in self.lst:
            w.timeout(dt)

    def check_and_set(self, data:dict):
        for w in self.lst:
            w.check_and_set(data)

    def receiveNotfication(self, values):
        #print("ok, receiveNotfication.pogoda", values)
        self.check_and_set(values)        




    