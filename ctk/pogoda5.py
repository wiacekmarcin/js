from customtkinter import CTkLabel, CTkImage


from base_plugin import LFrame
from PIL import Image
from wykres_temperatury import Wykres
class Pogoda5Day(LFrame):
    def __init__(self, master, app, *args, **kwargs):
        super().__init__(0, 350, 1080, 600, master, app, *args, **kwargs)
        
        self.r_img = Image.new("RGB", (1080, 600), "black")
        img = CTkImage(self.r_img, size=self.r_img.size)

        self.photo_label = CTkLabel(self, fg_color="black", image=img, text="")
        self.photo_label.place(x=0, y=0)
        self.dayCalc = None
        self.wykres = Wykres()
        
    def timeout(self, dt):
        
        dday = dt.date().day
        dmonth = dt.date().month
        dyear = dt.date().year
        second = dt.time().second

        if self.dayCalc is None or self.dayCalc != dday:
            if self.dayCalc is not None:
                return
            self.dayCalc = dday
            self.wykres.minDTemp = self.wykres.maxDTemp = None
            self.r_img = self.wykres.createImage()
            #print("Szie", self.r_img.size)
            t_img = CTkImage(self.r_img, size=self.r_img.size)
            self.photo_label.configure(image=t_img)

            print(self.wykres.minDTemp, self.wykres.maxDTemp)
            if self.wykres.minDTemp is not None:
                self.sendNotification({"minimum-temperature" : self.wykres.minDTemp})
            if self.wykres.maxDTemp is not None:
                self.sendNotification({"maximum-temperature" : self.wykres.maxDTemp})
