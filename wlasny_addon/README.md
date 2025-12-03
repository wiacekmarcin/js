# Analizator energii
Dodatek korzysta z mqtt a dokładnie z topic zigbee2mqtt aby śledzić zużycie energii urządzeń
## Przykłady użycia
- Dodatek wymaga automatyzacji, który będzie publikował w topic hmd/sensor/tauron_taryfa {"taryfa" = 'dzienna'/'nocna', 'price' = aktualna cena wg taryfy g12w, 'g11' = cene w taryfie g11 }
- Urządzenie zmianę energii muszą publikować w zigbee2mqtt/urządzenie/{"energy" : } a całe zużycie w zigbee2mqtt/energy/{"energy" : }

