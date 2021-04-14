import mysql.connector
cnx = mysql.connector.connect(user='kb_ster', password='kb_ster',
                              host='127.0.0.1',
                              database='kb_ster_test')
                              
cursor = cnx.cursor()

zlacza = {
  'A:88' : [
    '-',
    '-',
    '-',
    '-',
    ':A5-E8',
    ':A6-E7',
    ':A7-E6',
    ':A8-E5'
  ],
  'B:199' : [
    '+5V',
    'Kanał L',
    'Kanał N',
    'T4.E'
  ],
  'C:122' : [
    '-',
    '-',
    '-',
    ':C4-F8',
    ':C5-F7',
    ':C6-F6',
    ':C7-F5',
    ':C8-F4',
    ':C9-F3',
    ':C10-F2'
  ],
  'D:123' : [
    '0x24.B5',
    '0x24.B4',
    '0x24.B3',
    '0x24.B2',
    '0x24.B1',
    '0x24.B0',
    'T1.E',
    'T2.E',
    'GND',
    'GND'
  ],
    'E:198' : [
    '+5V', 
    'GND',   
    '0x24.B6',
    '0x24.B7',
    ':A8-E5',
    ':A7-E6',
    ':A6-E7',
    ':A5-E8'
  ],
  'F:42' : [
    '-',
    ':C10-F2',
    ':C9-F3',
    ':C8-F4',
    ':C7-F5',
    ':C6-F6',
    ':C5-F7',
    ':C4-F8'
  ],
  'G:119' : [
    '+5V',
    'GND',
    'SCL',
    'SDA',
    '0X24.INT',
    ':G6-I2',
    'T2.B',
    'T3.B'
  ],
  'H:93' : [
    'TX93',
    'RX93',
    '+24V',
    'GND',
    '0X24.A4',
    '0X24.A3',
    '0X24.A2',
    '0X24.A1'
  ],
  'I:64' : [
    '0X24.A0',
    ':G6-I2',
    '0X20.B7',
    '0X24.A7',
    '0X24.A6',
    '0X24.A5',
    'T3.E',
    '+5V',
  ],
  'J:121' : [
    '0X20.B4',
    'T3.E',
    '+5V'
  ],
  'K:118' : [
    '0x20.B0',
    '0x20.B1',
    '0x20.B2',
    '0x20.B3',
    'T3.E',
    '+5V',
  ],
  'L:120' : [
    '0x20.A0',
    '0x20.A1',
    '0x20.A2',
    '0x20.A3',
    '0x20.A4',
    '0x20.A5',
    '0x20.A6',
    '0x20.A7',
    'T3.E',
    '+5V'
  ],
  'M:124' : [
    'RX',
    'TX'
  ]
}
letterMap = {}
plytka_id = 3
nazwaPol = {}
zlaczaMap = {}

for k in zlacza.keys():
    letter, przewod = k.split(':')
    letterMap[letter] = przewod

for k in zlacza.keys():
    letter, przewod = k.split(':')
    
    sql = "INSERT INTO `elementy_plytkowe`(`id`, `nazwa`, `ilosc_pin`, `plytka_id`, `rodzaj_urzadzenia`) VALUES (NULL,\"%s\", %d, %d, 5)" % (letter, len(zlacza[k]), plytka_id);
    print(sql)    
    cursor.execute(sql)
    epid = cursor.lastrowid;
    zlaczaMap[letter] = epid;
    pos = 0
    for zl in zlacza[k]:
        pos += 1
        if zl[0] == ':':
            zn1, zn2 = zl[1:].split('-')
            p = ''
            if zn1[0] == k[0]:
                p = zn2
            elif zn2[0] == k[0]:
                p = zn1
            nazwa = "%s%s" % (letterMap[p[0]], p)
            nazwapinow = zl[1:]
        else:
            nazwa = zl
            nazwapinow = nazwa
        
        sqlinsert = "INSERT INTO `elementy_plytkowe_pin`(`id`, `nazwa`, `pos`, `element_plytkowy_id`) VALUES "
        sqlinsert += "(NULL, \"%s\", %d, %d)" % (nazwa, pos, epid)
        print(sqlinsert)    
        cursor.execute(sqlinsert)
        eppid = cursor.lastrowid
        if nazwapinow not in nazwaPol.keys():
            nazwaPol[nazwapinow] = [];
        nazwaPol[nazwapinow].append(eppid)       
    #end for
    if przewod == "999":
        continue
    sqlsel = "SELECT `id`  FROM `ZakonczenieView` WHERE `przewod_id` = %s AND `etykieta` = '%s' AND `miejsce_id` = 1 AND `rodzaj_zakonczenia` = 1" % (przewod, letter)    
    print(sqlsel)
    cursor.execute(sqlsel)
    res = cursor.fetchall();
    zid = res[0][0]    
    sqlins = "INSERT INTO `zlacze_wtyczka`(`id`, `wtyczka_id`, `zlacze_id`) VALUES (NULL,%s,%d)" % (zid, epid)
    print(sqlins)
    cursor.execute(sqlins)

for n in nazwaPol.keys():
    sqlinsert = "INSERT INTO `polaczenie_plytka`(`id`, `nazwa`, `plytka_id`) VALUES (NULL,'%s',%d)" % (n, plytka_id)
    print(sqlinsert)    
    cursor.execute(sqlinsert)
    ppid = cursor.lastrowid
    for pid in nazwaPol[n]:
        sqlins = "INSERT INTO `polaczenie_plytka_polaczenie`(`id`, `polaczenie_plytka_id`, `elementy_plytkowe_piny_id`) "
        sqlins += "VALUES (NULL, %d, %d)" % (ppid, pid)
        print(sqlins)
        cursor.execute(sqlins)


cnx.commit()
cnx.close()
