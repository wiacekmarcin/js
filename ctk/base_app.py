import threading, time, sys
import tkinter as tk
from customtkinter import CTk, CTkFrame
import datetime



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
    def __init__(self, *args, **kwargs): 
        
        # __init__ function for class Tk
        CTk.__init__(self, *args, **kwargs)
        
        # creating a container
        self.container = tk.Frame(self, width=1080, height=1920,)  
        self.container.pack(side = "top", fill = "both", expand = True) 
 
        self.container.grid_rowconfigure(0, weight = 1)
        self.container.grid_columnconfigure(0, weight = 1)
 
        # initializing frames to an empty array

        self.frames = {}

        for fname in ["zegar", "normal"]:
            frame = CTkFrame(master=self.container, width=1080, height=1920)
            self.frames[fname] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("zegar")
        self.cntFrame = 0

        #self.frame = CTkFrame(master=self.container, width=1080, height=1920)
        #self.frame.grid(row=0, column=0, sticky="nsew")
        
        self.title("Lustro")
        w, h = self.winfo_screenwidth(), self.winfo_screenheight()
        
        self.configure(bg_color = "black")
        self.configure(fg_color = "black")

        #self.geometry("%dx%d+0+0" % (w, h))
        #self.geometry("400x400")
        if w==3000:
            self.geometry("1080x1920+1920+0")
            self.attributes('-fullscreen', True)
        elif w == 7680:
            self.geometry("1080x1920+3840+0")
        else:
            self.geometry("%dx%d+0+0" % (w, h))
            self.attributes('-fullscreen', True)
        self.focus_set()
        self.bind("<Escape>", lambda e: e.widget.quit())
        self.plgs = []

        self.t1sec = TimeoutClass(lambda : self.after(0, self.update1Sec))

    def show_frame(self, page_name:str):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

    def get_frame(self, page_name:str) -> CTkFrame:
        if page_name in self.frames:
            return self.frames[page_name]
        return CTkFrame()

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

    def registerPlugin(self, plg):
        self.plgs.append(plg)

    def update1Sec(self):
        dt = datetime.datetime.now()
        #return
        #print("--")
        t = dt.time()
        if t.second == 0:
            self.cntFrame += 1
            if self.cntFrame == len(self.frames):
                self.cntFrame = 0
            self.show_frame(["zegar", "normal"][self.cntFrame])
        
        try:
            for p in self.plgs:
                #try:
                if 1:
                    p.timeout(dt)
                #except :
                #    pass
        except KeyboardInterrupt:
            print("ctrl-c")
            self.t1sec.stopTimer()
            sys.exit(0)