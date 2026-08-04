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
        
        pogoda = Pogoda(self, app)
        pogoda.pack(anchor='nw', expand=True, pady=5, side='left')

        calendar = CalendarDay(self, app)
        calendar.pack(anchor='nw', expand=True, padx=5, side='left')

        aclock = AnalogClock(self, app)
        aclock.pack(anchor='nw', expand=True, padx=5, side='left')

        

        #maxheight = max(maxheight, r3[3] + r4[3] + 5)
        #self.configure(height=maxheight)