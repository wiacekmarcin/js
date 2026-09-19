from customtkinter import CTkImage


from base_plugin import LSimpleFrame, LCTkLabel
from PIL import Image
from wykres_temperatury import Wykres
#class Pogoda5Day(LFrame):
#    def __init__(self, master, app, *args, **kwargs):
#        super().__init__(0, 350, self._wwidth, 600, master, app, *args, **kwargs)

class Pogoda5Day(LSimpleFrame):
    
    def __init__(self, master, app, *args, **kwargs):
        super().__init__(master, app, *args, **kwargs)
        self._wwidth = app._max_width
        #print("rss", self._wwidth)
        self.configure(width = self._wwidth, height = 100)

        self.r_img = Image.new("RGB", (self._wwidth, 600), "black")
        img = CTkImage(self.r_img, size=self.r_img.size)

        self.photo_label = LCTkLabel(master=self, image=img, text="",
                                    width=self._wwidth, height=5)
        self.photo_label.place(x=0, y=0)
        self.dayCalc = None
        self.wykres = Wykres(self._wwidth)
        
    def timeout(self, dt):
        
        dday = dt.date().day
        dmonth = dt.date().month
        dyear = dt.date().year
        minute = dt.time().minute

        if self.dayCalc is None or (self.dayCalc != dday and minute == 5):
            #if self.dayCalc is not None:
            #    return
            self.dayCalc = dday
            self.wykres.minDTemp = self.wykres.maxDTemp = None
            self.r_img = self.wykres.createImage()
            #print("Image Szie", self.r_img.size)
            t_img = CTkImage(self.r_img, size=self.r_img.size)
            self.photo_label.configure(image=t_img, height=self.r_img.size[1])
            self.configure(height = self.r_img.size[1])

            #print(self.wykres.minDTemp, self.wykres.maxDTemp)
            if self.wykres.minDTemp is not None:
                self.sendNotification({"minimum-temperature" : self.wykres.minDTemp})
            if self.wykres.maxDTemp is not None:
                self.sendNotification({"maximum-temperature" : self.wykres.maxDTemp})
