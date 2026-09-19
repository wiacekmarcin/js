from customtkinter import CTkFont
import tkinter as tk
import feedparser
import random

from base_plugin import LSimpleFrame, LCTkLabel

class ExpandoText(tk.Text):
    def insert(self, *args, **kwargs):
        result = tk.Text.insert(self, *args, **kwargs)
        self.reset_height()
        return result

    def reset_height(self):
        height = self.tk.call((self._w, "count", "-update", "-displaylines", "1.0", "end"))
        print(height)
        self.configure(height=height)


class BannerMeteoWarning(LSimpleFrame):
    
    def __init__(self, master, app, *args, **kwargs):
        super().__init__(master, app, *args, **kwargs)
        self._wwidth = app._max_width
        self.configure(width=self._wwidth)
        self.configure(height=0)
        self.configure(fg_color = "silver")
        #print("rss", self._wwidth)

        font_info   = CTkFont("Roboto Regular", size=28, weight="normal", slant="roman")
        font_info_b = CTkFont("Roboto Regular", size=28, weight="bold", slant="roman")

        fm10 = font_info.measure("0123456789")
        #print(fm10)
        mw = 0.99*self._wwidth
        #print(mw)
        cw = int(10*mw/fm10)
        #print()
        #self.warning = LCTkLabel(master=self, text="", font=self.font_info,
        #                     wraplength=int(0.95*self._wwidth), justify="center")
        #self.warning.pack(pady=5)

        self.color_ostrzezenia = ['#ffff00', '#fe7f00', '#ff0000']

        self.t_ostrzezenia = ExpandoText(self, width = cw, height=1, wrap = 'word', font=font_info, 
                                     background="black", foreground="white", 
                                     borderwidth=0, border=0, highlightthickness = 0)
        self.t_ostrzezenia.pack(side="top", fill='x')

        self.t_ostrzezenia.tag_configure("bold", font=font_info_b)
        self.t_ostrzezenia.tag_configure("st1", foreground=self.color_ostrzezenia[0])
        self.t_ostrzezenia.tag_configure("st2", foreground=self.color_ostrzezenia[1])
        self.t_ostrzezenia.tag_configure("st3", foreground=self.color_ostrzezenia[2])


    def timeout(self, dt):
        return

    def receiveNotfication(self, dictValue):
            
        if 'ostrzezenia' in dictValue:
            
            self.t_ostrzezenia.delete('1.0', tk.END)
            if len(dictValue['ostrzezenia']) == 0:
                print("hier")
                self.t_ostrzezenia.pack_forget()
                self.t_ostrzezenia.configure(height=0)
                self.configure(height=0)
            else:
                self.t_ostrzezenia.configure(height=1)
                self.t_ostrzezenia.pack(side="top")
                for o in dictValue['ostrzezenia']:
                    self.t_ostrzezenia.insert(tk.END, o['nazwa_zdarzenia'].upper(), "st%s" % o['stopien'])
                    self.t_ostrzezenia.insert(tk.END, " ")
                    self.t_ostrzezenia.insert(tk.END, o['czas'], "bold") 
                    self.t_ostrzezenia.insert(tk.END, ". ")
                    self.t_ostrzezenia.insert(tk.END, o['tresc'])
                    if dictValue['ostrzezenia'].index(o) < len(dictValue['ostrzezenia']) - 1:
                        self.t_ostrzezenia.insert(tk.END, "\n")
                