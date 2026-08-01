import customtkinter

from analogclock import AnalogClock
from calendarday import CalendarDay
from digtialclock import DigitalClock
from pogoda import Pogoda
from pogoda5 import Pogoda5Day
from rss import RssInfo
from read_serial import SerialReader
from biganalogclock import BigAnalogClock

from base_app import LustroApp

plugs = [
    AnalogClock, 
    CalendarDay,
    DigitalClock,
    Pogoda,
    Pogoda5Day,
    RssInfo,
    SerialReader
]

class LApp(LustroApp):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        clock = BigAnalogClock(self.get_frame("zegar"), self)
        #clock = AnalogClock(self.get_frame("zegar"), self)
        #x, y, _, _ = clock.getRect()
        #clock.place(x=x, y=y, anchor='nw')
        
        for P in plugs:
            p = P(self.get_frame("normal"), self)

        self.after(0, lambda: self.state('normal'))

    def setPlugins(self, master, plg):
        #print("geometry", self.geometry())
        self.plgs = []
        for p in plg:
            fr = p(master, self)
            if fr.frame:
                x, y, w, h = fr.getRect()
                #print("xywh", x, y, w, h)
                fr.place(x=x, y=y, anchor='nw')
            self.plgs.append(fr)
            #print("rect", fr.cget('width'), fr.cget('height'),)
            #print("-----")

        #self.plgs[0].setWschod(6, 45)
        #self.plgs[0].setZachod(21, 25)

        #self.plgs[0].setMinimumTemp("-6.2")
        #self.plgs[0].setMaximumTemp("26.2")
            
    

    

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")
app = LApp()
app.startTimer()
app.mainloop()






