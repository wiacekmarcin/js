#import mysql.connector

def getCalendarEvents():
	return {}
"""
    mydb = mysql.connector.connect(
    host="192.168.10.250",
    user="h_cal_user",
    password="h_cal_user",
    database="home_calendar"
    )


    mycursor = mydb.cursor()

    mycursor.execute("SELECT `id`, `day`, `btime`, `etime`, `name`, `descr`, (`day` - CURRENT_DATE()) as diff FROM `ZdarzeniaWidok` where (`day` - CURRENT_DATE()) >= 0 and (`day` - CURRENT_DATE()) <= 5;")
    wydarzenia = {}
    for x in mycursor:
        if x[1] not in wydarzenia:
            wydarzenia[x[1]] = []
        
        rstr = x[4] + ': '
        secs = x[2].total_seconds()
        bh = int(secs/3600)
        bm = int((secs-bh*3600)/60)
        if bh != 0 or bm != 0:
            rstr += ' %d:%d' % (bh, bm)
        
        secs = x[3].total_seconds()
        eh = int(secs/3600)
        em = int((secs-eh*3600)/60)
        if eh != 0 or em != 0:
            rstr += '-%d:%d' % (eh, em)

        if bh != 0 or bm != 0 or eh != 0 or em != 0:
            rstr += '\n\t'
        rstr += x[5]
        wydarzenia[x[1]].append(rstr)
    return wydarzenia
"""
