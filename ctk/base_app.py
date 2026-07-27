from customtkinter import CTk

class LustroApp(CTk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title("Lustro")
        w, h = self.winfo_screenwidth(), self.winfo_screenheight()
        self.configure(bg_color = "black")
        self.configure(fg_color = "black")

        #self.geometry("%dx%d+0+0" % (w, h))
        self.geometry("400x400")
        self.focus_set()
        self.bind("<Escape>", lambda e: e.widget.quit())
        self.plgs = []
        
    def sendNotification(self, dictValue):
        self.after(0, self._sendNotification, dictValue)    
    
    def _sendNotification(self, valueDict):
        for p in self.plgs:
            p.receiveNotfication(valueDict)

    def sendMqtt(self, topic, valueDict):
        self.after(0, self._sendMqtt, topic, valueDict)

    def _sendMqtt(self, topic, valueDict):
        for p in self.plgs:
            p.receiveMqtt(topic, valueDict)
