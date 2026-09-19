from datetime import datetime

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

    d_od = datetime(int(year_od), int(month_od), int(day_od), dhour, dminute, dsecs+1)
    d_do = datetime(int(year_do), int(month_do), int(day_do), dhour, dminute, dsecs+1)
    days_od = (d_od - dt).days 
    days_do = (d_do - dt).days
    print(days_od)
    print(days_do)

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

    print(okres)
    return True, ' '.join(okres)                     

msg = { 'obowiazuje_od': '2026-08-28 09:00:00', 
        'obowiazuje_do': '2026-08-29 22:00:00', 
        
        'nazwa_zdarzenia': 'Burze', 
        'stopien': '2', 
        'tresc': 'Prognozowane są burze, którym miejscami będą towarzyszyć silne opady deszczu od 30 mm do 40 mm, lokalnie do 50 mm oraz porywy wiatru do 75 km/h. Lokalnie grad.', 
        'info': ''
    }

ok, smsg = create_msg(datetime.now(), msg)
if ok:
    print(smsg)