tmp = """
      - type: grid
        cards:
          - type: heading
            heading: %(name)s
            heading_style: title
            badges:
              - type: entity
                show_state: true
                show_icon: true
                entity: sensor.%(entity)s
          - show_name: true
            show_icon: false
            show_state: true
            type: glance
            entities:
              - entity: sensor.%(idn)s_cost_dzienna_m
                name: tar. dzienna
                show_last_changed: false
              - entity: sensor.%(idn)s_cost_nocna_m
                name: tar. nocna
              - entity: sensor.%(idn)s_cost_all_m
                name: g12
              - entity: sensor.%(idn)s_cost_g11_m
                name: g11
            grid_options:
              columns: full
              rows: auto
            state_color: true
          - show_name: true
            show_icon: false
            show_state: true
            type: glance
            entities:
              - entity: sensor.%(idn)s_cost_dzienna_y
                name: tar. dzienna
                show_last_changed: false
              - entity: sensor.%(idn)s_cost_nocna_y
                name: tar. nocna
              - entity: sensor.%(idn)s_cost_all_y
                name: g12
              - entity: sensor.%(idn)s_cost_g11_y
                name: g11
            grid_options:
              columns: full
              rows: auto
            state_color: true
"""

lisent = [
    #("Całe zużycie", "moc_pobrana", "energy_all"),
    #("Oświetlenie", "light_energy", "light"),
    #("Centrala Sieciowa", "centrala_sieciowa_energy", "centrala_sieciowa"),
    #("Lodówka", "fidge_energy", "fridge"),
    #("Komputer", "computer_energy", "computer"),
    #("Pralka", "washing_machine_energy", "washing_machine"),
    #("Szuszarka el.", "electric_dryer_energy", "electric_dryer"),
    #("Piekarnik", "roaster_energy", "roaster"),
    #("Mikrofala", "microwave_energy", "microwave"),
    #("Zmywarka", "dishwasher_energy", "dishwasher"),
    #("Czajnik", "teapot_electric_energy", "teapot_electric"),
    #("Okap", "kitchen_hood_energy", "kitchen_hood")
    ("Ogrzewanie", "heating_energy", "heating")
]

mapEntity = {}
for name, entity, idn in lisent:
    mapEntity = {"name" : name, "entity" : entity, "idn" : idn}
    print (tmp % mapEntity)

#('zigbee2mqtt/energy',              BothTariff("energy_all", "Całe zużycie", "")),
    #('zigbee2mqtt/wifi_access_point_1', BothTariff("wifi_access_point_1", "Bramka WiFi 1", "0xa4c1380673912699")),
    #('zigbee2mqtt/heating',             BothTariff("heating", "Ogrzewanie")),
    #('zigbee2mqtt/power_24v_on',        BothTariff("power_24v_on", "Zasilacz 24V on")),
    #('zigbee2mqtt/power_24v_off',       BothTariff("power_24v_off", "Zasilacz 24V off")),

    #('zigbee2mqtt/power_guaranted',     BothTariff("power_guaranted", "Zasilanie gwarantowane")),

    #('zigbee2mqtt/main_power_switch',   BothTariff("main_power_switch", "Wyłącznik główny")),


    #('zigbee2mqtt/vectra_decoder',      BothTariff("vectra_decoder", "Dekoder Vectry")),
    #('zigbee2mqtt/charger_1',           BothTariff("charger_1", "Ładowarka tel. 1")),
    #('zigbee2mqtt/charger_2',           BothTariff("charger_2", "Ładowarka tel. 2")),

    #('zigbee2mqtt/dvd_player',          BothTariff("microwave", "Odtwarzacz DVD")),
    #('zigbee2mqtt/tv_samsung',          BothTariff("tv_samsung", "Telewizor Samsung")),
    #('zigbee2mqtt/washing_machine',     BothTariff("washing_machine", "Pralka")),
    #('zigbee2mqtt/bathroom_el_socket',  BothTariff("bathroom_el_socket", "Gniazda łazienka")),
    #('zigbee2mqtt/iron',                BothTariff("iron", "Żelazko")),
    #('zigbee2mqtt/brama_vectra',        BothTariff("brama_vectra", "Router Vectry")),


    #('zigbee2mqtt/vacuum_cleaner',      BothTariff("vacuum_cleaner", "Odkurzacz")),

