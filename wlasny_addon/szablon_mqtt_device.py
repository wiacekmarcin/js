devide_id = "calkowitezuzycie"
device_name = "Całkowite zużycie"

sensor_id = "zuzycie_miesiac"
sensor_class = "energy"

name = "Mięsieczne zużycie"
topik = "hmd/sensor/CalcEn/energy_all/energy"

sensor_unit = "kWh"
sensor_pay = ".m.a"

tmpl = \
"""
- sensor:
    device:
      identifiers:
      - %(device_id)s
      name: "%(device_name)s"
      model: "Analizator zużycia energii"
    device_class: %(sensor_class)s
    name: "%(name)s"
    qos: 0.0
    state_class: total
    state_topic: %(topik)s
    suggested_display_precision: 2
    default_entity_id: "sensor.%(device_id)s_%(sensor_id)s"
    unique_id: %(device_id)s_%(sensor_id)s
    unit_of_measurement: %(sensor_unit)s
    value_template: '{{ value_json.%(sensor_pay)s }}'
"""



def createOneDevice(device_id, device_name, topik):
    sensorlist = [
        ("zuzycie_miesiac", "Miesięczne zużycie", "energy", "kWh", "energy.m.a"),
        ("zuzycie_dzienna_miesiac", "Miesięczne zużycie t. dzienna", "energy", "kWh", "energy.m.d"),
        ("zuzycie_nocna_miesiac", "Miesięczne zużycie t. nocna", "energy", "kWh", "energy.m.n"),
        ("zuzycie_rok", "Roczne zużycie", "energy", "kWh", "energy.y.a"),
        ("zuzycie_dzienna_rok", "Roczne zużycie t. dzienna", "energy", "kWh", "energy.y.d"),
        ("zuzycie_nocna_rok", "Roczne zużycie t. nocna", "energy", "kWh", "energy.y.n"),
        ("koszt_g12w_miesiac", "Miesięczny koszt (g12w)", "monetary", "PLN", "cost.m.g12w"),
        ("koszt_g11_miesiac", "Miesięczny koszt (g11)", "monetary", "PLN", "cost.m.g11"),
        ("koszt_dzienna_miesiac", "Miesięczny koszt t. dzienna", "monetary", "PLN", "cost.m.d"),
        ("koszt_nocna_miesiac", "Miesięczny koszt t. nocna", "monetary", "PLN", "cost.m.n"),
        ("koszt_g12w_rok", "Roczny koszt (g12w)", "monetary", "PLN", "cost.y.g12w"),
        ("koszt_g11_rok", "Roczny koszt (g11)", "monetary", "PLN", "cost.y.g11"),
        ("koszt_dzienna_rok", "Roczny koszt t. dzienna", "monetary", "PLN", "cost.y.d"),
        ("koszt_nocna_rok", "Roczny koszt t. nocna", "monetary", "PLN", "cost.y.n"),
    ]


    for sens in sensorlist:
        smap = {
            "device_id" : device_id,
            "device_name" : device_name,
            "topik" : topik,

            "sensor_id" : sens[0],
            "name" : sens[1],
            "sensor_class" : sens[2],
            "sensor_unit" :  sens[3],
            "sensor_pay" : sens[4],
        }
        print(tmpl % smap)

tmpl2 = \
"""
- sensor:
    device:
      identifiers:
      - %(device_id)s
      name: "%(device_name)s"
      model: "Virtual Device"
    device_class: %(sensor_class)s
    name: "%(name)s"
    qos: 0.0
    state_class: %(state_class)s
    state_topic: %(topik)s
    suggested_display_precision: %(precision)s
    default_entity_id: "sensor.%(device_id)s_%(sensor_id)s"
    unique_id: %(device_id)s_%(sensor_id)s
    unit_of_measurement: %(sensor_unit)s
    value_template: '{{ value_json.%(sensor_pay)s }}'
"""

def createVirtualDevice(device_id, device_name, topik):
    sensorlist = [
        ("current", "Prąd", "current", "A", "measurement", "2", "current"),
        ("voltage", "Napięcie", "voltage", "V", "measurement", "1", "voltage"),
        ("power", "Moc", "power", "W", "measurement", "1", "power"),
        ("energy", "Energia", "energy", "kWh", "total", "2", "energy"),
    ]

    #state_class = 
    #precision

    for sens in sensorlist:
        smap = {
            "device_id" : device_id,
            "device_name" : device_name,
            "topik" : topik,

            "sensor_id" : sens[0],
            "name" : sens[1],
            "sensor_class" : sens[2],
            "sensor_unit" :  sens[3],
            "state_class"  : sens[4],
            "precision" : sens[5],
            "sensor_pay" : sens[6],
        }
        print(tmpl2 % smap)



print("mqtt:")
topik = "hmd/sensor/CalcEn/energy_all/energy"
device_id = "calkowitezuzycie"
device_name = "Całkowite zużycie"        
createOneDevice(device_id, device_name, topik)

topik = "hmd/sensor/CalcEn/centrala_sieciowa/energy"
device_id = "centralasieciowa"
device_name = "Centrala sieciowa"        
createOneDevice(device_id, device_name, topik)

topik = "hmd/sensor/CalcEn/rozrywka/energy"
device_id = "rozrywka"
device_name = "Rozrywka"    
createOneDevice(device_id, device_name, topik)

topik = "hmd/sensor/CalcEn/inne_gniazda/energy"
device_id = "sprzet_agd"
device_name = "Sprzęt AGD"    
createOneDevice(device_id, device_name, topik)

topik = "hmd/sensor/CalcEn/inne_gniazda/energy"
device_id = "kuchnia_agd"
device_name = "Kuchenny sprzęt AGD"    
createOneDevice(device_id, device_name, topik)

topik = "hmd/sensor/CalcEn/server_ha/energy"
device_id = "centrala_ha"
device_name = "Centrala HA"        
createOneDevice(device_id, device_name, topik)

topik = "hmd/sensor/CalcEn/bathroom_el_socket/energy"
device_id = "bathroom_el_socket"
device_name = "Gniazda łazienka"        
createOneDevice(device_id, device_name, topik)

topik = "hmd/sensor/CalcEn/brama_vectra/energy"
device_id = "brama_vectra"
device_name = "Router Vectry"        
createOneDevice(device_id, device_name, topik)

topik = "hmd/sensor/CalcEn/charger_1/energy"
device_id = "charger_1"
device_name = "Ładowarka tel. 1"        
createOneDevice(device_id, device_name, topik)

topik = "hmd/sensor/CalcEn/charger_2/energy"
device_id = "charger_2"
device_name = "Ładowarka tel. 2"        
createOneDevice(device_id, device_name, topik)

topik = "hmd/sensor/CalcEn/computer/energy"
device_id = "computer"
device_name = "Komputer"        
createOneDevice(device_id, device_name, topik)

topik = "hmd/sensor/CalcEn/computer/energy"
device_id = "computer"
device_name = "Komputer"        
createOneDevice(device_id, device_name, topik)

topik = "hmd/sensor/CalcEn/dishwasher/energy"
device_id = "dishwasher"
device_name = "Zmywarka"        
createOneDevice(device_id, device_name, topik)

topik = "hmd/sensor/CalcEn/dvd_player/energy"
device_id = "dvd_player"
device_name = "Odtwarzacz DVD"        
createOneDevice(device_id, device_name, topik)

topik = "hmd/sensor/CalcEn/electric_dryer/energy"
device_id = "electric_dryer"
device_name = "Szuszarka elektryczna"        
createOneDevice(device_id, device_name, topik)

topik = "hmd/sensor/CalcEn/fridge/energy"
device_id = "fridge"
device_name = "Lodówka"        
createOneDevice(device_id, device_name, topik)

topik = "hmd/sensor/CalcEn/heating/energy"
device_id = "heating"
device_name = "Ogrzewanie"        
createOneDevice(device_id, device_name, topik)

topik = "hmd/sensor/CalcEn/choinka/energy"
device_id = "choinka"
device_name = "Choinka"        
createOneDevice(device_id, device_name, topik)

topik = "hmd/sensor/CalcEn/iron/energy"
device_id = "iron"
device_name = "Żelazko"        
createOneDevice(device_id, device_name, topik)

topik = "hmd/sensor/CalcEn/kitchen_hood/energy"
device_id = "kitchen_hood"
device_name = "Okap w kuchni"        
createOneDevice(device_id, device_name, topik)

topik = "hmd/sensor/CalcEn/light/energy"
device_id = "light"
device_name = "Oświetlenie"        
createOneDevice(device_id, device_name, topik)

topik = "hmd/sensor/CalcEn/main_power_switch/energy"
device_id = "main_power_switch"
device_name = "Wyłącznik główny"        
createOneDevice(device_id, device_name, topik)

topik = "hmd/sensor/CalcEn/main_power_switch/energy"
device_id = "microwave"
device_name = "Mikrofala"        
createOneDevice(device_id, device_name, topik)

topik = "hmd/sensor/CalcEn/power_24v_on/energy"
device_id = "power_24v_on"
device_name = "Zasilacz 24V on"        
createOneDevice(device_id, device_name, topik)

topik = "hmd/sensor/CalcEn/power_24v_off/energy"
device_id = "power_24v_off"
device_name = "Zasilacz 24V off"        
createOneDevice(device_id, device_name, topik)

topik = "hmd/sensor/CalcEn/power_guaranted/energy"
device_id = "power_guaranted"
device_name = "Zasilanie gwarantowane"        
createOneDevice(device_id, device_name, topik)

topik = "hmd/sensor/CalcEn/reserved_lte/energy"
device_id = "reserved_lte"
device_name = "Zapasowy router LTE"        
createOneDevice(device_id, device_name, topik)

topik = "hmd/sensor/CalcEn/roaster/energy"
device_id = "roaster"
device_name = "Piekarnik"        
createOneDevice(device_id, device_name, topik)

topik = "hmd/sensor/CalcEn/server_nas/energy"
device_id = "server_nas"
device_name = "Server Synology"        
createOneDevice(device_id, device_name, topik)

topik = "hmd/sensor/CalcEn/teapot_electric/energy"
device_id = "teapot_electric"
device_name = "Czajnik elektryczny"        
createOneDevice(device_id, device_name, topik)

topik = "hmd/sensor/CalcEn/tv_samsung/energy"
device_id = "tv_samsung"
device_name = "Telewizor Samsung"        
createOneDevice(device_id, device_name, topik)

topik = "hmd/sensor/CalcEn/vacuum_cleaner/energy"
device_id = "vacuum_cleaner"
device_name = "Odkurzacz"        
createOneDevice(device_id, device_name, topik)

topik = "hmd/sensor/CalcEn/vectra_decoder/energy"
device_id = "vectra_decoder"
device_name = "Dekoder Vectry"        
createOneDevice(device_id, device_name, topik)

topik = "hmd/sensor/CalcEn/washing_machine/energy"
device_id = "washing_machine"
device_name = "Pralka"        
createOneDevice(device_id, device_name, topik)

topik = "hmd/sensor/CalcEn/wifi_access_point_1/energy"
device_id = "wifi_access_point_1"
device_name = "Bramka WiFi 1"        
createOneDevice(device_id, device_name, topik)

####virtual device
topik = "hmd/sensor/CalcEn/centrala_sieciowa/state"
device_id = "centrala_sieciowa"
device_name = "Centrala sieciowa"        
createVirtualDevice(device_id, device_name, topik)

topik = "hmd/sensor/CalcEn/rozrywka/state"
device_id = "rozrywka"
device_name = "TV Rozrywka"        
createVirtualDevice(device_id, device_name, topik)

topik = "hmd/sensor/CalcEn/inne_gniazda/state"
device_id = "inne_gniazda"
device_name = "Pozostały sprzęt agd"        
createVirtualDevice(device_id, device_name, topik)

topik = "hmd/sensor/CalcEn/kuchnia_gniazda/state"
device_id = "kuchnia_gniazda"
device_name = "Sprzęt AGD kuchnia"        
createVirtualDevice(device_id, device_name, topik)

