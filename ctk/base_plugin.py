from customtkinter import CTkFrame
from base_app import LustroApp
import datetime
class LPlugin:
    def __init__(self, app:LustroApp):
        self._app:LustroApp = app
        self.frame = False
        self._app.registerPlugin(self)

    def receiveNotfication(self, dictValue):
        pass

    def sendNotification(self, dictValue):
        self._app.sendNotification(dictValue)

    def sendMqtt(self, topic, valueDict):
        self._app.sendMqtt(topic, valueDict)

    def timeout(self, dt:datetime.datetime):
        pass

class LFrame(LPlugin, CTkFrame):
    wx = 0
    wy = 0
    wwidth = 0
    wheight = 0
    def __init__(self, x, y, w, h, master:CTkFrame, app:LustroApp, *args, **kwargs):
        #super(LPlugin).__init__(master)
        #super(CTkFrame).__init__(master, **kwargs)

        LPlugin.__init__(self, app)
        CTkFrame.__init__(self, master, *args, **kwargs)
        #super().__init__(master, **kwargs)
        self.frame = True
        self.wx = x
        self.wy = y
        self.wwidth = w
        self.wheight = h
        self.configure(fg_color = "black")
        self.configure(bg_color = "black")
        #self.configure(fg_color = "silver")
        self.configure(width = w)
        self.configure(height = h)

        #self.place(x=x, y=y, anchor='ne')
        self.pack()
        self.place(x=x, y=y, anchor='ne')

    def getRect(self) -> tuple[int, int, int, int]:
        return (self.wx, self.wy, self.wwidth, self.wheight)

