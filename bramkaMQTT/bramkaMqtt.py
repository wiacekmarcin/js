#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
import paho.mqtt.client as paho
import json

broker="192.168.10.254"


prevHum = "0"
prevTemp = "0"

#{"cpuTemp":"54.8°C\n","sysLoad":["1.08","0.67","0.52","2/362","12371\n"],"freeMem":"8.69267\n","upTime":["96759.08","350131.65\n"],"freeSpace":"6,4G\n"}

#{"coord":{"lon":20.85,"lat":52.19},
# "weather":[{"id":701,"main":"Mist","description":"zamglenie","icon":"50n"}],"base":"stations",
# "main":{"temp":4.38,"feels_like":2.38,"temp_min":3.89,"temp_max":5,"pressure":1025,"humidity":100},
# "visibility":1300,
# "wind":{"speed":1.07,"deg":89},
# "clouds":{"all":75},"dt":1608161885,"sys":{"type":1,"id":1713,"country":"PL","sunrise":1608187273,"sunset":1608215074},"timezone":3600,"id":7532279,
# "name":"Piastów","cod":200}


#                this.sendNotification("CURRWEATHER_TEMP_HUMI", { temp : data.main.temp, humi : data.main.humidity }); 
#                this.sendNotification("CURRWEATHER_FEELS_TEMP", data.main.feels_like);
#                this.sendNotification("CURRWEATHER_PRESSURE", data.main.pressure );
#                this.sendNotification("CURRWEATHER_WIND", data.wind);



decoder = json.JSONDecoder()
#define callback
def on_message(client, userdata, message):
    if 1 :
        mssgrec = message.payload.decode("utf-8")
        #print(message.topic) 
        #print(mssgrec)
        global prevHum
        global prevTemp
        global decoder

        if message.topic == "house/humi/laz/umy":
            prevHum = mssgrec
            client.publish("domoticz/in", '{"idx":16, "nvalue":0, "svalue":"%s;%s;0"}' % (prevTemp, prevHum))
            return

        if message.topic == "house/temp/laz/umy":
            prevTemp = mssgrec
            client.publish("domoticz/in", '{"idx":16, "nvalue":0, "svalue":"%s;%s;0"}' % (prevTemp, prevHum))
            return

        if message.topic == "house/temp/mm/rasmon":
            temps = decoder.decode(mssgrec)
            for t in temps:
                if t['label'] == 'Monitor':
                    client.publish("domoticz/in", '{"idx":17, "nvalue":0, "svalue":"%s"}' % t['value'].replace("&deg;" , ""))
                if t['label'] == 'Raspberry':
                    client.publish("domoticz/in", '{"idx":18, "nvalue":0, "svalue":"%s"}' % t['value'].replace("&deg;" , ""))
            return

        if message.topic == "house/temp/mm/core":
            temp = decoder.decode(mssgrec)
            client.publish("domoticz/in", '{"idx":19, "nvalue":0, "svalue":"%s"}' %temp[:-3])
            return 

        if message.topic == "house/wheather/today":
            th = decoder.decode(mssgrec)
            client.publish("domoticz/in", '{"idx":293, "nvalue":0, "svalue":"%s;%s;0;%s;0"}' % (th["t"], th["h"], th["p"]))
            
            return

        if message.topic == "house/temp/wheather/todayfeels":
            client.publish("domoticz/in", '{"idx":21, "nvalue":0, "svalue":"%s"}' % mssgrec)
            return

        #print("message topic=",message.topic)
        #print("message qos=",message.qos)
        #print("message retain flag=",message.retain)
        #print("message received " , mssgrec)
    #except :
    #    pass
    

client= paho.Client("MqttDomoticzHttpGtw") 

#print("connecting to broker ",broker)
client.connect(broker);

#print("subscribing ")
client.subscribe("house/#")

client.on_message=on_message        #attach function to callback




client.loop_start() #start loop to process received messages

while True:
    time.sleep(2);

client.loop_stop() #stop loop
client.disconnect() #disconnect


