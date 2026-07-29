import threading, time

from customtkinter import CTk

class TimeoutClass(threading.Thread):

    def __init__(self, f):
        super().__init__(target=self.timeout)
        self.next_call = time.time()
        self.f = f
        self.daemon = True
        self.trun = True
        self.start()
        

    def timeout(self):
        next_call = time.time()
        while self.trun:
            next_call = next_call+1
            self.f()
            time.sleep(max(1, next_call - time.time()))

    def stopTimer(self):
        self.trun = False

    def __delete__(self, instance):
        self.trun = False
        self.join()

class LustroApp(CTk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title("Lustro")
        w, h = self.winfo_screenwidth(), self.winfo_screenheight()
        print(w, h)
        self.configure(bg_color = "black")
        self.configure(fg_color = "black")

        #self.geometry("%dx%d+0+0" % (w, h))
        #self.geometry("400x400")
        if w==3000:
            self.geometry("1080x1920+1920+0")
        else:
            self.geometry("%dx%d+0+0" % (w, h))
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
