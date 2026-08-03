from typing import Any, Tuple

from customtkinter import CTk, CTkFrame
from base_app import LustroApp

from analogclock import AnalogClock
from calendarday import CalendarDay
from digtialclock import DigitalClock
from pogoda import Pogoda

class TopBanner(CTkFrame):
    def __init__(self, master:CTkFrame, app:LustroApp):
        super().__init__(master, bg_color="brown", fg_color = "brown", width=1080)

        self.configure(width = 1080)
        
        fr1 = CTkFrame(self)
        fr1.pack(anchor='ne', expand=True, padx=5, side='left')

        fr2 = CTkFrame(self)
        calendar = CalendarDay(fr2, app)
        fr2.pack(anchor='ne', expand=True, padx=5, side='left', after=fr1)

        aclock = AnalogClock(self, app)
        aclock.pack(anchor='ne', expand=True, padx=5, side='right', after=fr2)

        fr1a = CTkFrame(fr1)
        #dclock = DigitalClock(fr1a, app)
        #r3 = dclock.getRect()
        #fr1a.pack(anchor='ne', expand=True, pady=5, side='top')

        fr1b = CTkFrame(fr1)
        #pogoda = Pogoda(fr1b, app)
        #r4 = pogoda.getRect()
        #fr1b.pack(anchor='ne', expand=True, pady=5, side='bottom')

        #maxheight = max(maxheight, r3[3] + r4[3] + 5)
        #self.configure(height=maxheight)