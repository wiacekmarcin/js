from urllib.request import urlopen
from urllib.error import HTTPError
import json
from datetime import datetime
from base_plugin import LPlugin

class OstrzeniaMeteo(LPlugin):
    
    def __init__(self,  app, *args, **kwargs):
        super().__init__(app, *args, **kwargs)
        self.actMinute = None
        self.teryt = '1421'
        self.lastUpdated = None        
        self.events = []

    def get_warnings(self):
        url = "https://danepubliczne.imgw.pl/api/data/warningsmeteo"
        try:
            response = urlopen(url)
        except HTTPError:
            return []
        data_json = json.loads(response.read().decode('utf-8'))

        
        if 'status' in data_json and data_json['status'] == False:
            return []
        return data_json

    def timeout(self, dt):

        if self.lastUpdated is None or (dt-self.lastUpdated).total_seconds() > 4*3600:
            self.lastUpdated = dt
            self.events = []
            
            #data_json = self.get_warnings_test()
            data_json = self.get_warnings()
            #print(data_json)
            for msg in data_json:
                for key in ['teryt', 'id', 'obowiazuje_do', 'obowiazuje_od']:
                    if not key in msg:
                        continue

                if self.teryt not in msg['teryt']:
                    continue

                ok, message = create_msg(dt, msg)
                if not ok:
                    continue   

                self.events.append({
                    'czas' : message,
                    'nazwa_zdarzenia' : msg['nazwa_zdarzenia'],
                    'stopien' : msg['stopien'],
                    'tresc' : msg['tresc'],
                })

                
            if len(self.events) > 0:
                self.sendNotification({"ostrzezenia" : self.events})
            else:
                self.sendNotification({"ostrzezenia" : []})


def create_msg(dt, msg):

    dhour = dt.hour
    dminute = dt.minute
    dsecs = dt.second
    date_od, time_od = msg['obowiazuje_od'].split(' ')
    year_od, month_od, day_od = date_od.split('-')
    hour_od, _, _ = time_od.split(':')

    date_do, time_do = msg['obowiazuje_do'].split(' ')
    year_do, month_do, day_do = date_do.split('-')
    hour_do, _, _ = time_do.split(':')

    d_od = datetime(int(year_od), int(month_od), int(day_od), dhour, dminute, (dsecs+1)%60)
    d_do = datetime(int(year_do), int(month_do), int(day_do), dhour, dminute, (dsecs+1)%60)
    days_od = (d_od - dt).days 
    days_do = (d_do - dt).days
    #print(days_od)
    #print(days_do)

    okres = []

    addHod = False
    if days_od == days_do:
        if days_od < 0:
            return False, ''
        elif days_od == 0:
            okres.append('dzisiaj')
        elif days_od == 1:
            okres.append('jutro')
        else:
            return False, ''
    else:
        addHod = True
        if days_od == -1:
            okres.append('od wczoraj')
        elif days_od == 0:
            okres.append('od dzisiaj')
        elif days_od == 1:
            okres.append('od jutra')
        else:
            return False, ''
    
    if addHod:
        okres.append('od %d godziny' % int(hour_od))
    else:
        okres.append('od %d do %d godziny' % (int(hour_od), int(hour_do)))

    if addHod:
        addHdo = True
        if days_do == -1:
            return False, ''
        elif days_do == 0:
            okres.append('do dzisiaj')
        elif days_do == 1:
            okres.append('do jutra')
        else:
            addHdo = False

        if addHdo:
            okres.append('do %d godziny' % int(hour_do))

    #print(okres)
    return True, ' '.join(okres)  
                     
    def get_warnings_test(self):
        return [{ 'id' : 1, 'teryt' : ['1421'],
            'obowiazuje_od': '2026-08-31 09:00:00', 
            'obowiazuje_do': '2026-08-31 22:00:00', 
            'nazwa_zdarzenia': 'Burze', 
            'stopien': '2', 
            'tresc': 'Prognozowane są burze, którym miejscami będą towarzyszyć silne opady deszczu od 30 mm do 40 mm, lokalnie do 50 mm oraz porywy wiatru do 75 km/h. Lokalnie grad.', 
            },
            ]
