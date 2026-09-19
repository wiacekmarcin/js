from customtkinter import CTkFont

import feedparser
import random

from base_plugin import LSimpleFrame, LCTkLabel

class RssInfo(LSimpleFrame):
    
    def __init__(self, master, app, width, *args, **kwargs):
        super().__init__(master, app, *args, **kwargs)
        self._wwidth = width
        #print("rss", self._wwidth)

        self.font_head = CTkFont("Roboto Regular", size=48, weight="bold", slant="roman")
        self.font_info = CTkFont("Roboto Regular", size=28, weight="normal", slant="roman")
        
        self.head = LCTkLabel(master=self, text="", font=self.font_head,
                             wraplength=int(0.95*self._wwidth), justify="center")
        self.head.pack(pady=20)

        self.info = LCTkLabel(master=self, text="", font=self.font_info, 
                                 wraplength=int(0.95*self._wwidth), justify="left")
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
            
