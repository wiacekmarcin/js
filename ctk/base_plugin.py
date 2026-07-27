from customtkinter import CTkFrame
from base_app import LustroApp
class LFrame(CTkFrame):
    wx = 0
    wy = 0
    wwidth = 0
    wheight = 0
    def __init__(self, x, y, w, h, master:LustroApp, **kwargs):
        super().__init__(master, **kwargs)
        self.master:LustroApp = master
        self.wx = x
        self.wy = y
        self.wwidth = w
        self.wheight = h
        self.configure(fg_color = "black")
        self.configure(bg_color = "black")
        #self.configure(fg_color = "silver")
        self.configure(width = w)
        self.configure(height = h)


    def getRect(self) -> tuple[int, int, int, int]:
        return (self.wx, self.wy, self.wwidth, self.wheight)

    def receiveNotfication(self, dictValue):
        pass

    def sendNotification(self, dictValue):
        self.master.sendNotification(dictValue)

    def sendMqtt(self, topic, valueDict):
        self.master.sendMqtt(topic, valueDict)