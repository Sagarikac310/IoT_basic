import os
import Adafruit_DHT
import serial
import time
import urllib3

print("hi")
http = urllib3.PoolManager()
while True:

    try:
        humidity, temperature = Adafruit_DHT.read_retry(11,25)
        print("Temperature = %f" % temperature)
        print("Humidity = %f" % humidity)
        print("-------------------------------")
        
        baseURL = "https://api.thingspeak.com/update?api_key=J3A5Q5TLPLOPYC8F"
       
        url1 = (baseURL + "&field1=%f&field2=%f" %(temperature,humidity))
        response1 = http.request('GET',url1)
        print(response1.status)
        print(response2.status)
        print("-------------------------------")
        time.sleep(0.01 )
    except:
        pass
