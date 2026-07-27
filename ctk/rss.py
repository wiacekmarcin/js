from customtkinter import CTkLabel, CTkFont

import feedparser
import random

from base_plugin import LFrame

class RssInfo(LFrame):
    def __init__(self, master, **kwargs):
        super().__init__(0, 1000, 1080, 600, master, **kwargs)

        self.font_head = CTkFont("Roboto Condensed", size=32, weight="bold", slant="roman")
        self.font_info = CTkFont("Roboto Condensed", size=18, weight="normal", slant="roman")
        
        self.head = CTkLabel(self, fg_color="black", text="", 
                             wraplength=1080, justify="center",   
                             font=self.font_head)
        self.head.pack()

        self.info = CTkLabel(self, fg_color="black", text="", 
                                 wraplength=1080, justify="left",
                                 font=self.font_info)
        self.info.pack()
        
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
            
