from customtkinter import CTkFont


from base_plugin import LFrame, LCTkLabel


class DigitalClock(LFrame):
    def __init__(self, master, app, *args, **kwargs):
        super().__init__(0, 0, 200, 110, master, app, *args, **kwargs)

        font_hour_min = CTkFont("Roboto Condensed", size=96, weight="bold", slant="roman")
        self.lhour_min = LCTkLabel(master=self, text="00:00", font=font_hour_min, anchor="n")
        self.lhour_min.grid(row=0, column=0, sticky="n")

        font_sec = CTkFont("Roboto Condensed", size=48, weight="bold", slant="roman")
        self.lsecond = LCTkLabel(master=self, text="00", font=font_sec)
        self.lsecond.grid(row=0, column=1, sticky="n")
        #print("---\nDigitalClock\n---")


    def timeout(self, dt):
        hour = dt.hour
        mins = dt.minute
        secs  = dt.second
        shour = ''
        if hour < 10:
            shour+='0'
        shour+='%d:' % hour
        if mins < 10:
            shour+='0'
        shour+='%d' % mins
        self.lhour_min.configure(text=shour)
        self.lsecond.configure(text="%02d" % secs)