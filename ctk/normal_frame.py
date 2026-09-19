from typing import Any, Tuple

from customtkinter import CTkFrame, CTkLabel
from base_app import LustroApp
from base_plugin import LCTkFrame, LCTkLabel
from analogclock import AnalogClock
from calendarday import CalendarDay
from digtialclock import DigitalClock
from pogoda import Pogoda
from zigbee_temp_humi import TempZTiHAll
from banner_ostrzezenia import BannerMeteoWarning
from pogoda_dzis_info import DzisPogodaInfo

class TopBanner(CTkFrame):
    def __init__(self, master:CTkFrame, app:LustroApp):
        super().__init__(master, bg_color="black", fg_color = "black", width=app._max_width)

        self.configure(width =app._max_width)

        top_frame = LCTkFrame(master=self, width=app._max_width)
        top_frame.pack(side='top')

        left_frame = LCTkFrame(master=top_frame, width=400)
        left_frame.pack(side='left')
        zegar = DigitalClock(left_frame, app)
        zegar.pack(anchor='nw', expand=True, side='top')
        pogoda = Pogoda(left_frame, app)
        pogoda.pack(anchor='nw', expand=True, side='top')

        ostrzenie = DzisPogodaInfo(left_frame, app)
        ostrzenie.pack(anchor='nw', expand=True, side='top')

        center_frame = LCTkFrame(master=top_frame, width=app._max_width-400-350)
        center_frame.pack(side='left')
        calendar = CalendarDay(center_frame, app)
        calendar.pack(side='top')

        right_frame = LCTkFrame(master=top_frame, width=350)
        right_frame.pack(side='left', expand=True, fill='x')

        aclock = AnalogClock(right_frame, app)
        aclock.pack(anchor='nw', expand=True, side='top')
        temps = TempZTiHAll(right_frame, app)
        temps.pack(anchor='nw', expand=True, side='top', fill='x')

        bottom_frame = BannerMeteoWarning(self, app)
        bottom_frame.pack(side='bottom', fill='x')
        

        #maxheight = max(maxheight, r3[3] + r4[3] + 5)
        #self.configure(height=maxheight)