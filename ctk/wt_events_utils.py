import datetime

def getPoraDnia(h:int)->str:
    if h < 6:
        return "noc"
    elif h < 9:
        return "rano"	
    elif h < 12:
        return "przedpołudnie"
    elif h < 15:
        return "południe"
    elif h < 18:
        return "popołudnie"
    elif h < 22:
        return "wieczór"
    else:
        return "noc"


def reduce_warning_temp(warning_time:dict[datetime.date, list]) -> dict[datetime.date, list[tuple[int, str]]]:

    reduced_day_warning = {}
    last_add = False
    for day in warning_time.keys():
        reduced_day_warning[day] = []
        fstart = None
        fend = None
        flist = (0, 0)
        fdescr = None
        for w in warning_time[day]:
            h, d = w
            if fstart is None:
                fstart = h
                fend = h + 3
                flist = (fstart, fend)
                fdescr = d[0]
                ftemp =  d[1]
                fl_temp = [d[2]]
                last_add = False

            elif d[0] == fdescr and ftemp == d[1] and h == fend:
                flist = (fstart, fend)
                fend = h + 3
                fl_temp.append(d[2])
                last_add = True

            else:
                reduced_day_warning[day].append((flist, fdescr, ftemp, fl_temp))

                fstart = h
                fend = h + 3
                flist = (fstart, fend)
                fdescr = d[0]
                ftemp =  d[1]
                fl_temp = [d[2]]
                last_add = False

        if not last_add:
            reduced_day_warning[day].append((flist, fdescr, ftemp, fl_temp))


    organize_tempwarning = {}
    for day in reduced_day_warning:
        organize_tempwarning[day] = []
        for et in reduced_day_warning[day]:
            minT = min(et[3])
            maxT = max(et[3])
            tdescr = '%d\u00BA-%d\u00BA ' % et[0]
            tdescr += et[1]
            # \u0366 \u05AF \u09FD \u0ECD \u102D

            if maxT > et[2]:
                tdescr += " %2.1f>%2.0f[\u00B0C]" % (maxT,et[2])
            else:
                tdescr += " %2.1f<%2.0f[\u00B0C]" % (minT, et[2])
            organize_tempwarning[day].append((et[0][0], tdescr))

    return organize_tempwarning 

def reduce_warning_rain(warning_time:dict[datetime.date, list]) -> dict[datetime.date, list[tuple[int, str]]]:
    return reduce_warning_rainsnow(warning_time, True)

def reduce_warning_snow(warning_time:dict[datetime.date, list]) -> dict[datetime.date, list[tuple[int, str]]]:
    return reduce_warning_rainsnow(warning_time, False)

def reduce_warning_rainsnow(warning_time:dict[datetime.date, list], rain:bool) -> dict[datetime.date, list[tuple[int, str]]]:

    reduced_day_warning = {}
    last_add = False
    for day in warning_time.keys():
        reduced_day_warning[day] = []
        fstart = None
        fend = None
        flist = (0, 0)
        fdescr = None
        for w in warning_time[day]:
            h, d = w

            if fstart is None:
                fstart = h
                fend = h + 3
                flist = (fstart, fend)
                fdescr = d[0]
                fl_value = [d[1]]
                last_add = False

            elif d[0] == fdescr and h == fend:
                flist = (fstart, fend)
                fend = h + 3
                fl_value.append(d[1])
                last_add = True

            else:
                reduced_day_warning[day].append((flist, fdescr, fl_value))

                fstart = h
                fend = h + 3
                flist = (fstart, fend)
                fdescr = d[0]
                fl_value = [d[1]]
                last_add = False

        if not last_add:
            reduced_day_warning[day].append((flist, fdescr, fl_value))

    organize_warning = {}
    for day in reduced_day_warning:
        organize_warning[day] = []
        for et in reduced_day_warning[day]:
            
            val = sum(et[2])
            tdescr = '%d\u00BA-%d\u00BA ' % et[0]
            tdescr += et[1]
            # \u0366 \u05AF \u09FD \u0ECD \u102D
            tdescr += " %2.1f mm" % (val)
            
            organize_warning[day].append((et[0][0], tdescr))
            

    return organize_warning 

def reduce_warning_wind(warning_time:dict[datetime.date, list]) -> dict[datetime.date, list[tuple[int, str]]]:
    
    reduced_day_warning = {}
    last_add = False
    for day in warning_time.keys():
        reduced_day_warning[day] = []
        fstart = None
        fend = None
        flist = (0, 0)
        fdescr = None
        for w in warning_time[day]:
            h, d = w

            if fstart is None:
                fstart = h
                fend = h + 3
                flist = (fstart, fend)
                fdescr = d[0]
                fl_value = [d[1]]
                last_add = False

            elif d[0] == fdescr and h == fend:
                flist = (fstart, fend)
                fend = h + 3
                fl_value.append(d[1])
                last_add = True

            else:
                reduced_day_warning[day].append((flist, fdescr, fl_value))

                fstart = h
                fend = h + 3
                flist = (fstart, fend)
                fdescr = d[0]
                fl_value = [d[1]]
                last_add = False

        if not last_add:
            reduced_day_warning[day].append((flist, fdescr, fl_value))

    organize_warning = {}
    for day in reduced_day_warning:
        organize_warning[day] = []
        for et in reduced_day_warning[day]:
            
            val = max(et[2])
            tdescr = '%d\u00BA-%d\u00BA ' % et[0]
            tdescr += et[1]
            # \u0366 \u05AF \u09FD \u0ECD \u102D
            #tdescr += " %2.1f mm" % (val)
            
            organize_warning[day].append((et[0][0], tdescr))
            

    return organize_warning 

def days24(warning_time:list[tuple[str, tuple]]) -> dict[datetime.date, list[tuple]]:
    day_warning = {}
    if len(warning_time) == 0:
        return day_warning
    day_prev = None

    for w in warning_time:
        
        dd = w[0]
        sdate, stime = dd.split(' ')
        y, m, d = sdate.split('-')
        sy = int(y)
        sm = int(m)
        sd = int(d)
        dkey = datetime.date(sy, sm, sd)
        if not dkey in day_warning:
            day_warning[dkey] = []

        h, _, _ = stime.split(":")
        sh = int(h)
        day_warning[dkey].append((sh, *w[1:]))
    return day_warning

def organize_warning(warning_time:list[tuple[str, tuple]], forg) -> dict[datetime.date, list[tuple[int, str]]]:
    if len(warning_time) == 0:
        return {}
    
    day_warning = days24(warning_time)
    

    if len(day_warning) == 0:
        return {}

    reduced_keys = forg(day_warning)

    if len(reduced_keys) == 0:
        return {}

    return reduced_keys

def sumWarnings(warning_list:list[dict[datetime.date, list[tuple[int, str]]]]) -> dict[datetime.date, list[str]]:
    
    return_warnings = {}
    days_k = set()
    for l in warning_list:
        for k in l.keys():
            days_k.add(k)
    
    for d in days_k:
        return_warnings[d] = []
        for wlist in warning_list:
            wdlist = wlist.get(d, [])
            for w in wdlist:
                return_warnings[d].append(w)
    
    sorted_return_warnings = {}
    for d in days_k:
        sorted_return_warnings[d] = []
        wlist = return_warnings[d]
        wlist.sort(key=lambda x : x[0])
        for w in wlist:
            sorted_return_warnings[d].append(w[1])

    

    return sorted_return_warnings

