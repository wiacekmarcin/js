from customtkinter import CTkLabel, CTkFont

import feedparser
import random

from base_plugin import LFrame, LSimpleFrame

#class RssInfo(LFrame):
#    def __init__(self, master, app, *args, **kwargs):
#        super().__init__(0, 1000, 1080, 600, master, app, *args, **kwargs)
class RssInfo(LSimpleFrame):
    
    def __init__(self, master, app, *args, **kwargs):
        super().__init__(master, app, *args, **kwargs)
        self._wwidth = app._max_width
        #print("rss", self._wwidth)

        self.font_head = CTkFont("Roboto Regular", size=48, weight="bold", slant="roman")
        self.font_info = CTkFont("Roboto Regular", size=28, weight="normal", slant="roman")
        
        self.head = CTkLabel(self, fg_color="black", text="", 
                             wraplength=int(0.95*self._wwidth), justify="center",   
                             font=self.font_head)
        self.head.pack(pady=20)

        self.info = CTkLabel(self, fg_color="black", text="", 
                                 wraplength=int(0.95*self._wwidth), justify="left",
                                 font=self.font_info)
        self.info.pack(pady=20)
        
        self.prevH = None
        self.prevM = None
        self.rssSource = ["https://www.polsatnews.pl/rss/wszystkie.xml"]
        self.entries = []



    def timeout(self, dt):
        
        hour = dt.hour
        min = dt.minute
        #sec = dt.second
                
        if self.prevH != hour:
            self.prevH = hour
            self.entries = []
            for source in self.rssSource:
                nf = feedparser.parse(source)
                for e in nf.entries:
                    self.entries.append(e)
        
        if self.prevM != min:
            self.prevM = min
            cntId = random.randrange(len(self.entries))
            self.head.configure(text=self.entries[cntId].title)
            self.info.configure(text=self.entries[cntId].summary)
            
