import customtkinter
import datetime, sys

from analogclock import AnalogClock
from calendarday import CalendarDay
from digtialclock import DigitalClock
from pogoda import Pogoda
from pogoda5 import Pogoda5Day
from rss import RssInfo
from base_app import LustroApp, TimeoutClass





plugs = [
    AnalogClock,
    CalendarDay,
    DigitalClock,
    Pogoda,
    Pogoda5Day,
    RssInfo
]

class LApp(LustroApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.setPlugins(self, plugs)
        self.t1sec = TimeoutClass(lambda : self.after(0, self.update1Sec))

        self.attributes('-fullscreen', True)
        

        self.after(0, lambda: self.state('normal'))

    def setPlugins(self, master, plg):
        #print("geometry", self.geometry())
        self.plgs = []
        for p in plg:
            fr = p(master)
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
            
    def update1Sec(self):
        dt = datetime.datetime.now()
        #return
        #print("--")
        try:
            for p in self.plgs:
                #try:
                if 1:
                    p.timeout(dt)
                #except :
                #    pass
        except KeyboardInterrupt:
            print("ctrl-c")
            self.t1sec.stopTimer()
            sys.exit(0)

    

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")
app = LApp()
app.mainloop()






