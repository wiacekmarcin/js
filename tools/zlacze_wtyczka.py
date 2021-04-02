import mysql.connector
cnx = mysql.connector.connect(user='kb_ster', password='kb_ster',
                              host='127.0.0.1',
                              database='kb_ster_test')
                              
cursor = cnx.cursor()

zlacza = {
  'A:195' : [
    '+24V off',
    'GND'
  ],
  'B:194' : [
    'Zas. awar.',
    '2 taryfa',
    'noc',
    'wieczor',
    '+24V off',
    'GND',
    'GND',
    '+24V'
  ],
  'C:193' : [
    '+5V',
    'GND'
  ],
  'D:192' : [
    ':D1-F5',
    ':D2-F4',
    ':D3-F3',
    ':D4-F2',
    ':D5-F1',
    ':D6-Z5',
    ':D7-G6',
    ':D8-G5',
    ':D9-G4',
    ':D10-G3',
    ':D11-G2',
    ':D12-G1'
  ],
    'E:191' : [
    'Zas. awar.', #BRAZ
    '2 taryfa',   #NIEB
    'noc',        #ZOLTY
    'wieczor'     #BIALY
  ],
  'F:42' : [
    ':D5-F1',
    ':D4-F2',
    ':D3-F3',
    ':D2-F4',
    ':D1-F5',
    'GND',
    'GND',
    '+5V'
  ],
  'G:54' : [
    ':D12-G1',
    ':D11-G2',
    ':D10-G3',
    ':D9-G4',
    ':D8-G5',
    ':D7-G6',
  ],
  'H:93' : [
    'RX93',
    'TX93',
    'GND',
    '+24V off',
    'wieczor',
    'noc',
    '2 taryfa',
    'Zas. awar.',
  ],
  'I:190' : [
    ':I1-L4',
    ':I2-L3',
    ':I3-L2',
    ':I4-L1',
    ':I5-Z4',
    ':I6-Z3',
    ':I7-M8',
    ':I8-M7',
    ':I9-M6',
    ':I10-M5'
  ],
  'J:189' : [
    '+24V',
    'GND',
    'GND',
    '+5V'
  ],
  'K:86' : [
    'RX86',
    'TX86',
    'Zas. awar.',
    '2 taryfa',
    'noc',
    'wieczor',
    '+24V off',
    'GND'
  ],
  'L:35' : [
    ':I4-L1',
    ':I3-L2',
    ':I2-L3',
    ':I1-L4',
    ':L5-M2',
    ':L6-M3',
    ':L7-M4',
    'GND'
  ],
  'M:59' : [
    ':M1-Z2',
    ':L5-M2',
    ':L6-M3',
    ':L7-M4',
    ':I10-M5',
    ':I9-M6',
    ':I8-M7',
    ':I7-M8',
  ],
  'N:57' : [
    'RX57',
    'TX57',
    'GND',
    '+24V off',
    'wieczor',
    'noc',
    '2 taryfa',
    'Zas. awar.',
  ],
  'P:58' : [
    'GND',
    ':P2-S7',
    ':P3-S6',
    ':P4-S5',
    ':P5-S4',
    ':P6-S3',
    ':P7-S2',
    ':P8-S1',
  ],
  'Q:188' : [
    ':Q1-T6',
    ':Q2-T5',
    ':Q3-T4',
    ':Q4-T3',
    ':Q5-T2',
    ':Q6-T1',
    ':Q7-U3',
    ':Q8-U8',
    ':Q9-U7',
    ':Q10-U6',
    ':Q11-U5',
    ':Q12-U4',
  ],
  'O:34' : [
    'Zas. awar.',
    '2 taryfa',
    'noc',
    'wieczor',
    '+24V off',
    'GND',
    'TX34',
    'RX34'
  ],
  'R:52' : [
    'RX52',
    'TX52',
    'GND',
    '+24V off',
    'wieczor',
    'noc',
    '2 taryfa',
    'Zas. awar.',
  ],
  'S:94' : [
    ':P8-S1',
    ':P7-S2',
    ':P6-S3',
    ':P5-S4',
    ':P4-S5',
    ':P3-S6',
    ':P2-S7',
    'GND',
  ],
  'T:83'  : [
    ':Q6-T1',
    ':Q5-T2',
    ':Q4-T3',
    ':Q3-T4',
    ':Q2-T5',
    ':Q1-T6',
    '+5V',
    'GND'
  ],
  'U:999'  : [
    'GND',
    '+5V',
    ':Q7-U3',
    ':Q12-U4',
    ':Q11-U5',
    ':Q10-U6',
    ':Q9-U7',
    ':Q8-U8',
  ], 
  'V:186' : [
    'Zas. awar.', #BRAZ
    '2 taryfa',   #NIEB
    'noc',        #ZOLTY
    'wieczor'     #BIALY
  ],
  'W:187' : [
    'GND',
    '+5V'
  ],
  'X:185' : [
    'RX93',
    'TX93',
    'RX86',
    'TX86',
    'RX57',
    'TX57',
    'RX34',
    'TX34',
    'RX52',
    'TX52',
    'GND',
    '+5V'
  ],
  'Y:184' : [
    'GND',
    '+24V'
  ],
  'Z:53' : [
    'GND',
    ':M1-Z2',
    ':I6-Z3',
    ':I5-Z4',
    ':D6-Z5',
    '+5V'
  ],
}
letterMap = {}
plytka_id = 9
nazwaPol = {}
zlaczaMap = {}

sql = "SELECT `id`  FROM `ZakonczenieView` WHERE `przewod_id` = 52 AND `miejsce_id` = 1 AND `rodzaj_zakonczenia` = 1"
cursor.execute(sql)
rid = cursor.fetchall()[0][0]
cursor.execute("UPDATE `zakonczenie` SET `etykieta`='R' WHERE `id` = %s" % rid)

sql = "SELECT `id`  FROM `ZakonczenieView` WHERE `przewod_id` = 42 AND `miejsce_id` = 1 AND `rodzaj_zakonczenia` = 1"
cursor.execute(sql)
rid = cursor.fetchall()[0][0]
cursor.execute("UPDATE `zakonczenie` SET `etykieta`='F' WHERE `id` = %s" % rid)

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
