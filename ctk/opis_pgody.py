from datetime import datetime

from base_app import LustroApp
from base_plugin import LPlugin

import datetime
import re

from urllib.request import urlopen
import json


class OpisPogodyDnia(LPlugin):
    def __init__(self, app: LustroApp):
        super().__init__(app)
        self.lastUpdate = None
        self.min_pressure = (-1, 0)
        self.max_pressure = (-1, 0)
        
        self.min_temp = (-1, 0)
        self.max_temp = (-1, 0)

    def timeout(self, dt: datetime.datetime):

        hour = dt.hour
        minute = dt.minute

        if self.lastUpdate is None or (dt-self.lastUpdate).total_seconds() > 3*3600:
            self.sendOstrzenia(self.get_data(dt))

        if hour == 0 and minute == 5:
            if self.lastUpdate is None or (dt-self.lastUpdate).total_seconds() > 70:
                self.min_pressure = (-1, 0)
                self.max_pressure = (-1, 0)
                self.min_temp = (-1, 0)
                self.max_temp = (-1, 0)
            self.sendOstrzenia(self.get_data(dt))


    def get_data(self, dt):
        print("get_data")
        url = "https://api.openweathermap.org/data/2.5/forecast?appid=b176485875db690244cb8acf93637572&id=7532279&lang=pl&units=metric"
        response = urlopen(url)
        data_json = json.loads(response.read().decode('utf-8'))
        self.lastUpdate = dt        
        cnt_items = int(data_json["cnt"]) or 0
        
        if cnt_items == 0:
            print("cnt_items == 0")
            return        
        
        items = data_json["list"]
        if items is None:
            print("items == 0")
            return
        
        tdregex=re.compile("^%d-%02d-%02d .*$" % (dt.year, dt.month, dt.day))
        
        rainMap = {
            'słabe opady deszczu' : 'słaby deszcz',
            'intensywne opady deszczu' : 'intensywny deszcz',
        }
        deszcz = []
        snieg = []
        wiatr = []
        porywy = []

        for i in items:
            dt_txt = i["dt_txt"]
        
            if i["dt_txt"] is None:
                continue
        
            if tdregex.match(dt_txt) is None:
                continue

            _, st = dt_txt.split(' ')
            h, _, _ = st.split(':')
            m = i['main'] or {}
            w = i['weather'] or {}

            h = int(h)
            if 'rain' in i.keys():
                deszcz.append((h, float(i['rain']["3h"])))
            else:
                deszcz.append((h, 0))
            
            if 'snow' in i.keys():
                snieg.append((h, float(i['snow']["3h"])))
            else:
                snieg.append((h, 0))

            if 'wind' in i.keys():
                wiatr.append((h, float(i['wind']['speed']) or 0))
                porywy.append((h, float(i['wind']['gust']) or 0)) 
                                        
            if 'pressure' in m.keys():
                if self.min_pressure[0] == -1 or self.min_pressure[1] > float(m['pressure']):
                    self.min_pressure = (h, float(m['pressure']))

                if self.max_pressure[0] == -1 or self.max_pressure[1] < float(m['pressure']):
                    self.max_pressure = (h, float(m['pressure']))
                                                                

            if 'temp' in m.keys():
                if self.min_temp[0] == -1 or self.min_temp[1] > float(m['temp']):
                    self.min_temp = (h, float(m['temp']))

                if self.max_temp[0] == -1 or self.max_temp[1] < float(m['temp']):
                    self.max_temp = (h, float(m['temp']))

                #3temperatura.append((h, float(m['temperatura'])))
                #if 'feel_temp' in m.keys():
                #    temperatura.append((h, float(m['feel_temp'])))

        ostrzezenia = []

        #wdeszcz
        for d in deszcz:
            if d[1] == 0:
                continue
            elif d[1] < 1:
                ostrzezenia.append("lekki deszcz %s" % (self.convert_h(d[0])))
            elif d[1] < 3:
                ostrzezenia.append("deszcz %s" % (self.convert_h(d[0])))
            elif d[1] < 12:
                ostrzezenia.append("ulewa %s" % (self.convert_h(d[0])))
            else:
                ostrzezenia.append("nawałnica %s" % (self.convert_h(d[0])))

        for s in snieg:
            if s[1] == 0:
                continue
            else:
                ostrzezenia.append("opad śniegu %s" % (self.convert_h(d[0])))

        if self.min_temp[0] != -1 and self.min_temp[1] < -10:
            ostrzezenia.append("duży mróz %2.1f \u00B0C %s" % (self.min_temp[1], self.convert_h(self.min_temp[0])))

        if self.max_temp[0] != -1 and self.max_temp[1] > 35:
            ostrzezenia.append("upał %2.1f \u00B0C %s" % (self.max_temp[1], self.convert_h(self.max_temp[0])))

        if self.max_temp[0] != -1 and self.min_temp[0] != -1:
            if self.max_temp[1] - self.min_temp[1] > 20:
                ostrzezenia.append("duża zmiana temperatur w ciągu dnia")


        if self.min_pressure[0] != -1 and self.min_pressure[1] <= 1000:
            ostrzezenia.append("niskie ciśnienie %d hPa %s" % (self.min_pressure[1], self.convert_h(self.min_pressure[0])))

        if self.max_pressure[0] != -1 and self.max_pressure[1] >= 1030:
            ostrzezenia.append("wysokie ciśnienie %d hPa %s" % (self.max_pressure[1], self.convert_h(self.max_pressure[0])))

        if self.max_pressure[0] != -1 and self.min_pressure[0] != -1:
            if self.max_pressure[1] - self.min_pressure[1] > 8:
                ostrzezenia.append("duża zmiana ciśnienia w ciągu dnia")

            
        return ostrzezenia

    def sendOstrzenia(self, ostrzezenia):
        print("warunki_pogodowe", ostrzezenia)
        self.sendNotification({'warunki_pogodowe_dzisiaj'  : ostrzezenia})

    def convert_h(self, h):
        if h < 6:
            return 'w nocy'
        elif h < 9:
            return 'rano'
        elif h < 15:
            return 'w południe'
        elif h < 18:
            return 'popołudniu'
        elif h < 22:
            return 'wieczorem'
        else:
            return 'w nocy'

            
                
            