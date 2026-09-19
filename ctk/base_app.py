import threading, time, sys
import tkinter as tk
from customtkinter import CTk, CTkFrame
import datetime
from mqtt_client import PahoMqttWriter
from udp_client import UdpSend

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
    _max_width = 1080
    _max_height = 1920
    def __init__(self, *args, **kwargs): 
        
        # __init__ function for class Tk
        CTk.__init__(self, *args, **kwargs)
        self._max_width = 1080
        self._max_height = 1920
        self.config(cursor="none")
        # creating a container
        #print(f"LustroApp, max_w", self._max_width)
        self.container = tk.Frame(self, width=self._max_width, height=self._max_height)  
        self.container.pack(side = "top", fill = "both", expand = True) 
        #self.container.place(x=0, y=0)
 
        self.container.grid_rowconfigure(0, weight = self._max_width)
        self.container.grid_columnconfigure(0, weight = self._max_height)
 
        # initializing frames to an empty array

        self.frames = {}
        self.selected_frame = ''
        for fname in ["zegar", "normal"]:
            frame = CTkFrame(master=self.container, width=self._max_width, height=self._max_height)
            self.frames[fname] = frame
            #frame.place(relx=0, rely=0, relwidth=1, relheight=1)
            frame.grid(row=0, column=0, sticky="nsew")
            frame.configure(bg_color = "black")
            frame.configure(fg_color = "black")

        #self.show_frame("zegar")
        #self.auto_change = True
        self.cntFrame = 0
        
        self.title("Lustro")
        w, h = self.winfo_screenwidth(), self.winfo_screenheight()
        #print(w, h)
        
        #print(w, h)
        
        self.configure(bg_color = "black")
        self.configure(fg_color = "black")

        #self.geometry("%dx%d+0+0" % (w, h))
        #self.geometry("400x400")
        if w==3000 and h==1920:
            self.geometry("1080x1920+1920+0")
            self.attributes('-fullscreen', True)
            pass
        elif w == 7680:
            self.geometry("1080x1920+3840+0")
        else:
            self.geometry("%dx%d+0+0" % (w, h))
            self.attributes('-fullscreen', True)
        #self.geometry("400x400")
        if w==3000 and h==1920:
            self.geometry("1080x1920+1920+0")
            self.attributes('-fullscreen', True)
            pass
        elif w == 7680:
            self.geometry("1080x1920+3840+0")
        else:
            self.geometry("%dx%d+0+0" % (w, h))
            self.attributes('-fullscreen', True)
        self.focus_set()
        self.bind("<Escape>", lambda e: e.widget.quit())
        self.plgs = []


        self.mqtt = PahoMqttWriter(self.receiveMqttMsg)

        self.udpCl = UdpSend()
        self.after(1000, self.startTimer)

    def startTimer(self):
        self.t1sec = TimeoutClass(lambda : self.after(0, self.update1Sec))
        self.focus_set()

    def show_frame(self, page_name:str):
        '''Show a frame for the given page name'''
        self.selected_frame = page_name
        if page_name == "auto":
            self.auto_change = True
            return
        if page_name in self.frames:
            frame = self.frames[page_name]
            self.auto_change = False
            frame.tkraise()

    def get_frame(self, page_name:str) -> CTkFrame | None:
        frame = None
        if page_name in self.frames:
            frame =  self.frames[page_name]
        return frame

    def sendNotification(self, dictValue):
        #print("sendNotification", dictValue)
        self.after(0, self._sendNotification, dictValue)

    
    def _sendNotification(self, valueDict):
        #print("_sendNotification", valueDict, len(self.plgs))
        self.udpCl.sendUdpNotfication(valueDict)    
        for p in self.plgs:
            p.receiveNotfication(valueDict)

    def sendMqtt(self, topic, valueDict):
        self.after(0, self._sendMqtt, topic, valueDict)

    def _sendMqtt(self, topic, valueDict):
        self.mqtt.sendMqtt(topic, valueDict)

    def registerPlugin(self, plg):
        self.plgs.append(plg)

    def update1Sec(self):
        dt = datetime.datetime.now()
        try:
            for p in self.plgs:
                p.timeout(dt)
            t = dt.time().hour

            if self.auto_change:
                zegar = t not in [6, 7, 8, 9, 19, 20, 21, 22, 23]
            
                if zegar and self.selected_frame != "zegar":
                    self.show_frame("zegar")
                elif not zegar and self.selected_frame != "normal":
                    self.show_frame("normal")
        

        except KeyboardInterrupt:
            print("ctrl-c")
            self.t1sec.stopTimer()
            sys.exit(0)

    def receiveMqttMsg(self, topic, msg):
        #print("receiveMqttMsg", topic, msg)
        if 'display' in msg:
            display = msg['display']
            mapD = {
                0 : "auto",
                1 : "normal",
                2 : "zegar"
            }
            if int(display) in mapD:
                print("Change display")
                self.show_frame((mapD[display]))
            else:
                print("error")
        self.sendNotification(msg)