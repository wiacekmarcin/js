from customtkinter import CTkFrame, CTkLabel, CTkFont,CTkImage
from base_app import LustroApp
import datetime

from typing import Union, Tuple, List, Optional, Any, overload

class LCTkFrame(CTkFrame):
    def __init__(self,
                 master: Any,
                 width: int = 200,
                 height: int = 200,
                 corner_radius: Optional[Union[int, str]] = None,
                 border_width: Optional[Union[int, str]] = None,

                 bg_color: Union[str, Tuple[str, str]] = "transparent",
                 fg_color: Optional[Union[str, Tuple[str, str]]] = None,
                 border_color: Optional[Union[str, Tuple[str, str]]] = None,

                 background_corner_colors: Union[Tuple[Union[str, Tuple[str, str]]], None] = None,
                 overwrite_preferred_drawing_method: Union[str, None] = None,
                 **kwargs):
        if bg_color == "transparent":
            bg_color = "black"
        if fg_color is None:
            fg_color = "black"
        
        super().__init__(master=master, width=width, height=height, corner_radius=corner_radius, border_width=border_width,
                            bg_color=bg_color, fg_color=fg_color, border_color=border_color,
                            background_corner_colors=background_corner_colors,
                            overwrite_preferred_drawing_method=overwrite_preferred_drawing_method,
                            **kwargs)
        self.width = width
class LCTkLabel(CTkLabel):
    def __init__(self,master: Any,
                 width: int = 0,
                 height: int = 28,
                 corner_radius: Optional[int] = None,

                 bg_color: Union[str, Tuple[str, str]] = "transparent",
                 fg_color: Optional[Union[str, Tuple[str, str]]] = None,
                 text_color: Optional[Union[str, Tuple[str, str]]] = None,
                 text_color_disabled: Optional[Union[str, Tuple[str, str]]] = None,

                 text: str = "CTkLabel",
                 font: Optional[Union[tuple, CTkFont]] = None,
                 image: Union[CTkImage, None] = None,
                 compound: str = "center",
                 anchor: str = "center",  # label anchor: center, n, e, s, w
                 wraplength: int = 0,
                 **kwargs):
        if bg_color == "transparent":
             bg_color = "black"
        if fg_color is None:
             fg_color = "black"
        if text_color is None:
            text_color = "white"
        if text_color_disabled is None:
            text_color_disabled = "silver"

        super().__init__(master=master, width=width, height=height, bg_color=bg_color, fg_color=fg_color, text_color=text_color,
                         text_color_disabled = text_color_disabled, text=text, font=font, image=image, compound=compound,
                         anchor=anchor, wraplength=wraplength, corner_radius=corner_radius, **kwargs)


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

class LSimpleFrame(LPlugin, CTkFrame):

    def __init__(self, master:CTkFrame, app:LustroApp, *args, **kwargs):
        LPlugin.__init__(self, app)
        CTkFrame.__init__(self, master, *args, **kwargs)
        #super().__init__(master, **kwargs)
        self.frame = True

        self.configure(fg_color = "black")
        self.configure(bg_color = "black")
        #self.configure(fg_color = "silver")


class LFrame(LSimpleFrame):
    wx = 0
    wy = 0
    wwidth = 0
    wheight = 0

    def __init__(self, x, y, w, h, master:CTkFrame, app:LustroApp, *args, **kwargs):
        LSimpleFrame.__init__(self, master, app, *args, **kwargs)


    def __init__(self, x, y, w, h, master:CTkFrame, app:LustroApp, *args, **kwargs):
        LSimpleFrame.__init__(self, master, app, *args, **kwargs)

        self.wx = x
        self.wy = y
        self.wwidth = w
        self.wheight = h

        self.configure(width = w)
        self.configure(height = h)

        self.place(x=x, y=y, anchor='nw')

    def getRect(self) -> tuple[int, int, int, int]:
        return (self.wx, self.wy, self.wwidth, self.wheight)