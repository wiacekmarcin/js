import customtkinter
import version as ver
#from analogclock import AnalogClock
#from calendarday import CalendarDay
#from digtialclock import DigitalClock
#from pogoda import Pogoda
from pogoda5 import Pogoda5Day
from rss import RssInfo
from read_serial import SerialReader
from biganalogclock import BigAnalogClock

from base_app import LustroApp
from base_plugin import LCTkLabel, LCTkFrame
from normal_frame import TopBanner
from ostrzezenia_meteo import OstrzeniaMeteo
from opis_pgody import OpisPogodyDnia
from energy import EnergyRaspberry

#plugs = [
#    AnalogClock, 
#    CalendarDay,
#    DigitalClock,
#    Pogoda,
#    Pogoda5Day,
#    RssInfo,
#    SerialReader
#]

class LApp(LustroApp):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        atmega = SerialReader(None, self)

        clock = BigAnalogClock(self.get_frame("zegar"), self)
        #print(self._max_width)
        frame2 = self.get_frame("normal")
        if frame2 is not None:
            frame_time_calendar_clock = TopBanner(frame2, self)
            frame_time_calendar_clock.pack(pady=10)

            pogoda5 = Pogoda5Day(frame2, self)
            pogoda5.pack()

            rss = RssInfo(frame2, self, self._max_width)
            rss.pack(pady=10)

            version = LCTkLabel(master=frame2, text="Wersja %d.%d.%d" % (ver.MAJOR, ver.MINOR, ver.NUMBER))
            version.place(x=0, y=1890)

        warning = OstrzeniaMeteo(self)
        pogoda = OpisPogodyDnia(self)
        stats = EnergyRaspberry(self)

        version2 = LCTkLabel(master=self.get_frame("zegar"), text="Wersja %d.%d.%d" % (ver.MAJOR, ver.MINOR, ver.NUMBER))
        version2.place(x=0, y=1890)

        self.auto_change = True
        #self.show_frame("zegar")


        self.after(0, lambda: self.state('normal'))

   

    

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")
app = LApp()
app.startTimer()
app.mainloop()






