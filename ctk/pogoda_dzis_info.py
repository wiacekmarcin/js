from customtkinter import CTkFont
from base_app import LustroApp

import datetime



from base_plugin import LSimpleFrame, LCTkFrame, LCTkLabel, LFrame


class DzisPogodaInfo(LSimpleFrame):
    def __init__(self, master:LCTkFrame, app:LustroApp, *args, **kwargs):
        super().__init__(master, app, *args, **kwargs)

        font_info = CTkFont("Roboto Condensed", size=32, weight="normal", slant="roman")
        self.info = LCTkLabel(master=self, text="0", font=font_info, anchor="n", wraplength=master.width)
        self.info.pack()

                


    def timeout(self, dt: datetime.datetime):
        return

    def receiveNotfication(self, dictValue):
        if 'warunki_pogodowe_dzisiaj' in dictValue:
            self.info.configure(text="Pogoda na dziś: %s" ','.join(dictValue['warunki_pogodowe_dzisiaj']))
        
    
        
         
