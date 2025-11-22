wzor =  "alias: tv_%(id)s_mqtt\n"
wzor += 'description: ""\n'
wzor += 'triggers:\n'
wzor += '  - trigger: state\n'
wzor += '    entity_id:\n'
wzor += '      - sensor.%(sensor)s\n'
wzor += 'conditions: []\n'
wzor += 'actions:\n'
wzor += '  - action: mqtt.publish\n'
wzor += '    metadata: {}\n'
wzor += '    data:\n'
wzor += '      qos: "2"\n'
wzor += '      topic: hmd/sensor/energy/%(id)s\n'
wzor += '      payload: "{{ states(\'sensor.%(sensor)s\') | float(0) }}"\n'
wzor += '      evaluate_payload: false\n'
wzor += 'mode: single\n'

wzor2 = '%(id)s = BothTariff("%(name)s")'

wzor3 = '\n'
wzor3 +='    if message.topic == "hmd/sensor/energy/%(id)s":\n'
wzor3 +='        %(id)s.calculate(allE.tariff_1, allE.price, float(msgrec))\n'
wzor3 +='        return'

varsHA = [
        {'id' : 'decoder_vectra', 'sensor': 'dekoder_energy', 'name': 'Dekoder Vectry'},
        {'id' : 'charger2', 'sensor': 'ladowarka_2_energy', 'name': 'Ładow. telef. 2'},
        {'id' : 'microwave', 'sensor': 'mikrofala_energy', 'name': 'Mikrofala'},
        {'id' : 'lights', 'sensor': 'oswietlenie_energy', 'name': 'Oświetlenie'},
        {'id' : 'roaster', 'sensor': 'piekarnik_energy', 'name': 'Piekarnik'},
        {'id' : 'kettle', 'sensor': 'czajnik_energy', 'name': 'Czajnik'},
        {'id' : 'computer', 'sensor': 'komputer_energy', 'name': 'Komputer'},
        {'id' : 'fridge', 'sensor': 'lodowka_energy', 'name': 'Lodówka'},
        {'id' : 'charger1', 'sensor': 'ladowarka_1_energy', 'name': 'Ładow. telef. 1'},
        {'id' : 'dvd', 'sensor': 'odtwarzacz_dvd_energy', 'name': 'Odtwarzacz DVD'},
        {'id' : 'heat', 'sensor': 'ogrzewanie_energy', 'name': 'Ogrzewanie'},
        {'id' : 'washing_machine', 'sensor': 'pralka_energy', 'name': 'Pralka'},
        {'id' : 'electric_dryer', 'sensor': 'suszarka_energy', 'name': 'Szuszarka el.'},
        {'id' : 'bathroom_el_socket', 'sensor': 'suszarka_do_wlosow_energy', 'name': 'Gniazda łazienka'},
        {'id' : 'kitchen_hood', 'sensor': 'wyciag_powietrza_energy', 'name': 'Okap'},
        {'id' : 'power_supply_24V_OFF', 'sensor': 'zasilacz_24v_off_energy', 'name': 'Zasilacz 24V off'},
        {'id' : 'power_supply_24V_ON', 'sensor': 'zasilacz_24v_on_energy', 'name': 'Zasilacz 24V on'},
        {'id' : 'dishwasher', 'sensor': 'zmywarka_energy', 'name': 'Zmywarka'},
        {'id' : 'power_supply_guaranteed', 'sensor': 'zasilanie_gwarantowane_energy', 'name': 'Zasilanie gwarantowane'},
        {'id' : 'main_switch', 'sensor': 'wlacznik_glowny_energy', 'name': 'Włącznik główny'},
        {'id' : 'iron', 'sensor': 'zelazko_energy', 'name': 'Żelasko'},
        {'id' : 'vacuum_cleaner', 'sensor': 'odkurzacz_energy', 'name': 'Odkurzacz'},
    ]

for v in varsHA:
    print(wzor % v)

#print(wzor % {'id' : 'centrala_sieciowa', 'sensor': 'centrala_sieciowa_energy', 'name': 'Centrala sieciowa'})
#print()
#print()
#print(wzor % {'id' : 'centrala_sieciowa', 'sensor': 'centrala_sieciowa_energy', 'name': 'Centrala sieciowa'})
#print()
#print()
