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


topik = "hmd/sensor/CalcEn/energy_all/energy"
device_id = "calkowitezuzycie"
device_name = "Całkowite zużycie"        
createOneDevice(device_id, device_name, topik)

topik = "hmd/sensor/CalcEn/centrala_sieciowa/energy"
device_id = "centralasieciowa"
device_name = "Centrala sieciowa"        
createOneDevice(device_id, device_name, topik)

topik = "hmd/sensor/CalcEn/server_ha/energy"
device_id = "centrala_ha"
device_name = "Centrala HA"        
createOneDevice(device_id, device_name, topik)

