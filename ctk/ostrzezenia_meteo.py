from urllib.request import urlopen
import json

from base_plugin import LPlugin

class OstrzeniaMeteo(LPlugin):
    
    def __init__(self,  app, *args, **kwargs):
        super().__init__(app, *args, **kwargs)
        self.actMinute = None
        self.teryt = '1421'

        self.events = {}
        
    def timeout(self, dt):
        
        #dday = dt.date().day
        #dmonth = dt.date().month
        #dyear = dt.date().year
        minute = dt.time().minute

        if self.actMinute is None or (self.actMinute != minute and minute in [0, 30]):
            self.actMinute = minute

            url = "https://danepubliczne.imgw.pl/api/data/warningsmeteo"
            response = urlopen(url)
            data_json = json.loads(response.read().decode('utf-8'))

            self.events = {}
            #print(data_json)
            for msg in data_json:
                for key in ['teryt', 'id', 'obowiazuje_do', 'obowiazuje_od']:
                    if not key in msg:
                        continue

                #if msg['id'] in self.events:
                #    continue

                if self.teryt not in msg['teryt']:
                    continue

                idx = msg['id']
                self.events[idx] = {
                    'obowiazuje_do' : msg['obowiazuje_do'],
                    'obowiazuje_od' : msg['obowiazuje_od'],
                    'nazwa_zdarzenia' : getattr(msg, 'nazwa_zdarzenia', ''),
                    'stopien' : getattr(msg, 'stopien', ''),
                    'tresc' : getattr(msg, 'tresc', ''),
                    'info' : ''
                }
                event = self.events[idx]
                event['info'] = 'Od %s do %s : %s, stopien %s. '  % (event['obowiazuje_od'][:-3], event['obowiazuje_do'][:-3], 
                                                                          event['nazwa_zdarzenia'], event['stopien'])
            if len(self.events) > 0:
                ret = 'Uwaga:\n'
                ret += '\n'.join([self.events[k]['info'] for k in self.events])
                self.sendNotification({"ostrzezenia" : ret})
            else:
                self.sendNotification({"ostrzezenia" : ''})
            