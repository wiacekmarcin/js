#============================================================================================
# plik dockerfile jest plikiem sterującym procesem tworzenia dockera przez HA
# nasz addon znajdzie się właśnie w tym niezależnym dokerze/konterze (izolowany serwer) w HA
#============================================================================================

# Bazowy obraz Dockera (Python 3.11 w lekkiej wersji "slim")
# To punkt startowy naszego własnego Dockera tworzonego w dodatku HA
# Wszystko poniżej buduje go krok po kroku – aż do gotowego serwera OLED

FROM python:3.11-slim
ARG DEBIAN_FRONTEND=noninteractive
ARG DEBCONF_NOWARNINGS="yes"

ENV PIP_ROOT_USER_ACTION=ignore
#--------------------------------------------------------------------------------------------

# Zainstaluj zależności systemowe i Pythonowe
# --no-install-recommends   mniej śmieci w obrazie, lżejszy Docker (~80 MB mniej)
# zlib1g-dev                pełna kompatybilność z Pillow (obsługa PNG, JPEG itp.)
# fonts-dejavu-core         zapewnia dostępność DejaVuSans.ttf dla Twojego OLED-a
# --no-cache-dir przy pip   nie trzyma śmieci z cache PIP (~100 MB mniej)
# apt-get clean + rm -rf    czyści cache APT (kolejne ~60 MB mniej)

RUN apt-get update && \
    apt-get install -y python3 && \
    pip3 install --upgrade pip && \
    pip3 install --break-system-packages --no-cache-dir --root-user-action=ignore ha_mqtt_discoverable && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

#--------------------------------------------------------------------------------------------

# Skopiuj aplikację
# (czyli plik run.py z folderu naszego instalacyjnego dodatku Home Assistanta do budowanego obrazu Dockera)
# Ten plik trafi do wnętrza tworzonego obrazu – to właśnie nasz główny serwer Flask (API dla OLED)

COPY run.py /root/run.py
COPY run.sh /root/run.sh
RUN mkdir -p /root/data
RUN chmod a+x /root/run.sh

#--------------------------------------------------------------------------------------------

# Uruchom Gunicorna z jednym workerem i jednym wątkiem
# (czyli start naszego serwera Flask wewnątrz kontenera)
# Gunicorn to lekki serwer HTTP dla aplikacji Python
# --workers=1 i --threads=1 bo OLED przez I2C nie jest w pełni wielowątkowy – to bezpieczne ustawienie
# Kontener nasłuchuje na porcie 8080 (REST API do komunikacji z Home Assistantem)
CMD ["/root/run.sh"]

